#substring işlemi
mesaj = "Merhaba dünya"

print(mesaj[2:5])   # : işareti 2 den 5 e kadar anlamına getirir

yeniMesaj = mesaj[ :3]
print(yeniMesaj)

#len
print(len(mesaj))  #len bize uzunluğu verir

yeniMesaj2 = mesaj[len(mesaj)-1:len(mesaj)] 
print(yeniMesaj2)

#lower upper(küçült,büyült)
print(mesaj.upper())
print(mesaj.lower())

#replace
mesaj=mesaj.replace("ü", "u") #bu satırı yazarsan genel olarak bu satırdan sonra hep ü yerine u kullanılır.
print(mesaj.replace("ü", "u"))  #replace değişim yapar ü yü u yaptı burda
print(mesaj)

print(mesaj.replace("a","e"))

#split ve strip
bilgi = " Berkay;Donmez;10;Bandirma " .strip()  # .strip() boşlukları düzeltir baştan sondan boşlukları götürür.
print(bilgi.split())  # .split kelime kelime ayırır boşluğa göre ayırır.
print("Adı = " + bilgi.split(";")[0])

#input kullanıcıdan girdi almaya yarar
ad = input ("Adınız?")
sayi1 = input("Sayı 1 =? ")
sayi2 = input("Sayı 2 =? ") #input metin toplaması yapar yani yan yana getirir.1020 der.
print(int(sayi1) + int(sayi2)) #int dediğimizde sayı gibi toplar 30 yani.
