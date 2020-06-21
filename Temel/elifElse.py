# -*- coding: utf-8 -*-

lights = ["red","yellow","pink"]

currentLight = lights[2]

print(currentLight)

if currentLight == "red":
    print("STOP!") 
elif currentLight == "yellow":              #elif i değilse gibi düşünebiliriz.
    print("READY!")  
else:                    #if ve elifle bi işlem gerçekleşmezse else kullanılır.
    print("GO!")