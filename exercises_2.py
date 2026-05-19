import re
from typing import Callable


def generator_numbers(text: str):
    # Шукаємо числа типу 123 або 123.45
    pattern = r"\d+\.\d+|\d+"
    
    # Знаходимо всі співпадіння у тексті
    matches = re.findall(pattern, text)
    
    # Проходимо по кожному знайденому числу
    for match in matches:
        # Перетворюємо рядок у float і повертаємо через yield, роблячі функцію генератором
        yield float(match)


def sum_profit(text: str, func: Callable) -> float:
    # Повертаємо генератор чисел і підсумовуємо всі значення генератора
    return sum(func(text))


# 🔽 Перевірка
if __name__ == "__main__":
    text = "Доходи: 1000.01 27.45 324.00"
    
    # Викликаємо функцію підрахунку
    total = sum_profit(text, generator_numbers)
    
    # Виводимо результат
    print(total)