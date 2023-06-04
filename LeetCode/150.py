import math 

class Solution:
    def evalRPN(self, tokens):
        OPERATORS = {"+", "-", "*", "/"}
        result = int(tokens[0])
        operandsStack = []
        if len(tokens) == 1:
            return result
        
        for token in tokens:
            if token in OPERATORS:
                rightOperand = operandsStack.pop()
                leftOperand = operandsStack.pop()
                result = self.singleOperation(leftOperand, rightOperand, token)
                operandsStack.append(result)
            else:
                operandsStack.append(token)

        return result

    
    def singleOperation(self, leftOperand, rightOperand, operation):
        leftOperand = int(leftOperand)
        rightOperand = int(rightOperand)
        if operation == "+":
            return leftOperand + rightOperand
        elif operation == "-":
            return leftOperand - rightOperand
        elif operation == "*":
            return leftOperand * rightOperand
        else:
            division = leftOperand / rightOperand
            if division > 0:
                return math.floor(division)
            else:
                return math.ceil(division)

solution = Solution()
print(solution.evalRPN(["2","1","+","3","*"]))
print("------\n")
print(solution.evalRPN(["4","13","5","/","+"]))
print("------\n")
print(solution.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
print("------\n")
print(solution.evalRPN(["4","-2","/","2","-3","-","-"]))



# Keep result in a variable
# Iterate over list, find arithimetic operator
# Operate with previous two integer tokens (maybe save two previous tokens and their indexes)
# Pop both tokens, insert new token at the position of the first one
# Iterate again


# ["4","-2","/","2","-3","-","-"]
# 4 / -2 = -2 (left = 2, right = 3)
# 


    