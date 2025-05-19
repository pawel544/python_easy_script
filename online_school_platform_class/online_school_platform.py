class Course:
    def __init__(self, title, description, price, ):

        self.title = title
        self.description = description
        self.price = price
        self.students = []

    def enroll(self, student_name):
        if student_name:
            self.students.append(student_name)
        else:
            return (f"Nie podałeś studenta")

    def __str__(self):
        return (f"{self.title}, \n"
                f"{self.description} \n "
                f"{self.price} zł\n"
                f"studenci którzy się zapisali: {len(self.students)}")

class User:
    def __init__(self, name, email  ):
        self.name = name
        self.email = email
        self.enrolled_courses =[]

    def enroll_in_course(self, course):
        if course:
            self.enrolled_courses.append(course)
        else:
            return f"Nie wybrałeś kursu"

    def __str__(self):
        return  (f"{self.name}\n" 
                f"{self.email}\n"
                 f"twoja ilość kórsów wynosi: {len(self.enrolled_courses)}")

class OnlineSchool:
    def __init__(self ):
        self.courses = []
        self.users=[]

    def add_course(self,course):
        if course:
            self.courses.append(course)
        else:
            return f"NIe wprowadziłeś kursu"

    def add_user(self, user):
        if user:
            self.users.append(user)
        else:
            return f"Nie wprowadziłeś urztkownika"

    def list_courses(self):
        if len(self.courses) > 0:
            return "\n".join(str(course) for course in self.courses)
        else:
            return "Brak kursów do wyświetlenia"

    def list_users(self):
        if len(self.users) > 0:
            return "\n".join( str(user) for user in self.users)
        else:
            return f"Brak kursantów do wyświetlenia"

    def find_user_by_email(self,email):
        for user in self.users:
            if email== user.email:
                corse = "\n".join(course.title for course in user.enrolled_courses)
                return (f"{user.name}\n" \
                       f"{user.email} \n" \
                       f"jego kursy: {corse} " )
        else:
            return f"brak emaila w bazie- dodaj użytkownika"
    def top_course(self):
        if not self.courses:
            return f"brak kursów albo stódentów"
        else:
            return max(self.courses, key=lambda c: len(c.students))