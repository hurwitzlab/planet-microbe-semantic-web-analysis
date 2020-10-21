#!/usr/bin/env python3
"""
Author : Kai
Date   : 2020-10-21
Purpose: Parse metadata from the NCBI browser: e.g., https://www.ncbi.nlm.nih.gov/sra/SRX482825
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

    parser.add_argument(
        'positional', metavar='str', help='A positional argument')

    parser.add_argument(
        '-a',
        '--arg',
        help='A named string argument',
        metavar='str',
        type=str,
        default='')

    parser.add_argument(
        '-i',
        '--int',
        help='A named integer argument',
        metavar='int',
        type=int,
        default=0)

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
    in_csv = args.positional

    sample_list = []
    pre_url = 'https://www.ncbi.nlm.nih.gov/sra/'
    post_url = '[accn]'

    # open input.csv
    with open(in_csv, mode ='r', encoding='utf-8-sig') as input:
        csv_reader = csv.reader(input, delimiter=',')
        for row in csv_reader:
            sample_list.append(row[0])

    sample_list =[pre_url + s + post_url for s in sample_list]
    dict_list = []

    for url in sample_list:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'lxml')
        # make dict to add values to https://www.guru99.com/python-dictionary-append.html
        dict = {}
        dict['experiment'] = url[33:]
        ### This works to get the instrument as a string from the Library information
        #https://stackoverflow.com/questions/2136267/beautiful-soup-and-extracting-a-div-and-its-contents-by-id
        lib_info = soup.find_all("div", class_="expand showed sra-full-data")
        # use https://www.tutorialspoint.com/pattern-matching-in-python-with-regex and https://regex101.com/
        regex1 = r"Instrument: <span>([\w|\s]+)</span>"
        if re.search(regex1, str(lib_info)):
            match = re.search(regex1, str(lib_info))
            dict['instrument'] = match.group(1)

        ## This works to parse the table at the bottom of the page that has "# Bases" and "Size" etc
        table = soup.find("table")
        regex2= r'\">([\d|a-zA-Z]+)</a></td><td align=\"right\">(\S+)</td><td align=\"right\">(\S+)</td><td align=\"right\">(\S+)</td><td>(\S+).*</td></tr></tbody></table>'
        if re.search(regex2, str(table)):
            match = re.search(regex2, str(table))
            dict['run'] = match.group(1)
            dict['spots'] = match.group(2)
            dict['bases'] = match.group(3)
            dict['size'] = match.group(4)
            dict['published'] = match.group(5)


        dict_list.append(dict)

    #print(dict_list)

    # Write out to csv
    csv_file = "output.csv"
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=list(dict_list[0].keys()))
        writer.writeheader()
        for data in dict_list:
            writer.writerow(data)

# --------------------------------------------------
if __name__ == '__main__':
    main()
