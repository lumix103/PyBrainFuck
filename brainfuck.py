from array import array

from bf_ast import BasicCommand, Command, While
from tokens import TokenType

LIMIT = 30000

class BrainFuck:
    def __init__(self, program) -> None:
        self.program = program
        self.array = array('i',(0 for i in range(0,30000)))
        self.ptr = 0
    def run(self):
        for cmd in self.program.commands:
            self.execute(cmd)
    def execute(self, cmd):
        if type(cmd) is Command:
            self.execute(cmd.command)
        if type(cmd) is BasicCommand:
            self.execute_basic(cmd)
        if type(cmd) is While:
            self.execute_while(cmd)
    def execute_basic(self, cmd):
        if cmd.token_literal() == TokenType.GREATER:
            self.ptr+= cmd.mult
        elif cmd.token_literal() == TokenType.LESSER:
            self.ptr -= cmd.mult
        elif cmd.token_literal() == TokenType.PLUS:
            self.array[self.ptr] += cmd.mult;
        elif cmd.token_literal() == TokenType.MINUS:
            self.array[self.ptr] -= cmd.mult;
        elif cmd.token_literal() == TokenType.DOT:
            for i in range(0, cmd.mult):
                print(chr(self.array[self.ptr]), end='')
        elif cmd.token_literal() == TokenType.COMMA:
            for i in range(0, cmd.mult):
                a = input('').split(" ")[0]
                self.array[self.ptr] = int(chr(a))
    def execute_while(self, while_):
        while(self.array[self.ptr]):
            for cmd in while_.expressions:
                self.execute(cmd)
        