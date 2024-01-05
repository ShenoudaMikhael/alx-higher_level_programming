#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """Adds two tuples element-wise."""
    new_tuple = list()
    new_tuple.append(
        (tuple_a[0] if len(tuple_a) >= 1 else 0)
        + (tuple_b[0] if len(tuple_b) >= 1 else 0)
    )
    new_tuple.append(
        (tuple_a[1] if len(tuple_a) >= 2 else 0)
        + (tuple_b[1] if len(tuple_b) >= 2 else 0)
    )
    return tuple(new_tuple)
