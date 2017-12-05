# coding:utf-8
'''
    author : minning 
    Date : 2017/7/23
    代码目的：剑指offer 第 9.2 题
            题目：一只青蛙一次可以跳上 1 级台阶，也可以跳上 2 级。
                 求该青蛙跳上一个 n 级的台阶总共有多少种跳法
            思路：使用动态规划方法，
                 当n=0时，有0种跳法
                 当n=1时，有1种跳法
                 当n=2时，有2种跳法
                 ...

                 当n很大时，等于n-1时的跳法数再跳一级台阶加上n-2时的跳法数再跳两层台阶
                 即f(n)=f(n-1)+f(n-2)  n>2
'''


# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):

        dp = []
        dp.append(0)
        dp.append(1)
        dp.append(2)

        if number <= 2:
            return dp[number]
        for i in range(3, number + 1):
            dp.append(0)
            for j in range(1, 3):
                dp[i] += dp[i - j]
        return dp[number]

s = Solution()
print s.jumpFloor(5)  # 8
