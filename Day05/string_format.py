# Auther: ZhengZhong,Jiang


s1 = "fdsafd %(name)s %(age)d" % {'age':20,'name':'alex'}
print(s1)


s2 ="fdsafd %(name)s %(age)d %(pp).2f" % {'age':20,'name':'alex','pp':1.236}
print(s2)


s3 = "fdsafd {0:s} {1:d}".format(*['alex',20])
print(s3)

s4 ="fdsafd {name:s} {age:d} {pp:.2%}".format(**{'age':20,'name':'alex','pp':0.236789})
print(s4)

s5 = "{:*^20}".format("admin")
print(s5)