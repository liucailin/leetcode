# https://www.imcao.cn/2022/02/24/calculate/


class StackCalculator:
    def precedence(self, op):
        if op in ('+', '-'):
            return 1
        if op in ('*', '/'):
            return 2
        return 0

    def apply_op(self, a, b, op):
        if op == '+':
            return a + b
        if op == '-':
            return a - b
        if op == '*':
            return a * b
        if op == '/':
            return a / b

    def calculate(self, expression):
        values = []
        ops = []
        i = 0
        while i < len(expression):
            if expression[i] == ' ':
                i += 1
                continue
            if expression[i] == '(':
                ops.append(expression[i])
            elif expression[i].isdigit() or expression[i] == '.':
                val = 0
                decimal_place = -1
                while (i < len(expression) and 
                       (expression[i].isdigit() or expression[i] == '.')):
                    if expression[i] == '.':
                        decimal_place = 0
                    else:
                        if decimal_place >= 0:
                            decimal_place += 1
                            val += int(expression[i]) * (10 ** -decimal_place)
                        else:
                            val = (val * 10) + int(expression[i])
                    i += 1
                values.append(val)
                i -= 1
            elif expression[i] == ')':
                while ops and ops[-1] != '(':
                    val2 = values.pop()
                    val1 = values.pop()
                    op = ops.pop()
                    values.append(self.apply_op(val1, val2, op))
                ops.pop()
            else:
                if expression[i] in ('+', '-') and (i == 0 or expression[i - 1] in '()+-*/'):
                    values.append(0)
                while (ops and self.precedence(ops[-1]) >= self.precedence(expression[i])):
                    val2 = values.pop()
                    val1 = values.pop()
                    op = ops.pop()
                    values.append(self.apply_op(val1, val2, op))
                ops.append(expression[i])
            i += 1

        while ops:
            val2 = values.pop()
            val1 = values.pop()
            op = ops.pop()
            values.append(self.apply_op(val1, val2, op))

        return values[0]

# 使用示例
calc = StackCalculator()
expression = "-3 + 5 * (-2 - 8)"
result = calc.calculate(expression)
print(f"Result of '{expression}' is {result}")
