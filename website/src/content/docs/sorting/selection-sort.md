---
title: Selection Sort
description: Learn how Selection Sort works
---

The Selection sort algorithm is based on the idea of finding the minimum or maximum element in an unsorted array and then putting it in its correct position in a sorted array.

-   Swapping is involved unlike insertion sorting

-   Here we are not looking for the perfect position for the element we pick(insertion sorting), we are looking for minimum, maximum value candidate to be changed.

```python
# Traverse through all array elements
for i in range(len(A)):

    # Find the minimum element in remaining
    # unsorted array
    min_idx = i
    for j in range(i+1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j

    # Swap the found minimum element with
    # the first element
    A[i], A[min_idx] = A[min_idx], A[i]
```

-   Time Complexity: O(n^2)
-   Space Complexity: O(1)
-   In place: Yes