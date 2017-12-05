# coding:utf-8
'''
    author : minning 
    Date : 2017/7/23
    代码目的：剑指offer 第 8 题
            题目：把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
            输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
            例如数组 {3,4,5,1,2} 为 {1,2,3,4,5} 的一个旋转，该数组的最小值为 1。
            NOTE：给出的所有元素都大于 0，若数组大小为 0，请返回 0。
    思路：首先这是一个特殊的有序数组，如果直接遍历一遍，找到最小值时间复杂度O(n)，不符合要求
          所以思考采用二分查找的方法，分别包含以下几种情况：
          1）如果数组长度为0，返回0
          2）如果数组第一个元素比最后一个元素小，意味着数组完全翻转（也即没有翻转），
             返回数组第一个元素
          3）使用二分法，构建两个索引，left，right代表左右两端的位置，设mid=(left+right)/2
             设置循环条件right-left>1，即左端点和右端点相距超过1才继续循环：
                 如果mid处的值比右端点的值大，则left=mid
                 如果mid处的值比左端点小，则right=mid
                 如果不满足以上两种情况，即同时满足array[mid]<=right,mid>=left，left>=right，即mid=left=right,
                     则表明左中右重复元素太多且包含最小元素，则遍历这一部分的元素找出最小值
             返回right索引位置的值
'''


class Solution(object):
    def minNumInRotateArray(self,rotateArray):
        if len(rotateArray)==0:
            return 0
        else:
            left = 0
            right = len(rotateArray)-1
            minVal = rotateArray[0]

            if rotateArray[left]<rotateArray[right]:
                return rotateArray[0]
            else:
                while right-left>1:
                    mid = (left+right)/2
                    if rotateArray[mid]<rotateArray[left]:
                        right=mid
                    elif rotateArray[mid]>rotateArray[right]:
                        left=mid
                    else:
                        for item in rotateArray[left:right+1]:
                            if item<minVal:
                                minVal = item
                            return minVal
                return rotateArray[right]

s = Solution()
ls = [4,5,6,1,2,3]
ls2 = [6501,6828,6963,7036,7422,7674,8146,8468,8704,8717,9170,9359,9719,9895,9896,9913,9962,154,293,334,492,1323,1479,1539,1727,1870,1943,2383,2392,2996,3282,3812,3903,4465,4605,4665,4772,4828,5142,5437,5448,5668,5706,5725,6300,6335]
print s.minNumInRotateArray(ls)  # 1
print s.minNumInRotateArray(ls2)  # 154

