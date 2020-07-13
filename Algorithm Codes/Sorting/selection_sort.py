def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

if __name__ == "__main__":
    arr = [7, 8, 0, 1, 2, 3, 8, 9, 4, 3, 4]
    print(selection_sort(arr))

    arr = [2, 1]
    print(selection_sort(arr))

    arr = [1]
    print(selection_sort(arr))