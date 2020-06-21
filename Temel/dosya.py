# -*- coding: utf-8 -*-

f = open("musteriler2.txt") #f file dan gelir
#print(f.read())  # .read okur read den sonra parantez içine sayı girersen  o sayı kadar karakter okur
print("***************")

print(f.readline())    # readline satır satır okur read ile tümünü okur

for l in f:     # bütün line(l)ları gezer
    print(l) 

f.close()

#r Read(okuma) 
#w Write(yazma) yoksa yeni dosya oluşturuyor dosyanın üzrenine yazma anlamı yeni veriler aktif olur eskiler silinir
#a Append  yazma yetkisi verir yeni datalar ekleyebilir
#x creat dosya yoksa oluşturur varsa hata verir

#ya read i kullanırız ya readline ı yada for döngüsünü kullanırız


fileToAppend = open("ogrenciler.txt","w")
fileToAppend.write("\n") # \n satır sonu yapar alt satır geçirir
fileToAppend.write("Ahmet")
fileToAppend.close() # dosyayı kapatır bir nevi kaydedip çıkar 


#%%
import os 

if os.path.exists("ogrenciler.txt"):
    os.remove("ogrenciler.txt") #dosyayı siler tamamen
else:
    print("Dosya yok")
    
os.rmdir("empty") #direk klasörü siler
