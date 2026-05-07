class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # defaultdict(list) crea automáticamente una lista vacía si la llave no existe, evitando KeyErrors
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())

        """
        Summary of Tools
        sorted() function: Takes any iterable (like a string) and returns a new sorted list of its elements.
        .join() method: Combines the list of sorted characters back into a string format.
        .sort() method: Modifies a list in-place. 
        You cannot use this directly on a string because strings are immutable; you must convert the string to a list first.
        """