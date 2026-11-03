#ascending bubble sort
def bubble_sort(arr):
    for i in range(len(arr)-1):
        swap_flag = False
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                swap_flag = True
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print(f"pass {i+1}: {arr}")
        if swap_flag == False:
            return arr
    return arr

array = [1,4,6,9,12,5,7]
print(bubble_sort(array))