"""Script for doing data visualization on data piped to standard in

Parameters
----------
--output_file_name : name of the output file generated from data visualization
--plot_type : specifies the type of plot to be created
    options:
        boxplot: returns boxplot representation
        histogram: returns histogram representation
        combo: returns both boxplot and histogram

Returns
-------
file : returns a file with the specified
    output file name containing the desired plot type
"""

import get_data
import data_viz
import argparse
import sys


def main():

    parser = argparse.ArgumentParser(description='Create plots'
                                                 ' with data from stdin.')

    parser.add_argument('--output_file_name', type=str,
                        help='Name of the output file', required=True)

    parser.add_argument(
        '--plot_type', type=str,
        help='The type of plot you wish to produce', required=True)

    args = parser.parse_args()

# Read data from standard in
    try:
        V = get_data.read_stdin_col(0)
    except TypeError:
        print('Data could not be read from stdin')
        sys.exit(1)

# plot generation
    if args.plot_type == str('boxplot'):
        data_viz.boxplot(V, args.output_file_name)
    if args.plot_type == str('histogram'):
        data_viz.histogram(V, args.output_file_name)
    if args.plot_type == str('combo'):
        data_viz.combo(V, args.output_file_name)


if __name__ == '__main__':
    main()
