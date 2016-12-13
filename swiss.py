#!/usr/bin/env python
from __future__ import print_function
import argparse
from sys import stdout

calc_parser = argparse.ArgumentParser(
    description="""
    A grid calculator. It finds a grid that fits within given constraints.
    """,
)
calc_parser.add_argument(
    "columns",
    help="Number of columns in grid",
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
    help="Gutter width (may be adjusted to conform to unit)",
    type=float,
    default=24
)
calc_parser.add_argument(
    '-o','--include_outer',
    help="Include an outer gutter to the left and right of the grid?",
    type=bool,
    nargs="?",
    const=True,
    default=False
)
calc_parser.add_argument(
    '-u','--unit',
    help="""An underlying pixel grid unit to fit layout grid to (defaults to 1).
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

def fit_grid(columns, width, gutter, unit=1, include_outer=False):
    """Generate a grid to fit conditions given"""
    gutter = fit_gutter(gutter, unit)
    include_outer = include_outer
    width = (width - (gutter * 2)) if include_outer else width
    column = fit_col(columns, width, gutter, unit)
    steps = [colspan(i + 1, column, gutter) for i in range(0, columns)]
    fit_width = colspan(columns, column, gutter)
    total_width = fit_width + (gutter * 2) if include_outer else fit_width
    return {
        "width": fit_width,
        "total_width": total_width,
        "gutter": gutter,
        "columns": steps
    }

def swiss_calc():
    """Calc command"""
    args = calc_parser.parse_args()
    grid = fit_grid(args.columns, args.width, args.gutter,
        unit=args.unit, include_outer=args.include_outer)
    print("Width: {}".format(grid["width"]))
    print("Total: {}".format(grid["total_width"]))
    print("Gutter: {}".format(grid["gutter"]))
    col_display = ", ".join(str(col) for col in grid["columns"])
    print("Columns: {}".format(col_display))
    # for n, column in grid["columns"]:
    #     print("{}x: {}".format(n, column))

if __name__ == '__main__':
    swiss_calc()