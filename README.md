# Concepts

## All you need to know before you start

### Before you start
For Data Structure Visualizations, this website might help(The method how it solves might be different from this page): 

https://www.cs.usfca.edu/~galles/visualization/Algorithms.html

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

```python
def bubbleSort(arr): 
    n = len(arr) 
  
    # Traverse through all array elements 
    for i in range(n): 
  
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
  
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
  
# Driver code to test above 
arr = [64, 34, 25, 12, 22, 11, 90] 
  
bubbleSort(arr) 
```
* Careful with the range of `j` cause we need to use `j + 1` as well. 

* Time Complexity: O(n^2)
* Space Compexity: O(1)
* Sorting in place: Yes

#### Selection Sort
The Selection sort algorithm is based on the idea of finding the minimum or maximum element in an unsorted array and then putting it in its correct position in a sorted array.

* Swapping is involved unlike insertion sorting

* Here we are not looking for the perfect position for the element we pick(insertion sorting), we are looking for minimum, maximum value candidate to be changed. 

```python
# Traverse through all array elements 
for i in range(len(A)): 
      
    # Find the minimum element in remaining  
    # unsorted array 
    min_idx = i 
    for j in range(i+1, len(A)): 
        if A[min_idx] > A[j]: 
            min_idx = j 
              
    # Swap the found minimum element with  
    # the first element         
    A[i], A[min_idx] = A[min_idx], A[i] 
```
* Time Complexity: O(n^2)
* Space Complexity: O(1)
* In place: Yes



#### Insertion Sort

* Inserting to the right place from the front of the array.

```python
# Traverse through 1 to len(arr)
def insertion_sort(arr): 
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        for j in range(i - 1, -1, -1): # j: i-1 ~~ 0
            if arr[j] <= key:  # Finally found the first arr[j] that should be located on the left side of the key
                break
            arr[j + 1] = arr[j]
        arr[j + 1] = key
```

* When Adding the key to the right place

| index 	|       j       	|     j'(= j + 1)    	| j' + 1 	|
|:-----:	|:-------------:	|:------------------:	|:------:	|
| Value 	|       A       	|          B         	|    B   	|
|       	|       ^       	| Put the `key` here 	|        	|
|       	| current point 	|                    	|        	| 

* Time Complexity: O(n^2)
* Space Complexity: O(1)
* Sorting in place: Yes



#### Quick Sort
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

Resource

Great explanation for quick sorting(last element pivot)-->  https://www.codementor.io/@garethdwyer/quicksort-tutorial-python-implementation-with-line-by-line-explanation-p9h7jd3r6

#### Merge Sort

#### Heap Sort

#### Counting Sort

#### Radix Sort

#### BucketSort

> Sort a large set of floating point numbers which are in range from 0.0 to 1.0 and are uniformly distributed across the range. How do we sort the numbers efficiently?


The process of bucket sort can be understood as scatter-gather approach. The elements are first scattered into buckets then the elements of buckets are sorted. Finally, the elements are gathered in order.
It is commonly used when elements are uniformly distributed.

You uniformly distribute all the elements and the best case is having every bucket for each element. in that case, we won't have to really sort the bucket.
and we The last step of bucket sort, which is concatenating all the sorted objects in each buckets, requires {\displaystyle O(k)} O(k) time


> When the range is not limited for the input values, this sorting algorithm shouldn't be used.
> 
> 
> When thinking of making buckets for this case  we never know
>the range of the integers that will be input. And even if we try to think all the cases, we can't make every buckets beforehand until infinite. 

Conventionally, insertion sort would be used for sorting buckets, but other algorithm could be used as well

Bucket sort performs at its worst, O(n^2), when all elements at allocated to the same bucket

* Time Complexity: Best--> O(n + k) / Worst --> O(n^2) 
* Space Complexity: 
* Bucket sort is not a comparison sorting algorithm!

References

https://en.wikipedia.org/wiki/Bucket_sort#Average-case_analysis

https://stackoverflow.com/questions/54808131/how-is-the-time-complexity-of-bucket-sort-onk-if-it-uses-insertion-sort-to-so

https://stackoverflow.com/questions/31633391/when-should-i-choose-bucket-sort-over-other-sorting-algorithms

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

#### Operations

##### Creation

#### Example of Using Doubly LinkedList
1. LRU Cache

