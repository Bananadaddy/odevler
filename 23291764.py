import random

congratulations = ["Çok iyi!", "Doğru cevap!", "Bravo, doğru bildin!"]
condolences = ["Hayır. Lütfen tekrar deneyin.", "Yanlış. Bir kez daha deneyin.", "Denemeye devam edin."]

#Determine the level of questions
zorluk_seviyesi = int(input("Choose level of questions (1 or 2): "))
if zorluk_seviyesi != 1 and zorluk_seviyesi != 2:
    while True:
        zorluk_seviyesi = int(input("Choose level of questions (1 or 2): "))
        if zorluk_seviyesi == 1 or zorluk_seviyesi == 2:
            break
        
#Make function to generate random number
def random_generate_easy():
    sayi1 = random.randrange(1, 10)
    sayi2 = random.randrange(1, 10)
    return sayi1, sayi2

def random_generate_hard():
    sayi1 = random.randrange(10, 20)
    sayi2 = random.randrange(10, 20)
    return sayi1, sayi2

while True:
    if zorluk_seviyesi == 1:
        s1, s2 = random_generate_easy()
    elif zorluk_seviyesi == 2:
        s1, s2 = random_generate_hard()
    
    correct_answer = s1 * s2
    print(f'{s1} kere {s2} kaç eder?')
    while True: 
        cevap = int(input("Cevabınızı girin ya da çıkmak için -1 girin: "))
        if cevap == -1:
            print("Çıkış yapıldı")
            break
        elif cevap == correct_answer:
            print(congratulations[random.randrange(0, 3)])
            break
        else:
            print(condolences[random.randrange(0, 3)])

    devam_et = input('Başka bir çarpma sorusu çözmek ister misin? (e/h) ').lower()
    if devam_et != 'e':
        print('Çalıştığın için teşekkürler! Hoşça kal.')
        break