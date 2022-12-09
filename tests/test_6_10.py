import os
import sys

DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))

if DIR not in sys.path:
    sys.path.append(DIR)

import day_06  # noqa: E402
import day_07  # noqa:E402
import day_08  # noqa:E402
import day_09  # noqa:E402
import helpers as h  # noqa: E402


def test_06():
    data = h.load_day_data('06', sample=True)
    one, two = day_06.solution(data)

    assert one == 7
    assert two == 19


def test_07():
    data = h.load_day_data('07', sample=True)
    one, two = day_07.solution(data)

    assert one == 95437
    assert two == 24933642


def test_08():
    data = h.load_day_data('08', sample=True)
    one, two = day_08.solution(data)

    assert one == 21
    assert two == 8


def test_09():
    data = h.load_day_data('09', sample=True)
    one, two = day_09.solution(data)

    assert one == 13
    assert two == 1
