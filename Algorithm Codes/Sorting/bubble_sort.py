def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

if __name__ == "__main__":
    arr = [7, 8, 0, 1, 2, 3, 8, 9, 4, 3, 4]
    print(bubble_sort(arr))

    arr = [2, 1]
    print(bubble_sort(arr))

    arr = [1]
    print(bubble_sort(arr))