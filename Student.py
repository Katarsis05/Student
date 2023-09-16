import statistics

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __eq__(self, other):
        return self.average() == other.average()

    def __gt__(self, other):
        return self.average() > other.average()

    def __ge__(self, other):
        return self.average() >= other.average()

    def rate_hw(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in lector.courses_attached and course in self.courses_in_progress:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        score = self.average()
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание:"\
         f"{score}\nКурсы в процессе обучения: {', '.join(self.courses_in_progress)}"\
         f"\nЗавершенные курсы: {', '.join(self.finished_courses)}"

    def average(self):
        value = []
        mid = 0
        for i in self.grades.values():
            value += i
        mid = statistics.mean(value)     
        return mid
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    
class Lecturer(Mentor):
    #@total_ordering
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        self.grades = {}

    def __eq__(self, other):
        return self.average() == other.average()

    def __gt__(self, other):
        return self.average() > other.average()

    def __ge__(self, other):
        return self.average() >= other.average()

    def average(self):
        value = []
        mid = 0
        for i in self.grades.values():
            value += i
        mid = statistics.mean(value)     
        return mid
  
    def __str__(self):
        score = self.average()
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {score}"
 
class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
                return f"Имя: {self.name}\nФамилия: {self.surname}"



best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Java']
best_student.finished_courses += ['C#']

stella_student = Student("Стелла", "Савинкова", "Кошка")
stella_student.courses_in_progress += ['C#']
 
lector = Lecturer("Марина", "Савинкова")
lector.courses_attached += ['Python']
lector.courses_attached += ['Java']
lector1 = Lecturer("Александра", "Манжос")
lector1.courses_attached += ['Java']


best_student.rate_hw(lector, 'Python', 10)
#best_student.rate_hw(lector, 'Python', 5)
#best_student.rate_hw(lector, 'Java', 7)
best_student.rate_hw(lector1, 'Java', 7)


reviewer1 = Reviewer("Владислав", "Савинков")
reviewer1.courses_attached += ['Python']
reviewer1.courses_attached += ['C#']

reviewer1.rate_hw(best_student, 'Python', 10)
reviewer1.rate_hw(best_student, 'Python', 10)
reviewer1.rate_hw(stella_student, 'C#', 5)
reviewer1.rate_hw(stella_student, 'C#', 10)



print(best_student)
print()
print(reviewer1)
print()
print(lector)
print()

