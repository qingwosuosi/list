#! /user/bin/python3
# -*- coding:UTF-8 -*-

import random

i=j=k=0

k=random.randint(0,100)

while(1):

    print(f'这是您的第{j}次尝试\n请输入您猜测的数字:')
    i=input()
    j+=1
    i=int(i)
    if(i>k):
        print(f'您输入的数字大了！')
        continue
    elif(i<k):
        print(f'您输入的数字小了！')
        continue
    else:
        break