#!/usr/bin/env python3
"""
Author : kai
Date   : 2020-10-28
Purpose: Rock the Casbah

run: ./parse_size.py -i size_in.csv -o size_out.csv
"""

import argparse
import sys
import csv
import re

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # parser.add_argument(
    #     'positional', metavar='str', help='A positional argument')


    parser.add_argument(
        '-i',
        '--input',
        help='input csv',
        metavar='str',
        type=str,
        default='')

    parser.add_argument(
        '-o',
        '--output',
        help='output csv',
        metavar='str',
        type=str,
        default='')

    parser.add_argument(
        '-f', '--flag', help='A boolean flag', action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def warn(msg):
    """Print a message to STDERR"""
    print(msg, file=sys.stderr)


# --------------------------------------------------
def die(msg='Something bad happened'):
    """warn() and exit with error"""
    warn(msg)
    sys.exit(1)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    in_arg = args.input
    out_arg = args.output

    input_list = []

    # open input.csv
    with open(in_arg, mode ='r', encoding='utf-8-sig') as input:
        csv_reader = csv.reader(input, delimiter=',')
        for row in csv_reader:
            input_list.append(row[0])


    regex_size = r"(\d*[.]?\d+)([a-z|A-Z]+)"
    div_size = '1024'

    f = open(out_arg, 'a')

    for x in input_list:
        if re.search(regex_size, str(x)):
            match = re.search(regex_size, str(x))
            #print(match.group(1), match.group(2))
            number = match.group(1)
            letter = match.group(2)

            if letter == 'Gb':
                print(number,file=f)
            if letter == 'Mb':
                print(round(float(number)/float(div_size),4),file=f)


# --------------------------------------------------
if __name__ == '__main__':
    main()
