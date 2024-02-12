def sum(arr):
    sum = 0
    for element in arr:
        sum += element
    return sum


def first_fill(data, capacity):
    arr = []
    for element in data:
        added = False
        i = 0
        while i < len(arr) and added == False:
            el = arr[i]
            if sum(el) + element <= capacity:
                el.append(element)
                added = True
            i += 1
        if added == False:
            arr.append([element])  
        
    return(arr)

def first_fill_descending(data, capacity):
    arr = []
    data.sort()
    data = data[::-1]
    for element in data:
        added = False
        i = 0
        while i < len(arr) and added == False:
            el = arr[i]
            if sum(el) + element <= capacity:
                el.append(element)
                added = True
            i += 1
        if added == False:
            arr.append([element])
    return arr  

def full_bin(data, capacity):
    #find highest number 
    #first check all the two combos, then check all the 3 combos left over, then all the 4 combos yeah yeah yeah
    arr = []
    #check 2 combos 
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if data[i] + data[j] == capacity and data[i] != -1 and data[j] != -1:
                arr.append([data[i], data[j]])
                data[i] = -1
                data[j] = -1
    #check 3 combos
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            for k in range(j+1, len(data)):
                if data[i] + data[j] + data[k] == capacity and data[i] != -1 and data[j] != -1 and data[k] != -1:
                    arr.append([data[i], data[j], data[k]])
                    data[i] = -1
                    data[j] = -1
                    data[k] = -1           
    #work through rest of data
    for element in data:
        if element != -1:
            added = False
            i = 0
            while i < len(arr) and added == False:
                el = arr[i]
                if sum(el) + element <= capacity:
                    el.append(element)
                    added = True
                i += 1
            if added == False:
                arr.append([element])
    return arr  


print(full_bin([8,7,10,13,11,17,4,6,12,14,9], 25))