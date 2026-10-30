# Module 5 Analysis: Stacks and Queues

The linked-list stack performs pushes and pops at the head instead of the tail to maintain a constant time complexity of O(1). If operations were performed at the tail, traversing the entire singly linked list would be required, resulting in an inefficient O(n) time complexity. 

An array-based queue must be implemented as a circular queue to prevent the continuous shifting of elements or wasting available memory space. Without wrap-around mechanics, the front index would constantly move forward after each dequeue operation, eventually making the queue appear "full" even when physical slots remain open at the beginning of the array.