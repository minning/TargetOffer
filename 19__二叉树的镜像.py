# coding:utf-8
'''
    author : minning 
    Date : 2018/1/7
    代码目的：剑指offer 第 19 题：二叉树的镜像
            题目：操作给定的二叉树，将其变换为源二叉树的镜像。
            输入描述:
            二叉树的镜像定义：源二叉树
                        8
                       /  \
                      6   10
                     / \  / \
                    5  7 9 11
                    镜像二叉树
                        8
                       /  \
                      10   6
                     / \  / \
                    11 9 7  5
            思路：递归的将当前节点的左右子结点进行替换即可

'''


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        if root == None:
            return None
        temp = root.left
        root.left = self.Mirror(root.right)
        root.right = self.Mirror(temp)

        return root
