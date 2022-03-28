from . import tokens
from .errors import CorruptedException, InvalidCharacterException 

def parse(line: str):
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

def score_lines(lines: list[str]) -> int:
    score = 0
    for line in lines:
        try:
            parse(line)
        except CorruptedException as err:
            score += err.points
    return score