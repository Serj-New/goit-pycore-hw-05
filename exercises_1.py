def caching_fibonacci():
    # Створюємо порожній словник cache
    cache = {}

    # Перевіряємо число для обчислення
    def fibonacci(n: int) -> int:
        if n <= 0:
            return 0
        if n == 1:
            return 1
        
        if n in cache:
            return cache[n]
        
        # Додаємо результат в словник
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        # Повертаємо словник
        return cache[n]

    # Повертаємо функцію fibonacci
    return fibonacci


# Перевірка
if __name__ == "__main__":
    # Отримуємо функцію fibonacci
    fib = caching_fibonacci()
    
    # Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
    print(fib(10))  # 55
    print(fib(15))  # 610