# -*- coding: utf-8 -*-
#%%
import sqlite3

def selectOperasyonlari():
    connection = sqlite3.connect("chinook.db")
    
    cursor = connection.execute("""select FirstName,LastName 
                                    from customers 
                                    where city='Prague' or city='Berlin' 
                                    order by FirstName,LastName desc""")


# DİKKAT! sonda desc demezsek a-z alfabetik sırada sıralar sqlite3
# DİKKAT! order by LastName desc dersek tersten sıralar, baştaki FirstName eğer aynı isimde birileri varsa soyada göre tersten sırala demek
#order by .....   . yerine ne yazarsak ona göre sıralar alfabetik 
#execute içine baş ve sonda 3 " çift tırnak koyarsak satıları alt alta devam ettirebiliriz.
#cursor sorgulama 
#FirstName,LastName yerine * koyabiliriz  
# * kolonların tümü demek 
# üstteki selecten sonra * yerine sütun ismini de yazabilirsin FirstName,LastName gibi.
#Prague nin string olduğunu söylemek için ' '(tek tırnak) içine yazarız.
#or yada anlamındadır and kullanırsak ta ve kullanırız.tüm eylemlerde  



    for row in cursor:
              print("First Name = "+row[0])
              print("Last Name = "+row[1])
              print("*********")
    
    connection.close() 

selectOperasyonlari()

#row satır demektir
# row 1(sayıyı değiştirerek sütunu değiştirebilirsin) customersdaki first name satırından sütünları alır
#üstte row un 0 dan başlama nedeni select first name dediğimiz için 1.sütun first name dir
#%%
import sqlite3

connection = sqlite3.connect("chinook.db")

cursor = connection.execute("""select city,count(*) from customers
                            group by city having count(*)>1
                            order by count(*)""")

 
#count(*)'da * sütun farketmezsizin satır sayısı. Yani kayıt sayısı. count(city) şehir kayıt sayısı. Ama şehir boş ise onları saymaz.
#üstte yazılan:şehre göre grupla sayısı 1 den fazla olanları bana ver
#group by gruplama yapar
#count(*) city deki tüm kolonlar

for row in cursor:
          print("City = "+row[0])
          print("Count = "+str(row[1]))
          print("*********")

connection.close() 

#%%

import sqlite3

connection = sqlite3.connect("chinook.db")

cursor = connection.execute("""select FirstName,LastName 
                                from customers 
                                where FirstName like'%a%' """)

# a% dersek ismi a ile başlayanlar, %a ise ismi a ile bitenler demektir
# %a% içerisinde a geçenler demektir. % ifadeleri başının ve sonunun önemsiz olduğunu gösterir.
# like komutu ismi içerisinde a olanlar ab olanlar gibi aramalar için kullanırız
# like zaten gibi demektir

for row in cursor:
          print("First Name = "+row[0])
          print("Last Name = "+row[1])
          print("*********")

connection.close() 

#%%

import sqlite3

def InsertCustomer():
    connection = sqlite3.connect("chinook.db")
    connection.execute("""insert into customers
                       (firstName,lastName,city,email)
                       values('Berkay','Dönmez','Bandırma','berkaydonmez01@hotmail.com')""")
    connection.commit()
    connection.close()

InsertCustomer()   

# insert ekleme yapar 
# commit() girilen verileri işleyebilmek için

#%%

import sqlite3

def updateCustomer():
    connection = sqlite3.connect("chinook.db")
    connection.execute("""update customers set city='Bandırma'
                       where city='İstanbul'""")
    
    
    connection.commit()
    connection.close()

updateCustomer()

#update güncelleme yapar

#%%

import sqlite3

def deleteCustomer():
    connection = sqlite3.connect("chinook.db")
    connection.execute("""delete from customers
                       where city='Bandırma'""")
    
    connection.commit()
    connection.close()   
      
deleteCustomer()

#delete veri tabanından siler

#%%

import sqlite3

def joinOperasyonlari():
    connection = sqlite3.connect("chinook.db")
   
    cursor=connection.execute("""select albums.Title, 
                       artists.Name from artists 
                       inner join albums
                       on artists.ArtistId = albums.ArtistId""")

    for row in cursor:
                  print("Title = "+row[0]+" Name = "+row[1])
      
    connection.close()               
     
joinOperasyonlari()

#join 2 veya daha fazla tabloyu birbirine birleştirmek için
