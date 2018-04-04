# -*- coding: utf-8 -*-
# @author ZhengZhong,Jiang
# @time 2018/4/4 11:03

#https://foofish.net/daily-question2.html


import  random



class GuessNum:
    def __init__(self, min_num, max_num, choice):
        """

        :param min_num: 最小值
        :param max_num: 最大值
        :param choice: 猜测次数
        """
        self.min_num = min_num
        self.max_num = max_num
        self.target = random.randint(min_num, max_num)
        self.choice = choice

    def guess_num(self):
        choice = self.choice
        print(self.target)
        while choice > 0:
            choice -= 1
            try:
                guess = int(input("猜一个0-100之间的整数："))
            except:
                print("请输入合法的数字！")
                continue
            if guess < self.target and guess > 0:
                print("猜小了！你还剩下%d次机会！" % choice)
            elif guess > self.target and guess < 100:
                print("猜大了！你还剩下%d次机会！" % choice)
            elif guess == self.target:
                print("恭喜，猜对了！")
                break
        else:
            print("很遗憾，您的猜测机会用完了， 正确结果是：%s" % self.target)


if __name__ == "__main__":
    GuessNum(1, 100, 5).guess_num()