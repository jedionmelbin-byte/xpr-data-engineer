from person import Person


class Student:
    def __init__(self, name, grade):
        self.person = Person(name)  # Se llama a Person dentro de Student
        self.grade = grade

    def show_info(self):
        self.person.show()
        print(f"Grado: {self.grade}")


