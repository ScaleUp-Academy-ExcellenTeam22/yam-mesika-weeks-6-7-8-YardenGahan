from collections import defaultdict


def group_by(func, param):
    d = defaultdict(list)

    for val in param:
        d[func(val)].append(val)
    return d


print(group_by(len, ["hi", "bye", "yo", "try"]))