# coding:utf-8
'''
    author : minning 
    Date : 2017/7/23
    代码目的：剑指offer 第 11 题
            题目：给定一个 double 类型的浮点数 base 和 int 类型的整数 exponent。
                求 base 的 exponent 次方。
    
'''


class Solution:
    def Power(self, base, exponent):
        # write code here
        flag = 1
        if exponent<0:
            flag = -1
            exponent = -1*exponent
        if exponent==0:
            if base == 0:
                return 0
            else:
                return 1
        else:
            if exponent == 1:
                return base
            ret = self.Power(base, exponent>>1)
            ret *= ret
            if exponent%2 == 1:
                ret *= base
        if flag==1:
            return ret
        else:
            return 1.0/ret


    def pow2(self, base, exponent):
        if exponent == 0:
            return 1
        elif exponent == 1:
            return base
        elif exponent == -1:
            return 1.0/base

        ret = self.pow2(base, exponent>>1)
        ret *= ret
        if exponent%2==1:
            ret *= base
        return ret


s = Solution()
print s.pow2(2,3)