# coding:utf-8
'''
    author : minning 
    Date : 2018/1/16
    代码目的：剑指offer 第 25 题：二叉树中和为某一值的路径
            题目：输入一颗二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
                  路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
            思路：利用递归的思路寻找当前结点的左右子树中路劲和为所需整数减去根节点值的路径
'''


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        if root and (not root.left) and (not root.right) and root.val == expectNumber:
            return [[root.val]]
        left = self.FindPath(root.left, expectNumber - root.val)
        right = self.FindPath(root.right, expectNumber - root.val)

        ret = []
        for i in left + right:
            ret.append([root.val] + i)
        return ret
