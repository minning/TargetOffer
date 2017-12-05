# coding:utf-8
'''
    author : minning 
    Date : 2017/7/23
    代码目的：剑指offer 第 9.4 题
            题目：我们可以用 2*1 的小矩形横着或者竖着去覆盖更大的矩形。
            请问用 n 个 2*1 的小矩形无重叠地覆盖一个 2*n 的大矩形，总共有多少种方法？
    思路：覆盖一个 2*n 的大矩形的方法数等于
            1)使用一个2*1 的小矩形竖放在最左边，剩下的部分相当于覆盖一个 2*（n-1） 的大矩形的方法
            2）使用两个2*1 的小矩形横放在最左边，剩下的部分相当于覆盖一个 2*（n-2） 的大矩形的方法
            即f(x)=f(x-1)+f(x-2)
        再处理好边界值，f(0)=0,f(1)=1,f(2)=2
'''


class Solution:
    def rectCover(self, number):
        # write code here
        dp = []
        dp.append(0)
        dp.append(1)
        dp.append(2)

        if number <= 2:
            return dp[number]

        for i in range(3, number + 1):
            dp.append(0)
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[number]


s = Solution()
print s.rectCover(5)  # 8



