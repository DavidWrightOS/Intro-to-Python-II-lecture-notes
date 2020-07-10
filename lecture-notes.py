### Python Basics II

print('\n\n//**********************// FUNCTIONS //**********************//')

print('\nFunctions pass arguments by-reference:\n')

# Python functions pass arguments by-reference (unless a parameter is immutable)

l = [1, 2, 3, 4]

def mult2_list(l):
    for i in range(len(l)):
        l[i] *= 2
    return l

# Calling 'mult2_list(l)' will change 'l' because it is passed-by-reference

print(l)                                            # [1, 2, 3, 4]
print(mult2_list(l))                                # [2, 4, 6, 8]
print(l)                                            # [2, 4, 6, 8]



print('\n\n//**********************// LISTS //**********************//')

print('\nDoubling a list:\n')

l2 = [1, 2, 3, 4]

print(l2)                                           # [1, 2, 3, 4]
print(l2 + l2)                                      # [1, 2, 3, 4, 1, 2, 3, 4]
print(l2 * 2)                                       # [1, 2, 3, 4, 1, 2, 3, 4]



print('\n\n//**********************// MAP //**********************//')

print('\nDoubling each element in a list:\n')

# Use Python's built-in 'map' function to Double each element in a list

# When using 'lambda', define a temporary variable (e.g. 'x') to represent each element
# In the code below, 'x' is similar to '$0' in Swift's closure syntax
# The 'map' function returns an 'iterator' type, so we need to cast back to a 'list'

print(l2)                                           # [1, 2, 3, 4]
print(list(map(lambda x: x*2, l2)))                 # [2, 4, 6, 8]
print(l2)                                           # [1, 2, 3, 4]