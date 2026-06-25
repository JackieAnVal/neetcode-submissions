class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for col in range(len(strs[0])):
            for word in strs:
                if col == len(word) or word[col] != strs[0][col]:
                    return prefix
            prefix += word[col]
        return prefix