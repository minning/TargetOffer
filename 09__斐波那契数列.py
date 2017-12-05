# coding:utf-8
'''
    author : minning 
    Date : 2017/7/23
    代码目的：剑指offer 第 9 题
            题目：大家都知道斐波那契数列，现在要求输入一个整数 n，
                请你输出斐波那契数列的第 n 项。n<=39
                数列如下：0 1 1 2 3 5 8 ...
    
'''
class Solution(object):
    def fib_recru(self,n):
        '''
        递归方法，思路简单，但是不能通过在线测试，
        因为复杂度高，做了很多重复运算
        '''
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            return self.fib_recru(n-1)+self.fib_recru(n-2)

    def fib_dp(self,n):
        '''
            动态规划方法，依次保存前面的结果，复杂度低
        '''
        dp = [0, 1, 1]

        for index in range(3, n + 1):
            dp.append(0)
            dp[index] = dp[index - 1] + dp[index - 2]

        return dp[n]

s = Solution()
print s.fib_recru(5)
print s.fib_dp(5)
