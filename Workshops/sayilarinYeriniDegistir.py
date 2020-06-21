# -*- coding: utf-8 -*-

x = 10
y = 20

x,y = y,x # bu da sayıları değiştirir

temp = x  #temp te sayıları değiştirir
x = y
y = temp

print("x = " + str(x))
print("y = " + str(y))