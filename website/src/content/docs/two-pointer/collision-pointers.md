---
title: Collision Pointers
description: Learning Sliding Window
---

Collision Pointers
The two pointers start at two different points, usually the two ends, and move towards each other. This is used in problems like "two sum", where you need to find two numbers in a sorted array that add up to a target value. This technique is often used on sorted arrays or linked lists.

```python
def two_sum_sorted_array(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return (left, right)  # or return the elements: return (arr[left], arr[right])
        elif current_sum < target:
            left += 1  # Move right to increase the sum
        else:
            right -= 1  # Move left to decrease the sum

    return None  # No pair was found

```

| **Problem**                    | **Topic**    | **Platform** |
| ------------------------------ | ------------ | ------------ |
| Two Sum II                     | Two-Pointers | Leetcode     |
| 3Sum                           | Two-Pointers | Leetcode     |
| 3Sum Closest                   | Two-Pointers | Leetcode     |
| 4Sum                           | Two-Pointers | Leetcode     |
| Valid Triangle Number          | Two-Pointers | Leetcode     |
| Trapping Rain Water            | Two-Pointers | Leetcode     |
| Container With Most Water      | Two-Pointers | Leetcode     |
| Partition Array                | Two-Pointers | Leetcode     |
| Valid Palindrome               | Two-Pointers | Leetcode     |
| Sort Colors                    | Two-Pointers | Leetcode     |
| Parition Array by Odd and Even | Two-Pointers | Leetcode     |
| Sort Letters by Case           | Two-Pointers | Leetcode     |
