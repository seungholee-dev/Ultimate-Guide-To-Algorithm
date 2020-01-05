def insertion_sort(arr):
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        for j in range(i - 1, -1, -1):
            if arr[j] <= key:  # When looping through all when key is equal or greater at some point, break the loop!
                break
            arr[j + 1] = arr[j]
        arr[j + 1] = key


a = [1, 3, 3, 2, 4, 54, 4, 23, 2]
insertion_sort(a)
print(a)