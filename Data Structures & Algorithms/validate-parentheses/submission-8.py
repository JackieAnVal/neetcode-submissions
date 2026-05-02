class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closedBrackets = {
            ']':'[',
            ')':'(',
            '}':'{'
        }

        for c in s:
            if c not in closedBrackets:
                stack.append(c)
            else: #if it is a closed bracket
                if stack and closedBrackets[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return stack == []
        