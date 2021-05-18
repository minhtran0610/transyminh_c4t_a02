class PolishNotation:
    def __init__(self):
        self.stack = []
    
    def calculate(self, equation):
        self.stack = []
        for v in equation:
            if v in "0123456789":
                self.stack.append(int(v))
            elif v in "+-*/":
                second_operand = self.stack.pop()
                first_operand = self.stack.pop()
                if v == "+":
                    result = first_operand + second_operand
                elif v == "-":
                    result = first_operand - second_operand
                elif v == "*":
                    result = first_operand * second_operand
                else:
                    result = first_operand / second_operand
                self.stack.append(result)
        final_result = self.stack.pop()
        return final_result

            