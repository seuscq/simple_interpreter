#!/usr/bin/python3
''' first phase of this compiler is to evaluate '1+2' '''
# grammar for this language:
# 
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

    def advance():
        self.pos++

    def get_next_token(self):
        if self.pos > len(self.text) - 1:
            return Token(EOF, None)

        if self.text[self.pos].isdigit():
            d = self.text[self.pos]
            self.advance()
            return Token(INTEGER, d)
        if self.text[self.pos].

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise Exception('syntax error')

    def eat(self, type):
        if self.current_token.type == type:
            self.current_token = self.lexer.get_next_token()
        else
            self.error()

    def expr(self):
        token = self.current_token
        if token.type == INTEGER:
            self.eat(INTEGER)
            self.op()
            self.eat(INTEGER)
        else
            self.error()
            
    def op(self):
        token = self.current_token
        if token.type == PLUS:
            self.eat(PLUS)
        elif token.type == MINUS:
            self.eat(MINUS)
        else:
            self.error()

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
