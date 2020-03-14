plants = {"C": "Clover", "G": "Grass", "R": "Radishes", "V": "Violets"}
students = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred",
            "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]

class Garden:
    def __init__(self, diagram, students = students):
         self.students = sorted(students)
         self.rows = diagram.splitlines()
    
    def plants(self, student):
        i = self.students.index(student)*2
        key = self.rows[0][i: i+2] + self.rows[1][i:i+2]
        return [plants[ke] for ke in key]
        
        
