# coding:utf-8
'''
    author : minning 
    Date : 2017/8/20
    二叉树的递归方法
    https://sagittariusyx.github.io/2016/07/22/Python-binary-tree-traverse/
'''


class BinTree(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def setLeft(self, left):
        self.left = left

    def setRight(self, right):
        self.right = right


def preOrder( root):
    if not root:
        return
    print root.val
    preOrder(root.left)
    preOrder(root.right)

def midOrder(root):
    if not root:
        return
    midOrder(root.left)
    print root.val
    midOrder(root.right)

def postOrder( root):
    if not root:
        return
    postOrder(root.left)
    postOrder(root.right)
    print root.val

a = BinTree('a')
b = BinTree('b')
c = BinTree('c')
d = BinTree('d')
e = BinTree('e')

a.setLeft(b)
a.setRight(c)
b.setLeft(d)
b.setRight(e)

preOrder(a)
print "*"*20
midOrder(a)
print "*"*20
postOrder(a)