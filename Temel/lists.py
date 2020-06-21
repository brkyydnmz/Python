# -*- coding: utf-8 -*-

#listeler değiştirilir tuplelar değiştirilmez.
ogrenci1 = "Engin"
ogrenci2 = "Derin"
ogrenci3 = "Salih"

ogrenciler = ["Engin","Derin","Salih"]


ogrenciler.append("Ahmet") # append ekleme yapar.
ogrenciler[0] = "Veli"
print(ogrenciler[3])
ogrenciler.remove("Salih")  # .remove kaldırır.
print(ogrenciler)

#list liste oluşturucudur
sehirler = list(("Ankara","İstanbul","Ankara"))
print(len(sehirler)) #len kaç elemandan oluştuğunu gösterir.

#diğer fonksiyonlar
 #print(sehirler.clear()) # .clear ile liste temizler
print("Ankara sayısı = " + str(sehirler.count("Ankara"))) # .count kaç tane olduğunu gösterir.
print("Ankara indexi = " + str(sehirler.index("Ankara")))  # .index ankarayı bulur ilk nerde bulursa orda durur
sehirler.pop(1) # .pop ta 1 deki sehiri kaldırır elle yazmayız remove gibi.
sehirler.insert(0,"İstanbul") # .insert 0.index e ekleme yapar.
sehirler.reverse() # .reverse ters çevirir.
print(sehirler)

sehirler3= sehirler.copy() # .copy direk kopya aldı.

sehirler2 = sehirler #  = ile sehirlerin yedeğini aldık aynısı.
sehirler2[0]="İzmir"


print(sehirler)
print(sehirler2)
print(sehirler3)

sehirler.extend(sehirler3) # .extend birleştirir.
sehirler.sort() # .sort alfabetik yada sayısal listelemeye yarar. a-z
sehirler.reverse() # .reverse tersten yazdırır. z-a
print(sehirler)

