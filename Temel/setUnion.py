# -*- coding: utf-8 -*-

setA = {1,2,3,4,5}
setB = {1,3,4,6,7,8}

print(setA | setB)  # | işareti birleştirir(union) setleri ortakları tekrar tekrar yazmaz.
print(setA.union(setB)) # bu da union yapar sıralar önemsiz.
print(setB.union(setA))


print(setA & setB)  # & işareti kesişimini(intersection) alır. 
print(setA.intersection(setB)) 
print(setB.intersection(setA))


print(setA - setB)  # - işareti fark(difference) alır.
print(setA.difference(setB)) 
print(setB.difference(setA))


print(setA ^ setB)  # ^ ile simetrik fark(symmetric_difference) alır yani kümelerin kesişimini almaz sadece
print(setA.symmetric_difference(setB)) 
print(setB.symmetric_difference(setA))
