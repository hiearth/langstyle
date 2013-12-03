#!/usr/bin/env python3

def try_index(alist, value):
    if not alist:
        return None
    try:
        return alist.index(value)
    except ValueError:
        return None