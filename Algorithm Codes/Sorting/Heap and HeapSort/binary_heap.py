def build_max_heap(arr, n):
    last_leaf = (n - 1 - 1) // 2 # n - 1 for the last index of the array and others are the formula for getting the parent's index
    for i in range(last_leaf, -1, -1):
        max_heapify(arr, n, i)

def max_heapify(arr, n, i):
    largest = i
    left_index = 2 * i + 1
    right_index = 2 * i + 2

    if left_index < n and arr[left_index] > arr[i]:
        arr[i], arr[left_index] = arr[left_index], arr[i]
        largest = left_index


    if right_index < n and arr[right_index] > arr[i]:
        arr[i], arr[right_index] = arr[right_index], arr[i]
        largest = right_index

    if largest != i:
        max_heapify(arr, n, largest)

def delete_root(arr,n):
    pass

def extractRoot(arr, n):
    root = None
    if n > 1:
        root = arr[0]
        arr[0] = arr[n - 1]
        max_heapify(arr, n - 1, 0)
    return root

def insertNode():
    pass
        

if __name__ == "__main__":
    arr = [7, 3]
    build_max_heap(arr, len(arr))
    print(arr)

    print("-----extracting root-----")
    print(extractRoot(arr, len(arr)))
    print(arr)

    print(extractRoot(arr, len(arr)))
    print(arr)



