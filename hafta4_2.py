#Finding the biggest number

#This function finds the biggest number taking in 3 number
def en_buyuk(deger1, deger2, deger3):
    
    en_buyuk_deger = deger1
    if deger2 > en_buyuk_deger:
        en_buyuk_deger = deger2
    if deger3 > en_buyuk_deger:
        en_buyuk_deger = deger3
    return en_buyuk_deger 

a1 = input()
a2 = input()
a3 = input()

print(en_buyuk(a1, a2, a3))