"""
This module teaches the basics of classes in Python
"""

class Person:
    name = 'Mehdi'
    age = 40
    height = 6




print ('Person information: ', Person.name, ', ', Person.age, ' years old', ',', Person.height, ' high')

Person.name = 'Jack'

print ('Person information: ', Person.name, ', ', Person.age, ' years old', ',', Person.height, ' high')


class Car:
    def __init__(self, model: str, color: str, price: int):
        self.model = model
        self.color = color
        self.price = price
    
volkswagen = Car("Volkswagen Atlas", "Red", 20000)

chevrolet = Car("Chev Tahoe", "Black", 30)


print('Volkswagen: ', volkswagen.model, ',', volkswagen.color, ',', volkswagen.price)

print('Chevrolet: ', chevrolet.model, ', ', chevrolet.color, ', ', chevrolet.price)

