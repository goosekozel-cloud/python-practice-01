import argparse  # импорт библиотеки аргументов
from datetime import datetime  # импорт даты и времени

# словарь со всеми твоими 9 формулами конвертации
CONVERSIONS = {
    "km-miles": lambda x: x * 0.621371,  # КМ в мили
    "kg-pounds": lambda x: x * 2.20462,  # КГ в фунты
    "celsius-fahrenheit": lambda x: x * 9 / 5 + 32,  # Цельсий в Фаренгейт
    "m-feet": lambda x: x * 3.28084,  # Метры в футы
    "liters-gallons": lambda x: x * 0.264172,  # Литры в галлоны
    "celsius-kelvin": lambda x: x + 273.15,  # Цельсий в Кельвин
    "fahrenheit-celsius": lambda x: (x - 32) * 5 / 9,  # Фаренгейт в Цельсий
    "cm-inches": lambda x: x / 2.54,  # Сантиметры в дюймы
    "hours-minutes": lambda x: x * 60  # Часы в минуты
}


# функция записи ошибок в лог
def log_error(error_type, description, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # текущее время

    with open("errors.log", "a", encoding="utf-8") as file:  # открываем файл на дописывание
        file.write(f"[{timestamp}] {error_type}: {description}\n")  # пишем дату и тип
        file.write(f"Message: {message}\n")  # пишем сообщение


# форматирование названия (Celsius-> Fahrenheit)
def format_name(conv_str):
    parts = conv_str.split('-')  # разбиваем по дефису
    return f"{parts[0].capitalize()}-> {parts[1].capitalize()}"  # делаем заглавные буквы


def main():
    parser = argparse.ArgumentParser(description="Конвертер единиц измерения")  # создаем парсер

    # аргументы командной строки
    parser.add_argument("value", type=float, nargs='?', help="Значение")  # число (необязательное)
    parser.add_argument("--conversion", type=str, help="Тип конвертации")  # тип (именованный)
    parser.add_argument("--precision", type=int, default=2, help="Точность")  # знаков после запятой
    parser.add_argument("--list", action="store_true", help="Список")  # флаг вывода списка

    args = parser.parse_args()  # разбираем аргументы

    if args.list:  # если вызвали --list
        print("Доступные преобразования:")
        for key in CONVERSIONS.keys():  # цикл по словарю
            print(f"- {key}")  # выводим ключи
        return  # выходим

    try:  # блок перехвата ошибок
        if args.value is None or not args.conversion:  # проверка обязательных аргументов
            raise ValueError("Не указаны обязательные аргументы.")  # кидаем ошибку

        if args.conversion not in CONVERSIONS:  # проверка типа конвертации
            raise ValueError(f"Неизвестный тип: {args.conversion}")  # кидаем ошибку

        result = CONVERSIONS[args.conversion](args.value)  # считаем по формуле
        result = round(result, args.precision)  # округляем результат

        print(f"Input value: {args.value}")  # выводим значение
        print(f"Conversion: {format_name(args.conversion)}")  # выводим тип
        print(f"Result: {result}")  # выводим результат

    except ValueError as e:  # ловим ошибки значений
        log_error("ValueError", str(e), "Error validating input.")  # пишем в лог
        print(f"Ошибка ввода: {e}")  # выводим в консоль

    except ZeroDivisionError as e:  # ловим деление на ноль
        log_error("ZeroDivisionError", "Division by zero.", "Error calculating.")  # пишем в лог
        print("Ошибка: Деление на ноль.")  # выводим в консоль

    except Exception as e:  # ловим остальные ошибки
        log_error(type(e).__name__, str(e), "Unexpected error.")  # пишем в лог
        print(f"Непредвиденная ошибка: {e}")  # выводим в консоль


if __name__ == "__main__":
    main()  # запуск программы