def format_time(seconds):
    days, remainder = divmod(seconds, 86400)  # 86400 секунд в одному дні
    hours, remainder = divmod(remainder, 3600)  # 3600 секунд в одній годині
    minutes, seconds = divmod(remainder, 60)  # 60 секунд в одній хвилині
    if days == 1:
        day_word = "день"
    elif 2 <= days <= 4:
        day_word = "дні"
    else:
        day_word = "днів"

    formatted_time = f"{days} {day_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"
    return formatted_time

try:
    user_input = int(input("Введіть кількість секунд (від 0 до 8640000): "))
    if 0 <= user_input <= 8640000:
        print(format_time(user_input))
    else:
        print("Помилка: введене число повинно бути в діапазоні від 0 до 8640000.")
except ValueError:
    print("Помилка: введене значення повинно бути цілим числом.")