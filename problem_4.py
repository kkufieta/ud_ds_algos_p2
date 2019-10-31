#%% [markdown]
# # Problem 4: Dutch National Flag Problem
# 
# Given an input array consisting on only `0`, `1`, and `2`, sort the array in a single traversal. You're not allowed to use any sorting function that Python provides.
# 
# Note: `O(n)` does not necessarily mean single-traversal. For e.g. if you traverse the array twice, that would still be an `O(n)` solution but it will not count as single traversal.

#%%
def sort_012(a):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       a(list): List to be sorted
    """
    # lo keeps track of the running index coming from the beginning of the list
    # hi keeps track of the running index coming from the end of the list
    # m1 and m2 keep track where the subarray of 1's is located 
    # (keeps track of the first and last index of the 1's subarray)
    assert(type(a) == list), "Array has to be a list"
    lo, m1 = 0, 0
    hi, m2 = len(a)-1, len(a)-1
    runtime = 0
    while lo <= hi:
        runtime += 1
        if a[lo] == 0:
            if m1 < lo:
                a[m1] = 0
                a[lo] = 1
            m1 += 1
            lo += 1
        elif a[hi] == 2:
            if m2 > hi:
                a[m2] = 2
                a[hi] = 1
            m2 -= 1
            hi -= 1
        elif a[lo] == 1:
            lo += 1
        elif a[hi] == 1:
            hi -= 1
        elif a[lo] == 2 and a[hi] == 0:
            if lo == m1:
                a[lo] = 0
            else:
                a[m1] = 0
                a[lo] = 1
            lo += 1
            m1 += 1
            if hi == m2:
                a[hi] = 2
            else:
                a[m2] = 2
                a[hi] = 1
            m2 -= 1
            hi -= 1
        else:
            print("Warning: Logic problem")    
    return a, runtime

#%% [markdown]
# ## Testing

#%%
DEBUG = False
def debug_print(text):
    if DEBUG:
        print(text)

def test_function(a):
    debug_print("\nTesting: {}".format(a))
    sorted_array, runtime = sort_012(a)
    debug_print("Result: {}".format(sorted_array))
    debug_print("len(a): {}, runtime: {}".format(len(a), runtime))
    assert(sorted_array == sorted(a) and runtime <= len(a))

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([])
test_function([0])
test_function([1])
test_function([2])
test_function([0, 0, 0])
test_function([0, 1, 2])
test_function([2, 1, 0])
test_function([0, 0, 0, 1, 1, 1, 2, 2, 2])
test_function([0, 0, 0, 0, 0, 0])
test_function([1, 1, 1, 1, 1, 1])
test_function([2, 2, 2, 2, 2, 2])
test_function([2, 2, 2, 1, 1, 1, 0, 0, 0, 0])

print("No AssertionError? We passed all tests!")


#%%
# This will throw an error as expected.
# test_function(0)


