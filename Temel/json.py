# -*- coding: utf-8 -*-

import json

data = '{"firstName":"berkay","lastName":"dönmez"}'

y = json.loads(data) # .loads veriyi alır.

print(y["firstName"])
print(y["lastName"])

customer = {
    "firstName":"berkay",
    "email":"berkaydonmez01@hotmail.com"
    }

customerJson = json.dumps(customer)
print(customer)

print(json.dumps("Berkay")) # .dumps json oluşturur.
