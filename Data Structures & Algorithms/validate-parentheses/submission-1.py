class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '[' or i == '(' or i == '{':
                stack.append(i)
                print(stack)
            else:
                if len(stack) == 0:
                    return False
                if i == ')':
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                elif i == '}':
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
                else:
                    if stack[-1] == '[':
                        stack.pop()

                    else:
                        return False
        if len(stack) == 0:
            return True
        else:
            return False          
