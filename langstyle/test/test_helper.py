#!/usr/bin/env python

import os
import sys
import itertools
import random

def generate_character(prefixes=[], rests=[], length=None):
    if length == 0:
        return ""
    if not prefixes:
        prefixes = _A_to_Z_a_to_z()
    if not rests:
        rests = _A_to_Z_a_to_z()
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

def choice(seq):
    return random.choice(seq)

def _A_to_Z_a_to_z():
    return [str(chr(char_int)) 
            for char_int in itertools.chain(range(65,91), range(97, 123))]

def _0_to_9():
    return [str(num) for num in range(0, 10)]

def generate_int_exclude(exclude_ints = []):
    random_int = random.randrange(0, 1000000000)
    if random_int not in exclude_ints:
        return random_int
    return generate_int_exclude(exclude_ints)

def generate_some_ids(count):
    '''generate distinct ids'''
    if count< 0:
        count = 0
    ids =[]
    for i in range(0, count):
        ids.append(generate_int_exclude(ids))
    return ids

def generate_mock_image():
    image_data = []
    image_data_src = [os.linesep]
    image_data_src.extend(_A_to_Z_a_to_z())
    image_data_src.extend(_0_to_9())
    length = random.randrange(100, 1000)
    for i in range(0, length):
        image_data.append(random.choice(image_data_src))
    return "".join(image_data)

def generate_some_mock_images(count):
    images = []
    if count is None or count <= 0:
        count = 0
    for i in range(0, count):
        images.append(generate_mock_image())
    return images

def generate_mock_image_exclude(exclude_images=[]):
    random_image = generate_mock_image()
    if random_image not in exclude_images:
        return random_image
    return generate_mock_image_exclude(exclude_images)