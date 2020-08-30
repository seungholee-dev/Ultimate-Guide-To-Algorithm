def regular_binary_search_recursive(arr, l, r, target):
    if l > r:
        return -1
    
    mid = l + (r - l) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return regular_binary_search_recursive(arr, l + 1, r, target)
    elif arr[mid] > target:
        return regular_binary_search_recursive(arr, l, r - 1, target)
    


# Non-biased Binary Search Algorithm (Could return any index of any duplicate elements.)
def regular_binary_search_iterative(arr, target):
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
             l = mid + 1
        elif arr[mid] > target:
            r = mid - 1
    return -1

# Left-biased Binary Search Algorithm
def left_binary_search_iterative(arr, target):
    pass

def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    lo = 0
    hi = len(nums)
    # Left-biased Binary Search
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < target:
            lo = mid + 1 # If lo = mid, ==> this will cause infinite loop
        else:
            hi = mid
    assert lo == hi
    if lo == len(nums) or nums[lo] != target:
        return -1
    return lo

if __name__== "__main__":
    arr = [2, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 6]
    key = 5
    print("Index", regular_binary_search_iterative(arr, key))
    # print("Index", left_binary_search_iterative(arr, key))
    print(search(arr, key))