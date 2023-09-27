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
        if len(value) != 0:
            mid = statistics.mean(value)
            return mid
        else:
            return ' нет оценок' 
     
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
        if len(value) != 0:
            mid = statistics.mean(value)
            return mid
        else:
            return ' нет оценок'     
  
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

def average_all(self, course):
    value = []
    mid = 0
    tupl1, tupl2 = '', ''
    if isinstance(self[0], Student): 
            tupl1 = 'студентов'
            tupl2 = "Студенты" 
    else:
        tupl1 = "лекторов"
        tupl2 = "Лекторы"

    for i in self:
        for k in i.grades.keys():
            if k == course:
                value += i.grades.get(k)
    if len(value) != 0:
        mid = statistics.mean(value)
        return f'Средняя оценка {tupl1} на курсе {course}: {mid}'  
        
    else:
        return f'{tupl2} на курсе {course} не обучаются'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Java']
best_student.courses_in_progress += ['C++']
best_student.finished_courses += ['C#']

stella_student = Student("Стелла", "Савинкова", "Кошка")
stella_student.courses_in_progress += ['C#']
stella_student.courses_in_progress += ['C++']
 
lector = Lecturer("Марина", "Савинкова")
lector.courses_attached += ['Python']
lector.courses_attached += ['Java']

lector1 = Lecturer("Александра", "Манжос")
lector1.courses_attached += ['Java']


best_student.rate_hw(lector, 'Python', 10)
best_student.rate_hw(lector, 'Java', 7)


reviewer1 = Reviewer("Владислав", "Савинков")
reviewer1.courses_attached += ['Python']
reviewer1.courses_attached += ['C#']

reviewer2 = Reviewer('Валентина', 'Парфенова')
reviewer2.courses_attached += ['C++']

reviewer1.rate_hw(best_student, 'Python', 10)
reviewer1.rate_hw(best_student, 'Python', 5)
reviewer1.rate_hw(stella_student, 'C#', 5)
reviewer1.rate_hw(stella_student, 'C#', 10)
reviewer2.rate_hw(stella_student, 'C++', 5)



#print(best_student)
#print()
#print(reviewer1)
#print()
#print(lector)
#print()

list_students = []


for i in range(6):
    list_students.append(Student(f'Студент_{i}', f'Фамилия_{i}', 'ж'))
    list_students[i].courses_in_progress += ['Python']
    list_students[i].courses_in_progress += ['C#']
    reviewer1.rate_hw(list_students[i], 'Python', i+1)
    reviewer1.rate_hw(list_students[i], 'C#', i-1)
    print(f'{list_students[i]}\n')
  
print(average_all(list_students, 'Python'))
print(average_all(list_students, "C#"))
print(average_all(list_students, 'C++'))

list_lecturers = []
for i in range(6):
    list_lecturers.append(Lecturer(f'Лектор_{i}', f'Фамилия_{i}'))
    list_lecturers[i].courses_attached += ['Python']
    list_lecturers[i].courses_attached += ['C++']
    best_student.rate_hw(list_lecturers[i], 'Python', i+2)
    best_student.rate_hw(list_lecturers[i], 'C++', i+1)
    print(f'{list_lecturers[i]}\n')
 
print(average_all(list_lecturers, 'Python'))
print(average_all(list_lecturers, 'C#'))
print(average_all(list_lecturers, 'C++'))