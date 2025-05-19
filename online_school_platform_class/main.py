from online_school_platform import Course, User, OnlineSchool


c1 = Course("Python", "Nauka podstaw", 99.0)
c2 = Course("SQL", "Bazy danych", 79.0)

u1 = User("Paweł", "pawel@example.com")
u1.enroll_in_course(c1)
u1.enroll_in_course(c2)

c1.enroll("Paweł")
c2.enroll("Paweł")

school = OnlineSchool()
school.add_course(c1)
school.add_course(c2)
school.add_user(u1)

print("--- Kursy ---")
print(school.list_courses())

print("\n--- Użytkownicy ---")
print(school.list_users())

print("\n--- TOP Kurs ---")
print(school.top_course())

print("\n--- Szukaj użytkownika ---")
print(school.find_user_by_email("pawel@example.com"))
