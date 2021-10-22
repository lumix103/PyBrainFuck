from brainfuck import BrainFuck
from lexer import Lexer
from bf_parser import Parser
from tokens import TokenType
def main():
    #Lexer is load with Hello World code from https://en.wikipedia.org/wiki/Brainfuck
    lexer = Lexer("++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.")
    parser = Parser(lexer)
    program = parser.parse_program()
    bf = BrainFuck(program)
    bf.run()

if __name__ == "__main__":
    main()