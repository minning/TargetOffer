# coding:utf-8
'''
    Author:minning
    Date:2018/1/8
    代码目的：剑指offer 第 21 题：包含min函数的栈
            题目：定义栈的数据结构，请在该类型中实现一个能够得到栈最小元素的 min 函数。
            思路：
    
'''


class Solution:
    def __init__(self):
        self.arr = []

    def push(self, node):
        self.arr.append(node)

    def pop(self):
        return self.arr.pop()

    def top(self):
        return self.arr[-1]

    def min(self):
        return min(self.arr)

