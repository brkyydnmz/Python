# -*- coding: utf-8 -*-

ogrenciler = ["Engin","Derin","Salih","Ali","Ayse"]


fileToAppend = open("ogrenciler.txt","a")

for ogrenci in ogrenciler:
    fileToAppend.write(ogrenci)
    fileToAppend.write("\n")
    
fileToAppend.close()