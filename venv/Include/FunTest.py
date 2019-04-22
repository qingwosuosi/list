#! /user/bin/python3
# -*- coding:UTF-8 -*-

'''

def person_info_var(arg,*vartuple):
    print(arg)
    for var in vartuple:
        print(f'我属于不定长参数部分:{var}')

    return

print('-------------------------不带可变参数---------------------------------')

person_info_var('小萌')
person_info_var('liming',21,'beijing')
person_info_var('zhangsan',21,'beijing',123,'shanghai','happy')

'''

def exp(p1,p2,df=0,*vart,**kw):
    print(f'p1={p1},p2={p2},df={df},vart={vart},kw={kw}')

exp(1,2)
print('-------')
exp(1,2,c=3)
print('-------')
exp(1,2,3,'a','b')
print('-------')
exp(1,2,3,'abc',x=9)
