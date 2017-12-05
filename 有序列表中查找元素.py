# coding:utf-8
'''
    author : minning 
    Date : 2017/9/13
    代码目的：剑指offer 第  题
            题目：
    
'''


def get_index(ls, num):

    length = len(ls)
    left = 0
    right = length-1
    mid = (left+right)/2

    while left <= right:
        if ls[mid] == num:
            return mid
        elif ls[mid] > num:
            right = mid-1
        elif ls[mid] < num:
            left = mid+1
        mid = (left+right)/2

    return False


def binary_search_loop(lst,value):

    low, high = 0, len(lst)-1

    while low <= high:
        mid = (low + high) / 2
        if lst[mid] < value:
            low = mid + 1
        elif lst[mid] > value:
            high = mid - 1
        else:
            return mid

    return None

ls = [1,2,2,2,3,4]
num = 2
print get_index(ls,num)
print binary_search_loop(ls,num)

