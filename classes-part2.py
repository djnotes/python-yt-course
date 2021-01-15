"""
    This module contains some classes and teaches inheritance in Python
"""

class NumberException(Exception):
    pass
        

input_num = int(input('Enter a number between 1 and 10:'))

if (1<= input_num <= 10) is False:
    raise NumberException("Number entered is not in the accepted range")


    
