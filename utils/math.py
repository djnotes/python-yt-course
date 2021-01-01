def power(a, b):
    """
    Return the value of a ^ b
    """
    base = a
    for i in range(1, b):
        a = a*base
    
    return a

