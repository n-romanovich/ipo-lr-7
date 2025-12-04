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

#Функция для вычисления площади соприкосновения прямоугольников
def intersectionAreaRect(rect_one, rect_two):

    #Проверка существуют ли прямоугольники
    if not isCorrectRect(rect_one):
        raise ValueError("1-й прямоугольник некорректный")
    if not isCorrectRect(rect_two):
        raise ValueError("2-й прямоугольник некорректный")

    #Формула вычисления площади пересечения прямоугольников
    s = (min(rect_one[1][0], rect_two[1][0]) - max(rect_one[0][0], rect_two[0][0])) * (min(rect_one[1][1], rect_two[1][1]) - max(rect_one[0][1], rect_two[0][1]))
    return s

#Функция для обработки площади пересечения > 2 многоугольников
def intersectionAreaMultiRect(rects):

    #Проверка существуют ли прямоугольники
    i = 0
    for rect in rects:
        i += 1
        if not isCorrectRect(rect):
            raise RectCorrectError(i)
    
    #Списки для координат
    x1_list = []
    y1_list = []
    x2_list = []
    y2_list = []

    #Заполнение списков для координат
    for rect in rects:
        x1_list.append(rect[0][0])
        y1_list.append(rect[0][1])
        x2_list.append(rect[1][0])
        y2_list.append(rect[1][1])

    #Нахождение значений для вычисления
    left_x   = max(x1_list)
    bottom_y = max(y1_list)
    right_x  = min(x2_list)
    top_y    = min(y2_list)

    #Вычисление площади пересечения
    if left_x < right_x and bottom_y < top_y:
        return (right_x - left_x) * (top_y - bottom_y)