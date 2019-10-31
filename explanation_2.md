# Explanation for Problem 2:  Search in a Rotated Sorted Array

## Requirements
The required runtime complexity for this algorithm is `O(log(n))`.

## Code Design
I decided to use and modify binary search in order to achieve `O(log(n))` time efficiency.

Since the array is rotated, this introduces a violation of the assumption that the array is completely sorted. The condition that the array has to be sorted for binary search to work has to be checked at each iteration. In cases when the (sub)array is rotated, we have to take extra measures in order for binary search to work.

## Efficiency

### Time Efficiency
At each iteration, after checking if the middle element is the number we search for, we do search the left and right subarrays not only if we think that the number lies left or right to the middle element based on comparing their values, but also if either the left or right subarray is rotated.

In the best case, the number we search for is always in the rotated subarray, which would result in `O(log(n))` time complexity.

In the worst case, we have to search both left and right side each time. That would double the original time efficiency of binary search, since we have to perform binary search twice at each step. The resulting time complexity is `O(2 * log(n))`, which converges for large `n` to `O(log(n))`.

### Space Efficiency
My implementation uses recursion, which requires extra stack space, leading to a `O(log(n))` space efficiency.

This could be reduced to `O(1)` by using an interative implementation (but I was a bit in a rush, it's on my todo list).