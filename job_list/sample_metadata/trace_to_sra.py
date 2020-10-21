#!/usr/bin/env python3
"""
Author : Kai
Date   : 2020-10-21
Purpose: Given list of trace urls i.e, https://trace.ncbi.nlm.nih.gov/Traces/sra/?run=SRR1185413 get SRA urls https://www.ncbi.nlm.nih.gov/sra/SRX482825 (or SRX experiment numbers)
run: python3 trace_to_sra.py -i input.csv -o experiment.csv
"""

import argparse
import sys
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import requests #for lxml
import re #for regex string matching
import csv
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




# attempting webscraping based on the code from:
# https://github.com/julia-git/webscraping_ny_mta/blob/master/Webscraping.ipynb
# Could also try https://www.freecodecamp.org/news/web-scraping-python-tutorial-how-to-scrape-data-from-a-website/

# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    #in_csv = args.positional
    in_csv = args.input
    sample_list = []
    pre_url = 'https://trace.ncbi.nlm.nih.gov/Traces/sra/?run='

    # open input.csv
    with open(in_csv, mode ='r', encoding='utf-8-sig') as input:
        csv_reader = csv.reader(input, delimiter=',')
        for row in csv_reader:
            sample_list.append(row[0])

    sample_list =[pre_url + s for s in sample_list]
    dict_list = []

    for url in sample_list:

        dict = {}
        dict['accession'] = url[47:]
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'lxml')
        regex= r'id=\"exp-accession\">(\S+)</a></td>'

        if re.search(regex, str(soup)):
            match = re.search(regex, str(soup))
            dict['experiment'] = match.group(1)

        dict_list.append(dict)

    #print(dict_list)

    # Write out to csv
    csv_file = args.output
    #csv_file = "output.csv"
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=list(dict_list[0].keys()))
        writer.writeheader()
        for data in dict_list:
            writer.writerow(data)

# --------------------------------------------------
if __name__ == '__main__':
    main()