* LRU Cache uses `HashMap` and `Doubly LinkedList` to make Adding and deleting *O(1)* operation.
--> Because of *O(1)* Time Complexity, we need to use use both of those data structure!

* Also there's a

Link

https://www.interviewcake.com/concept/java/lru-cache  

https://leetcode.com/problems/lru-cache


### When to use Singly LinkedList and Doubly LinkedList?


Resource  
About LinkedList: https://medium.com/@kojinoshiba/data-structures-in-python-series-1-linked-lists-d9f848537b4d

Singly LinkedList vs Doubly LinkedList: https://stackoverflow.com/questions/10708790/microsoft-asks-singly-list-or-doubly-list-what-are-the-pros-and-cons-of-using

---

## Stack

* A stack is a data structure that stores items in an Last-In/First-Out manner. This is frequently referred to as LIFO.

* For `stack`, we have 
>* *`push()`: put new element into stack
>* *`pop()`: pop the top element
>* `peek()`: see what's on the top(but not removing)
>* `empty()`: boolean, `true` if empty

#### Implementation

For Python, we have 3 ways of implementing `Stack`.

1.Using `list` Built-in

* Using `append()` for `push()` and `pop()` for `pop()`.

* `push()` and `pop()` takes Amortized *O(1)* time complexity in list.

* When searching element from the stack, it has a benefit of taking *O(1)* time complexity.

2.Using `collections.deque`

* Using `append()` for `push()` and `pop()` for `pop()`.

* The deque class implements a double-ended queue which supports addition and removal of elements from either end in *O(1)* time (non-amortized).

* Because deques support adding and removing elements from both ends equally well, they can serve both as `queue`s and as `stack`s.

* Python’s `deque` objects are implemented as `doubly-linked lists` which gives them proper and consistent performance insertion and deletion of elements, but poor *O(n)* performance as they randomly access elements in the middle of the stack.

3.Using `queue.LifoQueue`

#### Resource

https://realpython.com/how-to-implement-python-stack/

https://www.edureka.co/blog/stack-in-python/

https://www.geeksforgeeks.org/stack-in-python/




## Queue

>* enqueue(): Adds an item to the queue
>* dequeue(): Removes an item from the queue
>* front(): Get the front item
>* end(): Get the last item

### Implementation

There are also 3 ways to implement `Queue` on Python.

1. Using `list`

* Instead of enqueue() and dequeue(), append() and pop() function is used.

* However, lists are quite slow for this purpose because inserting or deleting an element at the beginning requires shifting all of the other elements by one, requiring O(n) time.



2. Using `collections,deque`

* Deque is preferred over list in the cases where we need quicker append and pop operations from both the ends of container, as deque provides an O(1) time complexity for append and pop operations as compared to list which provides O(n) time complexity. Instead of `enqueue` and `deque`, `append()` and `popleft()` functions are used.

3. Using `queue.Queue`

---

## Trees


### Overall Concepts

#### Kinds of Trees
* Full Binary Tree: A full binary tree (sometimes proper binary tree or 2-tree) is a tree in which every node other than the leaves has two children.

![](images/fullBinaryTree.jpg)

* Complete Binary Tree: 
A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible.

![](images/completeBinaryTree.jpg)

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


### Maipulating Trees

#### Copying a tree

Recursive

```java
public TreeNode cloneTree(TreeNode root) {
        if (root == null) return null;
        TreeNode newNode = new TreeNode(root.val);
        newNode.left = cloneTree(root.left);
        newNode.right = cloneTree(root.right);
        return newNode;
}
```

Iterative



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

When relating graphs, BFS is usually good for finding shortest path (fastest path). 

### BFS
### DFS


#### Directed Graph

One thing we have to think carefully is that unlike `tree` data structure, Graphs can be visited more than once. So we have to be aware of that.

+ We want to make sure that we visit all the vertices!


Below code works for when every node is quite strongly connected and assuming there will be no left out ones.
```python
# V: A list of vertices/ adj: adjacency list / s: vertex we are visiting
parent = {s: None}
def dfs_visit(V, adj, s): 
    for v in adj[s]:
        if v not in parent:
            parent[v] = s
            dfs_visit(V, adj, v) 
```


