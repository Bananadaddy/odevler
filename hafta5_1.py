#Global degisken tanimlamasi
yonetici_mi = False

#Fonksiyon: Calisanin toplam maasini hesaplar
#(prim sadece yonetici ise eklenir)
def maas_hesapla(sabit_maas, prim):
    if yonetici_mi:
        return sabit_maas + prim
    else:
        return sabit_maas


#Fonksiyon: yoneticilik durumunu gunceller
def yonetici_durumunu_ayarla(durum):
    global yonetici_mi
    yonetici_mi = durum

#Testler
#1. Calissan yonetici degilken
yonetici_durumunu_ayarla(False)
print(maas_hesapla(5000, 1000))

#2. Calisan yonetici iken
yonetici_durumunu_ayarla(True)
print(maas_hesapla(5000, 1000))