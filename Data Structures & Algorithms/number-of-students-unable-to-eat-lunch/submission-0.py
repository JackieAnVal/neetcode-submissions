class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # circular = 0
        # square = 1
        """ # students = # sandwiches
        students = [1,1,1], sandwiches = [0,1,1]"""

        res = len(students)
        count = Counter(students)
        for sandwich in sandwiches: 
            if count[sandwich] > 0:
                count[sandwich]-=1
                res -=1
            else:
                return res
        return res
