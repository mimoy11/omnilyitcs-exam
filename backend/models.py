import os
import sys
import random
import string
import math
import csv

import config

MAX_MB = 2 # 2000KB or 2MB


def get_size_compact(filepath):
    value = os.path.getsize(filepath)
    kb = float(1024)
    return float(value / float(kb ** 2))


def generate_random(_type, length):
    return ''.join( random.choice( _type ) for i in range(length))

def generate_random_float(length):
    return ''.join( str(round(random.uniform(0, 99999),
                    int(random.choice(string.digits)))) \
                        for i in range(length))


def producer():
    """This method produces a random type of character set to generate.
    Each character type can either be 
    """
    length = random.randint(10, 30)
    bucket = {
        # alphabet
        "alphabet": generate_random(string.ascii_letters, length),
        # Real Numbers
        "real_numbers": generate_random(string.digits, length),
        # Alphanumeric Numbers
        "alphanumeric": generate_random(string.hexdigits, length),
        # Integers
        "integers": generate_random_float(length)
    }
    key = random.choice(list(bucket.keys()))
    return key, bucket[key]


def gen_random_alphabet(filename):
    """This method produces random strings into a file
    then generates a report based on the number of generated
    strings
    """
    value = ""
    stats_list = {
        "alphabet": 0,
        "real_numbers": 0,
        "integers": 0,
        "alphanumeric": 0
    }

    filepath = config.DOWNLOAD_PATH % filename

    # Produce random chars into a file
    with open(filepath, "w") as _file:
        row = []
        while get_size_compact(filepath) <= MAX_MB:
            key, item = producer()
            item += ", "
            stats_list[key] += 1
            _file.write(item)

    with open(filepath, "rb+" ) as _file:
        _file.seek(_file.tell()-2, 2)
        _file.truncate()

    return stats_list
