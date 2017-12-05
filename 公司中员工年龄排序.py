# coding:utf-8
'''
    author : minning 
    Date : 2017/9/21
    题目：公司里有一万名员工，年龄范围0--99，需要对员工年龄进行排序
    解题思路：新建一个长度为100的列表，对所有员工年龄进行遍历，在每次遍历到某值时给对应元素加一
    
'''

import random


def sortStaffAge(ls):

    ageLs = [0]*100
    for item in ls:
        ageLs[item] += 1

    ret = []
    for index, num in enumerate(ageLs):
        if num != 0:
            ret += [index]*num

    return ret

ls = []
for i in range(1000):
    ls.append(random.randint(0, 99))

print ls
print sortStaffAge(ls)
