---
title: Collision Pointers 
description: Learning Sliding Window
---
3. Parallel Pointers
Parallel pointers typically refer to a situation where you have two pointers each traversing their own separate but related arrays or lists. This is often used when you need to merge two sorted arrays or compare elements between the arrays. Here's a quick Python example showing how you might use parallel pointers to merge two sorted arrays:

```python
def merge_sorted_arrays(arr1, arr2):
    i = j = 0  # initialize two pointers
    result = []

    # Traverse both arrays
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    # Add remaining elements if any
    while i < len(arr1):
        result.append(arr1[i])
        i += 1
    while j < len(arr2):
        result.append(arr2[j])
        j += 1

    return result
```