But what if some graphs are not strongly connected and there are more than one cluster? For those cases we can use the above function recursively like below!
And this methodology should be used usually for Graph DFS!
```python
def dfs(V, adj):
    parent = {}
    for s in V:
        if s not in parent: # This means we didn't visit s
            parent[s] = None 
            dfs_visit(v, adj, s) # So let's visit s!
```

Time Complexity: O(V + E) --> Linear Time

* The above code will make directed graph get visited once and undirected graph get visited twice(one from each side)

### Edge Classification
* Tree edge: the edge that leads us to new edge (it forms a tree in the end that's why it's called that way)

* Forward edge: takes node to descendant in the tree

* Backward edge: takes node to ancestor in the tree

* Cross edge: takes sibling node to sibling node in the tree 

To detect Forward edge, Cross edge --> use counter for it just like the level!

To detect backward edge: use stack to see if the current node


You can't have forward edges and cross edges in undirected graphs (Still can have tree edges and Backward edges)


### Cycle detection

* Graph has a cycle <==> Graph has a backward edge

### Topological Sort
> One good example of using Topological Sort is 'Job Scheduling'

Givven directed acyclic graph (DAG), order vertices so that all edges point from lower order to higher order.

* Topological Sorting result can be more than one since the requirement of it is to only have forward edges left to right in the printed result.


#### Using DFS with Stack
```python
#Python program to print topological sorting of a DAG 
from collections import defaultdict 

#Class to represent a graph 
class Graph: 
	def __init__(self,vertices): 
		self.graph = defaultdict(list) #dictionary containing adjacency List 
		self.V = vertices #No. of vertices 

	# function to add an edge to graph 
	def addEdge(self,u,v): 
		self.graph[u].append(v) 

	# A recursive function used by topologicalSort 
	def topologicalSortUtil(self,v,visited,stack): 

		# Mark the current node as visited. 
		visited[v] = True

		# Recur for all the vertices adjacent to this vertex 
		for i in self.graph[v]: 
			if visited[i] == False: 
				self.topologicalSortUtil(i,visited,stack) 

		# Push current vertex to stack which stores result 
		stack.insert(0,v) 

	# The function to do Topological Sort. It uses recursive 
	# topologicalSortUtil() 
	def topologicalSort(self): 
		# Mark all the vertices as not visited 
		visited = [False]*self.V 
		stack =[] 

		# Call the recursive helper function to store Topological 
		# Sort starting from all vertices one by one 
		for i in range(self.V): 
			if visited[i] == False: 
				self.topologicalSortUtil(i,visited,stack) 

		# Print contents of the stack 
		print stack 

g= Graph(6) 
g.addEdge(5, 2); 
g.addEdge(5, 0); 
g.addEdge(4, 0); 
g.addEdge(4, 1); 
g.addEdge(2, 3); 
g.addEdge(3, 1); 

print "Following is a Topological Sort of the given graph"
g.topologicalSort() 
#This code is from geeksforgeeks

# Following is a Topological Sort of the given graph
# 5 4 2 3 1 0

```
* Time Complexity : O(V + E)


#### Kahn's Algorithm (BFS method)

* Time Complexity : O (V + E)


Resource

MIT Course-DFS, Topological sort, Edge classification, Cycle detection
https://www.youtube.com/watch?v=AfSk24UTFS8

DFS and Topological sorting medium  
https://medium.com/@yasufumy/algorithm-depth-first-search-76928c065692

Topoloical sort
https://www.geeksforgeeks.org/topological-sorting/


Kahn's Algorithm
https://www.educative.io/edpresso/what-is-topological-sort

https://www.geeksforgeeks.org/topological-sorting-indegree-based-solution/

## Dynamic Programming (DP)

