from . import tokens

class CorruptedException(Exception):
    SCORES = {
        tokens.R_PAREN: 3,
        tokens.R_BRACKET: 57,
        tokens.R_CURLY_BRACKET: 1197,
        tokens.R_ANGLE_BRACKET: 25137
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