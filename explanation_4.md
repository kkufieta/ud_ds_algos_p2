# Explanation for Problem 4:  Dutch National Flag Problem

## Requirements
Sort the array in a single traversal, which is stricter than `O(n)`.

## Code Design
In order to sort the array in a single traversal, we have to sort it as we loop through the elements.

Since we have only 3 types of elements in the array, {0, 1, 2}, we can assume that the sorted array is going to be divided into 3 sections, where the first section has only 0's, the second one has only 1's, and the third one has only 2's. 

Using that knowledge, we can keep track of indices that separate those 3 sections, and shuffle around values and the separating indices to conform to the 3-section rule as we look at elements one by one from both sides.

## Efficiency

### Time Efficiency
We look at each element only once, and then do a small number of swaps at each step. Thus, the time complexity is a single traversal, and `O(n)`.

### Space Efficiency
We use only `O(1)` space, since we are sorting the array in place, and we're only keeping track of the current values we look at, and the indices separating the three sections of the array.