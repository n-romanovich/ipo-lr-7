import json #Модуль json

found = False

#Функция вывода данных на экран
def disp_data(code):
    global found    #Использование глобальной переменной found

    for item in data: #Перебор данных
        if item.get("model") == "data.specialty": #Проверка на специальность
            fields = item.get("fields", {}) #Получение полей
            if fields.get("code") == code: #Сравнение кода
                print("============== Найдено ===============") #Вывод заголовка
                print(fields.get("code"), ">> Специальность \"" + fields.get("title") + "\", " + fields.get("c_type")) #Вывод специальности
                found = True #Меняем флаг
                for skill in data: #Цикл по всем объектам для поиска квалификаций
                    if skill.get("model") == "data.skill": #Проверка на квалификацию
                        s_fields = skill.get("fields", {}) #Получение полей
                        if s_fields.get("code", "").startswith(code): #Проверка кода
                            print(s_fields.get("code"), ">> Квалификация \"" + s_fields.get("title") + "\"") #Вывод квалификации

    if not found: #Если ничего не найдено
        print("============== Не найдено ===============") #Вывод сообщения

#Функция открытия файла
def file_open():
    f = open("dump.json", "r", encoding="utf-8") #Открытие файла
    data = json.load(f) #Загрузка данных
    f.close() #Закрытие файла

    return data



data = file_open() #Вызов функции открытия файла

code = input("Введите номер квалификации: ") #Ввод кода квалификации

disp_data(code) #Вызов функциии вывода данных на экран

