#!/usr/bin/env python
from __future__ import print_function
import argparse
from sys import stdout
from math import floor

calc_parser = argparse.ArgumentParser(
    description="""
    A grid calculator. It finds a grid that fits within given constraints.
    """,
)
calc_parser.add_argument(
    "columns",
    help="Number of columns",
    type=int,
    default=12
)
calc_parser.add_argument(
    "width",
    help="Space that grid must fit within",
    type=int,
    default=1024
)
calc_parser.add_argument(
    "gutter",
    help="Gutter width",
    type=int,
    default=24
)
calc_parser.add_argument(
    '-g','--include_gutter',
    help="Include gutter on the left and right of the grid?",
    type=bool,
    default=False
)
calc_parser.add_argument(
    '-o','--out_file',
    help="A file to write results to. If no file is provided, stdin will be used.",
    type=argparse.FileType('w'),
    default=stdout
)

def fit_col(columns, width, gutter):
    """
    Calculate nearest column width that will fit `columns` number of columns
    within `width` given `gutter`.
    """
    return int(floor((width - (gutter * (columns - 1))) / columns))

def colspan(span, column, gutter):
    return int((column * span) + (gutter * (span - 1)))

def swiss_calc():
    """Calc command"""
    args = calc_parser.parse_args()
    columns = args.columns
    gutter = args.gutter
    include_gutter = args.include_gutter
    width = (args.width - (gutter * 2)) if include_gutter else args.width
    column = fit_col(columns, width, gutter)
    print("Width: {}".format(colspan(columns, column, gutter)))
    print("Gutter: {}".format(gutter))
    for i in range(1, columns):
        print("Column {}x: {}".format(i, colspan(i, column, gutter)))

if __name__ == '__main__':
    swiss_calc()