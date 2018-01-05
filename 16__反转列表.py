# coding:utf-8
'''
    Author:minning
    Date:2018/1/5
    代码目的：剑指offer 第 15 题
            题目：输入一个链表，反转链表后，输出链表的所有元素。
            思路：反转链表就得依次遍历链表，然后头结点指向下一节点，当前节点指向反转后的链表
            代码中temp用来保存当前节点后的链表，last代表反转后的链表（初始为None），pHead始终当前节点
            每反转一个结点，把 pHead 结点的下一个结点指向 last, last 指向 pHead 成为反转后首结点, 再把 pHead 向前移动一个结点直至 None 结束
'''


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if (not pHead) or (not pHead.next):
            return pHead

        last = None

        while pHead:
            temp = pHead.next
            pHead.next = last
            last = pHead
            pHead = temp

        return last
