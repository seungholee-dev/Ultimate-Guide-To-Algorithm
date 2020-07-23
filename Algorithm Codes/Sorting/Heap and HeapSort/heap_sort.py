from binary_heap import *

# Time Complexity: O(NlogN) --> N for building heap, logN for heapifying root everytime. 

def heap_sort(arr):
    build_max_heap(arr, len(arr)) # Make arr as a Heap.
    new_arr = [None] * len(arr)
    for i in range(len(arr)):
        new_arr[i] = arr[0] # extract Root
        delete_root(arr, len(arr)) # delete_root does max_heapify in itself at the end.
        print(arr)
    return new_arr


if __name__ == "__main__":
    arr = [8, 7, 0, 1, 2, 3, 8, 9, 4, 3, 4]
    print(heap_sort(arr))

    # arr = [2, 1]
    # print(heap_sort(arr))

    # arr = [1]
    # print(heap_sort(arr))

    # build_max_heap(a, len(a))
    # print(a)