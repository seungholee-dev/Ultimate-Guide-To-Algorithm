# Concepts

## Trees

### Heaps


# Coding Interview questions
**Dynamic Programming**

Easy
1. Climbing Stairs
- Careful with indexOutOfRange when using the tabulation method. --> Remedy: Don't take array as 0-starting index (rather, 1-starting)

Solution
```python
def climbStairs(self, n):
    a = b = 1
    for _ in range(n):
        a, b = b, a + b
    return a
```
Medium
1. Longest Palindrome
- when returning value, think of the type of returning cause it might affect the runtime.
- function(i, i + 1) but putting function(i, i) is useful when needed.
