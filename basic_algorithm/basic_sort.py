# coding:utf-8
'''
    author : minning 
    Date : 2017/7/22
    代码目的：实现各种排序
    
'''


def quick_sort(ls):
    if not ls:
        return []
    else:
        left = [item for item in ls if item<ls[0]]
        right = [item for item in ls if item>ls[0]]
        mid = [item for item in ls if item==ls[0]]
        return quick_sort(left) + mid + quick_sort(right)


def bubble_sort_increasing(ls):
    for i in range(len(ls)-1, 0, -1):
        for j in range(i):
            if ls[j]>ls[j+1]:
                ls[j], ls[j+1] = ls[j+1], ls[j]
    return ls


def bubble_sort_decline(ls):
    for i in range(len(ls)-1,0,-1):
        for j in range(i):
            if ls[j]<ls[j+1]:
                ls[j], ls[j+1] = ls[j+1], ls[j]
    return ls


def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                 exchanges = True
                 alist[i], alist[i+1] = alist[i+1], alist[i]
        passnum = passnum-1
    return alist


def select_sort(ls):
    for i in range(len(ls)-1,0,-1):
        maxindex = 0
        for index in range(i+1):
            if ls[index]>ls[maxindex]:
                maxindex = index
        ls[maxindex],ls[i] = ls[i],ls[maxindex]
    return ls


def insert_sort(ls):
    for i in range(len(ls)):
        for j in range(i,0,-1):
            if ls[j]>=ls[j-1]:
                break
            else:
                ls[j],ls[j-1] = ls[j-1],ls[j]
    return ls


def insertionSort(alist):
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index
        while position>0 and alist[position-1]>currentvalue:
            alist[position]=alist[position-1]
            position = position-1
        alist[position]=currentvalue
    return alist


ls = [7,1,3,4,2,9,6,3,5,8]
# print shortBubbleSort(ls)
# print bubble_sort_increasing(ls)
# print bubble_sort_decline(ls)
# print select_sort(ls)
# print insert_sort(ls)
print insertionSort(ls)
print quick_sort(ls)
