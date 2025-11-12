import json #Модуль json

f = open("dump.json", "r", encoding="utf-8") #Открытие файла
data = json.load(f) #Загрузка данных
f.close() #Закрытие файла

code = input("Введите номер квалификации: ") #Ввод кода квалификации

found = False #Флаг результата поиска

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
