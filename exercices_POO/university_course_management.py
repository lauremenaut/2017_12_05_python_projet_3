""" Models course management system in a university """


class Person: # Classe abstraite
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

    def contact_someone(self, contact):
        pass


class Student(Person):
    def __init__(self, student_id, name, email, group):
        super().__init__(student_id, name, email)
        self.group = group


class Group: # collection
    def __init__(self, curriculum_name, level, *taught_subject):
        self.curriculum_name = curriculum_name
        self.level = level
        self.taught_subject = taught_subject
        self.students = []

    def add_student(self, student):
        self.students.append(student)


class Teacher(Person):
    def __init__(self, teacher_id, name, email, *taught_subject):
        super().__init__(teacher_id, name, email)
        self.taught_subject = taught_subject


class TaughtSubject:
    def __init__(self, name, *teacher_name):
        self.name = name
        self.teacher_name = teacher_name


class Enrollment:
    def __init__(self, student_id, curriculum_name, level, date):
        self.student_id = student_id
        self.curriculum_name = curriculum_name
        self.level = level
        self.date = date


class CourseSchedule:
    def __init__(self, group, taught_subject):
        pass


class Results:
    def __init__(self, student_id, **notes):
        self.student_id = student_id
        self.notes = notes
        success = False
