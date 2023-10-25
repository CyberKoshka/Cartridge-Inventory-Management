# Словарь, где ключ - модель картриджа, значение - количество
cartridges = {}

# Функция для добавления нового картриджа
def add_cartridge(model, count):
    if model in cartridges:
        cartridges[model] += count
    else:
        cartridges[model] = count

# Функция для удаления картриджа
def remove_cartridge(model, count):
    if model in cartridges:
        if cartridges[model] >= count:
            cartridges[model] -= count
            if cartridges[model] == 0:
                del cartridges[model]
        else:
            print(f"Недостаточно картриджей модели {model} для удаления {count} штук.")
    else:
        print(f"Картридж модели {model} отсутствует.")

# Функция для вывода информации о всех картриджах
def print_cartridges():
    for model, count in cartridges.items():
        print(f"Модель: {model}, количество: {count}")

# Главный цикл программы
while True:
    print("\n1. Добавить картридж")
    print("2. Удалить картридж")
    print("3. Вывести информацию о всех картриджах")
    print("4. Выход")
    
    choice = int(input("Выберите действие: "))
    
    if choice == 1:
        model = input("Введите модель картриджа: ")
        count = int(input("Введите количество: "))
        add_cartridge(model, count)
    elif choice == 2:
        model = input("Введите модель картриджа: ")
        count = int(input("Введите количество: "))
        remove_cartridge(model, count)
    elif choice == 3:
        print_cartridges()
    elif choice == 4:
        break
    else:
        print("Неверный выбор. Пожалуйста, выберите действие из списка.")