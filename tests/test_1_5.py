import os
import sys

DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))

if DIR not in sys.path:
    sys.path.append(DIR)

import day_01  # noqa: E402
import day_02  # noqa: E402
import day_03  # noqa: E402
import day_04  # noqa: E402
import day_05  # noqa: E402
import helpers as h  # noqa: E402


def test_01():
    data = h.load_day_data('01', sample=True)
    one, two = day_01.solution(data)

    assert one == 24000
    assert two == 45000


def test_02():
    data = h.load_day_data('02', sample=True)
    one, two = day_02.solution(data)

    assert one == 15
    assert two == 12


def test_03():
    data = h.load_day_data('03', sample=True)
    one, two = day_03.solution(data)

    assert one == 157
    assert two == 70


def test_04():
    data = h.load_day_data('04', sample=True)
    one, two = day_04.solution(data)

    assert one == 2
    assert two == 4


def test_05():
    data = h.load_day_data('05', sample=True)
    one, two = day_05.solution(data)

    assert one == 'CMZ'
    assert two == 'MCD'
