def stray(arr):
    return [num for num in arr if arr.count(num) == 1][0]
print(stray([1, 1, 1, 1, 1, 1, 2]))