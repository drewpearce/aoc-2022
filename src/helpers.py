import os

import requests


REPO_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DATA_DIR = os.path.join(REPO_DIR, 'data')


def load_day_data(day, sample=False):
    if sample is True:
        path = os.path.join(DATA_DIR, day, 'sample.txt')
    else:
        path = os.path.join(DATA_DIR, day, 'data.txt')

    with open(path) as f:
        data = f.read()

    return data


def load_env():
    with open(os.path.join(REPO_DIR, '.env')) as f:
        items = f.read().splitlines()

    for item in items:
        item = item.split('=')
        var = item[0]
        val = item[1] if len(item) == 2 else '='.join(item[1:])
        os.environ[var] = val


def call_aoc_api(path, method=None, headers=None, data=None, year=None):
    load_env()
    method = method if method else 'get'

    if not year:
        year = os.environ.get('year', '2022')

    base = f'https://adventofcode.com/{year}'
    call = getattr(requests, method, requests.get)
    kwargs = {}
    _headers = {'Cookie': f"session={os.environ.get('AOC_COOKIE', '')}"}

    if headers and isinstance(headers, dict):
        _headers.update(headers)

    kwargs['headers'] = _headers

    if data:
        kwargs['data'] = data

    response = call(f'{base}{path}', **kwargs)

    if response.status_code >= 200 and response.status_code < 300:
        return response.content
