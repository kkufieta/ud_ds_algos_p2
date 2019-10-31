# Explanation for Problem 7:  Request Routing in a Web Server with a Trie

## Requirements
There are no space or time complexity requirements for this problem.

## Code Design
The Router's functionality is to add paths and their respective handlers, as well as retrieve handlers for a given path.

The underlying datastructure is a RouteTrie, a trie that stores path segments as keys (as opposed to single characters).

## Efficiency
We are assuming that we store `n` paths and their respective handlers, and the "length" of a path is `m`. I believe that `n` can be a big number, while `m` should be a relatively small constant number.

### Time Efficiency
There are three main operations:

1. Insert a path & handler
2. Look up a handler for a given path

Given the assumptions mentioned above, it takes `O(m)` time complexity for both insertion and lookup of a path. That's `O(n*m)` to insert or look up `n` paths.

### Space Efficiency
The trie requires at most `O(n*m)` space.