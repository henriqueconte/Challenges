class Solution:
    def isValid(self, s):
        stack = []

        for char in s:
            if char == "(" or char == "[" or char == "{":
                stack.append(char)
            else:
                if stack: 
                    if stack[-1] == "(" and char == ")":
                        stack.pop()
                    elif stack[-1] == "[" and char == "]":
                        stack.pop()
                    elif stack[-1] == "{" and char == "}":
                        stack.pop()
                    else:
                        return False
                else:
                    return False
                
        if stack:
            return False
        else:
            return True

solution = Solution()

print(solution.isValid("()"))
print(solution.isValid("()[]{}"))
print(solution.isValid("(]"))
print(solution.isValid("(([[{}]]))"))
print(solution.isValid("([)]"))