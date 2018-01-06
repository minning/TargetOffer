# coding:utf-8
'''
    author : minning 
    Date : 2018/1/6
    代码目的：剑指offer 第 18 题：树的子结构
            题目：输入两棵二叉树 A，B，判断 B 是不是 A 的子结构。（ps：我们约定空树不是任意一个树的子结构）
            思路：定义两个函数，一个用来判断后者是否为前者的子结构（无限制），
                 一个也是用来判断后者是否为前者子结构（限制条件为当前从头结点开始比较，虚一一对应）

'''


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        ret = False

        if (pRoot1 != None) and (pRoot2 != None):
            if pRoot1.val == pRoot2.val:
                ret = self.HasHeadSubtree(pRoot1, pRoot2)
            if not ret:
                ret = self.HasSubtree(pRoot1.left, pRoot2)
            if not ret:
                ret = self.HasSubtree(pRoot1.right, pRoot2)

        return ret

    # 判断从头结点开始pRoot2是否为pRoot1的子结构
    # 其中下式中if必须按照这个顺序，因为一旦判断pRoot2为空，则返回True
    def HasHeadSubtree(self, pRoot1, pRoot2):

        if pRoot2 == None:
            return True
        if pRoot1 == None:
            return False
        if pRoot1.val != pRoot2.val:
            return False

        return self.HasHeadSubtree(pRoot1.left, pRoot2.left) and self.HasHeadSubtree(pRoot1.right, pRoot2.right)


