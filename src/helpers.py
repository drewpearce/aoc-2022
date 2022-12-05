import os


DATA_DIR = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', 'data'))


def load_day_data(day, sample=False):
    if sample is True:
        path = os.path.join(DATA_DIR, day, 'sample.txt')
    else:
        path = os.path.join(DATA_DIR, day, 'data.txt')

    with open(path) as f:
        data = f.read()

    return data
