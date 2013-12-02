#!/usr/bin/env python

import sys
import itertools
import random

def generate_character(prefixes=[], rests=[], length=None):
    if length == 0:
        return ""
    if not prefixes:
        prefixes = A_to_Z_a_to_z()
    if not rests:
        rests = A_to_Z_a_to_z()
    if length is None or length < 0:
        length = random.randrange(1, 50)
    random_character = []
    random_character.append(random.choice(prefixes))
    for i in range(0,length):
        random_character.append(random.choice(rests))
    return "".join(random_character)

def generate_some_characters(count):
    '''generate distinct characters'''
    if count < 0:
        count = 0
    characters = []
    for i in range(0, count):
        characters.append(generate_character_exclude(characters))
    return characters

def generate_character_exclude(exclude_characters = []):
    random_character = generate_character()
    if random_character not in exclude_characters:
        return random_character
    return generate_character_exclude(exclude_characters)

def choice_character(characters):
    return random.choice(characters)

def A_to_Z_a_to_z():
    return [str(chr(char_int)) 
            for char_int in itertools.chain(range(65,91), range(97, 123))]

def generate_int_exclude(exclude_ints = []):
    random_int = random.randrange(0, sys.maxsize)
    if random_int not in exclude_ints:
        return random_int
    return generate_int_exclude(exclude_ints)
