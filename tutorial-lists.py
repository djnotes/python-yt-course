"""
    Tutorial about lists, tuples, sets, and dictionaries
"""

scores = [1,2,3,4,5,6,7,8,9,10]

scores.append(11)

print(f"First number: {scores[0]}")

print(f"Last number: {scores[-1]}")


print("Removing 11")
scores.remove(11)
print(f"After removing 11: {scores}")


print('Running a loop...')
i = 0
for number in scores:
    scores[i] = number*number
    i += 1

print(f'After running loop: {scores}')


print('Adding heterogenous list members')
scores.append(20.5)
scores.append('Jack')

print('After adding 20.5 and Jack...')
print(scores)

print('Creating a set...')
myset = {21,22,23,24,25,26,27,28,29,30}
print(f'List: {myset}')

print('Adding 31...')
myset.add(31)
print(f'Set members: {myset}')

print(f'Checking membership of 27 in the set...')
print(f'27 is in the set: {27 in myset}')

print(f'Checking membership of 50 in the set...')
print(f'50 is in the set: {50 in myset}')

print('Removing 31 from set...')
myset.remove(31)
print(f'After removing 31: {myset}')

print('removing two items...')
myset.pop()
myset.pop()

print(f'Set after removing items: {myset}')

my_tuple = 1,2.0, 'John', ['a','b','c']

print(f'This is my tuple: {my_tuple}')

for i in my_tuple:
    print(f'Tuple Member: {i}')


dict1 = {'a' : 1, 
'b' : 10, 
'c' : {'x' : 1000}
}

# dict2 = {
#     'info' : '/app/log/info.log',
#     'error' : '/app/log/error.log',    
#     'debug' : '/app/log/debug.log',
# }

dict2 = dict(
    info =  '/app/log/info.log',
    error = '/app/log/error.log',    
    debug = '/app/log/debug.log',
)

print(f'Dictionary1: {dict1} \n Dictionary 2: {dict2}')

print(f"Error log file (using get()): {dict2.get('error')}")

print(f"Error log file (using brackets): {dict2['error']}")

print(f'Operating on the log files dictionary: ')

for key,value in dict2.items():
    print(f'Log file {key}: {value}')