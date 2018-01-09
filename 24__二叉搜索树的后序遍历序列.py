# coding:utf-8
'''
    Author:minning
    Date:2018/1/9
    剑指offer 第 24 题：二叉搜索树的后序遍历序列
            题目：输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
                  如果是则输出 Yes, 否则输出 No。假设输入的数组的任意两个数字都互不相同。
    
'''


class Solution:
    def VerifySquenceOfBST(self, sequence):
        lens = len(sequence)
        if lens == 0:
            return True
        elif lens == 1:
            return True
        else:
            root = sequence[-1]
            left = 0
            while sequence[left] < root:
                left += 1

            for index in range(left, lens-1):
                if sequence[index] < root:
                    return False
        return self.VerifySquenceOfBST(sequence[:left]) and self.VerifySquenceOfBST(sequence[left:lens-1])


s = Solution()
sequ = [4, 8, 9, 12, 16, 14, 10]
print s.VerifySquenceOfBST(sequence=sequ)
