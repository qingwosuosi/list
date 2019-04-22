#! /user/bin/python3
# -*- coding:UTF-8 -*-

student = ['lilei','wangzhong','qianlei','qinlang','jiaoguanping']
number = [1,2,3,4,5]

'''
for i in range(len(student)):
    print(f'{student[i]}的学号是:{number[i]}')
'''

for name,num in  zip(student,number):
    print(f'{name}的学号是:{num}')


