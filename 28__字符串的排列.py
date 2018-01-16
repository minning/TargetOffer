# coding:utf-8
'''
    author : minning 
    Date : 2018/1/17
    代码目的：剑指offer 第 28 题 : 字符串的排列
            题目：输入一个字符串, 按字典序打印出该字符串中字符的所有排列。例如输入字符串 abc,
                  则打印出由字符 a,b,c 所能排列出来的所有字符串 abc,acb,bac,bca,cab 和 cba。
            输入描述:输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。
            思路：
'''


from itertools import permutations
class Solution:
    def Permutation(self, ss):
        # write code here
        ret = []
        if not ss:
            return []
        return sorted(list(set(map(''.join, permutations(ss)))))
