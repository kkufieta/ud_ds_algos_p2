#%% [markdown]
# # Problem 2: Search in a Rotated Sorted Array
# 
# You are given a sorted array which is rotated at some random pivot point.
# 
# Example: `[0,1,2,4,5,6,7]` might become `[4,5,6,7,0,1,2]`
# 
# You are given a target value to search. If found in the array return its index, otherwise return `-1`.
# 
# You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of `O(log n)`.
# 
# Example: `Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4`

#%%
def rotated_array_search(a, num):
    """
    Find the index by searching in a rotated sorted array

    Args:
       a(array), num(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    assert(type(a) == list), "a has to be an array"
    assert(type(num) == int), "num has to be an integer"
    return binary_search(a, num, 0, len(a)-1)


#%%
def is_sorted(a, lo, hi):
    """
    Checks if the array is sorted.
    
    This is based on the assumption that the array is sorted
    and then possibly rotated at a pivot point. Thus, we
    check if the array is rotated (which equals to not being sorted 
    here).
    """
    return a[lo] <= a[hi]

def binary_search(a, num, lo, hi):
    """
    Search for a number in the array using a modified binary search.
    """
    assert(type(a) == list), "a has to be an array"
    assert(type(num) == int), "num has to be an int"
    assert(type(lo) == int), "index lo has to be an int"
    assert(type(hi) == int), "index hi has to be an int"
    if lo > hi:
        return -1
    
    # Since the array is rotated, this introduces a violation of the
    # assumption that the array is completely sorted. The condition that
    # the array has to be sorted for binary search to work has to
    # be checked and accounted for.
    
    # The following is a modified version of binary search. The
    # key difference is that in addition to checking which subarray to
    # search based on whether the number we look for is smaller or 
    # greater than the number in the middle of the array,
    # we do also search a subarray if we detect that the subarray is
    # rotated. This does not add much to the time complexity, since
    # the chance that we have to search both subarrays (which are
    # divided by the middle element) is only 50% at each iteration.
    # More details can be found in the explanation.
    mid = (lo + hi)//2
    if num == a[mid]:
        return mid
    if not is_sorted(a, lo, mid) or (num < a[mid] and num >= a[lo]):
        result = binary_search(a, num, lo, mid-1)
        if result is not -1:
            return result
    if not is_sorted(a, mid, hi) or (num > a[mid] and num <= a[hi]):
        result = binary_search(a, num, mid+1, hi)
        if result is not -1:
            return result
    return -1

#%% [markdown]
# ## Tests

#%%
def linear_search(input_list, number):
    """
    Searches the array in linear time. 
    
    This is a helper function for testing.
    """
    assert(type(input_list) == list), "input_list has to be an array"
    assert(type(number) == int), "number has to be an integer"
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    a = test_case[0]
    number = test_case[1]
    result = rotated_array_search(a, number)
    assert(linear_search(a, number) == result)

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[], 10])
test_function([[5,6,7,8,9,1], 1])

print("No AssertionError? We passed all tests!")


