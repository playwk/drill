#Author ZhengZhong,Jiang

import sys
import time


def view_bar(num, total):
    rate = float(num) / float(total)
    rate_num = int(rate * 50)
    r = '\r%s%s%d%%' % (rate_num * '#', (50-rate_num) * ' ', rate_num*2)
    sys.stdout.write(r)
    sys.stdout.flush()


if __name__ == '__main__':
    for i in range(0, 51):
        time.sleep(0.1)
        view_bar(i, 50)
