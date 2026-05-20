# Декоратор для обробки помилок
def input_error(func):
    def inner(*args, **kwargs):
        try:
            # Викликаємо функцію
            return func(*args, **kwargs)

        except ValueError:
            # Помилка при неправильній кількості аргументів
            return "Give me name and phone please."

        except KeyError:
            # Контакт не знайдено
            return "Contact not found."

        except IndexError:
            # Користувач не ввів аргументи
            return "Enter the argument for the command."

    return inner


# Функція розбору команди
def parse_input(user_input: str):
    # Розділяємо введений рядок на команду та аргументи
    cmd, *args = user_input.split()

    # Повертаємо команду у нижньому регістрі
    return cmd.lower(), args


# Додавання контакту
@input_error
def add_contact(args, contacts):
    # Розпаковуємо ім'я та телефон
    name, phone = args

    # Додаємо контакт у словник
    contacts[name] = phone

    return "Contact added."


# Зміна номера телефону
@input_error
def change_contact(args, contacts):
    # Розпаковуємо аргументи
    name, phone = args

    # Якщо контакту не існує — викликаємо помилку
    if name not in contacts:
        raise KeyError

    # Оновлюємо номер телефону
    contacts[name] = phone

    return "Contact updated."


# Пошук номера телефону
@input_error
def show_phone(args, contacts):
    # Отримуємо ім'я
    name = args[0]

    # Якщо контакту не існує — помилка
    if name not in contacts:
        raise KeyError

    # Повертаємо номер
    return contacts[name]


# Виведення всіх контактів
@input_error
def show_all(contacts):
    # Якщо словник пустий
    if not contacts:
        return "No contacts saved."

    result = ""

    # Формуємо рядок з усіма контактами
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"

    return result.strip()


# Головна функція
def main():
    # Словник для зберігання контактів
    contacts = {}

    print("Welcome to the assistant bot!")

    # Нескінченний цикл роботи бота
    while True:
        # Отримуємо команду від користувача
        user_input = input("Enter a command: ")

        # Перевірка на пустий ввід
        if not user_input.strip():
            print("Invalid command.")
            continue

        # Розбираємо команду
        command, args = parse_input(user_input)

        # Команда завершення роботи
        if command in ["close", "exit"]:
            print("Good bye!")
            break

        # Привітання
        elif command == "hello":
            print("How can I help you?")

        # Додавання контакту
        elif command == "add":
            print(add_contact(args, contacts))

        # Зміна контакту
        elif command == "change":
            print(change_contact(args, contacts))

        # Пошук номера
        elif command == "phone":
            print(show_phone(args, contacts))

        # Виведення всіх контактів
        elif command == "all":
            print(show_all(contacts))

        # Невідома команда
        else:
            print("Invalid command.")


# Точка входу в програму
if __name__ == "__main__":
    main()