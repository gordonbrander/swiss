from math import floor

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