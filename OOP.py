class Subject:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)


class Student:
    def __init__(self, name):
        self.name = name


class Diary:
    def __init__(self, student):
        self.student = student
        self.subjects = []

    def add_subject(self, subject):
        self.subjects.append(subject)



student = Student("Liliya")
math = Subject("Mathematics")
liliyas_diary = Diary(student)
liliyas_diary.add_subject(math)
math.add_grade(85)
math.add_grade(92)



print(f"Student: {liliyas_diary_diary.student.name}")
print(f"Subjects in Liliya's Diary: {', '.join([subject.name for subject in liliyas_diary.subjects])}")
