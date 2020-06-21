# -*- coding: utf-8 -*-

sehirler = ["Ankara","İstabul","İzmir"]

for sehir in sehirler:
    if sehir == "İstanbul":  # != demek şehir ankaradan farklıysa demek (eşit değilse),== (eşittir işareti)
        continue #sadece sadece istanbul için kod yazmaz 
        break # break kırar devamını yazdırmaz break döngüyü bitirir
    print(sehir + " için kod = " + sehir[0:3])
    print("********")


for x in range(1,10,2): #range kadar demek sonuncuyu dahil etmez 1 den başladı 10 a kadar 2 şer 2 şer arttırdı
    print(x) 