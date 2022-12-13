import os
import sys

DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))

if DIR not in sys.path:
    sys.path.append(DIR)

import day_11  # noqa: E402
import day_12  # noqa:E402
import day_13  # noqa:E402
import helpers as h  # noqa: E402


def test_11():
    data = h.load_day_data('11', sample=True)
    one, two = day_11.solution(data)

    assert one == 10605
    assert two == 2713310158


def test_12():
    data = h.load_day_data('12', sample=True)
    one, two = day_12.solution(data)

    assert one == 31
    assert two == 29


def test_13():
    data = h.load_day_data('13', sample=True)
    one, two = day_13.solution(data)

    assert one == 13
    assert two == 140
