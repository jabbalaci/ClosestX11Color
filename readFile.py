import re

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


def read_file():
    with open(INPUT) as f:
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
