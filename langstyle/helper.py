#!/usr/bin/env python3

import os
import hashlib

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

def get_matched_items(iter, filter_fn, count):
    matched = []
    for item in iter:
        if len(matched) >= count:
            break
        if filter_fn(item):
            matched.append(item)
    return matched

def chain_lists(*lists):
    return [item for list_item in lists for item in list_item]

def md5_hash_str(str_arg):
    return md5_hash(str_arg.encode())

def md5_hash(bytes_args):
    md5 = hashlib.md5()
    md5.update(bytes_args)
    return md5.hexdigest()

def md5_hash_file(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(file_path)
    md5 = hashlib.md5()
    chunk_size = 1024
    with open(file_path, "rb") as f:
        while True:
            file_piece = f.read(chunk_size)
            if not file_piece:
                break
            md5.update(file_piece)
    return md5.hexdigest()

def generate_path_from_md5(md5):
    return md5[0:2] + os.sep + md5[2:4] + os.sep + md5

def create_dir_if_not_exist(full_path):
    owner_dir = os.path.dirname(full_path)
    if not os.path.exists(owner_dir):
        os.makedirs(owner_dir)
 
