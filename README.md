# Concepts

## All you need to know before you start


#### Amortized vs Averaged Runtime?

* Averaged is often used when the case is random(unpredictable).
* Amortized is often used when the case is predictable but is too good to just diminish all the runtime performance just because of some slow cases(predictable).

Resource

Amortized vs Averaged runtime: https://gist.github.com/jconnolly/5acf05f279a7e9e40371

## Searching Algorithms

#### Linear Search

#### Binary Search

##### Iterative
```python
def binary_search(arr, x):
    l, r = 0, len(arr)-1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] < x:
            l = mid + 1
        elif x < arr[mid]:
            r = mid - 1
        else:
            return mid
    return -1
```

* Time Complexity: O(log(n))

* Space Complexity: O(1)

##### Recursive
```python
# Returns index of x in arr if present, else -1 
def binarySearch (arr, l, r, x): 
    
    # Check base case
    if l > r:
        return -1

    mid = (l + r) // 2

    # If element is present at the middle itself 
    if arr[mid] == x: 
        return mid 
      
    # If element is smaller than mid, then it can only 
    # be present in left subarray 
    elif arr[mid] > x: 
        return binarySearch(arr, l, mid-1, x) 

    # Else the element can only be present in right subarray 
    else: 
        return binarySearch(arr, mid+1, r, x) 

```
* Note that we are SEARCHING not SORTING so we don't check every element.
--> That's why it takes O(logn)

* when calling this function, `l` should be `0` and `r` should be `len(arr) - 1`
like `binarySearch(arr, 0, len(arr) - 1, 15)`

* Time Complexity: O(log(n)) 

* Space Complexity: O(log(n)) --> Because of `call stack`


##### Resource
 
https://www.sanfoundry.com/python-program-implement-binary-search-recursion/

https://blog.finxter.com/iterative-vs-recursive-binary-search-algorithms-in-python/
#### Bubble Sort

#### Selection Sort

#### Insertion Sort

#### Quick Sort

#### Merge Sort

#### Heap Sort

#### Counting Sort

#### Radix Sort

#### BucketSort

#### Tim Sort 


## LinkedList
>Python does not have linked lists in its standard library. We implement the concept of linked lists using the concept of nodes

> Side Note: It’s weird to talk about linked lists in python because this data structure is too low level to be useful in python programs. So don’t blame me if you don’t see the point of coding all this in Python. After all, there’s not much point in using linked list in Python besides its educational value and usefulness in coding interviews. In other languages like C and C++, where linked lists are actually crucial to any programs you’re implementing.
### Singly LinkedList

* Note that the SinglyLinkedList class only remembers the head `Node` of the linkedlist (The `Node` class remembers its next node).

Advantages  
* A linked list saves memory. It only allocates the memory required for values to be stored. In arrays, you have to set an array size before filling it with values, which can potentially waste memory.  
* Linked list nodes can live anywhere in the memory. Whereas an array requires a sequence of memory to be initiated, as long as the references are updated, each linked list node can be flexibly moved to a different address.

Disadvantages  
* Linear look up time. When looking for a value in a linked list, you have to start from the beginning of chain, and check one element at a time for a value you’re looking for. If the linked list is n elements long, this can take up to n time. On the contrary many languages allow constant lookups in arrays.
  Like for an array, if you do `a[100]` then the result pops out in constant time. However if you want to get the third item from the linked list, you would have to traverse through the linkedlist(until the 100th).

#### Creation
```python
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

list1 = SLinkedList()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
# Link first Node to second node
list1.headval.nextval = e2
# Link second Node to third node
e2.nextval = e3
```
#### Traversing
```python
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval

list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# Link first Node to second node
list.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3

list.listprint()
```
Time Complexity: O(N)


#### Inserting an element
##### Inserting at the beginning
```python
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None
    def AtBegining(self,newdata):
            NewNode = Node(newdata)
    
            # Update the new nodes next val to existing node
            NewNode.nextval = self.headval
            self.headval = NewNode
```
Time Complexity: O(1)

##### Inserting in between two Nodes
```python
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

# Function to add node
    def Inbetween(self,middle_node,newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return

        NewNode = Node(newdata)
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode
```

##### Inserting at the end
```python
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head_node = None

# Function to add newnode
    def AtEnd(self, newdata):
        new_node = Node(newdata)
        
        if not self.head_node: # if head_node doesn't exist.
            self.head_node = new_node
            return
        
        last_element = self.head_node
        while last_element.next:
            last_element = last_element.nextval
        last_element.next = new_node
```
Time Compleixty: O(N)


##### Removing an item

Input: the value you want to delete.

