def sum_cubes(n):
    # your code here
    total = 0
    while n > 0:
        total += n ** 3
        n -= 1
    return total