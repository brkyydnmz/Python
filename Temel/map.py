# -*- coding: utf-8 -*-

sayilar = [1,2,3,4,5]

sayilarKareli = list(map(lambda sayi: sayi**2,sayilar)) #sayilar listesi içinde her bir sayının karesini al ve iterate ettiğin her bir değeri listeye ekle demek bu satır
   # alttaki for düngüsü de üstteki map ile aynı işi yapar
# for sayi in sayilar:
#     sayilarKareli.append(sayi*sayi) 
    
sayilarFiltreli = list(filter(lambda sayi : sayi>2,sayilar))  # filter sayilarda her bir sayı için sayi eğer 2 den büyükse onu listeye ekle demektir

print(sayilarKareli)
print(sayilarFiltreli)

from functools import reduce
sayilarFaktoriyel =  reduce(lambda x,y:x*y,sayilar) # başta x ilk sayı y ikinci sayı

# 1 çarpı 2 =2 olunca x=2 olup y=3 oluyor =6
#x=6 olup y=4 oluyor= 24
#x=24 olup y=5 olup = 120 oluyor bu şekilde çalışır reduce fonksiyonu
#x le y nin çarpımı bir sonraki x oluyor diyebiliriz.

print(sayilarFaktoriyel)