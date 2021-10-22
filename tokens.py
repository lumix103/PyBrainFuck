from enum import Enum

class TokenType(Enum):
    _to_err     = "err"
    _end        = "end"
    GREATER     = ">"
    LESSER      = "<"
    PLUS        = "+"
    MINUS       = "-"
    DOT         = "."
    COMMA       = ","
    LBRACKET    = "["
    RBRACKET    = "]"

class Token:
    def __init__(self, ttype, lexeme) -> None:
        self.ttype = ttype
        self.lexeme = lexeme
    def __str__(self) -> str:
        return f"({self.ttype} : '{self.lexeme}')"