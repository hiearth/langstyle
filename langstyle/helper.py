#!/usr/bin/env python3

def try_index(alist, value):
    if not alist:
        return None
    try:
        return alist.index(value)
    except ValueError:
        return None

def find_first(iter, find_fn):
    find_generator = (item for item in iter if find_fn(item))
    return next(find_generator, None)

def list_comprehension_by_index(iter, index):
    return [item[index] for item in iter]