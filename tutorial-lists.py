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

