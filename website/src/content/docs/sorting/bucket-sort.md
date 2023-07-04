---
title: Bucket Sort
description: Learn how bucket sort works
---


> Sort a large set of floating point numbers which are in range from 0.0 to 1.0 and are uniformly distributed across the range. How do we sort the numbers efficiently?

The process of bucket sort can be understood as scatter-gather approach. The elements are first scattered into buckets then the elements of buckets are sorted. Finally, the elements are gathered in order.
It is commonly used when elements are uniformly distributed.

You uniformly distribute all the elements and the best case is having every bucket for each element. in that case, we won't have to really sort the bucket.
and we The last step of bucket sort, which is concatenating all the sorted objects in each buckets, requires {\displaystyle O(k)} O(k) time

> When the range is not limited for the input values, this sorting algorithm shouldn't be used.
>
> When thinking of making buckets for this case we never know
> the range of the integers that will be input. And even if we try to think all the cases, we can't make every buckets beforehand until infinite.

Conventionally, insertion sort would be used for sorting buckets, but other algorithm could be used as well

Bucket sort performs at its worst, O(n^2), when all elements at allocated to the same bucket

-   Time Complexity: Best--> O(n + k) / Worst --> O(n^2)
-   Space Complexity:
-   Bucket sort is not a comparison sorting algorithm!

References

https://en.wikipedia.org/wiki/Bucket_sort#Average-case_analysis

https://stackoverflow.com/questions/54808131/how-is-the-time-complexity-of-bucket-sort-onk-if-it-uses-insertion-sort-to-so

https://stackoverflow.com/questions/31633391/when-should-i-choose-bucket-sort-over-other-sorting-algorithms
