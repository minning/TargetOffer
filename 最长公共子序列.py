# coding:utf-8
'''
    author : minning 
    Date : 2017/12/21
    代码目的：
    
'''


class LCS:
    def lcs_base(self, input_x, input_y):
        if len(input_x) == 0 or len(input_y) == 0:
            return ""
        else:
            a = input_x[0]
            b = input_y[0]
            if a == b:
                return self.lcs_base(input_x[1:], input_y[1:]) + a
            else:
                # get the max one
                return self.getMax(self.lcs_base(input_x[1:], input_y), self.lcs_base(input_x, input_y[1:]))
    # construct a list by the input string
    def getList(self, inputStr):
        listRes = list()
        if len(inputStr) != 0:
            for i in range(0, len(inputStr)):
                listRes.append(inputStr[i])
        return listRes
    # return the max one between a and b, equivalently return the longest one
    def getMax(self, a, b):
        if len(a) >= len(b):
            return a
        else:
            return b
if __name__ == '__main__':
    lcs = LCS()
    l1 = lcs.getList('我的大中国')
    l2 = lcs.getList('大中国我的')
    l3 = lcs.lcs_base(l1, l2)
    print(l3[::-1])
    l3 = lcs.lcs_base(l2, l1)
    print(l3[::-1])
    l1 = '1233433236676'
    l2 = '98723765655423'
    l3 = lcs.lcs_base(l1, l2)
    print(l3[::-1])
    l1 = '123s212346我的大中国啊33z'
    l2 = '33z的大中国'
    l3 = lcs.lcs_base(l1, l2)
    print(l3[::-1])

