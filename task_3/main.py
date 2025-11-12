import json #Импорт json

operations = 0 #Счетчик операций

while True: #Бесконечный цикл
    print("\nМеню:") #Вывод меню
    print("1 - Вывести все записи") #Пункт 1
    print("2 - Вывести запись по полю (id)") #Пункт 2
    print("3 - Добавить запись") #Пункт 3
    print("4 - Удалить запись по полю (id)") #Пункт 4
    print("5 - Выйти из программы") #Пункт 5

    choice = input("Ваш выбор: ") #Ввод пункта меню

    f = open("stars.json", "r", encoding="utf-8") #Открыть файл
    content = f.read().strip() #Прочитать содержимое
    f.close() #Закрыть файл
    if content == "": #Если пустой
        data = [] #Список пустой
    else:
        data = json.loads(content) #Загрузить данные

    if choice == "1": #Вывод всех записей
        for i in range(len(data)): #Цикл по списку
            print("---------------------- Запись", i+1, "-----------------------") #Заголовок
            print("id:", data[i]["id"]) #Вывод id
            print("Название:", data[i]["name"]) #Вывод названия
            print("Созвездие:", data[i]["constellation"]) #Вывод созвездия
            print("Видна без телескопа:", data[i]["is_visible"]) #Вывод видимости
            print("Радиус (в солнечных):", data[i]["radius"]) #Вывод радиуса
        operations += 1 #Прибавить операцию

    elif choice == "2": #Вывод записи по id
        search_id = int(input("Введите id: ")) #Ввод id
        found = False #Флаг поиска
        for i in range(len(data)): #Цикл
            if data[i]["id"] == search_id: #Сравнение id
                print("Позиция в списке:", i) #Вывод позиции
                print("Запись:", data[i]) #Вывод записи
                found = True #Нашли
        if not found: #Если не нашли
            print("Запись с таким id не найдена") #Сообщение
        operations += 1 #Прибавить операцию

    elif choice == "3": #Добавить запись
        new_id = int(input("Введите id: ")) #Ввод id
        new_name = input("Введите название: ") #Ввод названия
        new_constellation = input("Введите созвездие: ") #Ввод созвездия
        new_visible = input("Видна без телескопа (True/False): ") #Ввод видимости
        new_radius = float(input("Введите радиус (в солнечных): ")) #Ввод радиуса
        data.append({ #Добавить словарь
            "id": new_id,
            "name": new_name,
            "constellation": new_constellation,
            "is_visible": new_visible == "True",
            "radius": new_radius
        })
        f = open("stars.json", "w", encoding="utf-8") #Открыть файл на запись
        json.dump(data, f, ensure_ascii=False, indent=2) #Сохранить список
        f.close() #Закрыть файл
        print("Запись добавлена") #Сообщение
        operations += 1 #Прибавить операцию

    elif choice == "4": #Удалить запись
        del_id = int(input("Введите id для удаления: ")) #Ввод id
        found = False #Флаг
        for i in range(len(data)): #Цикл
            if data[i]["id"] == del_id: #Сравнение id
                del data[i] #Удалить
                found = True #Нашли
                break #Прервать цикл
        if found: #Если нашли
            f = open("stars.json", "w", encoding="utf-8") #Открыть файл
            json.dump(data, f, ensure_ascii=False, indent=2) #Сохранить список
            f.close() #Закрыть файл
            print("Запись удалена") #Сообщение
        else: #Если не нашли
            print("Запись с таким id не найдена") #Сообщение
        operations += 1 #Прибавить операцию

    elif choice == "5": #Выход
        print("Количество выполненных операций:", operations) #Вывод счетчика
        break #Прервать цикл

    else: #Иначе
        print("Неверный пункт меню") #Сообщение
