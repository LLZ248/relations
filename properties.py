"""
last modified on 7/10/2020 3.12pm by LLZ
"""

# put in your R and set here (modify here), use square brackets [] don't use {}
set_for_R = [0, 1, 2, 3]
# example: R = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 2), (2, 3)]
R = [(0, 0), (1, 1), (1, 3), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]

print("set =", set_for_R)
print("R =", R)
print("\nResult: ")
if len(R) != 1:

    # all self-loop pairs such as {(0, 0), (1, 1), (2, 2), (3, 3)}
    all_selfloop_pairs = True
    for i in R:
        x, y = i[0], i[1]
        if x != y:
            all_selfloop_pairs = False
            break

    if all_selfloop_pairs:
        reflexive = True
        for i in set_for_R:
            if (i, i) not in R:
                reflexive = False
                print("not reflexive, expecting", (i, i))
                break
        if reflexive:
            print("reflexive")
        print("symmetric")
        print("antisymmetric")
        print("transitive")
        if reflexive:
            print("partial order")
            print("equivalence")
        else:
            print("not partial order")
            print("not equivalence")

    else:
        reflexive = True
        reflexiveSet = []
        for i in set_for_R:
            reflexiveSet.append((i, i))

        for i in reflexiveSet:
            if i not in R:
                reflexive = False
                print("not reflexive, expecting:", i)
                break
        if reflexive:
            print("reflexive")

        symmetric = True
        antisymmetric = True
        for i in R:
            x, y = i[0], i[1]
            if x != y:
                if (y, x) not in R:
                    print("not symmetric, there is", (x, y), "but no", (y, x))
                    symmetric = False
                    break

        if symmetric:
            print("symmetric")

        for i in R:
            x, y = i[0], i[1]
            if x != y:
                if (y, x) in R:
                    print("not antisymmetric, there are", (x, y), "and", (y, x))
                    antisymmetric = False
                    break
        if antisymmetric:
            print("antisymmetric")

        transitive = True
        end = len(R)
        transitive_loop_break = False
        for i in range(len(R)):
            for j in range(1, end):
                if R[i][1] == R[j][0]:
                    x, y = R[i][0], R[i][1]
                    y1, z = R[j][0], R[j][1]
                    if (x, z) not in R:
                        transitive = False
                        print("not transitive, there are", (x, y), "and", (y1, z), "but no", (x, z))
                        transitive_loop_break = True
                        break
            if transitive_loop_break:
                break
        if transitive:
            print("transitive")
        if reflexive and antisymmetric and transitive:
            print("partial order", end=" ")
        else:
            print("not partial order", end=" ")
        print("because (Reflexive:" + str(reflexive), ", Antisymmetric:" + str(antisymmetric),
              ", Transitive:" + str(transitive) + ")")
        if reflexive and symmetric and transitive:
            print("equivalence", end=" ")
        else:
            print("not equivalence", end=" ")
        print("because (Reflexive:" + str(reflexive), ", Symmetric:" + str(symmetric),
              ", Transitive:" + str(transitive) + ")")

else:  # if the R only has one element
    x, y = R[0][0], R[0][1]
    reflexive = False
    if len(set_for_R) == 1:
        if x == y and x == set_for_R[0]:
            reflexive = True
            print("reflexive")
    else:
        print("not reflexive")
    print("not symmetric")
    print("antisymmetric")
    print("transitive")
    if reflexive:
        print("partial order\nnot equivalence")
    else:
        print("not partial order\nnot equivalence")
