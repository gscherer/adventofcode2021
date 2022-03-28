from . import tokens
from .errors import CorruptedException, InvalidCharacterException 

def parse(line: str) -> list[str]:
    stack = []
    for i, c in enumerate(line):
        if c in tokens.OPENERS:
            stack.append(c)
        elif c in tokens.CLOSERS:
            last = stack.pop()
            expected = tokens.CLOSERS[c]
            if last != expected:
                raise CorruptedException(f'expected {expected}, but found {c} instead', c)
        else:
            raise InvalidCharacterException(f'invalid character {c} at position {i}')
    return stack 

def fill_incomplete_line(line: str) -> str:
    try:
        remaining = parse(line)
    except Exception:
        return ''
    fill_tokens = []
    while remaining:
        c = remaining.pop()
        fill_tokens.append(tokens.OPENERS[c])
    return ''.join(fill_tokens)

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
        score += tokens.COMPLETION_SCORES[c]
    return score