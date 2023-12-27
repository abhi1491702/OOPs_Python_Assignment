from student import Student
from teacher import Teacher
from course import Course
from payment import Payment
from enrollment import Enrollment
from datetime import datetime
#from Exception import StudentNotFoundException,CourseNotFoundException,TeacherNotFoundException
class SIS:
    def __init__(self):
        self._enrollments = []
        self._teachers_assigned_courses = []
        self._payments = []
        self.students = []
        self.courses = []
        self.teachers = []
        self.enrollments = []
        self.payments = []

    def EnrollStudentInCourse(self, student, course):
        enrollment = {"student": student, "course": course}
        self._enrollments.append(enrollment)
        print(f"Student {student.FirstName} enrolled in {course.CourseName}.")


    def AssignTeacherToCourse(self, teacher, course):
        teacher_assignment = {"teacher": teacher, "course": course}
        self._teachers_assigned_courses.append(teacher_assignment)
        print(f"Teacher {teacher.FirstName} assigned to {course.CourseName}.")

    def RecordPayment(self, paymentid,studentid, amount, paymentDate):
        payment = Payment(paymentid,studentid, amount, paymentDate)
        self._payments.append(payment)
        print(f"Payment of {amount}  recorded successfully.")

    def GenerateEnrollmentReport(self, course):
        enrolled_students = [enrollment["student"] for enrollment in self._enrollments if enrollment["course"] == course]
        print(f"Enrollment Report for {course.CourseName}:")
        for student in enrolled_students:
            print(f"- {student.FirstName} {student.LastName}")

    def GeneratePaymentReport(self, student):
        student_payments = [payment for payment in self._payments if payment.StudentID == student.StudentID]
        print(f"Payment Report for {student.FirstName} {student.LastName}:")
        for payment in student_payments:
            print(f"- Amount: {payment.amount}, Date: {payment.paymentDate}")

    def CalculateCourseStatistics(self, course):
        enrollments_count = len([enrollment for enrollment in self._enrollments if enrollment["course"] == course])
        total_payments = sum([payment.Amount for payment in self._payments if payment.CourseID == course.CourseID])
        print(f"Course Statistics for {course.CourseName}:")
        print(f"- Enrollments: {enrollments_count}")
        print(f"- Total Payments: {total_payments}")

student=Student(StudentID=1, FirstName="Abhishek", LastName="Kanoujia", DateOfBirth=datetime(2001, 6, 7),
            Email="abhishekk@gmail.com", PhoneNumber="7894561230")
teacher =Teacher(101,"Mr.","Swami","swami@gmail.com")
python_course = Course(105, "Python", "305", "Mr. swami")

sis = SIS()
sis.EnrollStudentInCourse(student,python_course)
sis.AssignTeacherToCourse(teacher, python_course)
sis.RecordPayment( 201,1,8000,"2023-01-15")
sis.GenerateEnrollmentReport(python_course)
sis.GeneratePaymentReport(student)
sis.CalculateCourseStatistics(python_course)