Most of the DP problems can be solved by trying out these methods! (More optimize# BFS

    
1. Find recursive relation
2. Recursive (top-down)
3. Recursive + memo (top-down)
4. Iterative + memo (bottom-up)
5. Iterative + N variables (bottom-up)

For this, please check this link for a good example of solving DP!   
--> https://leetcode.com/problems/house-robber/discuss/156523/From-good-to-great.-How-to-approach-most-of-DP-problems.

---



# Coding Problems Practice
**Tree**

Easy  
1. Invert Binary Tree
```python
# DFS Solution
class Solution:
    def invertTree(self, root):
        if root is None:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

# BFS Solution
def invertTree2(self, root):
    queue = collections.deque([(root)])
    while queue:
        node = queue.popleft()
        if node:
            node.left, node.right = node.right, node.left
            queue.append(node.left)
            queue.append(node.right)
    return root
    
```

>Deque can be implemented in python using the module “collections“. Deque is preferred over list in the cases where we need quicker append and pop operations from both the ends of container, as deque provides an O(1) time complexity for append and pop operations as compared to list which provides O(n) time complexity.
> * Under the hood, a deque is a doubly-linked list.
> * Use deque only if you need insert/remove to be fast from both ends, and don't care about read speeds. List has constant time append/pop from one end and also constant time access anywhere in the list. You should almost always prefer list over deque, which is why list is builtin.

>For reading random data in the list, it can be accessed constant time. However, Linked Lists like queues and double linked lists like deques don't have that ability. So we gotta choose wisely which one to use.

Resource  

https://www.geeksforgeeks.org/deque-in-python/


2. Merge Two Binary Trees

Solution
```python
def mergeTrees(self, t1, t2):
        if t1 and t2:
            root = TreeNode(t1.val + t2.val)
            root.left = self.mergeTrees(t1.left, t2.left)
            root.right = self.mergeTrees(t1.right, t2.right)
            return root
        else:
            return t1 or t2

```


Solution2
```java
public class Solution {
    public TreeNode mergeTrees(TreeNode t1, TreeNode t2) {
        if (t1 == null)
            return t2;
        if (t2 == null)
            return t1;
        t1.val += t2.val;
        t1.left = mergeTrees(t1.left, t2.left);
        t1.right = mergeTrees(t1.right, t2.right);
        return t1;
    }
}
```

**Iterative Solution(Important)**
```python
def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 or not t2: return t1 or t2
        s = [(t1, t2)]
        while s: 
            n1, n2 = s.pop()
            #nothing to add on
            if not n2: continue
            n1.val += n2.val
            if not n1.right: n1.right = n2.right
            else: s.append((n1.right, n2.right))
            if not n1.left: n1.left = n2.left
            else: s.append((n1.left, n2.left))
        return t1
```
* The above solution is mocking how the recursive algorithm works (Using call stack).


When `m` is the minimum number of nodes from the two given trees 

Time Complexity: *O(m)* ---> Cause even if you have to add the rest of the nodes that the minimum number tree doesn't have, you only have to add only one root node of the remaining part.
So it's not *O(M)* (`M` for maximum)

Space Complexity: *O(m)* --> Cause the tree that has the minimum number of nodes can be skewed and in that case, it means you will have to repeat m times.

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

2. House Robber

Key take aways

* When using bottom up approach, no need to make the whole table --> Can be reduced by using only a few variables and reusing them!


MUST READ --> https://leetcode.com/problems/house-robber/discuss/156523/From-good-to-great.-How-to-approach-most-of-DP-problems.

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

2. Coin Change 1
* Key takeaway: I tried out this problem with Greedy Algorithm and failed with some cases. You should be careful when solving it.

  * e.g. coins = [6, 4], amount = 20 ==> When using Greedy Algorithm answer is -1 (6 * 3 + 2(can't get 2)) However, the actual answer is actually 4 (6 * 2 + 4 * 2)

  * For more info, please search `Greedy` in the discussion tab on Leetcode.
    
  * This problem can have many variations like into StairCase Problem
  
Solution

1. Top-Down approach


2. Bottom-up approach 
  
  
Resource

Explanation video: 
https://leetcode.com/problems/coin-change/discuss/218340/Top-Down-Recursive-and-Bottom-Up-Iterative-Approach-Explanation

**Two Pointer**

Medium

1. Container with most water.
* The widest container (using first and last line) is a good candidate, because of its width. Its water level is the height of the smaller one of first and last line.

* All other containers are less wide and thus would need a higher water level in order to hold more water.

* The smaller one of first and last line doesn't support a higher water level and can thus be safely removed from further consideration.

Code
```python
class Solution:
    def maxArea(self, height):
        i, j = 0, len(height) - 1
        water = 0
        while i < j:
            water = max(water, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return water
```

2. Longest substring without repeating characters

Solution

* Use 'Sliding Window' --> keep tracking the `start` and the `end` index of the window.



```Java
public int lengthOfLongestSubstring(String s) {
    int i = 0, j = 0, max_len = 0;
    Set<Character> set = new HashSet<>();
    
    while (j < s.length()) {
        if (!set.contains(s.charAt(j))) {
            set.add(s.charAt(j++));
            max_len = Math.max(max_len, set.size());
        } else {
            set.remove(s.charAt(i++));
        }
    }
    
    return max;
}
```

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sliding_set = set()
        l, r = 0, 0
        max_len = 0
        
        while r < len(s):
            if s[r] in sliding_set:
                sliding_set.remove(s[l])
                l += 1
            else:
                sliding_set.add(s[r])
                r += 1
                max_len = max(max_len, r - l) # --> we already did r += 1 so no need to do r - l + 1
        return max_len
```

* --> Using HashSet
* Only have to update max_len when adding non duplicate ones cause otherwise max_len won't get bigger anywyas.
* Also, when getting the length, note that `len(set)` is not used but `r - l`

```Java
 public int lengthOfLongestSubstring(String s) {
        if (s.length()==0) return 0;
        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        int max=0;
        for (int i=0, j=0; i<s.length(); ++i){
            if (map.containsKey(s.charAt(i))){
                j = Math.max(j,map.get(s.charAt(i))+1);
            }
            map.put(s.charAt(i),i);
            max = Math.max(max,i-j+1);
        }
        return max;
    }
```

--> Using HashMap
```python
def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d, res, start = {}, 0, 0
        for i, ch in enumerate(s):
            if ch in d:  # This also get triggered when there's duplicate one out of the window range (before the start index) so in the below code we gotta use max to make that happen
                start = max(start, d[ch]+1) # Since we are not creating new dictionary everytime when duplicate one is found, 
                                            # We have to make sure we stay inside the window range (There might be no duplicate one in the window but if we don't use max for this, then it might get the old one in front of the starting point and think it's a duplicate one)
            res = max(res, i-start+1)            
            d[ch] = i
        return res
```
--> using dictionary.



**Stack**

Hard

1. Largest Rectangle in Histogram

Take aways) When doing brute forcing, thinking of picking every combinations (like thinking of pairs of them) helps!


Using stack 
```python
def largestRectangleArea(self, height):
    height.append(0)
    stack = [-1]
    ans = 0
    for i in xrange(len(height)):
        while height[i] < height[stack[-1]]:
            h = height[stack.pop()]
            w = i - stack[-1] - 1
            ans = max(ans, h * w)
        stack.append(i)
    height.pop()
    return ans
```

- `height.pop()` that last line is to recover the original state of the input, since python list is passed by reference instead of shadow copy. It is not gonna give you wrong result for this problem. However in real world development, think about your colleague created a list contains some values that he will need in the future, you added a sentinel value to make your life easier, if you don't clean it up afterward, your colleague's code is very likely to crash. This is a good programming habit, it added one more "redundant" line, but it also make everybody's life easier.

- `height.append(0)` and `stack = [-1]` was added to deal with the last element left in the stack. The last one in the stack should be the minimum height index. So, to make 
it h * len(height), we added these two.

* Time Complexity: O(n) --> Operated only one `push` and `pop` for each n elements. 

* Space Complexity: O(n) --> We only used a `Stack`

* Resource: https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/28917/AC-Python-clean-solution-using-stack-76ms

* Here's another great solution without using stack(Haven't understood yet): https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/28902/5ms-O(n)-Java-solution-explained-(beats-96)
2. Maximal Rectangle

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
(a // 2) + (b // 2) + ((a % 2 + b % 2) / 2) #  --> If the average needs to be specific with decimal points
(a // 2) + (b // 2) + ((a % 2 + b % 2) // 2) # --> If the average needs to be rounded down (no decimal points)
```

Resource:
https://www.geeksforgeeks.org/compute-average-two-numbers-without-overflow/

# Useful coding tips for Python

### Using `and` and `or` for returning value

* In python, `and` operation will not return a boolean value, it depends on the 'values'. Some values like '0', '', '{}', '[]' and so on, will be judged by false. And other values will be judged by true. The whole sentence will be judged like a boolean value. If it's true, it will return the last true value, remember is the value, not True. Otherwise, it will return the first false value.

> e.g. 3 and [] and 34 --> will return [] (the first false element)
>
>e.g. 3 and 5 and 1 --> will return 1 (the last true element)

* `or` will return the most first, true value(if there s any)
> e.g. 0 or 3 or [] --> 3
> e.g. [] or [] --> []

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


### Using `collections.defaultdict`