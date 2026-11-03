def multiply(a,b):
    a_arr = [a]
    b_arr = [b]
    while 1 not in a_arr:
        a_arr.append(a_arr[-1]//2)
        b_arr.append(b_arr[-1]*2)
    print(b_arr)
    print(a_arr)
    sum = 0
    for i in range(len(a_arr)):
        if a_arr[i]%2 != 0:
            sum += b_arr[i]
    return sum

print(multiply(66,56))