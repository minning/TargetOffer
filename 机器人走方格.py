# coding:utf-8
'''
    author : minning 
    Date : 2017/12/22
    题目：有一个 XxY 的网格，一个机器人只能走格点且只能向右或向下走，要从左上角走到右下角。
        请设计一个算法，计算机器人有多少种走法。给定两个正整数 int x,int y，请返回机器人的走法数目。
        保证 x＋y 小于等于 12。
    解法：动态规划问题，f(x,y) = f(x-1,y) + f(x,y-1)
    
'''

class Robot:
    def countWays(self, x, y):
        if x==0 or y==0:
            return 0
        if x==1 or y==1:
            return 1
        return self.countWays(x-1,y)+self.countWays(x,y-1)

s = Robot()
print s.countWays(4, 5)
