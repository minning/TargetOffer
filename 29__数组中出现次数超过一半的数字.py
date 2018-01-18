# coding:utf-8
'''
    author : minning 
    Date : 2018/1/18
        代码目的：剑指offer 第 29 题 ： 数组中出现次数超过一半的数字
            题目：数组中有一个数字出现的次数超过数组长度的一半，
                 请找出这个数字。例如输入一个长度为 9 的数组 {1,2,3,2,2,2,5,4,2}。
                 由于数字 2 在数组中出现了 5 次，超过数组长度的一半，因此输出 2。如果不存在则输出 0。
            思路：构建一个字典存储数组中每个数字出现的次数，从而找出出现次数超过一半的元素
    
'''


class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        dt = {}
        for item in numbers:
            if item not in dt:
                dt[item] = 1
            else:
                dt[item] += 1
        for i in dt:
            if dt[i] * 2 > len(numbers):
                return i
        return 0


s = Solution()
s.MoreThanHalfNum_Solution([1,2,3,2,2,2,5,4,2])

