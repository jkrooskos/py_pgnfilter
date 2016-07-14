"""Tool to create a new pgn filtered by games where white or black moves first.

Sample usage:

python pgn_filter.py --color=b --input-pgn=games.pgn --output-pgn=output.pgn
"""

import sys
import click


def color_match(variation, filter_by_color):
    """Filter variation by white or black.

    If the variation does not include a FEN string in the tag pair section
    the variation will not be included in the output file.

    :variation: variation to analyze
    :filter_by_color: w to denote white, b to denote black
    :rtype: variation if color filter is a match

    """
    match = False
    for item in variation:
        if item[0:4] == '[FEN':
            starting_color = item.split()[2]
            match = starting_color == filter_by_color

    return match


@click.command()
@click.option('-c', '--color', help='Color to filter by...w for white, b for black')
@click.option('--input-pgn',
              type=click.Path(exists=True),
              help='Path to PGN file to filter')
@click.option('--output-pgn',
              help='Path of new PGN file with filter applied')
def filter_pgn(color, input_pgn, output_pgn):
    """Tag pair and movetext.

    * is a tag meaning incomplete dame or result unknown
    """
    game_end_tags = ['*', '1-0', '0-1', '1/2-1/2']
    variation = []
    with open(output_pgn, 'w') as output, open(input_pgn, 'r') as pgn:
        for line in pgn:
            variation.append(line.strip())
            if line.strip() != '' and line.split()[-1] in game_end_tags:
                if color_match(variation, color):
                    output.writelines(line + '\n' for line in variation)
                variation = []

if __name__ == '__main__':
    sys.exit(filter_pgn())
