class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        circle = 0
        square = 0

        for i in range(len(students)):
            if students[i] == 0:
                circle += 1
            else:
                square += 1
        
        # At this stage, circle and square var contains sum num of each sandwich
        for sandwich in sandwiches:                
            if sandwich == 0 and circle >= 1:
                circle -= 1
            elif sandwich == 1 and square >= 1:
                square -= 1
            else:     # will never drop below 0
                return (circle + square)
        
        return 0
            