def happy(number):
    sums = []
    repeated = False
    while number != 1 and repeated == False:
        sum = 0
        for i in str(number):
            sum += int(i)**2       

        if sum in sums:
            repeated = True
        else:
            number = sum
            sums.append(sum)
    return (not repeated)
