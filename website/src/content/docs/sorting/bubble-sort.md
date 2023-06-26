---
title: Bubble Sort
description: A reference page in my new Starlight docs site.
---




```python
def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)
```

-   Careful with the range of `j` cause we need to use `j + 1` as well.
-   Time Complexity: `O(n^2)`
-   Space Compexity: `O(1)`
-   Sorting in place: `Yes`


### Coding Problem
