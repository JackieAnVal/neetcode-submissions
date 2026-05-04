class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # circular = 0
        # square = 1
        """Counter() maps the items of the list
        is like doing
        
        """
        res = len(students)
        count = Counter(students)
        for sandwich in sandwiches: 
            if count[sandwich] > 0:
                count[sandwich]-=1
                res -=1
            else:
                return res
        return res
