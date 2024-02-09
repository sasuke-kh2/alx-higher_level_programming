#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    result = 0
    x = 0
    y = 0
    if not tuple_a:
        tuple_a = (0, 0)
    elif not tuple_b:
        tuple_b = (0, 0)
    elif len(tuple_a) == 1:
        tuple_a = (tuple_a[0], 0)
    elif len(tuple_b) == 1:
        tuple_b = (tuple_b[0], 0)
    x = tuple_a[0] + tuple_b[0]
    y = tuple_a[1] + tuple_b[1]
    result = (x, y)
    return result
