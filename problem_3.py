#%% [markdown]
# # Problem 3: Rearrange Array Digits
# 
# Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers. You can assume that all array elements are in the range `[0, 9]`. The number of digits in both the numbers cannot differ by more than `1`. You're not allowed to use any sorting function that Python provides and the expected time complexity is `O(nlog(n))`.
# 
# for e.g. `[1, 2, 3, 4, 5]`
# 
# The expected answer would be `[531, 42]`. Another expected answer can be `[542, 31]`. In scenarios such as these when there are more than one possible answers, return any one.
#%% [markdown]
# ## Mergesort
# Getting the digits is trivial when the array is sorted. We can sort the array in `O(nlog(n))` time and `O(n)` space complexity.

#%%
def merge(a1, a2):
    '''
    Merges two sorted arrays into a single sorted array.
    '''
    assert(type(a1) == list), "a1 has to be an array"
    assert(type(a2) == list), "a2 has to be an array"
    
    i1, i2 = 0, 0
    len1, len2 = len(a1), len(a2)
    b = []
    while i1 < len1 and i2 < len2:
        if a1[i1] > a2[i2]:
            b.append(a1[i1])
            i1 += 1
        else:
            b.append(a2[i2])
            i2 += 1
    if i1 < len1:
        b = b + a1[i1:]
    if i2 < len2:
        b = b + a2[i2:]
    return b
    
    
def merge_sort(a):
    '''
    Sorts an array using merge sort.
    '''
    assert(type(a) == list), "a has to be an array"
    if len(a) == 1:
        return a
    mid = len(a)//2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    return merge(left, right)

#%% [markdown]
# ## Get digits from the sorted array
# This requires to loop through the sorted array once, which requires `O(n)` time. Together with the time efficiency for sorting the array, `O(n*log(n))`, the total time complexity is `O(n*log(n))`.

#%%
def get_digits(a):
    """
    Forms two numbers from the array digits such that their sum is maximum.
    """
    assert(type(a) == list), "a has to be an array"
    a = merge_sort(a)
    i = 0
    length_a = len(a)
    num_1, num_2 = "", ""
    for i, el in enumerate(a):
        if i%2 == 0:
            num_1 += str(el)
        else:
            num_2 += str(el)
    return [int(num_1), int(num_2)]


#%%
def rearrange_digits(a):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       a(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    assert(type(a) == list), "a has to be an array"
    assert(len(a) > 0), "a has to have at least one element"
    if (len(a) == 1):
        return [a[0], 0]
    if (len(a) == 2):
        if a[0] > a[1]:
            return [int(str(a[0]) + str(a[1])), 0]
        else:
            return [int(str(a[1]) + str(a[0])), 0]
    return get_digits(a)

#%% [markdown]
# ## Testing

#%%
def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    assert(sum(output) == sum(solution))

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[1], [1, 0]])
test_function([[9, 8], [98, 0]])
test_function([[8, 9], [98, 0]])
test_function([[9, 9, 9], [99, 9]])

print("No AssertionError? We passed all tests!")


#%%
# This will throw an error as expected:
# test_function([[], []])


