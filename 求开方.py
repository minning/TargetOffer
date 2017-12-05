# coding:utf-8
'''
    author : minning 
    Date : 2017/8/22
    题目：求一个浮点数的开方
    
'''


def sprt(n):
    '''
        二分查找的思想
    :param n:
    :return:
    '''
    if n<0:
        return None
    else:
        n = float(n)
        if n>=1:
            min = 1
            max = n
        elif 0<n<1:
            min = n
            max = 1
        mid = (min+max)/2
        bias = 10**(-16)

        while abs(mid**2-n) >= bias:
            if mid**2>n:
                max = mid
            else:
                min = mid
            mid = (min+max)/2
        return mid

def squareRoot(n):
    '''
        牛顿迭代法求开方
        x = sqrt(a)
        x**2 = a
        x**2 - a = 0
        f(x) = x**2 - a
        f'(x) = 2x
        X_(n+1) = X_(n) - f(X_(n)) / f'(X_(n))
        X_(n+1) = X_(n) - diff / 2x
    '''
    n = float(n)
    x_n = n
    diff = x_n**2-n
    bias = 10**(-10)

    while diff>bias:
        x_n = x_n - diff/(2*x_n)
        diff = x_n**2 - n
    return x_n


print sprt(4)
print squareRoot(4)
