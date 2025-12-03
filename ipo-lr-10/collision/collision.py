#Функция для проверки прямоугольника на правильность
def isCorrectRect(list):
    if list[0][0] < list[1][0] and list[0][1] < list[1][1]:
        return True
    else:
        return False

