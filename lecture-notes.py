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
