def detect_ranges(L):
    l = L.copy()
    l.sort()
    output = []
    m = n = l[0]   # initialize the start and the end, m = start and n = end
    lst = [m, n]   # create a new range in the sorted list
    # print(l)
    for i in l[1:] + [None]:    # iterate over the sorted list from the second number to the last number of the list.
        # [None] is to ensure the last number of the sorted range can be added to the output
        if i is not None and n + 1 == i:  # determine weather the next number i is consecutive after end
            # if it's ture,then the range[m,n] should update
            n = i  # update the n with i
            # print(m, n) # new list after update
        else: # if the current number is not consecutive, we consider

            if m == n: # if the range only contains single number
                # print("m = n = ", m)
                output.append(m)
            else:
                # print(f"m = {m}, n = {n}") # if the range contains more than on number
                output.append((m, n + 1))
            if i is not None:  # if it's not the end of the list
                m = n = i  # restart a new range
        # print(m, n)

    return output


def main():
    pass
    res = detect_ranges([2, 5, 4, 8, 12, 6, 7, 10, 13, 14])
    print(res)