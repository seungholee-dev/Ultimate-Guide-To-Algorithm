---
title: Time Complexity 
description: A guide on understanding time complexity
---

### What is Time Complexity? 

Time Complexity is computational complexity that describes **the amount of computer time it takes to run an algorithm**

Here are some examples of time complexity
<br>

##### Question 1

```python
nums = [1, 2, 3, 4, 5]
for n in nums:
    print(n)
```

<details>
<summary>Answer</summary>
<div markdown="1">
<b>O(N)</b>
<br>
The code runtime depends on length of nums. As the nums gets bigger, the run time only gets bigger in linear time O(N)
</div>
</details>

<br>

##### Question 2

```python
nums = [1, 2, 3, 4, 5]

for n1 in nums:
    for n2 in nums:
        print(n1, n2)
```

<details>
<summary>Answer</summary>
<div markdown="1">
<b>O(N^2)</b>
<br>
The code runtime depends on length of nums. As the nums gets bigger, the run time gets bigger by N^2 because of the nested loop
</div>
</details>
<br>

#### Amortized vs Averaged Runtime?

-   Averaged is often used when the case is random(unpredictable).
-   Amortized is often used when the case is predictable but is too good to just diminish all the runtime performance just because of some slow cases(predictable).

-   From: Amortized vs Averaged runtime https://gist.github.com/jconnolly/5acf05f279a7e9e40371