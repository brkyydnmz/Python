# -*- coding: utf-8 -*-

#%% Basic
#self class ın içindeki metotlara parametrelere ulaşmak için kullanılır.self zorunlu yazılır.
class Matematik:
    def __init__(self,sayi1,sayi2): # __init__(genelde def başında kullanılır)başlatma işlemlerini gerçekleştirir.
        self.sayi1 = sayi1
        self.sayi2 = sayi2
    def topla(self):
        return self.sayi1 + self.sayi2
    
    def cikar(self):
        return self.sayi1 - self.sayi2
    
    def carp(self):
        return self.sayi1 * self.sayi2
    
    def bol(self):
        return self.sayi1 / self.sayi2
    
matematik = Matematik(2,78) #class ı bu halde çağırırız matematik yazdıkça Matematik class ı çağırılacak
matematik2 = Matematik(3,76)
print("Toplam = " + str(matematik.topla()))
print("Toplam = " + str(matematik2.topla()))

#%% Property

class Person:
    def __init__(self,firstName,lastName,age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age

person1 = Person("Berkay","Dönmez","18")
print(person1.firstName)


class Worker(Person): #Person miras ile geldi
    def __init__(self,salary):
        self.salary = salary
        
class Customer(Person):
    def __init__(self,creditCardNumber):
        self.creditCardNumber = creditCardNumber
        
ahmet = Worker("3565")
print("Ahmet Salary: " + ahmet.salary)


mehmet = Customer("31122434343254")
print("Mehmet Credit Card Number: "+ mehmet.creditCardNumber)