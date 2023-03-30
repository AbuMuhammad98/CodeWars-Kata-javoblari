def longest(a1, a2):
    long = a1 + a2
    return ''.join(sorted(set(long)))
print(longest("aretheyhere", "yestheyarehere"))