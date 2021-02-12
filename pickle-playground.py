"""
Let's talk about pickle
"""
import pickle

class student:
    def __init__(self, name, family_name, student_number) -> None:
        self.name = name
        self.family_name = family_name
        self.student_number = student_number


jack = student('Jack', 'McCane', 10)

melisa = student('Melisa', 'Gregor', 11)

print('Serializing jack and melisa...')


jack_bytes = pickle.dumps(jack)

melisa_bytes = pickle.dumps(melisa)

print(f'jack : {jack_bytes}\n melisa: {melisa_bytes} ')

print('Deserializing jack and melisa...')

jack_obj = pickle.loads(jack_bytes)

melisa_obj = pickle.loads(melisa_bytes)

print(f'Jack info: {jack_obj.name}, {jack_obj.family_name}, {jack_obj.student_number}')

print(f'Melisa info: {melisa_obj.name}, {melisa_obj.family_name}, {melisa_obj.student_number}')

