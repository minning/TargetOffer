# coding:utf-8
'''
    Author:minning
    Date:2018/1/8
    剑指offer 第 22 题：栈的压入弹出序列
            题目：输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。
                  假设压入栈的所有数字均不相等。例如序列 1,2,3,4,5 是某栈的压入顺序，
                  序列 4,5,3,2,1 是该压栈序列对应的一个弹出序列，但 4,3,5,1,2 就不可能是该压栈序列的弹出序列。
                  （注意：这两个序列的长度是相等的）
'''


class Solution:
    def IsPopOrder(self, pushV, popV):
        ls = []
        while popV:
            if pushV and pushV[0] == popV[0]:
                pushV.pop(0)
                popV.pop(0)
            elif ls and ls[-1] == popV[0]:
                ls.pop()
                popV.pop(0)
            elif pushV:
                ls.append(pushV.pop(0))
            else:
                return False
        return True
