# coding:utf-8
'''
    author : minning 
    Date : 2018/1/20
    代码目的：剑指offer 第 32 题：整数中 1 出现的次数（从 1 到 n 整数中 1 出现的次数）
            题目：求出 1~13 的整数中 1 出现的次数, 并算出 100~1300 的整数中 1 出现的次数？
                  为此他特别数了一下 1~13 中包含 1 的数字有 1、10、11、12、13 因此共出现 6 次,
                  但是对于后面问题他就没辙了。ACMer 希望你们帮帮他, 并把问题更加普遍化,
                  可以很快的求出任意非负整数区间中 1 出现的次数。
            思路：遍历查询
'''

class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        sum = 0
        for item in range(n+1):
            for i in str(item):
                if i=='1':
                    sum += 1
        return sum
