#!/usr/bin/env python3

import re
from pprint import pprint


def distance(p1, p2):
    a = abs(p1[0] - p2[0])
    b = abs(p1[1] - p2[1])
    c = abs(p1[2] - p2[2])

    return a + b + c


def find_closest(d, rgb_tuple):
    li = []
    for k, v in d.items():
        dist = distance(v['rgb_values'], rgb_tuple)
        v = v.set('rgb_dist', dist)
        li.append(v)
        # print(k)
        # print(v)
        # print("point:", p)
        # print(dist)
        # print("=" * 78)
    #
    
    newli = sorted(li, key=lambda e: e['rgb_dist'])
    (closest, second, third) = newli[:3]
    
    return (closest, second, third)


def find_closest_color(rgb_tuple):
    #d = read_file(INPUT)
    #pprint(d)
    return find_closest(d, rgb_tuple)

##############################################################################

if __name__ == "__main__":
    p = (123, 201, 22)
    result = find_closest_color(p)
    text = ""
    for k, v in result.items():
        text += (f"{k}: {v}\n")
    print(result)
    print(text)
