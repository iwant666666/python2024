def merge(L1, L2):
    l = L1.copy()
    t = L2.copy()
    l.extend(t)
    T = []
    while len(l) > 0:
        a = min(l)
        l.remove(a)
        T.append(a)
    return T


def for_loop(L1, L2):
    l = L1 + L2
    print(l)

    for i in range(len(l)):
        for j in range(i, len(l)):
            if l[j] < l[i]:
                temp = l[i]
                l[i] = l[j]
                l[j] = temp
    return l


def main():
    L1 = [1, 5, 9, 12, 2, 6, 10]
    L2 = [5, 3, 7, 1, 10]
    # print(merge(sorted(L1), sorted(L2)))
    print(for_loop(L1, L2))
    # print([1, 5, 9, 12, 2, 6, 10, 5, 3, 7, 1, 10])
