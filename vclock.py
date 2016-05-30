from functools import cmp_to_key, partial


def from_size(n):
    return (0,) * n


def merge(a, b):
    return tuple(max(j, k) for j, k in zip(a, b))


def compare(a, b):
    greater = False
    smaller = False
    for j, k in zip(a, b):
        greater |= j > k
        smaller |= j < k
    return int(greater) - int(smaller)


sort = partial(sorted, key=cmp_to_key(compare))


def is_concurrent(a, b):
    return (a != b) and compare(a, b) == 0
