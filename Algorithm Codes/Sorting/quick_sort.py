# Divide and conquer 
def quick_sort(arr, l, r):
    if l < r:
        border = partition(arr, l, r) # Partition the array and get the first index of the right segment
        quick_sort(arr, l, border - 1) # quicksort left half: l ~ (border - 1) 
        quick_sort(arr, border, r) # quicksort right half: (border) ~ r

# Paritioning the left and right parts (based on the pivot)
def partition(arr, l, r):
    pivot_value = arr[(l + r) // 2]
    l_pointer = l
    r_pointer = r
    
    while l_pointer < r_pointer:
        # Pick one from the left (That is larger than or equal to the pivot_value)
        while arr[l_pointer] < pivot_value and l_pointer < len(arr) - 1:
            l_pointer += 1
        
        # Pick one from the right (That is smaller than or equal to the pivot_value)
        while arr[r_pointer] > pivot_value and r_pointer > 0:
            r_pointer -= 1
            
        # Swap the two
        if l_pointer < r_pointer:
            arr[l_pointer], arr[r_pointer] = arr[r_pointer], arr[l_pointer]
            l_pointer += 1
            r_pointer -= 1
        
    # Return the first element of the right half (border)
    return l_pointer

if __name__ == "__main__":
    arr = [2, 1, 4]
    print(arr)
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)

    arr = [1, 4, 8, 1, 3, 4, 0, 3, 9, 4, 2, 3, 1, 9]
    print(arr)
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)

    # arr = [1]
    # print(arr)
    # quick_sort(arr, 0, len(arr) - 1)
    # print(arr)

    # arr = [1, 4, 8, 1, 3, 4, 0, 3, 9, 4, 2, 3, 1, 9]