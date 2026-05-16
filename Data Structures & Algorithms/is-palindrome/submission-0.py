class Solution:
    def isPalindrome(self, s: str) -> bool:
        phrase = "".join([char.lower() for char in s if char.isalnum()])
        left, right = 0, len(phrase) - 1
        while left <= right:
            if phrase[left] != phrase[right]:
                return False
            left += 1
            right -= 1
        return True