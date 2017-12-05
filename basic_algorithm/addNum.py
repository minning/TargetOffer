# coding:utf-8
'''
    author : minning 
    Date : 2017/7/23
    代码目的：计算1+2+3+...+n
    
'''


def addNum_basic(n):
    sum = 0
    for i in range(n+1):
        sum+=i
    return sum


def addNum_recru(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return n+addNum_recru(n-1)

print addNum_basic(10)
print addNum_recru(10)