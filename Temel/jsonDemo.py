# -*- coding: utf-8 -*-

import json

with open("users.json") as users:
    data = json.load(users)
    
    for x in range(5):       #ilk 4 değerin verileri yazdırılır
        print(data[x]["username"])
        print(data[x]["email"])
        print(data[x]["address"]["street"])
        print(data[x]["address"]["geo"]["lat"])
    
    