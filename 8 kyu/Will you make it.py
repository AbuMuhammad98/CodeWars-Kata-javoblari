def zero_fuel(distance_to_pump, mpg, fuel_left):
    #Happy Coding! ;)
    while True:
        if (distance_to_pump / mpg) <= fuel_left:
            return True
        else:
            return False
            
print(zero_fuel(94, 29, 4))