"""
last modified on 7/10/2020 3.12pm by LLZ
"""
from itertools import product

# modify a,b and condition then run

# initialize a and b (modify here)
# use square brackets [] don't use {} for a
# example: a = [1, 2, 3, 4]
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# use () for b
# example: b = (1, 2, 3, 4)
b = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)


def condition(x, y):
    # the condition (modify the condition after return)
    # example: if condition is x + y > 10, then return x + y > 10
    return x < (3*y)


# printing original list and tuple
print("a : " + str(a))
print("b : " + str(b))

# Construct Cartesian Product Tuple list
# using itertools.product()
res = list(product(b, a))
# printing result
print("The Cartesian Product is : " + str(res))
print("")
ans = []
for i in res:
    x, y = i[0], i[1]
    if condition(x, y):
        ans.append((x, y))
print("answer =", ans)

