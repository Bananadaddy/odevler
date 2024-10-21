#Make a program that counts a number's square and root
import math

def kare_ve_kok(sayi):
    kare = sayi ** 2 #Sayi power of 2
    karekok = math.sqrt(sayi)

    return kare, karekok

#Ask user for start and end numbers
baslangic = int(input("Baslangic sayisini girin: "))
bitis = int(input("Bitis sayisini girin: "))

#Create a table
print(f"{"Sayi":>10} {"Karesi":>10} {"Karekoku":>10}")

for sayi in range(baslangic, bitis + 1):
    kare, karekok = kare_ve_kok(sayi)
    print(f"{sayi:>10} {kare:>10} {karekok:>10.2f}")