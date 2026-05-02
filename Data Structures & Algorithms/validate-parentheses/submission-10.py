class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closedBrackets = {
            ']':'[',
            ')':'(',
            '}':'{'
        }

        for c in s:
            if c not in closedBrackets: #if it is an open bracket just add to stack
                stack.append(c)
            else: #if it is a closed bracket
                #check the stack, and if it contains the corresponding open value
                if stack and closedBrackets[c] == stack[-1]:
                    stack.pop() #delete from stack
                else: #if open bracket is not the corresponding
                    return False
        return stack == []

        """
        for c in s:
            if c in closedBrackets:
                if stack and stack[-1] == closedBrackets[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack 
        """
        