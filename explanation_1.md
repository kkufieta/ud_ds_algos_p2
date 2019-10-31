# Explanation for Problem 1:  Square Root of an Integer

## Requirements
Find the floor value of the square root of an integer without using any Python library.

The required time complexity is `O(log(n))`.

## Code Design
At first, I came up with an algorithm that seemed to work well with `O(log(n))` time complexity - but I tested it only for values for up to `n = 100` (and overlooked a few failed test cases, oups).

Once I added an edge case of `n = 999999`, the time complexity sky rocketed for my algorithm. So I searched for and found a simple [algorithm](http://www.math.com/school/subject1/lessons/S1U1L9DP.html) which solved my problem.

Inspired by this, I kept my own algorithm and added an optional section where I compare the results and time complexity of my own vs. the improved algorithm. The following efficiency analysis reflects that.

NOTE: The optional section is only available in the jupyter version of this assignment, under `jupyter/problem_1.ipynb`.

## Efficiency
For both algorithms (improved and my own), there are two steps. The first step is equal for both, whereas the second step makes the difference in time efficiency.

### Time Efficiency: Improved Algorithm
The improved algorithm has a runtime of `O(log(n))`. The two steps are:

1. Start with an estimated root `n=2` and multiply it by 2 until we come close to our actual root. Because we're doubling the estimated root at each step, this takes `O(log(n))` time.

2. Estimate two roots `num1` & `num2` such that `num1^2 <= number <= num2^2`. Next, we estimate the error between the two estimated roots and the actual root of our number. But since we don't have the actual root, we do have to estimate it by using the two estimated roots: `number/num1`, and `number/num2`. That way, we get two estimates of our root, and the actual root lies between those two estimates. Next, we divide the error between our estimated roots and our (estimated) actual root by two and update our estimated roots `num1` and `num2`. We repeat this process until we get the correct result. Since we're always dividing the error by two, this takes `O(log(n))` time. Looking closer at the formula, we can see that having to use the estimates for the root moves us even faster towards the solution than `O(log(n))`, because we reduce the error by more than half. Using estimates from both sides of our root number, we're making sure that we're moving with `O(log(n))` efficiency towards the solution no matter where the actual root lies between `num1` and `num2` (e.g. the root could be really close to `num2` and thus really far from `num1`, so if we only used `num1` to estimate the `root`, it would take more time). Since we're always reducing the error faster than dividing it by `2` at each step, the time complexity is actually less than `O(log(n))` for this part, which we can see from the plots I made in the optional part of my assignment. Looking at the plot, it seems like the time complexity is thus `O(1/2 * log(n))` for large numbers.

### Time Efficiency: Own Algorithm  (incorrect results and poor time efficiency)
My own algorithm has a time efficiency of `O(log(n) + n)` which is simplified to `O(n)`. The two steps are:

1. Start with an estimated root `n=2` and multiply it by 2 until we come close to our actual root. Because we're doubling the estimated root at each step, this takes `O(log(n))` time.

2. Using the estimated root as a starting point, search linearly until we find the (assumingly) correct square number. This fails for `number = 2` and `number = 3`, but I didn't bother fixing it since this is only an optional part that I decided to keep in the assignment.

### Space Efficiency

The space efficiency is `O(1)`, since we're only storing `ints` and `floats`.