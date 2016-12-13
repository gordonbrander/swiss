# Swiss

A simple tool for calculating layout grid dimensions.

## `swiss_calc`

Calculates a grid that will fit within a given space. Give swiss the number of columns, the space the layout grid must fit within, and a ballpark gutter. Swiss will find you a grid to fit these constraints.

Example:

```bash
$ swiss_calc 12 1024 34 --include_outer
Width: 950.0
Total: 1018.0
Gutter: 34.0
Columns: 48.0, 130.0, 212.0, 294.0, 376.0, 458.0, 540.0, 622.0, 704.0, 786.0, 868.0, 950.0
```

You can use the `--unit` flag to specify an underlying grid unit. For example, if you specify 8, the grid generated will cleanly fit on top of an 8px grid.

```bash
Width: 928.0
Total: 992.0
Gutter: 32.0
Columns: 48.0, 128.0, 208.0, 288.0, 368.0, 448.0, 528.0, 608.0, 688.0, 768.0, 848.0, 928.0
```

Note that when unit is specified, gutter may be adjusted to conform to unit.

## Install

Requirements:

- Python 2.x+

Install using pip:

    git clone https://github.com/gordonbrander/swiss.git
    cd swiss
    pip install -e .

Or just use directly:

    ./swiss.py 12 1024 32