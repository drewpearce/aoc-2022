#!/Users/andrew.f.pearce/.pyenv/versions/aoc/bin/python

import os
from pathlib import Path
import sys

from argparse import ArgumentParser


DIR = os.path.abspath(os.path.dirname(__file__))
SRC = os.path.abspath(os.path.join(DIR, '..', 'src'))
DATA = os.path.abspath(os.path.join(DIR, '..', 'data'))

if SRC not in sys.path:
    sys.path.append(SRC)

import helpers as h  # noqa: E402


def get_args():
    parser = ArgumentParser(
        prog='get-input',
        description='get challenge input'
    )
    parser.add_argument(
        '-d',
        '--day',
        type=int,
        help='The day to pull data for',
        required=True
    )

    return parser.parse_args()


def write_data(day, data):
    _dir = os.path.join(DATA, day)
    Path(_dir).mkdir(parents=True, exist_ok=True)

    with open(os.path.join(_dir, 'data.txt'), 'w') as f:
        f.write(data.decode('utf-8'))


def main():
    args = get_args()
    day = str(args.day) if args.day >= 10 else f'0{args.day}'
    data = h.call_aoc_api(f'/day/{args.day}/input')
    write_data(day, data)


if __name__ == '__main__':
    main()
