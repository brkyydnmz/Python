# -*- coding: utf-8 -*-

#set küme demektir
#setler index olmadığından karışık sırayla yanıt verebilir.
studentsSet = {"Engin","Derin","Salih","Ahmet"}
studentsSet2 = set("Mehmet")  #set oluşturma bu şekilde de yapılır {} ile yapıldığı gibi
print(studentsSet)

for student in studentsSet:
    print(student)

print("Derin"in studentsSet)


if "Derin"in studentsSet:
    print("Listede var")
    

studentsSet.add("Ali")
print(studentsSet)

studentsSet.update(["Berkay","Mert","Selin"]) 
print(studentsSet)

print(len(studentsSet))

studentsSet.remove("Mert") # .remove setten kaldırır.
print(len(studentsSet))

studentsSet.discard("Mert") # .discard sette bulamamasına rağmen hata vermemesi için kullanılır.
print(len(studentsSet))

x = studentsSet.pop() # .pop setten son eleman siler.karışık sıraladığı için hangisi tam bilemeyebiliriz.
print(len(studentsSet))

x = studentsSet.clear() # .clear seti temizler set duruyor ama içini temizliyor.
print(len(studentsSet))
del studentsSet  # del de seti tamamen yok eder.
print(studentsSet)

