# coding:utf-8
'''
    author : minning 
    Date : 2018/1/21
    代码目的：剑指offer 第 33 题：把数组排成最小的数
            题目：输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
                 例如输入数组 {3，32，321}，则打印出这三个数字能排成的最小数字为 321323。
            思路：将数组按照指定顺序大小排序，然后合并
'''


class Solution:
    def PrintMinNumber(self, numbers):
        if not numbers:
            return ""

        lmd = lambda a, b: int(str(a) + str(b)) - int(str(b) + str(a))
        numbers.sort(cmp=lmd)
        return int(''.join([str(item) for item in numbers]))


s = Solution()
ls = [3,5,1,4,2]
print s.PrintMinNumber(ls)
