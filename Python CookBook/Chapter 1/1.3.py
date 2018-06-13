# -*- coding: utf-8 -*-
# @author ZhengZhong,Jiang
# @time 2018/6/5 16:46

from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


# Example use on a file
if __name__ == '__main__':
    with open('somefile.txt', encoding='utf-8') as f:
        for line, prelines in search(f, 'python', 5):
            for pline in prelines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)
