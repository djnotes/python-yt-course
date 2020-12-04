# Dec 4, 2020

# 1. String Variables

first_name = 'John'
family_name = "Straw"

# print("Your name is "  + first_name + " " + family_name )

# 2. Evaluating string vaiables inside strings 

print(f"Your name is {first_name} {family_name}")


# 3. Substrings 


long_message = """ 
Hello and welcome to my Python course.
 Here we will talk about Python programming, 
 learn its basics, learn data types like strings, numbers, lists, etc.
 """
            
print(f'Long message: {long_message}')

partial_message = long_message[0:20]


print(f'The partial message is: {partial_message}')




p1 = 'He'
p2 = 'llo'

concat = p1 + p2
join = 'He' 'llo'

print(f'Joined string: {join}')

last_message = long_message[0:2000]

print(f'Last part: {last_message}')