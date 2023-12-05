__author__ = "Andrea Rubbi"
import time

def bypassbranch(subset, i):  # bypass a branch
    for j in range(i - 1, -1, -1):
        if subset[j] == 0:
            subset[j] = 1
            return subset, j + 1

    return subset, 0

def nextvertex(subset, i, m):
    if i < m:
        subset[i] = 0
        return subset, i + 1
    else:
        for j in range(m - 1, -1, -1):
            if subset[j] == 0:
                subset[j] = 1
                return subset, j + 1

    return subset, 0

def BB(universe, sets, costs):
    subset = [1 for x in range(len(sets))]  # all sets in
    subset[0] = 0
    bestCost = sum(costs)  # actually the worst cost
    i = 1

    while i > 0:

        if i < len(sets):
            cost, tSet = 0, set()  # t for temporary
            for k in range(i):
                cost += subset[k] * costs[k]  # if 1 adds the cost to total
                if subset[k] == 1: tSet.update(set(sets[k]))  # if 1 add the set to the cover

            if cost > bestCost:  # if the cost is larger than the currently best one, no need of further investigation
                subset, i = bypassbranch(subset, i)
                continue
            for k in range(i, len(sets)): tSet.update(set(sets[k]))
            if tSet != universe:  # that means that the set was essential at this point to complete the uni.
                subset, i = bypassbranch(subset, i)
            else:
                subset, i = nextvertex(subset, i, len(sets))

        else:
            cost, fSet = 0, set()  # f for final
            for k in range(i):
                cost += subset[k] * costs[k]
                if subset[k] == 1: fSet.update(set(sets[k]))

            if cost < bestCost and fSet == universe:
                bestCost = cost
                bestSubset = subset[:]
            subset, i = nextvertex(subset, i, len(sets))

    return bestCost, bestSubset

def main(a, b, c, z=time.time()):
    m = a
    S = b
    C = c
    F = set([x for x in range(1, m + 1)])
    X = BB(F, S, C)
    cost = X[0]
    sets = X[1]
    cover = []
    for x in range(len(sets)):
        if sets[x] == 1:
            cover.append(S[x])
    print('covering sets: ', cover, '\n', 'total cost: ', cost, '$')
    print('time:', time.time() - z)
