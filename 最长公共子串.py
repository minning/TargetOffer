# coding:utf-8
'''
    author : minning 
    Date : 2017/12/21
    代码目的：找出两个字符串s1和s2的最长公共子串，如 'abcdfg', 'abdfg' 的最长公共子串为 'dfg'
    代码思路：构建一个矩阵来存储s1和s2中字符的匹配情况，矩阵的shape大小为（s1长度+1， s2长度+1），
            依次遍历字符串s1和s2中的字符，若字符相同，则最长子串数为前面匹配数+1，最后遍历结束后最长的即为所求
    
'''
import numpy as np


def lcsubstr(s1, s2):
    arr = np.zeros((len(s1)+1, len(s2)+1))
    mmax = 0  # 最大匹配数
    p = 0  # 当前最大匹配在s1中尾部的位置

    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i]==s2[j]:
                arr[i+1, j+1] = arr[i, j]+1
                if arr[i+1, j+1]>mmax:
                    mmax = int(arr[i+1, j+1])
                    p = i+1
    return s1[p-mmax:p], mmax   # 返回最长子串及其长度


print lcsubstr('abcdfg', 'abdfg')