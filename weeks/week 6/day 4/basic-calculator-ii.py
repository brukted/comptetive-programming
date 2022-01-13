# https://leetcode.com/problems/basic-calculator-ii/

class Solution:
    def calculate(self, s: str) -> int:
        operators = {'+', '-', '*', '/'}
        ps = []
        isOp = s[0] in operators
        ps.append(s[0])
        for i in range(1, len(s)):
            if isOp:
                ps.append(s[i])
                if s[i] not in operators:
                    isOp = False
            else:
                if s[i] in operators:
                    isOp = True
                    ps.append(s[i])
                else:
                    ps.append(ps.pop()+s[i])
        operandStack = []
        operatorStack = []
        for i in ps:
            if i in operators:
                operatorStack.append(i)
            elif i != ' ':
                operandStack.append(int(i))
                if len(operatorStack):
                    while len(operatorStack) and (operatorStack[-1] == '/' or operatorStack[-1] == '*'):
                        a = operandStack.pop()
                        b = operandStack.pop()
                        if operatorStack[-1] == '/':
                            if b < 0:
                                operandStack.append((b//a)-1)
                            else:
                                operandStack.append((b//a))
                        else:
                            operandStack.append(b*a)
                        operatorStack.pop()

        last = operandStack[-1]
        while len(operatorStack):
            op = operatorStack.pop()
            a = operandStack.pop()
            b = operandStack.pop()
            if op == "-":
                a -= 2*last
                operandStack.append(b+a)
            else:
                operandStack.append(a+b)
            last = b
        return operandStack[-1]
