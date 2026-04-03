import json
import time
from datetime import datetime

operation = 0


def decoration(func):
    def wrapper(*args, **kwargs):
        global operation
        operation += 1
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        execution_time = end - start
        print(f"✔️ Операция №: {operation}")
        data_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Дата и время выполнения функции: {data_time}")
        print(f"Время выполнения функции: {execution_time:.5f}")
        print(f"Имя функции: {func.__name__}")
        print(f"Аргументы *args: {args}")
        print(f"Аргументы *kwargs: {kwargs}")
        print(f"Возвращаемое значение: {res}")

        # Создаем файл

        operation = (
            f"👉 Операция №: {operation}\n"
            f"Дата и время выполнения функции: {data_time}\n"
            f"Имя функции: {func.__name__}\n"
            f"Аргументы *args: {args}\n"
            f"Аргументы *kwargs: {kwargs}\n"
            f"Возвращаемое значение: {res}\n\n"
        )
        print("-" * 50)

        # Записываем данные в файл data.log
        try:
            with open("data.log", "a", encoding="UTF-8") as file:
                file.write(operation)
            print("✅ Все данные сохранены в файле 'data.log'")
        except Exception as e:
            print(f"❌ Ошибка при работе с файлом: {e}")
        return res

    return wrapper


while True:

    @decoration
    def my_fun(user_input):
        print("-" * 50)
        return [i for i in range(0, user_input + 1) if i % 2 == 0]

    user_input = int(input("\n👉 Введите число: "))
    res = my_fun(user_input)
    user_input2 = input("\nХотите продолжить (ДА/НЕТ)?: ").strip().upper()
    if user_input2 == "НЕТ":
        print("🔥Всего доброго. Отличного дня. И хорошего настроения")
        break