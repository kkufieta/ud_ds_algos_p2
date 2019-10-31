#%% [markdown]
# # Problem 1: Square Root of an Integer
# 
# Find the floor value of the square root of an integer without using any Python library.
# 
# E.g. if the given number is 16, then the answer would be 4.
# 
# If the given number is 27, the answer would be 5 because `sqrt(27) = 5.196` whose floor value is 5.
# 
# The expected time complexity is `O(log(n))`.
#%% [markdown]
# ## Algorithm choice
# At first, I came up with an algorithm that seemed to work well with `O(log(n))` time complexity - but I tested it only values for up to `n = 100` (and overlooked a few failed test cases, oups).
# 
# Once I added an edge case of `n = 999999`, the time complexity sky rocketed for my algorithm. So I searched for and found a simple [algorithm](http://www.math.com/school/subject1/lessons/S1U1L9DP.html) which solved my problem.
# 
# Inspired by this, I added an optional section where I compare the results and time complexity of my own vs. the improved algorithm.

#%%
def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    assert(type(number) == int), "The argument has to be an integer"
    assert(number >= 0), "The argument has to be positive"
    
    _steps = 0
    if number <= 1:
        return number, _steps
    
    # First, find two square numbers that our number lies between.
    # This takes <= O(log(n)) time.
    num = 2
    while num*2 < number//(num*2):
        _steps += 1
        num *= 2
    
    # These are the two square numbers:
    n1 = num
    n2 = num*2
        
    while True:
        _steps += 1
        # Divide the number by the two square numbers
        d1 = number/n1
        d2 = number/n2
        
        # Average the two square numbers and the divided numbers
        # to estimate the square root of our number
        root = (n1 + n2 + d1 + d2)/4
        
        # Check if we're close to the square root of our number
        root_floor = root//1
        root_ceil = (root + 1)//1
        if root_floor * root_floor <= number and root_ceil * root_ceil >= number:
            return int(root_floor), _steps
        else:
            n1 = root_floor
            n2 = root_ceil

#%% [markdown]
# # Tests

#%%
import math

def test_sqrt(number):
    own_square_root, _num_steps = sqrt(number)
    square_root = int(math.floor(math.sqrt(number)))
    
    correct_square_root = square_root == own_square_root
    correct_time_complexity = (number == 0) or _num_steps <= math.ceil(math.log2(number))

    assert(correct_square_root and correct_time_complexity), "Something is wrong for number: " + str(number)


#%%
for number in [10, 9, 0, 16, 1, 27, 2, 3, 4, 5, 25, 100, 999999, 92381739019381112]:
    test_sqrt(number)

print("No AssertionError? We passed all tests!")
# NOTE: The tests are commented out so the script won't stop running.
# test_sqrt(-1)
# test_sqrt('a')