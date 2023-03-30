def high_and_low(numbers):
   num = [int(x) for x in numbers.split()]
   numbers = " ".join([str(max(num)),  str(min(num))])
   return numbers

print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))