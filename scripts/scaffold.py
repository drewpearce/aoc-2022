#!/Users/andrew.f.pearce/.pyenv/versions/aoc/bin/python

import os
from pathlib import Path

from argparse import ArgumentParser


DIR = os.path.abspath(os.path.dirname(__file__))
SRC = os.path.abspath(os.path.join(DIR, '..', 'src'))


def get_args():
    parser = ArgumentParser(
        prog='scaffold',
        description='generate code scaffold for the day'
    )
    parser.add_argument(
        '-d',
        '--day',
        type=int,
        help='The day to generate',
        required=True
    )

    return parser.parse_args()


def write_template(day):
    t_path = os.path.join(DIR, 'template.txt')
    with open(t_path) as f:
        template = f.read()

    template = template.replace('%%DAY%%', day)
    f_path = os.path.join(SRC, f'day_{day}.py')

    if os.path.isfile(f_path):
        raise Exception(f'Cannot scaffold day {day}. File already exists.')

    with open(f_path, 'w') as f:
        f.write(template)


def write_test_template(day):
    _day = int(day)

    if _day < 6:
        f_name = 'test_1_5.py'
    elif _day < 11:
        f_name = 'test_6_10.py'
    elif _day < 16:
        f_name = 'test_11_15.py'
    elif _day < 21:
        f_name = 'test_16_20.py'
    else:
        f_name = 'test_21_25.py'

    f_path = os.path.abspath(os.path.join(DIR, '..', 'tests', f_name))

    if os.path.exists(f_path):
        with open(f_path) as f:
            tests = f.read()

        tests = tests.replace(
            'import helpers',
            f'import day_{day}  # noqa:E402\nimport helpers'
        )

        with open(os.path.join(DIR, 'test_func_template.txt')) as f:
            func = f.read()

        func = func.replace('%%DAY%%', day)
        tests += func
    else:
        with open(os.path.join(DIR, 'test_template.txt')) as f:
            tests = f.read()

        tests = tests.replace('%%DAY%%', day)

    with open(f_path, 'w') as f:
        f.write(tests)


def touch_data(day):
    data_dir = os.path.abspath(os.path.join(DIR, '..', 'data', day))
    Path(data_dir).mkdir(parents=True, exist_ok=True)
    Path(os.path.join(data_dir, 'data.txt')).touch()
    Path(os.path.join(data_dir, 'sample.txt')).touch()


def main():
    args = get_args()
    day = str(args.day) if args.day >= 10 else f'0{args.day}'
    write_template(day)
    write_test_template(day)
    touch_data(day)


if __name__ == '__main__':
    main()
