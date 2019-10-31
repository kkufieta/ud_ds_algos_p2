# Explanation for Problem 6:  Unsorted Integer Array

## Requirements
The time requirement is `O(n)`, and it is prohibited to use Python's inbuilt `min` and `max` functions. A single traversal is preferred.

## Code Design
This is such an easy problem, I wonder if I understood it wrong :P

Anyways, we have two variables to keep track of the current `min` and `max` in the array, and we update them as we traverse the array one single time.

## Efficiency

### Time Efficiency
The time efficiency is `O(n)`, and we can solve this problem in a single traversal, since we don't have to look at any elements more than once.

### Space Efficiency
We don't need extra space, so the space efficiency is `O(1)`.