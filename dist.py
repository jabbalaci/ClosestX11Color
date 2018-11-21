#!/usr/bin/env python3

import re
from pprint import pprint

INPUT = "colors.csv"

def extract_rgb_values(rgb_str):
    m = re.search(r"rgb\((.*),(.*),(.*)\)", rgb_str)
    if m:
        r = int(m.group(1))
        g = int(m.group(2))
        b = int(m.group(3))
        return (r, g, b)
    else:
        return None

def read_file(fname):
    with open(fname) as f:
        lines = f.read().splitlines()

    d = {}
    header = [part.strip() for part in lines[0].split(";")]
    # print(header)
    for line in lines[1:]:
        (xterm_number, xterm_name, hex_str, rgb_str, hsl_str) = [part.strip() for part in line.split(";")]
        # print(xterm_number, xterm_name, hex_str, rgb_str, hsl_str)
        d[int(xterm_number)] = {
            'xterm_number': xterm_number,
            'xterm_name': xterm_name,
            'hex_str': hex_str,
            'rgb_str': rgb_str,
            'rgb_values': extract_rgb_values(rgb_str),
            'hsl_str': hsl_str
        }
    #
    return d


def distance(p1, p2):
    a = abs(p1[0] - p2[0])
    b = abs(p1[1] - p2[1])
    c = abs(p1[2] - p2[2])
    return a + b + c


def find_closest(d, rgb_tuple):
    copy = d.copy()
    li = []
    for k, v in copy.items():
        dist = distance(v['rgb_values'], rgb_tuple)
        v['rgb_dist'] = dist
        li.append(v)
        # print(k)
        # print(v)
        # print("point:", p)
        # print(dist)
        # print("=" * 78)
    #
    closest = min(li, key=lambda e: e['rgb_dist'])
    return closest


def find_closest_color(rgb_tuple):
    d = read_file(INPUT)
    # pprint(d)
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
