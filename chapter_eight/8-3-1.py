# -*- coding: utf-8 -*-
# @author ZhengZhong,Jiang
# @time 2017/4/28 0028 下午 15:48

import os
import tarfile
import csv, fileinput
from xml.etree.ElementTree import Element, tostring
from xml.dom import minidom
from threading import Thread

import requests


class DownloadThread(Thread):
    def __init__(self, file_code):
        Thread.__init__(self)
        self.file_code = file_code

    def download(self, file_code):
        url = 'https://table.finance.yahoo.com/table.csv?s=%s.sz' % file_code
        print(url)
        response = requests.get(url, timeout=3)

        if response.ok:
            with open('%s.csv' % file_code, 'wb') as handle:
                for block in response.iter_content(1024):
                    handle.write(block)

    def run(self):
        data = self.download(self.file_code)




class ConvertThread(Thread):
    def __init__(self, file_code):
        Thread.__init__(self)
        self.file_code = file_code

    def csvToxml(self, file_code):
        fname = '.'.join([file_code, 'csv'])
        print(fname)
        with open(fname, 'r') as f:
            reader = csv.reader(f)
            headers = next(reader)
            # headers = map(lambda h: h.replace(' ', ''), headers) # 去掉headers空格
            headers[-1] = 'AdjClose'

            root = Element('Data')
            for row in reader:
                eRow = Element('Row')
                root.append(eRow)
                for tag, text in zip(headers, row):  # 使用zip方法 同时迭代两个可迭代对象
                    e = Element(tag)
                    e.text = text
                    eRow.append(e)
        root = tostring(root, 'utf-8')
        res = minidom.parseString(root)
        file_name = '.'.join([fname[:-4], 'xml'])
        print(file_name)
        with open(file_name, 'w') as wf:
            wf.write(res.toprettyxml(indent='\t'))

    def run(self):
        self.csvToxml(self.file_code)


if __name__ == '__main__':
    threads = []
    for code in range(4, 10):
        file_code = str(code).rjust(6, '0')
        t = Save(file_code)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

    print("main thread!")

