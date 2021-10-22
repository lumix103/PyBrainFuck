from typing import Match
from tokens import TokenType, Token

class Lexer:
    def __init__(self, input) -> None:
        self.input = input
        self.start = 0
        self.forward = 0
        self.ch = ' '
        self.read_char()
    def read_char(self):
        if self.forward >= len(self.input):
            self.ch = '\0'
        else:
            self.ch = self.input[self.forward]
        self.start = self.forward
        self.forward += 1
    def skip_whitespace(self):
        while self.ch == ' ' or self.ch == '\t' or self.ch == '\n' or self.ch == '\r':
            self.read_char()
    def make_simple_token(self,ttype, lexeme):
        return Token(ttype, lexeme)
    def peek_char(self):
        if self.forward >= len(self.input):
            return '\0'
        return self.input[self.forward]
    def read_identifier(self):
        start = self.start
        while self.ch.isalpha():
            self.read_char()
        return self.input[start:self.start]
    def match(self, ch):
        if ch == self.peek_char():
            self.read_char()
            return True
        return False
    def next_token(self):
        token = Token(TokenType._to_err, "err")
        self.skip_whitespace()
        if self.ch == '>':
            token = self.make_simple_token(TokenType.GREATER, '>')
        elif self.ch == '<':
            token = self.make_simple_token(TokenType.LESSER, '<')
        elif self.ch == '+':
            token = self.make_simple_token(TokenType.PLUS, '+')
        elif self.ch == '-':
            token = self.make_simple_token(TokenType.MINUS, '-')
        elif self.ch == '.':
            token = self.make_simple_token(TokenType.DOT, '.')
        elif self.ch == ',':
            token = self.make_simple_token(TokenType.COMMA, ',')
        elif self.ch == '[':
            token = self.make_simple_token(TokenType.LBRACKET, '[')
        elif self.ch == ']':
            token = self.make_simple_token(TokenType.RBRACKET, ']')
        elif self.ch == '\0':
            token = self.make_simple_token(TokenType._end, "end")    
        else:
            token = self.make_simple_token(TokenType._to_err, self.ch)
        self.read_char()
        return token