#!/usr/bin/env python3

def try_index(alist, value):
    not_found_index = -1
    if not alist:
        return not_found_index
    try:
        return alist.index(value)
    except ValueError:
        return not_found_index