```python
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
    
    def remove_Node(self, value):
        prev = None
        curr = self.head
        while curr:
            if curr.data == value:
                if prev: # General cases
                    prev.next(curr.next)
                else: # Edge case: When prev is None and curr is the head
                    self.head = curr.next
                return
            prev = curr
            curr = curr.next
```
Time Complexity: O(N)

### Doubly LinkedList
Pros
* Efficient iteration (especially when iterating reverse) 
* Delete operation is more efficient than Singly LinkedList

Cons
* More memory for storage (.prev pointer)
* Relatively complex implementation than Singly LinkedList(coding)

### When to use Singly LinkedList and Doubly LinkedList?


Resource  
About LinkedList: https://medium.com/@kojinoshiba/data-structures-in-python-series-1-linked-lists-d9f848537b4d

Singly LinkedList vs Doubly LinkedList: https://stackoverflow.com/questions/10708790/microsoft-asks-singly-list-or-doubly-list-what-are-the-pros-and-cons-of-using


## Trees

---

### Overall Concepts

#### Understanding the array-based tree index formula

> 1. left_child_i = parent_i * 2 + 1  
> 2. right_child_i = parent_i * 2 + 2  
> 3. parent_i = floor((child_i - 1) / 2) --> rounding down at the end. 
>
>```
>
>     0    T = 1
>    / \
>   1    2   T = 2
>  / \  / \
> 3   4 5  6  T = 3
> 
> ```
> **proof for 1. 2.)**  
> When T is the tier of the tree, 2^T - 1 is the index(value) of the first node of the next level(T + 1)  
> j is the index starting from the beginning of the Tier's index. (In the above tree, 5's j is 2)
>
>(parent_node_index) i = 2^T - 1 + j  
> (left_child_node_index) i' = 2^(T+1) - 1 + 2j'
>
>
>2j' --> When you take a look at the tree, for each node for i~j, i'~j' get 2 for each. So 2j' is correct.
>
>Therefore, i' = 2i + 1 (for the left child node)
#### Post Order

#### Pre Order

---

### BST(Binary Search Tree)

---

### AVL Tree



---

### Heaps

#### Building heaps

a. Heapify from the lowest-level to the root node.
```python
# Build a maxheap. 
    for i in range(n, -1, -1): #--> n could be ((n - 1) - 1) // 2 for the optimization cause we already the leaves node don't have any children.
        heapify(arr, n, i) 
```

* Note: Sift-Down is way more efficient than Sift-Up here. Sift-Down takes O(n) and Sift-Up takes O(nlog(n)) for building a heap.

Time Complexity: O(n) --> Check out the link

#### Heapify

1. Max Heapify

Process
a. compare the i node with its children a  
b. put the largest one on the top(swap with i node value.)   
-b-1. Call Max Heapify for the subtree(Heapify the subtrees of the largest one (cause the smaller element that swapped could violate the property of max heaps in the subtree))
```python
# To heapify subtree rooted at index i. 
# n is size of heap 
def heapify(arr, n, i): 
    largest = i # Initialize largest as root 
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
  
    # Compare with l and r to find the biggest candidate for the root node.
    # Eventually only the biggest node and the i node get swapped (only the value gets swapped.)

    # See if left child of root exists and is 
    # greater than root 
    if l < n and arr[i] < arr[l]: 
        largest = l 
  
    # See if right child of root exists and is 
    # greater than root 
    if r < n and arr[largest] < arr[r]: 
        largest = r 
  
    # Change root, if needed 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i] # swap 
  
        # Heapify the root. 
        heapify(arr, n, largest) 

```

Time Complexity: O(log(n))

#### Inserting element
Process
a. Add the new element on the lowest-level, left-most position.    
b. Sift up the new element.

This bottom-up approach is also called `Sift up`

Time Complexity: Worst --> O(log(n)), Average --> O(1)
Space Complexity: O(1)
#### Extract element
Process  
a. Remove the root node (We usually only want the root node cause we are only interested in Max and Min value)  
b. Replace the root node place with the lowest-level, right-most children.
c. Sift down the root node.

#### Delete element


#### Heapsorting

```python
# The main function to sort an array of given size 
def heapSort(arr): 
    n = len(arr) 
  
    # Build a maxheap. 
    for i in range(n, -1, -1): #--> n could be ((n - 1) - 1) // 2 for the optimization cause we already the leaves node don't have any children.
        heapify(arr, n, i) 
  
    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] # swap 
        heapify(arr, i, 0) 
```

#### Why do we use Array over Tree for Heaps?
~~~
The tree uses more time and memory. The complexities are the same, but the constant factors are different.

The pointers of the tree use a lot of memory, compared to the array-based heap, where you barely need any additional space but the one taken by the values themselves. And manipulating these pointers takes time too. Allocating and deallocating nodes might take some time and space also...

