# ============================================================
# oop_demo.py
# Concept: classes and objects — the pattern behind EVERY library
#          you'll use for the rest of this internship
# ============================================================
class Student:
    """A blueprint for representing one student's record."""
    def __init__(self, name, marks):
        # __init__ runs automatically the moment a new Student is created.
        # 'self' means "this particular student" — it's how each object
        # keeps its own separate name and marks instead of sharing one copy.
        self.name = name
        self.marks = marks   # a list of marks, e.g. [88, 92, 76]
    def average(self):
        """A method: a function that belongs to the class."""
        return round(sum(self.marks) / len(self.marks), 2)
    def has_passed(self, passing_average=40):
        return self.average() >= passing_average
# --- Creating three separate objects from the ONE Student blueprint ---
student_1 = Student("Ananya", [88, 92, 76])
student_2 = Student("Vikram", [35, 40, 28])
student_3 = Student("Zara", [76, 60, 82])
# Looping over a list of OBJECTS — this exact pattern shows up everywhere
# in data work: a list of model results, a list of dataset rows, etc.
for student in [student_1, student_2, student_3]:
    status = "PASSED" if student.has_passed() else "FAILED"
    print(f"{student.name}: average = {student.average()} → {status}")