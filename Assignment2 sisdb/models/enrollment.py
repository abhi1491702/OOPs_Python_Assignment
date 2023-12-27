from student import Student
from datetime import datetime
from course import Course
class Enrollment:
    def __init__(self, EnrollmentID, StudentID, CourseID, EnrollmentDate):
        self._EnrollmentID = EnrollmentID
        self._StudentID = StudentID
        self._CourseID = CourseID
        self._EnrollmentDate = EnrollmentDate

    @property
    def EnrollmentID(self):
        return self._EnrollmentID

    @EnrollmentID.setter
    def EnrollmentID(self, new_EnrollmentID):
        if isinstance(new_EnrollmentID, int) and new_EnrollmentID > 0:
            self._EnrollmentID = new_EnrollmentID
        else:
            raise ValueError("Enrollment ID must be a positive integer.")

    @property
    def StudentID(self):
        return self._StudentID

    @StudentID.setter
    def StudentID(self, new_StudentID):
        if isinstance(new_StudentID, int) and new_StudentID > 0:
            self._StudentID = new_StudentID
        else:
            raise ValueError("Student ID must be a positive integer.")

    @property
    def CourseID(self):
        return self._CourseID

    @CourseID.setter
    def CourseID(self, new_CourseID):
        if isinstance(new_CourseID, int) and new_CourseID > 0:
            self._CourseID = new_CourseID
        else:
            raise ValueError("Course ID must be a positive integer.")

    @property
    def EnrollmentDate(self):
        return self._EnrollmentDate

    @EnrollmentDate.setter
    def EnrollmentDate(self, new_EnrollmentDate):
        if isinstance(new_EnrollmentDate, str) and len(new_EnrollmentDate) == 10:
            self._EnrollmentDate = new_EnrollmentDate
        else:
            raise ValueError("Invalid enrollment date format.")


    def GetStudents(self):
        return self._enrollments
student_1 = Student(StudentID=1, FirstName="Abhishek", LastName="kanoujia", DateOfBirth=datetime(2002, 8, 3), Email="abhishekk@email.com", PhoneNumber="7894561230")
student_2 = Student(StudentID=2, FirstName="Ram", LastName="kumar", DateOfBirth=datetime(2001, 1, 13), Email="ram@email.com", PhoneNumber="7007408956")

python_course = Course(105, "Python", "305", "Mr. swami")
student_1.EnrollInCourse(python_course)
student_2.EnrollInCourse(python_course)

enrollments= python_course.GetEnrollments()

print("Enrolled Students:")
for student in enrollments:
    print(f"- Student ID: {student.StudentID}, Student Name: {student.FirstName} {student.LastName}")