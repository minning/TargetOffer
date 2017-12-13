# coding:utf-8
'''
    author : minning 
    Date : 2017/12/13
    代码目的：对于数字m、n，数字之间的运算只有 乘以2  或者  乘以10再加1
            问，从m到n最少需要几次上述的运算
    
'''

def getLessMul(m, n):
    num = 0
    while m<n:
        if n%10 == 1:
            n = n/10
            num += 1
        elif (n%10)%2 == 1:
            return False
        else:
            n = n/2
            num += 1
        if m == n:
            return num
    return False

print getLessMul(2, 21)  # 1
print getLessMul(2, 41)  # 2
print getLessMul(5, 21)  # False
print getLessMul(6, 53)  # False
