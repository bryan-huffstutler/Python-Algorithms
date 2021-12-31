Searching and Sorting

Binary Search
 - Cut the list in half and determine if search item is higher or lower than the mid.
 - Continue until it is found or not there.
 - Can be done with iterative or recursive function.

*Divide and Conquer algorithms are best suited for RECURSION*

Sorting
 - Sorting arranges items in a collection order
 - Items are re-arranged based on the comparison operator of the item.
 - The comparison operator can be modified or created based on your specific needs or the unique class structure.
 - Types of Sorting Algorithms:
    - Bubble Sort
    - Selection Sort
    - Insertion Sort
    - Quick Sort
    - Merge Sort

Bubble Sort
 - Makes multiple passes through list
 - Compares adjacent items and exchanges those that are out of order.
 - Each pass through the list places the next largest value in its proper place. In essence, each item 'bubbles' up to the location
 - Time complexity of O(n2) (Horrible Big O)
    
Selection Sort
 - Only one exchange per pass
 - Looks for largest value as it makes a pass and, after completing the pass, places it in the proper place
 - Still has same time complexity as Bubble Sort

Insertion Sort
 - Works by maintaining a sorted sublist in the lower positions of the list.
 - As a new item is found, it is inserted into the sublist in the correct position
 - Sublist grows by one with each new item, and the list decreases by one on each pass
 - Still has same time complexity of O(n2)

Quick Sort
 - Uses divide and conquer technique
 - Requires selecting and efficient pivot point. All the elements to be sorted will be compared to the pivot.
 - Pivot should be roughly larger than half 
 - Reorder the elements such that all elements less than the pivot are to the left of the pivat and all greater on the right. This is partitioning.
 - Next repeat the above steps recursvely to elements smaller than the pivot point. Then recursively to the elements that are greater. 
 - Time complexity is O(NlogN)
 - 

Merge Sort *Preferred Sorting Method*
 - Uses divide and conquer
 - Recursively splits collection in half
 - A collection of a single item is the base case
 - Uses a 'merge' operation to recombine two smaller sorted collections into a single collection
 - Time complexity is always O(NlogN)