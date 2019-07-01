'''Write function that takes two args: list of strings 
and a prefix (string). The function should iterate over the list and find all strings which start 
with the prefix, then return list of such strings'''


def Qsn(list,prefix):
    Lp=len(prefix)
    NewList=[]
    for i in list:
        if i[:Lp]==prefix:
            NewList.append(i)
    return NewList

list= ['aaa1aa12', 'a1aaaa22','adaaaa12','aaafaa12','aaaaa812']
prefix='aaaaa'
Ans=Qsn(list,prefix)
print(Ans)