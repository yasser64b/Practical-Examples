phone_letters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(len(phone_letters))
phone_digits='2223334445556667777888999922233344455566677778889999'
phone_mapping=str.maketrans(phone_letters,phone_digits)
phone=input('Phone number:')
digits=phone.translate(phone_mapping)
print(digits)



def PhNum(PhNumber):
    Num=PhNumber.split('-')
    AreaCod=Num[0]
    Num_code=Num[1:]
    Number=''
    for n in Num_code:
        for i in range (len(n)):
            if n[i] in 'ABC':
                Number=Number+'2'
            elif n[i] in 'DEF':
                Number=Number+'3'
            elif n[i] in 'GHI':
                Number=Number+'4'
            elif n[i] in 'JKL':
                Number=Number+'5'
            elif n[i] in 'MNO':
                Number=Number+'6'
            elif n[i] in 'PQRS':
                Number=Number+'7'
            elif n[i] in 'TUV':
                Number=Number+'8'
            elif n[i] in 'WXY':
                Number=Number+'8'
        Number=Number+'-'
    return AreaCod+'-'+Number[:-1]

PhNumber='555-GET-FOOD'
# PhNumber.split('-')
N=PhNum(PhNumber)
print(N)