def euclid(a,b):
    r = 100000
    while r != 0:
        p = a//b
        q = p*b
        r = a - q
        if r != 0:
            a = b
            b = r
    return b

print(euclid(507,52))
print(euclid(884,85))
print(euclid(4845, 3795))