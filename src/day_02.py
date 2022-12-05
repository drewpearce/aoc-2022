import re

from helpers import load_day_data


def solution(data):
    score_map_1 = {
        'A X': 4,  # RR (3+1)
        'A Y': 8,  # RP (6+2)
        'A Z': 3,  # RS (0+3)
        'B X': 1,  # PR (0+1)
        'B Y': 5,  # PP (3+2)
        'B Z': 9,  # PS (6+3)
        'C X': 7,  # SR (6+1)
        'C Y': 2,  # SP (0+2)
        'C Z': 6  # SS (3+3)
    }
    score_map_2 = {
        'A X': 3,  # Lose = RS (0+3)
        'A Y': 4,  # Draw = RR (3+1)
        'A Z': 8,  # Win = RP (6+2)
        'B X': 1,  # Lose = PR (0+1)
        'B Y': 5,  # Draw = PP (3+2)
        'B Z': 9,  # Win = PS (6+3)
        'C X': 2,  # Lose = SP (0+2)
        'C Y': 6,  # Draw = SS (3+3)
        'C Z': 7  # Win = SR (6+1)
    }
    score_1 = 0

    for k, v in score_map_1.items():
        _score = v * len(re.findall(k, data))
        score_1 += _score

    print(score_1)
    score_2 = 0

    for k, v in score_map_2.items():
        _score = v * len(re.findall(k, data))
        score_2 += _score

    print(score_2)

    return score_1, score_2


if __name__ == '__main__':
    data = load_day_data('02')
    solution(data)
