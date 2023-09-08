#Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях. Напишите к ним классы исключения с выводом
#подробной информации. Поднимайте исключения внутри основного кода. Например нельзя создавать прямоугольник со сторонами отрицательной 
#длины.

#семинар 11
class MatrixComparisonError(Exception):
    def __init__(self, message):
        super().__init__(message)


class MatrixAdditionError(Exception):
    def __init__(self, message):
        super().__init__(message)

class Matrix:
    def __init__(self, matrix: list) -> None:
        self.matrix = matrix

    def print(self):
        matrixString = ""
        for i in range(len(self.matrix)):
            matrixString = matrixString + '  '.join(map(str,self.matrix[i])) + "\n"
        return matrixString
    
    def comparison(self, other):
        if not isinstance(other, Matrix):
            raise MatrixComparisonError("Второй операнд должен быть матрицей")
            
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise MatrixComparisonError("Матрицы должны быть одинакового размера")
    
        if self.matrix > other.matrix:
            return "Первая матрица больше второй"
        elif self.matrix < other.matrix:
            return "Вторая матрица больше первой"
        else:
            return "Матрицы равны"
    
    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise MatrixAdditionError("Второй операнд должен быть матрицей")

        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise MatrixAdditionError("Матрицы должны быть одинакового размера")
    
        result = []
        numbers = []

        for i in range(len(self.matrix)): 
            for j in range(len(self.matrix[i])):
                summa = self.matrix[i][j] + other.matrix[i][j]
                numbers.append(summa)
                
                if len(numbers) == len(self.matrix[i]):
                    result.append(numbers)
                    numbers = []

        return result
    
matrix1 = Matrix([[1, 2, 3], [4, 5, 6]])
print(matrix1.print())
matrix2 = Matrix([[7, 8, 9], [1, 2, 3]])
print(matrix2.print())

try:
    print(matrix1 + matrix2)
except MatrixAdditionError as e:
    print(f"Ошибка сложения матриц: {str(e)}")

try:
    print(matrix1.comparison(matrix2))
except MatrixComparisonError as e:
    print(f"Ошибка сравнения матриц: {str(e)}")