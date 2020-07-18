# Divide and conquer 
def quick_sort(arr, l, r):
    border = partition(arr, l, r) # Partition the array and get the pivot index
    quick_sort(arr, l, border - 1) # quicksort l ~ (pivot - 1) 
    quick_sort(arr, border + 1, r) # quicksort (pivot + 1) ~ r

# Paritioning the left and right parts (based on the pivot)
def partition(arr, l, r):
    pivot_value = arr[(l + r) // 2]
    l_pointer = l
    r_pointer = r
    
    while l_pointer < 

    # Pick one from the left
    while arr[l_pointer] <= pivot_value:
        l_pointer += 1
    
    # Pick one from the right
    while arr[r_pointer] >= pivot_value:
        r_pointer -= 1
        
    # Swap two
    arr[l_pointer], arr[r_pointer] = arr[r_pointer], arr[l_pointer]
    
    

    return l_pointer

if __name__ == "__main__":
    # arr = [7, 8, 0, 1, 2, 3, 8, 9, 4, 3, 4, 6, 7, 8, 9, 10, 16]
    # print(arr)
    # quick_sort(arr, 0, len(arr) - 1)
    # print(arr)

    # arr = [2, 1]
    # print(arr)
    # quick_sort(arr, 0, len(arr) - 1)
    # print(arr)

    # arr = [1]
    # print(arr)
    # quick_sort(arr, 0, len(arr) - 1)
    # print(arr)

    # arr = [1, 4, 8, 1, 3, 4, 0, 3, 9, 4, 2, 3, 1, 9]