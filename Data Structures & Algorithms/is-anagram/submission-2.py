class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = Counter(s)
        b = Counter(t)
        return a == b

"""     #OJITO, distintas soluciones, puedes crear los maps y compararlos, usar Counter o sin.
        #También puedes convertir uno en mapa e ir decrementando valores con la segunda palabra, si llegas a 0 ese char ya estuvo demás, no es anagram
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1
        return countS == countT
"""