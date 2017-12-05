# coding:utf-8
'''
    代码目的：剑指offer 第 7 题
            题目：用两个栈来实现一个队列，完成队列的 Push 和 Pop 操作。
                  队列中的元素为 int 类型。
            思路：创建两个列表，stack1和stack2，
                stack1用来接收数据，stack2用来周转
                1）对于push操作，直接stack1列表的append方法就好了
                2）对于pop操作，为了实现队列的先进先出操作，需要分为三种情况：
                    A:如果stack1 和 stack2中均不包含元素，则return None
                    B:如果stack2中包含元素，则直接return stack2 pop出的元素
                    C:如果stack2中没有元素，意味着stack2作为缓冲区中已经没有元素了，
                       需要从stack1中获取新元素，而获取新元素就得同时获取完stack1中所有元素
                       这样通过stack2的pop操作才能实现队列的先进先出操作
'''


class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        self.stack1.append(node)

    def pop(self):
        if not self.stack1 and not self.stack2:
            return None
        if len(self.stack2) > 0:
            return self.stack2.pop()
        else:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()

s = Solution()
s.push("1")
s.push('2')
print s.pop()
print s.pop()
s.push('3')
s.push('4')
s.push('5')
print s.pop()
s.push('6')
print s.pop()
# 1
# 2
# 3
# 4
