# Декоратор для обробки помилок
def input_error(func):
    def inner(*args, **kwargs):
        try:
            # Викликаємо оригінальну функцію
            return func(*args, **kwargs)
        
        except ValueError:
            # Виключення,якщо неправильна кількість аргументів
            return "Give me name and phone please."
        
        except KeyError:
            # Виключення,якщо контакт не знайдено
            return "Contact not found."
        
        except IndexError:
            # Виключення,якщо аргументів взагалі нема
            return "Enter the argument for the command."
    
    return inner


@input_error
def add_contact(args, contacts):
    # Розпаковуємо аргументи (ім'я і телефон)
    name, phone = args
    
    # Додаємо у словник
    contacts[name] = phone
    
    return "Contact added."


@input_error
def change_contact(args, contacts):
    name, phone = args
    
    # Якщо контакту нема — викликаємо помилку
    if name not in contacts:
        raise KeyError
    
    # Оновлюємо номер
    contacts[name] = phone
    
    return "Contact updated."


@input_error
def show_phone(args, contacts):
    # Беремо ім'я
    name = args[0]
    
    # Якщо нема контакту
    if name not in contacts:
        raise KeyError
    
    return contacts[name]


# Перевірка
if __name__ == "__main__":
    contacts = {}
    
    print(add_contact(["John", "123456"], contacts))
    print(show_phone(["John"], contacts))
    
    # Перевірка помилок
    print(show_phone(["Bob"], contacts))
    print(add_contact(["OnlyName"], contacts))
    print(show_phone([] , contacts))