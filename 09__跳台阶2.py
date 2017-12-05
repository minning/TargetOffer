# coding:utf-8
'''
    author : minning 
    Date : 2017/7/23
    代码目的：剑指offer 第 9.3 题
            题目：一只青蛙一次可以跳上 1 级台阶，也可以跳上 2 级…… 它也可以跳上 n 级。
            求该青蛙跳上一个 n 级的台阶总共有多少种跳法。
    思路： 使用动态规划方法，
             当n=0时，有0种跳法
             当n=1时，有1种跳法
             当n=2时，有2种跳法
             ...

             当n很大时，等于n-1时的跳法数再跳一级台阶加上n-2时的跳法数再跳两层台阶。。。加上n-(n-1)时的跳法再跳n-1层台阶，再加上1
             即f(n)=f(n-1)+f(n-2)+...f(1)+1  n>2
             PS:上式中+1代表直接跳n层台阶这种玩法
'''

class Solution(object):
    def jumpFloor2(self, n):
        dp = []
        dp.append(0)
        dp.append(1)
        dp.append(2)

        if n<=2:
            return dp[n]

        for i in range(3,n+1):
            dp.append(0)
            for j in range(1,n+1):
                if j<i:
                    dp[i] += dp[j]
            dp[i] += 1
        return dp[n]

    def jumpFloor3(self,n):
        '''
            使用数学归纳法计算出跳n个台阶可能的情况为f(x)=2^(n-1)
        '''
        return 2**(n-1)

s = Solution()
print s.jumpFloor2(16)  # 16

