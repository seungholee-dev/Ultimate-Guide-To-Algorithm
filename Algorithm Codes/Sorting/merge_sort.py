# Does the actual merge sorting
# Sort from left till right index
def merge_sort(arr, l, r):
    if l == r:
        return

    m = (l + r) // 2

    merge_sort(arr, l, m) # Sort left half: l ~ m
    merge_sort(arr, m + 1, r) # Sort right half: (m + 1) ~ r
    merge(arr, l, m, r) # Merge left and right halves into one (pointer sort)


# Merges two arrays (in-place?)
# one: l ~ m
# two: m + 1 ~ r
def merge(arr, l, m, r):
    if l == r:
        return

    l_pointer, r_pointer = l, m + 1

    tmp_arr = [0] * (r - l + 1)
    
    # Comparing and sort
    tmp_pointer = 0
    while l_pointer < m + 1 and r_pointer < r + 1:
        # print(l_pointer, ":", arr[l_pointer], r_pointer, ":", arr[r_pointer])
        if arr[l_pointer] < arr[r_pointer]:
            tmp_arr[tmp_pointer] = arr[l_pointer]
            l_pointer += 1
        else:
            tmp_arr[tmp_pointer] = arr[r_pointer]
            r_pointer += 1
        tmp_pointer += 1


    # Put the rest from the left array (if there are any)
    while l_pointer < m + 1:
        tmp_arr[tmp_pointer] = arr[l_pointer]
        l_pointer += 1
        tmp_pointer += 1

    # Put the rest from the  array (if there are any)
    while r_pointer < r + 1:
        tmp_arr[tmp_pointer] = arr[r_pointer]
        r_pointer += 1
        tmp_pointer += 1

    # Copy back to the original array
    for i in range(len(tmp_arr)):
        arr[l + i] = tmp_arr[i]

if __name__ == "__main__":
    arr = [7, 8, 0, 1, 2, 3, 8, 9, 4, 3, 4, 6, 7, 8, 9, 10, 16]
    print(arr)
    merge_sort(arr, 0, len(arr) - 1)
    print(arr)

    arr = [2, 1]
    print(arr)
    merge_sort(arr, 0, len(arr) - 1)
    print(arr)

    arr = [1]
    print(arr)
    merge_sort(arr, 0, len(arr) - 1)
    print(arr)