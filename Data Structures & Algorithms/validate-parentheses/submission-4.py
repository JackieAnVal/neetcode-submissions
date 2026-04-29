class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closedBrackets = {
            ']':'[',
            ')':'(',
            '}':'{'
        }

        for c in s:
            if not stack and c in closedBrackets: 
                return False
            elif c not in closedBrackets:
                stack.append(c)
            elif stack[-1] == closedBrackets[c]: 
                stack.pop()
            else:
                return False
        
        return stack == []