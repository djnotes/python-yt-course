"""
    This module is an example of several functions in the ZomCast Python Tutorial series 
"""

def my_func():
    print('Hello from my_func')
    print('Another line from my_func')


def my_func2():
    return "Hello from my_func2"
    


print(f'Calling my_func... ')
my_func()

print(f'Calling my_func2...: {my_func2()}')

def say_hello(name: str): 
    """
    Says hello to `name`
    """    
    print(f'Hello {name}')