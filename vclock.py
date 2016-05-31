import sys
import itertools
from functools import cmp_to_key, partial

if sys.version_info[0] == 2:
    zip = itertools.izip
    map = itertools.imap


def from_size(n):
    return (0,) * n


def merge(a, b):
    return tuple(map(max, zip(a, b)))


def compare(a, b):
    gt = False
    lt = False
    for j, k in zip(a, b):
        gt |= j > k
        lt |= j < k
        if gt and lt:
            break
    return int(gt) - int(lt)


def sort(xs, key=None, reverse=False):
    cmpfunc = (
            compare if key is None else
            lambda a, b: compare(key(a), key(b))
        )
    return sorted(xs, key=cmp_to_key(cmpfunc),
                      reverse=reverse)


def is_concurrent(a, b):
    return (a != b) and compare(a, b) == 0


def increment(clock, index):
    return clock[:index] \
            + (clock[index] + 1,) \
            + clock[index+1:]
