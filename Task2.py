#Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях. Напишите к ним классы исключения с выводом
#подробной информации. Поднимайте исключения внутри основного кода. Например нельзя создавать прямоугольник со сторонами отрицательной 
#длины.

#семинар 12
class InvalidNameError(Exception):
    def __init__(self, message):
        super().__init__(message)

class NameDescriptor:
    def __set_name__(self, owner, name):
        self._name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self._name, None)

    def __set__(self, instance, value):
        if not value.istitle() or not value.isalpha():
            raise InvalidNameError("ФИО должно начинаться с заглавной буквы и может содержать только буквы")
        setattr(instance, self._name, value)

class Student:
    last_name = NameDescriptor()
    first_name = NameDescriptor()
    middle_name = NameDescriptor()

    def __init__(self, last_name: str, first_name: str, middle_name: str):
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name

    def print(self):
        print(self.last_name + ' ' + self.first_name + ' ' + self.middle_name)

try:
    s = Student('Иванов', 'Иван', 'Иванович')
    s.print()
except InvalidNameError as e:
    print(f"Ошибка создания студента: {str(e)}")

try:
    s = Student('иванов', 'И2ван', 'Иванович')
    s.print()
except InvalidNameError as e:
    print(f"Ошибка создания студента: {str(e)}")