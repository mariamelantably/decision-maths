def binary_search(arr, target):
    arr.sort() #ensure the list is sorted
    lowest = 0
    highest = len(arr) - 1
    while highest > lowest:
        midpoint = round((highest+lowest)/2) - 1
        if arr[midpoint] == target:
            return True
        elif arr[midpoint] > target:
            highest = midpoint - 1
        else:
            lowest = midpoint + 1
    return False

array = [1,4,6,9,12,5,7]
print(binary_search(array, 8))

        
