# Using for loop
# def insertion_sort(arr):
#     for i in range(len(arr)):
#         key = arr[i]
#         first_flag = True
#         for j in reversed(range(i)):
#             arr[j + 1] = arr[j]
#             if arr[j] < key:
#                 arr[j + 1] = key
#                 first_flag = False
#                 break
#         if first_flag:
#             arr[0] = key
#     return arr

# Using while loop
def insertion_sort(arr):
    for i in range(len(arr)):
        key = arr[i]
        j = i - 1
        while arr[j] > key and 0 <= j:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

if __name__ == "__main__":
    arr = [8, 7, 0, 1, 2, 3, 8, 9, 4, 3, 4]
    print(insertion_sort(arr))

    arr = [2, 1]
    print(insertion_sort(arr))
    arr = [1]
    print(insertion_sort(arr))