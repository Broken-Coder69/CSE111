class Exam:
    def __init__(self, name, questions, marks):
        self.name = name
        self.questions = questions
        self.marks = marks
        self.total = self.marks * self.questions

    def detail(self):
        print(f"Exam Type: {self.name}")
        print(f"Number of questions: {self.questions}")
        print(f"Marks per questions: {self.marks}")
        return (f"Total Marks: {self.total}")
        
        



e1 = Exam('Midterm', 2, 10)
print(e1.detail())
print("===========================")
e2 = Exam('Final', 3, 10)
print(e2.detail())


# Exam Type: Midterm
# Number of questions: 2
# Marks per questions: 10
# Total Marks: 20
# ============================
# Exam Type: Final
# Number of questions: 3
# Marks per questions: 10
# Total Marks: 30