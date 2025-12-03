#Класс для исключения RectCorrectError
class RectCorrectError(Exception):
    def __init__(self, rect_num):
        message = f"{rect_num}-й прямоугольник некорректный"
        super().__init__(message)

#Функция для проверки прямоугольника на правильность
def isCorrectRect(list):
    if list[0][0] < list[1][0] and list[0][1] < list[1][1]:
        return True
    else:
        return False

#Функция для проверки соприкосновения прямоугольников
def isCollisionRect(rect_one, rect_two):

    #Проверка существуют ли прямоугольники
    if not isCorrectRect(rect_one):
        raise RectCorrectError(1)
    if not isCorrectRect(rect_two):
        raise RectCorrectError(2)

    #Проверка соприкосновения прямоугольников
    if not (rect_one[1][0] < rect_two[0][0] or rect_two[1][0] < rect_one[0][0] or  rect_one[1][1] < rect_two[0][1] or rect_two[1][1] < rect_one[0][1]):
        return True
    else:
        return False