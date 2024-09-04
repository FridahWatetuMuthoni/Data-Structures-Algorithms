# Heaps

## Introduction

A heap data structure is a tree-based data structure in which each node of the tree has a specific
relationship with other nodes, and they are stored in a specific order. Depending upon the specific
order of the nodes in the tree, heaps can be of different types, such as a min heap and a max heap.

## Min Heap

The min-heap is a tree data structure where each node is smaller than or equal to its children.
The root is always the smallest element.

## Max-Heap

The max-heap is a data structure where each node is greater or equal to its children
The root is always the biggest element.

## Binary Heap

The binary heap is a complete binary tree that respects the heap property.

1. Complete Binary Tree - a complete binary tree is a binary tree where every level is completely filled expect maybe the last one but all its nodes have to be as far to the left as possible.
2. Heap property - each node is smaller than or equal to its children if its a min heap and each node should be larger than its children if its a max heap.

## Notes

A heap is a maximally efficient implementation of the priority queue abstract data type.
finding nodes.
Using Index: beacause it starts at 0
Node-Current : i
Left Child: 2i + 1
Right Child: 2i + 2
Parent: (i - 1) / 2
Using Items Count beacause it starts at 1
current = n
left = 2n
right = 2n + 1
root = n/2 => current/2

We fill heaps in the left to right , top to bottom order.
largest item and smallest item find problems.

We initialize the heap list with a zero to represent the dummy first element, and we are adding
a dummy element just to start the indexing of data items from 1 since if we start indexing from
1, accessing of the elements becomes very easy due to the parent-child relationship.

Insertion
The insertion of an item into a min heap works in two steps. First, we add the new element to the
end of the list (which we understand to be the bottom of the tree), and we increment the size of
the heap by one. Secondly, after each insertion operation, we need to arrange the new element up
in the heap tree, to organize all the nodes in such a way that satisfies the heap property.

Heaps and priority queue are basically the same thing because implementing priolity queues as heaps gives us the most efficient solutions.
