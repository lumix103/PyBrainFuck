from abc import abstractmethod
from tokens import Token

class AST:
    @abstractmethod
    def token_literal():
        pass
    @abstractmethod
    def __str__(self) -> str:
        pass

class Program:
    def __init__(self, commands) -> None:
        self.commands = commands

class Command(AST):
    def __init__(self, token, command= None) -> None:
        super().__init__()
        self.token = token
        self.command = command
    def token_literal(self):
        return self.token.ttype
    def __str__(self) -> str:
        if self.command is None:
            return "<Empty Command>"
        return str(self.command)

class BasicCommand(AST):
    def __init__(self, token, mult = 1) -> None:
        super().__init__()
        self.token = token
        self.mult = mult
    def token_literal(self):
        return self.token.ttype
    def __str__(self) -> str:
        return f'<{self.token.ttype}*{self.mult}>'

class While(AST):
    def __init__(self, token, expressions) -> None:
        super().__init__()
        self.token = token
        self.expressions = expressions
    def token_literal(self):
        return self.token.ttype
    def __str__(self) -> str:
        return f'<while: {str(self.expressions)}>'