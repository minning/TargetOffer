# coding:utf-8
'''
    author : minning 
    Date : 2017/8/22
            题目：使用快速幂对m的n次幂进行求解
    
'''


def pow(m, n):

    if n==0:
        return 1
    elif n==1:
        return m
    elif n == -1:
        return 1.0/m

    ret = pow(m, n>>1)
    ret = ret*ret
    if n%2 == 1:
        return ret*m
    else:
        return ret

print pow(2, 11)
