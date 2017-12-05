# coding:utf-8
'''
    author : minning 
    Date : 2017/7/25
    代码目的：剑指offer 第 15 题
            题目：输入一个链表，输出该链表中倒数第 k 个结点。
            思路：使用两个指针left，right都指向链表的头部head
                然后right向后先走k步，接着left、right同时向后走
                知道right走到头，此时left就是链表倒数第k个节点
    
'''

class listNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution(object):
    def FindKthToTail(self, head, k):
        left = head
        right = head

        if (not head) or (k<=0):
            return None
        else:
            for i in range(k-1):
                if not right.next:
                    return None
                else:
                    right = right.next

            while right.next:
                right = right.next
                left = left.next

            return left


s = Solution()
l1 = listNode('1')
l2 = listNode('2')
l3 = listNode('3')
l4 = listNode('4')
l1.next = l2
l2.next = l3
l3.next = l4
print s.FindKthToTail(l1, 2).val  # 3
