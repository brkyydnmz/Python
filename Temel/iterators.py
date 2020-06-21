# -*- coding: utf-8 -*-

#elimizde bir liste var o listenin elemanlarını tektek dolaşma yöntemidir iterasyon mesela for arkaplanda bi iteratördür
# biz liste tanımladık ama hepsi olur

sehirler = ["Ankara","İstanbul","İzmir","Bandırma"]
            
iteratorum = iter(sehirler)

print(next(iteratorum)) # next sırasıyla tek tek yazdırır
print(next(iteratorum))
print(next(iteratorum))
print(next(iteratorum))

for sehir in sehirler: 
    print(sehir)
