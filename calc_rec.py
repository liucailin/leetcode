class RecursiveCalculator:
    def parse_expression(self, expression):
        self.tokens = list(expression.replace(' ', ''))
        self.current_token = self.tokens.pop(0) if self.tokens else None
        return self.expr()

    def get_next_token(self):
        self.current_token = self.tokens.pop(0) if self.tokens else None

    def expr(self):
        result = self.term()
        while self.current_token in ('+', '-'):
            if self.current_token == '+':
                self.get_next_token()
                result += self.term()
            elif self.current_token == '-':
                self.get_next_token()
                result -= self.term()
        return result

    def term(self):
        result = self.factor()
        while self.current_token in ('*', '/'):
            if self.current_token == '*':
                self.get_next_token()
                result *= self.factor()
            elif self.current_token == '/':
                self.get_next_token()
                result /= self.factor()
        return result

    def factor(self):
        if self.current_token == '(':
            self.get_next_token()
            result = self.expr()
            self.get_next_token()  # Skip ')'
            return result
        elif self.current_token in ('+', '-'):
            sign = 1 if self.current_token == '+' else -1
            self.get_next_token()
            result = sign * self.factor()
            return result
        else:
            start = 0
            while (self.current_token is not None and
                   (self.current_token.isdigit() or self.current_token == '.')):
                start += 1
                if self.tokens:
                    self.get_next_token()
                else:
                    break
            return float(expression[:start])

    def calculate(self, expression):
        return self.parse_expression(expression)

# 使用示例
calc = RecursiveCalculator()
expression = "-3 + 5 * (2 - 8)"
result = calc.calculate(expression)
print(f"Result of '{expression}' is {result}")
