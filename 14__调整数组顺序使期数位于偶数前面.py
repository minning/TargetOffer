# coding:utf-8
'''
    author : minning 
    Date : 2017/7/23
    代码目的：剑指offer 第 14 题
            题目：输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
            所有的偶数位于位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
    
'''


class Solution:
    def reOrderArray(self, array):
        # write code here
        odd = []
        even = []

        for item in array:
            if item % 2 == 1:
                odd.append(item)
            else:
                even.append(item)
        return odd + even


s = Solution()
ls = [1,2,4,3,5,8,6,9,7]
print s.reOrderArray(ls)  # [1, 3, 5, 9, 7, 2, 4, 8, 6]
