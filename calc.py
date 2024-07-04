class Calculator:
    def __init__(self):
        self.operators = {'+': (1, lambda x, y: x + y), 
                          '-': (1, lambda x, y: x - y), 
                          '*': (2, lambda x, y: x * y), 
                          '/': (2, lambda x, y: x / y)}
    
    def parse_expression(self, expression):
        tokens = []
        value = ''
        for char in expression:
            if char in '0123456789.':
                value += char
            else:
                if value:
                    tokens.append(float(value))
                    value = ''
                if char in self.operators or char in "()":
                    tokens.append(char)
        if value:
            tokens.append(float(value))
        return tokens

    def infix_to_postfix(self, tokens):
        """
        “Shunting-yard”算法是由计算机科学家Edsger Dijkstra设计的一种用于解析数学表达式的算法。
        它可以将中缀表达式转换为后缀表达式（逆波兰表示法，RPN），然后可以轻松地对后缀表达式进行计算。
        以下是算法的主要步骤和规则：

        初始化：

        使用一个栈来保存操作符和括号。
        使用一个输出列表来保存转换后的后缀表达式。
        处理输入中的每个标记（token）：

        操作数   ：直接添加到输出列表。

        左括号 ( ：压入栈。

        右括号 ) ：弹出栈顶元素并添加到输出列表，直到遇到左括号。左括号随后被丢弃。

        操作符   ：根据操作符的优先级和栈顶操作符的优先级进行处理：
                如果当前操作符的优先级低于或等于栈顶操作符的优先级，则弹出栈顶操作符并添加到输出列表，直到找到优先级更低的操作符或左括号。
                最后，将当前操作符压入栈。

        处理完所有标记后：
        将栈中剩余的所有操作符弹出并添加到输出列表。
        """
        out = []
        stack = []
        for token in tokens:
            if isinstance(token, float):
                out.append(token)
            elif token in self.operators:
                while (stack and stack[-1] != '(' and
                       self.operators[token][0] <= self.operators[stack[-1]][0]):
                    out.append(stack.pop())
                stack.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    out.append(stack.pop())
                stack.pop()
        while stack:
            out.append(stack.pop())
        return out

    def evaluate_postfix(self, tokens):
        stack = []
        for token in tokens:
            if isinstance(token, float):
                stack.append(token)
            elif token in self.operators:
                y, x = stack.pop(), stack.pop()
                stack.append(self.operators[token][1](x, y))
        return stack[0]

    def calculate(self, expression):
        tokens = self.parse_expression(expression)
        postfix_tokens = self.infix_to_postfix(tokens)
        return self.evaluate_postfix(postfix_tokens)

# 使用示例
calc = Calculator()
expression = "3 + 5 * (2 - 8)"  
#  RPN 3 5 2 8 - * +
result = calc.calculate(expression)
print(f"Result of '{expression}' is {result}")
