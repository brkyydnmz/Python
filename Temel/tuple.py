# -*- coding: utf-8 -*-

#tuple demet demektir
tupleListe = (2,4,6,"Ankara",(2,3,4),[])
liste = [2,4,6,"Ankara",[3,4,5],()]

liste[0] =6

tupleDeger = ("Engin",) #tek elemanlı str sonuna , koyarsak o tek elemanlı tuple olur
print(type(tupleDeger))

print(tupleListe[1:2]) 
print(liste[1:2])

print(tupleListe[-2])  # -2 demek en sağdan 2.demektir.
print(liste[-2])




print(type(tupleListe))
print(type(liste))
print(tupleListe)
print(liste)
print(len(tupleListe))
print(len(liste))

