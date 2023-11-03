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

    def calculate_average_grade(self):
        total_grades = 0
        total_subjects = len(self.subjects)

        for subject in self.subjects:
            for grade in subject.grades:
                total_grades += grade

        return total_grades / (total_subjects * len(subject.grades))


student = Student("Liliya")
math = Subject("Mathematics")
liliyas_diary = Diary(student)
liliyas_diary.add_subject(math)
math.add_grade(85)
math.add_grade(92)



print(f"Student: {liliyas_diary_diary.student.name}")
print(f"Subjects in Liliya's Diary: {', '.join([subject.name for subject in liliyas_diary.subjects])}")
print(f"Average Grade for John: {liliyas_diary.calculate_average_grade()}")

print(f"Student: {alices_diary.student.name}")
print(f"Subjects in Alice's Diary: {', '.join([subject.name for subject in alices_diary.subjects])}")
print(f"Average Grade for Alice: {alices_diary.calculate_average_grade()}")
