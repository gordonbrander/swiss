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
    type=float,
    default=1024
)
calc_parser.add_argument(
    "gutter",
    help="Gutter width",
    type=float,
    default=24
)
calc_parser.add_argument(
    '-o','--include_outer',
    help="Include outer gutter on the left and right of the grid?",
    type=bool,
    default=False
)
calc_parser.add_argument(
    '-u','--unit',
    help="""An underlying pixel grid unit to fit grid to (defaults to 1).
    For example, if you specify 8, the grid generated will cleanly fit on top
    of an 8px grid.""",
    type=float,
    default=1
)

def nearest_divisible(n, x):
    """
    Find the nearest number below n that is divisible by x
    with no fraction remaining
    """
    return (n - (n % x)) if n > x else x

def fit_col(columns, width, gutter, unit=1):
    """
    Calculate nearest column width that will fit `columns` number of columns
    within `width` given `gutter`.

    unit (if given) will ensure that the grid fits on top of an underlying
    pixel grid.
    """
    span = (width - (gutter * (columns - 1))) / columns
    return nearest_divisible(span, unit)

def fit_gutter(gutter, unit=1):
    """Find nearest gutter that will fit on top of grid of `unit`"""
    return nearest_divisible(gutter, unit)

def colspan(span, column, gutter):
    """
    Calculate colspan for `span` number of columns given `column` and `gutter`
    width.
    """
    return (column * span) + (gutter * (span - 1))

def swiss_calc():
    """Calc command"""
    args = calc_parser.parse_args()
    columns = args.columns
    unit = args.unit
    gutter = fit_gutter(args.gutter, unit)
    include_outer = args.include_outer
    width = (args.width - (gutter * 2)) if include_outer else args.width
    column = fit_col(columns, width, gutter)
    print("Width: {}".format(colspan(columns, column, gutter)))
    print("Gutter: {}".format(gutter))
    for i in range(0, columns):
        print("Colspan {}: {}".format(i + 1, colspan(i + 1, column, gutter)))

if __name__ == '__main__':
    swiss_calc()