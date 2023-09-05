class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Not a lecturer")
            return
        return self.get_average_grade() < other.get_average_grade()

    def get_average_grade(self):
        total_grade = sum(sum(course_grades) for course_grades in self.grades.values())
        total_courses = sum(len(course_grades) for course_grades in self.grades.values())
        return total_grade / total_courses if total_courses > 0 else 0

    def __str__(self):
        total_grades = sum(sum(course_grades) for course_grades in self.grades.values())
        total_courses = sum(len(course_grades) for course_grades in self.grades.values())
        average_grade = total_grades / total_courses if total_courses > 0 else 0
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_grade:.1f}\n"


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\n"


class Student:
    def __init__(self, name, surname, gender, average_grade = 0.0):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grade = average_grade

    def mentor_evaluation(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        total_grades = sum(sum(course_grades) for course_grades in self.grades.values())
        total_courses = sum(len(course_grades) for course_grades in self.grades.values())
        average_grade = total_grades / total_courses if total_courses > 0 else 0
        courses_in_progress_str = ", ".join(self.courses_in_progress)
        finished_courses_str = ", ".join(self.finished_courses) if len(self.finished_courses) > 0 else "На данный момент таких нет"
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {average_grade:.1f}\nКурсы в процессе изучения: {courses_in_progress_str}\nЗавершенные курсы: {finished_courses_str}\n"

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Not a student")
            return
        return self.get_average_grade() < other.get_average_grade()

    def get_average_grade(self):
        total_grades = sum(sum(course_grades) for course_grades in self.grades.values())
        total_courses = sum(len(course_grades) for course_grades in self.grades.values())
        return total_grades / total_courses if total_courses > 0 else 0

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

another_student = Student('Alice', 'Johnson', 'female')
another_student.courses_in_progress += ['Python']

cool_lecturer = Lecturer('John', 'Doe')
cool_lecturer.courses_attached += ['Python']

another_lecturer = Lecturer('Jane', 'Smith')
another_lecturer.courses_attached += ['Python']

strict_reviewer = Reviewer('Alex', 'Smith')
strict_reviewer.courses_attached += ['Python']

another_reviewer = Reviewer('Anna', 'Brown')
another_reviewer.courses_attached += ['Python']

strict_reviewer.rate_hw(best_student, 'Python', 9)
strict_reviewer.rate_hw(another_student, 'Python', 8)

best_student.mentor_evaluation(cool_lecturer, 'Python', 7)
another_student.mentor_evaluation(cool_lecturer, 'Python', 8)

print(best_student)
print(another_student)
print(cool_lecturer)
print(another_lecturer)
print(strict_reviewer)
print(another_reviewer)


def student_grade(students, course):
    total_grade = 0
    count = 0
    for student in students:
        if course in student.grades:
            total_grade += sum(student.grades[course])
            count += len(student.grades[course])
    return total_grade / count if count > 0 else 0


def lecture_grade(lecturers, course):
    total_grade = 0
    count = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grade += sum(lecturer.grades[course])
            count += len(lecturer.grades[course])
    return total_grade / count if count > 0 else 0

students = [best_student, another_student]
lecturers = [cool_lecturer, another_lecturer]

avg_hw = student_grade(students, 'Python')
avg_lecture = lecture_grade(lecturers, 'Python')

print(f"Средняя оценка за домашние задания по курсу Python: {avg_hw:.1f}")
print(f"Средняя оценка за лекции по курсу Python: {avg_lecture:.1f}")