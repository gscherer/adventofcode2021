from .errors import CorruptedException
from .parse import fill_incomplete_line, parse
from . import tokens

COMPLETION_SCORES = {
    tokens.R_PAREN: 1,
    tokens.R_BRACKET: 2,
    tokens.R_CURLY_BRACKET: 3,
    tokens.R_ANGLE_BRACKET: 4
}

def score_corrupted_lines(lines: list[str]) -> int:
    score = 0
    for line in lines:
        try:
            parse(line)
        except CorruptedException as err:
            score += err.points
    return score

def score_completed_line(completed: str) -> int:
    score = 0
    multiplier = 5
    for c in completed:
        score *= multiplier
        score += COMPLETION_SCORES[c]
    return score

def find_middle_score_of_incomplete_lines(lines: list[str]):
    fills = [fill_incomplete_line(line) for line in lines]
    sorted_scores = sorted([score_completed_line(fill) for fill in fills if len(fill) > 0])
    middle = len(sorted_scores) // 2
    return sorted_scores[middle]