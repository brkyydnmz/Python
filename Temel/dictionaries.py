# -*- coding: utf-8 -*-

#ingilizce türkçe sözlük gibi düşün
sozluk = {
           "book" : "kitap",
           "table" : "masa",
          }

sozluk2 = dict(kitap ="book", masa = "table")


sozluk["book"] = "kitap 1"
sozluk["pencil"] = "kalem"
del(sozluk["book"]) # book ve anlamını siler
print(sozluk)
print(len(sozluk))


