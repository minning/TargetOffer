# coding:utf-8
'''
    author : minning 
    Date : 2018/1/21
    代码目的：剑指offer 第 34 题：丑数
            题目：把只包含因子 2、3 和 5 的数称作丑数（Ugly Number）。
                 例如 6、8 都是丑数，但 14 不是，因为它包含因子 7。
                 习惯上我们把 1 当做是第一个丑数。求按从小到大的顺序的第 N 个丑数。
            思路：丑数都是因子为2、3、5的数，因此不断保存原数组乘以2、3、5的值的最小值加入数组中
'''


class Solution:
    def GetUglyNumber_Solution(self, index):

        if not index:
            return 0
        ls = [1]
        s2 = s3 = s5 = 0

        nextIndex = 1

        while nextIndex < index:
            mmin = min(ls[s2] * 2, ls[s3] * 3, ls[s5] * 5)
            ls.append(mmin)

            while ls[s2] * 2 <= mmin:
                s2 += 1
            while ls[s3] * 3 <= mmin:
                s3 += 1
            while ls[s5] * 5 <= mmin:
                s5 += 1
            nextIndex += 1

        return ls[nextIndex - 1]


s = Solution()
print s.GetUglyNumber_Solution(5)
