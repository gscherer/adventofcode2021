import click

L_PAREN = '('
R_PAREN = ')'

L_CURLY_BRACKET = '{'
R_CURLY_BRACKET = '}'

L_BRACKET = '['
R_BRACKET = ']'

L_ANGLE_BRACKET = '<'
R_ANGLE_BRACKET = '>'

OPENERS = [ L_PAREN, L_CURLY_BRACKET, L_BRACKET, L_ANGLE_BRACKET ]

CLOSERS = {
    R_PAREN: L_PAREN,
    R_CURLY_BRACKET: L_CURLY_BRACKET,
    R_BRACKET: L_BRACKET,
    R_ANGLE_BRACKET: L_ANGLE_BRACKET
}

class CorruptedException(Exception):

    SCORES = {
        R_PAREN: 3,
        R_BRACKET: 57,
        R_CURLY_BRACKET: 1197,
        R_ANGLE_BRACKET: 25137
    }

    def __init__(self, message: str, token: str):
        super().__init__(message)
        self.token = token

    @property 
    def points(self):
        if self.token in self.SCORES:
            return self.SCORES[self.token]
        return 0

class InvalidCharacterException(Exception):
    pass

def parse(line: str):
    stack = []
    for i, c in enumerate(line):
        if c in OPENERS:
            stack.append(c)
        elif c in CLOSERS:
            last = stack.pop()
            expected = CLOSERS[c]
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

@click.command()
@click.argument('file_path', type=click.Path(exists=True))
def main(file_path):
    with open(file_path, 'r') as input:
        lines = [line.strip() for line in input.readlines()]
        print(score_lines(lines))

if __name__ == '__main__':
    main()