print("Конвертер единиц")

while True:
    print("\nВыберите тип преобразования:")
    print("1. Километры -> мили")
    print("2. Килограммы -> фунты")
    print("3. Цельсий -> Фаренгейт")
    print("4. Метры -> футы")
    print("5. Литры -> галлоны")
    print("6. Цельсий -> Кельвин")
    print("7. Фаренгейт -> Цельсий")
    print("8. Сантиметры -> дюймы")
    print("9. Часы -> минуты")

    choice = input("Ваш выбор: ")

    if choice in ("1", "2", "3", "4", "5", "6", "7", "8", "9"):
        try:
            value = float(input("Введите значение: "))
            if choice == "1":
                result = value * 0.621371
                print(f"{value} км = {result:.2f} миль")
            elif choice == "2":
                result = value * 2.20462
                print(f"{value} кг = {result:.2f} фунтов")
            elif choice == "3":
                result = value * 9 / 5 + 32
                print(f"{value} °C = {result:.2f} °F")
            elif choice == "4":
                result = value * 3.28084
                print(f"{value} м = {result:.2f} футов")
            elif choice == "5":
                result = value * 0.264172
                print(f"{value} л = {result:.2f} галлонов")
            elif choice == "6":
                result = value + 273.15
                print(f"{value} °C = {result:.2f} K")
            elif choice == "7":
                result = (value - 32) * 5 / 9
                print(f"{value} °F = {result:.2f} °C")
            elif choice == "8":
                result = value / 2.54
                print(f"{value} см = {result:.2f} дюймов")
            elif choice == "9":
                result = value * 60
                print(f"{value} ч = {result:.2f} минут")
        except ValueError:
            print("Ошибка: нужно ввести число.")
    else:
        print("Ошибка: неизвестный номер преобразования.")

    while True:
        answer = input("Хотите выполнить ещё одно преобразование? (да/нет): ").strip().lower()
        if answer == "да" or answer == "нет":
            break
        print("Ошибка: введите «да» или «нет».")

    if answer == "нет":
        break

print("Работа программы завершена.")