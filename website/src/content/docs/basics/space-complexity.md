---
title: Space Complexity 
description: A guide on understanding Space Complexity 
---

### What is Space Complexity?

Space Complexity is amount of **memory space required to run an algorithm**

Let's see some examples here too.

##### Question 1

```python
# Returns sum of the array
def get_sum(nums):
    total_sum = 0

    for n in nums:
        total_sum += n
    
    return total_sum
```

<details>
<summary>Answer</summary>
<div markdown="1">
<b>O(1)</b>
<br>
We don't need additional memory space other than the variable called <code>total_sum</code> which is constant regardless of the size of the input coming(<code>nums size</code>) 
</div>
</details>

<br>

##### Question 2

```python
# Returns 2D Array based on input
def create_matrix(n):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        matrix.append(row)
    return matrix 

```

<details>
<summary>Answer</summary>
<div markdown="1">
<b>O(N^2)</b>
<br>
Based on the input <code>n</code>, the code needs n^2 additional space for creating returned matrix.

</div>
</details>