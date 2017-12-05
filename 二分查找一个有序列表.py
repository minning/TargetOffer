# coding:utf-8
'''
    author : minning 
    Date : 2017/9/21
    题目：对于一个有序列表，其中可能包含重复元素，设计算法找出其中一个元素在列表中出现的最左、最右索引位置
        如果没找到，返回 -1
'''


def findIndex(ls, num):

    if not ls:
        return -1
    elif len(ls) == 1:
        if ls[0] == num:
            return 0
        else:
            return -1
    else:
        left = 0
        right = len(ls)-1
        mid = (left+right)/2

        while left<=right:

            if ls[mid] == num:
                return mid
            elif ls[mid] > num:
                right = mid-1
            elif ls[mid] < num:
                left = mid+1
            mid = (left+right)/2
            # if left > right:
            #     return -1
        return -1

def findRange(ls, num):
    mid = findIndex(ls, num)
    left = right = mid
    if mid<0:
        return -1,-1

    while 0<left<len(ls)-1:
        if ls[left-1]!=ls[mid]:
            break
        else:
            left -= 1

    while 0<right<len(ls)-1:
        if ls[right+1]!=ls[mid]:
            break
        else:
            right += 1
    return left, right


ls = [0,1,1,1,1,2]
ls2 = [0,1,1,2]
ls3 = [1,1,1,1,1,2,3]
ls4 = [0,1,1,1,1,2,3,4]
num = 1
print findRange(ls, num)
print findRange(ls2, num)
print findRange(ls3, num)
print findRange(ls4, num)
ls5 = [0,1,3,4,5]
num2 = 3
num3 = 7
num4 = 2
print findRange(ls5, num2)
print findRange(ls5, num3)
print findRange(ls3, num4)
ls6 = []
num5 = 3
print findRange(ls6, num5)
print findRange(ls5, num4)
print findIndex(ls5, 2)
print findRange(ls5, num3)
