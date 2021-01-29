"""
ZomCast 23: Working with File I/O
"""

FILE_NAME = 'names.txt'


print(f'Opening {FILE_NAME} for writing...')
text_file = open(FILE_NAME, 'w')

names = ['Mehdi', 'John', 'Matthew', 'Jack', 'Marie', 'Jane']

print(f'Writing names to {FILE_NAME}...')

with text_file as f:
    for name in names:
        f.write(name + '\n')
    
    
# text_file.close()

print(f'Done writing names to {FILE_NAME}.')


text_file = open(FILE_NAME, 'r')

print(f'Opening {FILE_NAME} again for reading...')

with text_file as f: 
    content = f.read()
    print(f'Content of the file read using file.read(): {content}')

print(f'Opening {FILE_NAME} again for reading line by line')
text_file = open(FILE_NAME, 'r')

with text_file as f: 
    lines = f.readlines()
    for line in lines:
        print(f'Line: {line}')  
        
              




