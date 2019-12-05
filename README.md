# Concepts

## Trees

### Heaps

#### Understanding the array-based tree index formula

left_child_i = parent_i * 2 + 1  
right_child_i = parent_i * 2 + 2
```

     0    T = 1
    / \
   1    2   T = 2
  / \  / \
 3   4 5  6  T = 3
 
 ```
 
When T is the tier of the tree, 2^T - 1 is the index(value) of the first node of the next level(T + 1)  
j is the index starting from the beginning of the Tier's index. (In the above tree, 5's j is 2)

(parent_node_index) i = 2^T - 1 + j  
(left_child_node_index) i' = 2^(T+1) - 1 + 2j'


2j' --> When you take a look at the tree, for each node for i~j, i'~j' get 2 for each. So 2j' is correct.

Therefore, i' = 2i + 1 (for the left child node)



###### Resources
Basics about Heaps: https://medium.com/basecs/learning-to-love-heaps-cef2b273a238

HeapSort: https://medium.com/basecs/heapify-all-the-things-with-heap-sort-55ee1c93af82

Array-based tree index formula Explanation: https://cs.stackexchange.com/review/suggested-edits/66932

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
