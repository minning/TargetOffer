# coding:utf-8
'''
    代码目的：剑指offer 第 4 题
            题目：请实现一个函数，将一个字符串中的空格替换成 “%20”。
                例如，当字符串为 We Are Happy.
                则经过替换之后的字符串为 We%20Are%20Happy。
    
'''


class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        return s.replace(' ', '%20')

    def replaceSpace2(self, s):
        tempstr = ''
        for cha in s:
            if cha != " ":
                tempstr += cha
            else:
                tempstr += "%20"
        return tempstr

    # def replaceSpace3(self, s):


s = Solution()
print s.replaceSpace('he  ll o')
# he%20%20ll%20o

