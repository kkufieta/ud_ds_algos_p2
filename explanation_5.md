# Explanation for Problem 5:  Autocomplete with Tries

## Requirements
There are no efficiency requirements for this problem.

## Code Design
The design was already given: The problem is solved using Tries.

## Efficiency
We're assuming there are `n` words stored in the Trie. The longest word has `m` characters.

We can think of the prefix as having `m1` characters, and the suffixes are `m2` characters long, with `m = m1 + m2`.

### Time Efficiency
There are three main operations for autocompletion using Tries:

1. Insert a word
2. Look up a word
3. Get all stored suffixes given a prefix.

Given the assumptions mentioned above, it takes `O(m)` time complexity for both insertion and lookup of a word. That's `O(n*m)` to insert or look up `n` words.

When we want to get all suffixes for a given prefix, we need:

1. `O(m1)` to get to the node that contains all possible suffixes.
2. `O(n*m2)` to look up all `n` suffixes

which results in a total of `O(m1 + n*m2) = O(m + m2*(n-1))` which can be simplified to an upper bound of `O(n*m)` time efficiency.

### Space Efficiency
The trie requires at most `O(n*m)` space.