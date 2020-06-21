# -*- coding: utf-8 -*-

#%%
sehir = "Ankara"

sonuc = sehir.upper()
print(sonuc)
print(sehir.endswith("e"))
#%%
def selamVer(isim = "ziyaretçi"):          #selamVer in ardından gelen parantez içine parametre yazılır
    print("Merhaba " + isim)

selamVer()
selamVer("Engin")
selamVer("Derin")
selamVer("Salih")
selamVer("Ahmet")
selamVer("Mehmet")
selamVer()

def selamVer2(isim , soyIsim = "arkadaş"):  #default değer her zaman fonksiyonda sonda olmalı burda mesela sadece soyIsim e değer versek olurdu başa verilmez
    print("Merhaba " + isim + " " + soyIsim)

selamVer2("Derin")
selamVer2("Engin","Demiroğ")  



#%%
def dikUcgenAlaniHesapla(a,b):
    return a*b/2              #return fonksiyonun geriye herhangi bir değer döndürmesini sağlar.Bu şekilde fonksiyonun döndürdüğü değeri yazdırmış olduk.

alan = dikUcgenAlaniHesapla(3,6)

print(alan)

#%%
dikUcgenAlaniHesapla2 = lambda a,b : a*b/2  #lambda tek satırda yazmak için pratiklik sağlar.return ün kolay yolu gibi
                                             #etiket = lambda parametre1,parametre2.... :  İşlem
print(dikUcgenAlaniHesapla2(3, 6))

print(type(dikUcgenAlaniHesapla2))

x = dikUcgenAlaniHesapla2

print(x(4,5))


