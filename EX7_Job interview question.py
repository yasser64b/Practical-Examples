# A= 'AAAAaaBCCCDDe'  A='A4a2B1C3D2e1' 
def SortSt(A):
    A=A+' '
    R=''
    j=0
    for i in range (len(A)):
        if A[i]!=A[j]:
            r=A[i-1]+str(i-j)
            j=i
            R=R+r
    return R


A= 'AAAAAaaBBBBCCCDDe'
R=SortSt(A)
print(R)