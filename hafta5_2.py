import random

def carpim(*argumanlar):
    sonuc = 1
    for sayi in argumanlar:
        sonuc = sonuc * sayi
    return sonuc

print(carpim(1, 2, 3, 4, 5))
print(carpim(8, 9))
liste = [1, 2, 3, 4]
print(carpim(*liste))

def random_generate():
    sayi1 = random.randrange(1, 10)
    sayi2 = random.randrange(1, 10)
    return sayi1, sayi2

congratulations = ["Çok iyi!", "Doğru cevap!", "Bravo, doğru bildin!"]
condolences = ["Hayır. Lütfen tekrar deneyin.", "Yanlış. Bir kez daha deneyin.", "Denemeye devam edin."]

print(congratulations[2])