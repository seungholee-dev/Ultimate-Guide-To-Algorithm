---
title: Sliding Window 
description: Learning Sliding Window
---


2. Forward Pointers
These pointers start at the same position and move to one direction. This approach is typically used in problems involving subarrays or subsequences where you need to keep track of a contiguous block of elements. For example, the problem of finding the longest substring with no repeating characters can be solved using this approach.

```python
def smallest_subarray_with_given_sum(s, arr):
    window_sum = 0
    min_length = float('inf')
    window_start = 0

    for window_end in range(0, len(arr)):
        window_sum += arr[window_end]  # add the next element

        # shrink the window as much as possible while maintaining the constraint
        while window_sum >= s:
            min_length = min(min_length, window_end - window_start + 1)
            window_sum -= arr[window_start]
            window_start += 1

    if min_length == float('inf'):
        return 0

    return min_length

```





1. Fixed Size


2. Flexible Size


Leetcode
Longest Repeating Character Replacement
