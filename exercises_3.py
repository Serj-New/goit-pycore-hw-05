from typing import List, Dict


def parse_log_line(line: str) -> dict:
    # Розділяємо рядок по пробілу
    parts = line.split(" ", 3)
    
    # Повертаємо словник зі ключами дата, час, рівень логування, повідомлення і відповідними значеннями логів
    return {
        "date": parts[0],
        "time": parts[1],
        "level": parts[2],
        "message": parts[3]
    }


def load_logs(file_path: str) -> List[dict]:
    # Створюємо пустий список
    logs = []
    
    try:
        # Відкриваємо файл
        with open(file_path, "r", encoding="utf-8") as file:
            # Читаємо кожен рядок
            for line in file:
                line = line.strip()
                
                # Пропускаємо пусті рядки
                if not line:
                    continue
                
                # Парсимо рядок і додаємо у список
                logs.append(parse_log_line(line))
    
    # Робимо виняток
    except FileNotFoundError:
        print("Файл не знайдено")
    
    # Повертаємо список логів
    return logs


def filter_logs_by_level(logs: List[dict], level: str) -> List[dict]:
    # Приводимо рівень до верхнього регістру (ERROR, INFO...)
    level = level.upper()
    
    # Фільтруємо список логів
    return [log for log in logs if log["level"] == level]


def count_logs_by_level(logs: List[dict]) -> Dict[str, int]:
    # Створюємо пустий словний
    counts = {}
    
    # Проходимо по всіх логах
    for log in logs:
        level = log["level"]
        
        # Якщо рівень вже є — збільшуємо
        if level in counts:
            counts[level] += 1
        else:
            # В іншому випадку створюємо запис
            counts[level] = 1
    
    # Повертаємо словник 
    return counts


def display_log_counts(counts: Dict[str, int]):
    # Виводимо заголовок таблиці
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    
    # Виводимо кожен рівень
    for level, count in counts.items():
        print(f"{level:<17} | {count}")


# Перевірка
if __name__ == "__main__":
    logs = load_logs("logfile.log")
    
    # Рахуємо статистику
    counts = count_logs_by_level(logs)
    
    # Виводимо таблицю
    display_log_counts(counts)
    
    # Додатково виводимо фільтр
    error_logs = filter_logs_by_level(logs, "error")
    
    print("\nДеталі ERROR:")
    for log in error_logs:
        print(f"{log['date']} {log['time']} - {log['message']}")