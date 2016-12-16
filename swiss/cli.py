#!/usr/bin/env python
from __future__ import print_function
from sys import stdout
import argparse
from swiss import fit_grid

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
    nargs="?",
    const=True,
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

def main():
    """Calc command"""
    args = calc_parser.parse_args()
    grid = fit_grid(args.columns, args.width, args.gutter,
        unit=args.unit, include_outer=args.include_outer)
    print("Width: {}".format(grid["width"]))
    print("Total: {}".format(grid["total_width"]))
    print("Gutter: {}".format(grid["gutter"]))
    col_display = ", ".join(str(col) for col in grid["columns"])
    print("Columns: {}".format(col_display))

if __name__ == '__main__':
    main()