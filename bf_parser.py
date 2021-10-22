from bf_ast import BasicCommand, Command, Program, While
from tokens import Token, TokenType
class Parser:
    def __init__(self, lexer) -> None:
        self.lexer = lexer
        self.peek = Token(TokenType._end, "")
        self.current = Token(TokenType._end, "")
        self.next_token()
        self.next_token()
    def next_token(self):
        self.current = self.peek
        self.peek = self.lexer.next_token()
    def current_is(self, ttype):
        return self.current.ttype == ttype
    def peek_is(self, ttype):
        return self.peek.ttype == ttype
    def parse_program(self):
        program = Program([])
        while not self.current_is(TokenType._end):
            stmt = self.parse()
            if not stmt is None:
                program.commands.append(stmt)
            self.next_token()
        return program
    def parse(self):
        stmt = Command(Token(TokenType._end, ""))
        stmt.command = self.parse_command()
        return stmt
    def parse_command(self):
        if self.current_is(TokenType.LBRACKET):
            while_ = While(self.current, [])
            self.next_token()
            while (not self.current_is(TokenType.RBRACKET)) and (not self.current_is(TokenType._end)):
                stmt = self.parse()
                if not stmt is None:
                    while_.expressions.append(stmt)
                self.next_token()
            return while_
        else:
            mult = 1
            current = self.current
            while self.peek_is(current.ttype):
                self.next_token()
                mult += 1
            return BasicCommand(current, mult)