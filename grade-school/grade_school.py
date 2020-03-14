class School:
    def __init__(self):
        
        self.student= {}
    
    def add_student(self, name, grade):
        
        self.student[name]=grade

    def roster(self):
         return [i for i, a in sorted(self.student.items(), key=lambda item: (item[1],item[0]))]

    def grade(self, grade_number):
       return sorted([i for i, a in self.student.items() if a == grade_number])
