---
title: Quick Sort
description: Learn how Quick Sort works
---

When thinking of Quick Sorting, think of the sorting version of Binary Search. Instead of searching the middle elements of the array like when doing Binary Search,
We are placing the pivot value in the right place (Depends on how you choose the pivot tho). and You keep doing it until every element is sorted.
Also, note that left and right side of the pivot doesn't have to be sorted in order. As long as the left side of the pivot is smaller than the pivot and the right side of the pivot is bigger
than the pivot, it's all good.

Usually, you make `quicksort()` funciton and another function called `partition()`

Here's a Python implementation (Using last element as a pivot)

```python
# To think easier about this algorithm: Note that the leftmost big element and the leftmost small element right after the boundary of big number will always be swapped.
# 2 7 8 8 5 3 2 2 4
#   ^|- - -|^
#   f       l


def partition(xs, start, end):
    follower = leader = start
    while leader < end: # no need to see more when it reaches the pivot element.This
        if xs[leader] <= xs[end]: # Comparing each element with pivot(xs[end]) --> the follower will always get stuck in the big element(if there's any bigger element than pivot in the array)
                                                                            # When it reaches the very first big element, the follower will get stuck, until then, follower and leader increases together.
                                                                            # Can add `if follower == leader, skip to next one together` if this confuses you.
            xs[follower], xs[leader] = xs[leader], xs[follower]
            follower += 1
        leader += 1 # leader always increases regardless of the follower
    xs[follower], xs[end] = xs[end], xs[follower] # Place the pivot in the right place
    return follower # because of the last follower+=1, it actually returns the +1 index of the last follower --> perfect place for pivot.

def _quicksort(xs, start, end):
    if start >= end:
        return
    p = partition(xs, start, end) # 1. sort the right, left part of array with the last pivot and 2. returns the index of that pivot.
    _quicksort(xs, start, p-1)
    _quicksort(xs, p+1, end)

def quicksort(xs):
    _quicksort(xs, 0, len(xs)-1)
```

Here's another implementation (Using last element as a pivot)

```python

# Python program for Quicksort
# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
def partition(arr, low, high):
	i = low - 1		 # index of smaller element
	pivot = arr[high]	 # pivot

	for j in range(low, high):
		# If current element is smaller than or
		# equal to pivot
		if arr[j] <= pivot:
			# increment index of smaller element
			i += 1
			arr[i], arr[j] = arr[j], arr[i]
	arr[i + 1], arr[high] = arr[high], arr[i + 1]
	return i + 1

# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low --> Starting index,
# high --> Ending index

# Function to do Quick sort
def quickSort(arr, low, high):
	if low < high:

		# pi is partitioning index, arr[p] is now
		# at right place
		pi = partition(arr, low, high)

		# Separately sort elements before
		# partition and after partition
		quickSort(arr, low, pi - 1)
		quickSort(arr, pi + 1, high)

# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print ("Sorted array is:")
for i in range(n):
	print ("%d" %arr[i]),
```

Great explanation for quick sorting(last element pivot)--> https://www.codementor.io/@garethdwyer/quicksort-tutorial-python-implementation-with-line-by-line-explanation-p9h7jd3r6