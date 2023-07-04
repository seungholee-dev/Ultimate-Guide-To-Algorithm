---
title: Insertion Sort
description: Learn how Insertion Sort works
---


-   Inserting to the right place from the front of the array.

```python
# Traverse through 1 to len(arr)
def insertion_sort(arr):
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        for j in range(i - 1, -1, -1): # j: i-1 ~~ 0
            if arr[j] <= key:  # Finally found the first arr[j] that should be located on the left side of the key
                break
            arr[j + 1] = arr[j]
        arr[j + 1] = key
```

-   When Adding the key to the right place

| index |       j       |    j'(= j + 1)     | j' + 1 |
| :---: | :-----------: | :----------------: | :----: |
| Value |       A       |         B          |   B    |
|       |       ^       | Put the `key` here |        |
|       | current point |                    |        |

-   Time Complexity: O(n^2)
-   Space Complexity: O(1)
-   Sorting in place: Yes