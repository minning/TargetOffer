# coding:utf-8
'''
    author : minning 
    Date : 2017/9/23
    題目：打印乘法竖式


          4321
           103
        ------
         12963
        4321
        ------
        445063

'''


def mul(a, b):
    bm = b / 10
    bn = b % 10
    result = a * b
    length = len(str(result))

    print ' ' * (length - len(str(a))) + str(a)
    print ' ' * (length - len(str(b))) + str(b)
    print '-' * length

    if b < 10:
        mid_result = b * a
        print ' ' * (length - len(str(mid_result))) + str(mid_result)

    i = 0
    while bm != 0:
        if bn == 0:
            b = (b - bn) / 10
            bm = b / 10
            bn = b % 10
            i += 1
            continue
        mid_result = bn * a
        num = (length - len(str(mid_result))-i)
        print ' ' * num + str(mid_result)
        b = (b - bn) / 10
        bm = b / 10
        bn = b % 10
        i += 1
    if bm==0 and bn!=0:
        mid_result = bn * a
        print ' ' * (length - len(str(mid_result))-i) + str(mid_result)


    print '-' * length
    print result
mul(4321, 103)
