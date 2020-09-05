# Divide and conquer 
def quick_sort(arr, l, r):
    if l < r:
        border = mid_pivot_partition(arr, l, r) # Partition the array and get the first index of the right segment
        quick_sort(arr, l, border - 1) # quicksort left half: l ~ (border - 1) 
        quick_sort(arr, border, r) # quicksort right half: (border) ~ r

# Paritioning the left and right parts (based on the pivot)
def mid_pivot_partition(arr, l, r):
    pivot_value = arr[(l + r) // 2]
    l_pointer = l
    r_pointer = r
    
    while l_pointer <= r_pointer:
        # Pick one from the left (That is larger than or equal to the pivot_value)
        # no need to add "and l_pointer < r" for the infinite loop because pivot_value is going is going to be somewhere in the array to break!
        while arr[l_pointer] < pivot_value:
            l_pointer += 1
        
        # Pick one from the right (That is smaller than or equal to the pivot_value)
        while arr[r_pointer] > pivot_value:
            r_pointer -= 1
            
        # Swap the two
        if l_pointer <= r_pointer:
            arr[l_pointer], arr[r_pointer] = arr[r_pointer], arr[l_pointer]
            l_pointer += 1
            r_pointer -= 1
        
    # Return the first element of the right half (border)
    return l_pointer


def last_pivot_quick_sort(arr, l, r):
    if l < r:
        pivot_spot = last_pivot_partition(arr, l, r)
        last_pivot_quick_sort(arr, l, pivot_spot - 1)
        last_pivot_quick_sort(arr, pivot_spot + 1, r)


def last_pivot_partition(arr, l, r):
    pivot_value = arr[r]
    follower = leader = l
    for leader in range(l, r):
        if arr[leader] < pivot_value:
            arr[follower], arr[leader] = arr[leader], arr[follower] 
            follower += 1
    arr[follower], arr[r] = arr[r], arr[follower]
    return follower
    

if __name__ == "__main__":
    arr = [5, 2, 3, 1]
    print(arr)
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)

    arr = [5, 2, 3, 1]
    last_pivot_quick_sort(arr, 0, len(arr)- 1)
    print(arr)

