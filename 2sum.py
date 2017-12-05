# coding:utf-8
'''
    author : minning 
    Date : 2017/8/31
    代码目的：leetcode 2sum
            https://leetcode.com/problems/two-sum/
'''


def solution(ls, target):
    dt = {}
    ll = []

    for index, item in enumerate(ls):
        if target-item in dt:
            ll.append((dt[target-item], index))
        dt[item] = index

    return ll

ls = [1,3,2,4,5,7]
print solution(ls, 7)
