# coding:utf-8
'''
    代码目的：剑指offer 第 5 题
            题目：输入一个链表，从尾到头打印链表每个节点的值。
            思路：新建一个空列表，从头到尾依次存放链表中的每一个元素
                然后倒序输出列表中的元素
    
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        ls = []

        if listNode is None:
            return ls

        while listNode.next:
            ls.append(listNode.val)
            listNode = listNode.next

        ls.append(listNode.val)

        return ls[::-1]

s = Solution()
l1 = ListNode('a')
l2 = ListNode('b')
l3 = ListNode('c')
l1.next = l2
l2.next = l3
print s.printListFromTailToHead(l1)
# ['c', 'b', 'a']
