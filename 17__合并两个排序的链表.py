# coding:utf-8
'''
    Author:minning
    Date:2018/1/5
    代码目的：剑指offer 第 17 题
            题目：输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
            思路：新建一个链表保存结果，依次遍历比较两个链表头结点的节点大小，将较小的节点添加入结果链表中，
                  节点较小的链表指向下一个节点，直到两个链表中有一个为空，则将另一个链表添加入结果链表中

'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        merge = ListNode(0)
        last = merge

        while pHead1 and pHead2:
            if pHead1.val <= pHead2.val:
                last.next = pHead1
                pHead1 = pHead1.next
            elif pHead1.val > pHead2.val:
                last.next = pHead2
                pHead2 = pHead2.next
            last = last.next

        if not pHead1:
            last.next = pHead2
        elif not pHead2:
            last.next = pHead1

        return merge.next
