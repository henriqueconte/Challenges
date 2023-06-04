import math 

class Solution:
    def evalRPN(self, tokens):
        OPERATORS = {"+", "-", "*", "/"}
        if len(tokens) == 1:
            return int(tokens[0])
        
        leftOp = 0
        rightOp = 1
        visited = [0 for i in range(len(tokens))]

        for i in range(0, len(tokens)):
            if visited[i]:
                continue
            if tokens[i] in OPERATORS:
                while visited[rightOp] and rightOp >= 0:
                    rightOp -= 1
                
                leftOp = rightOp - 1
                while visited[leftOp] and leftOp >= 0:
                    leftOp -= 1

                result = self.singleOperation(tokens[leftOp], tokens[rightOp], tokens[i])
                visited[rightOp] = 1
                visited[i] = 1
                tokens[leftOp] = str(result)

            else:
                rightOp = i
                leftOp = i - 1

        return tokens[leftOp]

    
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


    