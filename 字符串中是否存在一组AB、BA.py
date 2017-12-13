# coding:utf-8
'''
    author : minning 
    Date : 2017/12/13
    代码目的：对于一个字符串，其中字符均属于"A-Z"之间，判断字符串中是否至少包含一组 "AB"、"BA"，且不能重叠
            如 'ABAAB'、'ABBA'、'ABBBAB'合格
                'ABA' 不合格
'''
def ABBAinstr(s):
    f = {'AB':'BA', 'BA':'AB'}
    dt = {}

    for i in range(len(s)-1):
        if f.get(s[i]+s[i+1], -1) in dt:
            dt[s[i] + s[i + 1]] = i
            if abs(i-dt[f[s[i]+s[i+1]]]) >1:
                return True
        else:
            if (s[i]+s[i+1] == 'AB') or (s[i]+s[i+1] == 'BA'):
                dt[s[i]+s[i+1]] = i

    return False

print ABBAinstr('ABAAB')
print ABBAinstr('ABBA')
print ABBAinstr('ABA')
print ABBAinstr('ABBBAB')