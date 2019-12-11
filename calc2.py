#!/usr/bin/python3
''' first phase of this compiler is to evaluate '1+2' '''
# grammar for this language:
# expr => INTEGER op INTEGER
# op => PLUS | MINUS

PLUS, MINUS, INTEGER, EOF = ('PLUS', 'MINUS', 'INTEGER', 'EOF')

class Token:
    def __self__(self, type, value):
        self.type = type
        self.value = value

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = self.text[0]

    def get_next_token(self):
        if 
        return Token()

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def expr(self):
        token = self.lexer
        


class Interpreter:
    def __init__(self, parser):
        self.parser = parser

    def eval(self):
        return 1

def main():
    while True:
        try:
            text = input('calc> ')
            if not text:
                continue
            lexer = Lexer(text)
            parser = Parser(lexer)
            interpreter = Interpreter(parser)
            result = interpreter.eval()
            print(result)
        except EOFError:
            break
        
if __name__ == '__main__':
    main()
