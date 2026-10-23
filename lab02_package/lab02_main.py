# lab02_main.py
import sensors as sm 

def parse_input(input_str):
    """Перетворює введений рядок на список дійсних чисел (з перевіркою)."""
    parts = input_str.strip().split()
    result = []
    for p in parts:
        try:
            result.append(float(p))
        except ValueError:
            print(f"Помилка: значення '{p}' не є числом і було пропущено.")
    return result

def create_data_dict(temp_list, hum_list, pres_list):
    """Формує словник даних з мітками часу."""
    data = {"temperature": {}, "humidity": {}, "pressure": {}}
    for i, val in enumerate(temp_list):
        data["temperature"][f"T{i+1}"] = val
    for i, val in enumerate(hum_list):
        data["humidity"][f"T{i+1}"] = val
    for i, val in enumerate(pres_list):
        data["pressure"][f"T{i+1}"] = val
    return data

def process_measurements(title, data_dict, threshold):
    """Виводить таблицю та статистику для заданого виду даних."""
    if not data_dict:
        print(f"\nНемає даних для {title}")
        return
        
    sm.show_table(data_dict, title)
    
    avg = sm.get_average(data_dict)
    print(f"\nСереднє значення: {round(avg, 2) if avg is not None else 'None'}")
    print(f"Мінімум: {sm.get_min(data_dict)}")
    print(f"Максимум: {sm.get_max(data_dict)}")
    print(f"Медіана: {sm.get_median(data_dict)}")
    
    jumps = sm.find_jumps(data_dict, threshold)
    if jumps:
        print(f"Різкі перепади: {', '.join(jumps)}")
    else:
        print("Різкі перепади: відсутні")

def main():
    print("=== Обробка показів системи 'Розумний будинок' ===")
    
    t_str = input("Введіть температури (°C): ")
    h_str = input("Введіть вологість (%): ")
    p_str = input("Введіть тиск (Па): ")
    
    temp_list = parse_input(t_str)
    hum_list = parse_input(h_str)
    pres_list = parse_input(p_str)
    
    if not (len(temp_list) == len(hum_list) == len(pres_list)):
        print("\nУвага: кількість введених значень для різних показників не збігається!")
        
    data = create_data_dict(temp_list, hum_list, pres_list)
    
    process_measurements("Temperature", data["temperature"], 7)
    process_measurements("Humidity", data["humidity"], 20)
    process_measurements("Pressure", data["pressure"], 5000)

if __name__ == "__main__":
    main()