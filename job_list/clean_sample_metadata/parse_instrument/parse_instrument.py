#!/usr/bin/env python3
"""
Author : kai
Date   : 2020-10-28
Purpose: Rock the Casbah

run: ./parse_instrument.py -i instrument_in.csv -o instrument_out.csv
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

    list_illumina = ['Illumina Genome Analyzer IIx', 'Illumina MiSeq', 'Illumina HiSeq 2500', 'Illumina HiSeq 2000' ,'NextSeq 550', 'NextSeq 500']
    list_454 = ['454 GS FLX Titanium','454 GS FLX']


    f = open(out_arg, 'a')

    for x in input_list:
        #print(x)
        if x in list_454:
            print('454',file=f)
        if x in list_illumina:
            print('Illumina',file=f)


# --------------------------------------------------
if __name__ == '__main__':
    main()
