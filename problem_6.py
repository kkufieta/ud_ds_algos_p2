#%% [markdown]
# # Problem 6: Unsorted Integer Array
# 
# ## Max and Min in a Unsorted Array
# 
# In this problem, we will look for smallest and largest integer from a list of unsorted integers. The code should run in `O(n)` time. Do not use Python's inbuilt functions to find min and max.
# 
# Bonus Challenge: Is it possible to find the max and min in a single traversal?

#%%
def get_min_max(nums):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       nums(list): list of integers containing one or more integers
    """
    assert(type(nums) == list), "nums has to be a list"
    assert(len(nums) > 0), "get_min_max() arg is an empty sequence"
    min_ = nums[0]
    max_ = nums[0]
    for n in nums:
        assert(type(n) == int), "numbers in the list have to be an integer"
        if n < min_:
            min_ = n
        if n > max_:
            max_ = n
    return (min_, max_)

#%% [markdown]
# ## Tests

#%%
def test_min_max(l):
    min_, max_ = get_min_max(l)
    assert(min_ == min(l) and max_ == max(l))


#%%
## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

test_min_max(l)

l = [0, 0, 0, 1, 2, 3]
random.shuffle(l)
test_min_max(l)

l = [0, 0, 0]
random.shuffle(l)
test_min_max(l)

l = [0, 999]
random.shuffle(l)
test_min_max(l)

l = [i for i in range(999)]
random.shuffle(l)
test_min_max(l)

print("No AssertionError? We passed all tests!")


#%%
# This will throw an error as expected.
# test_min_max(None)


#%%
# This will throw an error as expected.
# l = []
# random.shuffle(l)
# test_min_max(l)


