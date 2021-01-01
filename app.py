import utils.math as mymath
import utils.words as words
import sys
import math

name = "Mehdi" #str
 
age = 30 #int 

height = 6.1 #float

weight = 176.37 #float

i_dont_know = None


print(f"Hello {name}")

print (f"You are {age} years old.")

print (f"Your height and weight: {height}, {weight}")

print('Calling fibo.fib()...')

import fibo

fibo.fib(50)

print('Calling fibo.fib2()...')
result = fibo.fib2(50)

print(f'fibo.fib2(50) result = {result}')


print('Making a call to utils.math.power()...')
print(f'{mymath.power(2,10)}')

print('Calling utils.words.reverse_text()....')
print(f'{words.reverse_text("Universe")}')

print(f'cos(45) = {math.cos(45)}')
sys.exit(0)
