# Explanation for Problem 3:  Rearrange Array Digits

## Requirements
The required time efficiency is `O(n*log(n))`, and the use of python's sorting functions is prohibited.

## Code Design
In order to achieve the required time efficiency, I decided to use mergesort, which has an `O(n*log(n))` time efficiency and an `O(n)` space complexity. After that, finding the max numbers is trivial.

## Efficiency

### Time Efficiency
First, the array has to be sorted. Using mergesort this is done in `O(n*log(n))` time. After that, we loop through the sorted array to form the two numbers, which takes `O(n)` time. Together, we end up with a time efficiency of `O(n*log(n))`.

### Space Efficiency
The space efficiency for mergesort is `O(n)`, which is the upper bound for the entire algorithm.