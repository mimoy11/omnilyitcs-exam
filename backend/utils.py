import math
import sys

def get_size(string):
    size_bytes = sys.getsizeof(string)
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    _int = int( math.floor( math.log( size_bytes, 1024 )))
    power = math.pow(1024, _int)
    print("POWER", power)
    size = round(size_bytes / power, 2)
    return "%s%s" % (size, size_name[_int])

