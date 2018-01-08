# coding:utf-8
'''
    Author:minning
    Date:2018/1/8
    剑指offer 第 23 题：从上往下打印二叉树
            题目：从上往下打印出二叉树的每个节点，同层节点从左至右打印。
'''


class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        ret = []
        quene = []
        quene.append(root)
        if not root:
            return []

        while len(quene) > 0:
            node = quene.pop(0)
            ret.append(node.val)
            if node.left:
                quene.append(node.left)
            if node.right:
                quene.append(node.right)

        return ret
