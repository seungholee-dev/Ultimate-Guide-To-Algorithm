---
title: Knapsack Problems
description: Ultimate guide to Knapsack Problems
---

### Overview

Knapsack problems are a family of problems in combinatorial optimization. They derive their name from the problem faced by someone who is constrained by a fixed-size knapsack and must fill it with the most valuable combination of items. The name "knapsack problem" dates back to the works of the mathematician Tobias Dantzig (1884–1956).
<br>
<br>

<img src="https://miro.medium.com/v2/resize:fit:720/format:webp/0*7qVrrJOuli5A3xwU.png">

<br>
<br>

The basic form of the problem is as follows:

> Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible.

<br>
<br>

There are many variations of the knapsack problem:

1. **0/1 Knapsack Problem**
   Each item can be included in the knapsack or not, making it a binary choice. You aim to maximize the total value of items without exceeding the weight limit of the knapsack.
   <br>
2. **Fractional Knapsack Problem**
   This problem permits fractions of items to be taken. This means if an item is too heavy to fully fit into the knapsack, a part of it can be included proportionally.
   <br>
3. **Unbounded Knapsack Problem**
   In this variation, there's no limit on how many times an item can be included in the knapsack, as long as the weight limit isn't exceeded.
   <br>

4. **Bounded Knapsack Problem**
   Each item in this problem has a limit on how many times it can be included in the knapsack. This is an intermediate of the 0/1 and unbounded problems.

While there are many other variants, these should be more than enough to know and solve most of the problems :)

<br>

### 1. 0/1 Knapsack Problem

Here's a sample Question:

> Given a list of items with specific weights and values, and a knapsack with a maximum weight capacity, determine the maximum value that can be placed in the knapsack.

| Item | Weight | Value |
|-------|--------|-------|
| Item1 | 1 | 60 |
| Item2 | 2 | 100 |
| Item3 | 3 | 120 |

And say we have a knapsack with a maximum weight capacity of **5**. The question is to find the maximum value we can fit into the knapsack.

In terms of the 0/1 Knapsack problem, the core idea is that **You calculate the maximum values when item i is included/not included**.

So to speak, keeping track of Two Possibilities for each item:

1. **The item is included in the optimal subset of items.**
   In this case, the problem is reduced to solving a smaller version of the same problem: finding the optimal subset of the remaining items to include in the knapsack, given that the weight capacity of the knapsack has been reduced by the weight of the item we've chosen to include.
   <br>
2. **The item is not included in the optimal subset.**
   Here, the problem is also reduced to solving a smaller version of the same problem, but in this case, the weight capacity of the knapsack remains the same because we didn't include the item.

Here's the code:

```python
def knapSack(W, wt, val, n):
    # K[i][j] will store the maximum value that can be achieved with i items and capacity j
    K = [[0 for w in range(W + 1)] for i in range(n + 1)]
 
    # Build the K[][] table in a bottom-up manner
    for i in range(n + 1):
        for w in range(W + 1):
            # Base case: If no items or no weight capacity, the value is 0
            if i == 0 or w == 0:
                K[i][w] = 0
            # If the weight of the current item is less than or equal to the current capacity
            # Consider the maximum value between including and excluding the item
            elif wt[i-1] <= w:
                # Max of (value of current item + value of remaining weight capacity after including the item, maximum value considering the previous items with the same weight capacity)
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w])
            else:
                # If the weight of the current item is more than the current weight capacity, we cannot include the item
                # So we carry forward the maximum value achieved considering the previous items with the same weight capacity
                K[i][w] = K[i-1][w]
 
    # K[n][W] holds the maximum value that can be achieved considering all items and the full weight capacity
    return K[n][W]
 
# Values and weights of the items
val = [60, 100, 120]
wt = [1, 2, 3]

# Maximum weight capacity of the knapsack
W = 5

# Number of items
n = len(val)

# Call the function with the inputs
print(knapSack(W, wt, val, n))  # Outputs: 220

```


- Do note in the Nested `for` loop, outer loop is about the items to show we are using items only once. Because 0/1 Knapsack problem doesn't allow using more than once for each item.


### 2. Fractional Knapsack Problem

> Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack.

### 3. Unbounded Knapsack Problem

> Given a knapsack of a specific capacity and lists of weights and values where you can choose an item any number of times, find out the maximum value that the knapsack can hold.

### 4. Bounded Knapsack Problem

> Given a list of items with specific weights, values, and quantity limits, determine the maximum value that can be placed in the knapsack of a certain capacity.
