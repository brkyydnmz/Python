# -*- coding: utf-8 -*-

try: # try bunu yapmaya çalış demektir
    sayi = int(input("Sayı giriniz"))
except (ValueError,ZeroDivisionError): # except ValueError eğer ValueError hatası alırsan demek
    print("Tip uyuşmazlığı : Lütfen sayı giriniz") # yukarıdaki ,virgül her 2 sinden biri olursa bunu yazdır demek
except ZeroDivisionError: 
    print("Payda sıfır olamaz")        
except: # except hata olursa ne yapayım demektir 
    print("Bir hata oluştu")
    


print("Bitti")