In addition, there's no guarantee that the nodes of the tree will be together in memory. If any of the two alternatives takes benefit of the cache, it is the array-based heap.
~~~


#### Priority Queue and the Binary Heap
When using priority queue, if we use binary heap, it is much faster than the using the normal array(or other datastructure) cause it only takes O(n) to add. However, Like sorting, it takes O(nlogn). 



###### Resources
Basics about Heaps: https://medium.com/basecs/learning-to-love-heaps-cef2b273a238


Time Complexity of building a heap: 
* https://www.growingwiththeweb.com/data-structures/binary-heap/build-heap-proof/ --> In this link, `h(height)` starts from the leaf node(leaves nodes `h` is 0).
* https://stackoverflow.com/questions/9755721/how-can-building-a-heap-be-on-time-complexity

Sift down vs Sift up: https://www.reddit.com/r/algorithms/comments/8n543e/what_is_the_difference_between_maxheapify_and/

HeapSort: https://medium.com/basecs/heapify-all-the-things-with-heap-sort-55ee1c93af82 --> There are things that's quite not right so check the comments!

HeapSort: https://www.geeksforgeeks.org/heap-sort/

Array vs Tree for Heaps: https://stackoverflow.com/questions/14719007/why-is-a-binary-heap-better-as-an-array-than-a-tree

Array-based tree index formula Explanation: https://cs.stackexchange.com/review/suggested-edits/66932

About Priority Queue: https://www.geeksforgeeks.org/priority-queue-set-1-introduction/

Priorty Queue and Binary Heap: https://runestone.academy/runestone/books/published/pythonds/Trees/PriorityQueueswithBinaryHeaps.html


## Graphs

### BFS
### DFS

---



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


**Heap**

Medium
1. Top K Frequent Elements
- Knowing time complexity of heap operations are important!

Solution
```python
# heap
class Solution(object):
    def topKFrequent(self, nums, k):
        opt = []
        counter = collections.Counter(nums)

        heap = [(-count, num) for num, count in counter.items()]
        heapq.heapify(heap)
        
        while len(opt)<k:
            opt.append(heapq.heappop(heap)[1])

        return opt
```
Time Complexity: O(N + klogn)
--> Building the counter: N + Building a heap: N + logn(extracting) * k(k times)
Space Complexity: O(N)


Second Solution(Using bucket sort)
```python
# bucket sort
class Solution(object):
    def topKFrequent(self, nums, k):
        opt = []
        counter = collections.Counter(nums)
        bucket = collections.defaultdict(list)

        for num, count in counter.items():
            bucket[count].append(num)

        for i in reversed(xrange(len(nums)+1)):
            if i in bucket:
                opt.extend(bucket[i])
                if len(opt)>=k: break

        return opt[:k]

```
Check the below link for time complexity and space complexity for this solution.


Resources
Solution for Top K Frequent elements --> https://leetcode.com/problems/top-k-frequent-elements/discuss/325463/2-Clean-Python-Solution-(Bucket-Sort-Heap-Explained)


**Bit Manipulation**

Easy

1. Single Number


Solution1 (Hash Table)
Code
```python
def singleNumber(self, nums: List[int]) -> int:
        d = {}
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
            
        for i in d:
            if d[i] == 1:
                return i
```

Time Complexity: O(N)
Space Complexity: O(N)
Solution2 (Bit manipulation)


Code
```python
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in nums:
            a ^= i
        return a
```

Key takeaways
* Associative property and Communtative property works for Xor(Exclusive or) Operations.

Time Complexity: O(N)  
Space Complexity: O(1)

## Tips and advanced topics

### Compute average of two numbers without overflow

Given two numbers, a and b. Compute the average of the two numbers.

The well know formula (a + b) / 2 may fail at the following case :
If, a = b = (2^31) – 1; i.e. INT_MAX.
Now, (a+b) will cause overflow and hence formula (a + b) / 2 wont work



* Java 
```java
(a / 2) + (b / 2) + ((a % 2 + b % 2) / 2); 
```

* Python
```python
(a // 2) + (b // 2) + ((a % 2 + b % 2) // 2) 
```

Resource:
https://www.geeksforgeeks.org/compute-average-two-numbers-without-overflow/

# Useful coding tips for Python

### Using `collections.Counter()`

```python
>>> from collections import Counter
 
>>> myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
>>> print(Counter(myList))
Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})

>>> print(Counter(myList).items())
[(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]

>>> print (Counter(myList).keys())
[1, 2, 3, 4, 5]

>>> print(Counter(myList).values())
[3, 4, 4, 2, 1]
```

### Using `heapq`