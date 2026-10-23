# stats_module.py
import statistics

def get_average(data_dict):
    """Повертає середнє значення."""
    if not data_dict:
        return None
    return sum(data_dict.values()) / len(data_dict)

def get_min(data_dict):
    """Повертає мінімальне значення."""
    if not data_dict:
        return None
    return min(data_dict.values())

def get_max(data_dict):
    """Повертає максимальне значення."""
    if not data_dict:
        return None
    return max(data_dict.values())

def get_median(data_dict):
    """Повертає медіану."""
    if not data_dict:
        return None
    return statistics.median(data_dict.values())

def find_jumps(data_dict, threshold):
    """Знаходить різкі перепади між сусідніми значеннями."""
    jumps = []
    items = list(data_dict.items())
    for i in range(len(items) - 1):
        t1, v1 = items[i]
        t2, v2 = items[i+1]
        diff = abs(v2 - v1)
        if diff > threshold:
            jumps.append(f"між {t1} → {t2} ({round(diff, 2)})")
    return jumps

def show_table(data_dict, title):
    """Виводить таблицю значень."""
    print(f"\n=== Таблиця показів: {title} ===")
    print("Мітка часу | Значення")
    for time_label, value in data_dict.items():
        print(f"{time_label:<10} {value}")