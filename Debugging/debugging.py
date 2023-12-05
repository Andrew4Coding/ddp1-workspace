'''
Use this file to debugging codes
'''

def ratakan(lst):
    if lst == []:
        return lst
    elif isinstance(lst[0], list):
        return ratakan(lst[0]) + ratakan(lst[1:])
    elif isinstance(lst[0], int) and lst[0] % 2 == 0:
        return [lst[0]] + ratakan(lst[1:])
    else:
        return ratakan(lst[1:])

print(ratakan([[1, 2, 3], 'A', 2, [1]]))

def gcd(a, b):
    if b == 0:
        return a
    else:
        return (b, a%b)

print(gcd(8, 32))