def invert(lst):
    a = []
    for i in lst:
        a+=[-i]
        
    return a


print(invert([1, -2, -3, 4, 5]))