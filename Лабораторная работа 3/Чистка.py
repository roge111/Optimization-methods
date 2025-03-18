def remove_duplicate_string(input_string):
    # Разделяем строку на две части, если она состоит из двух одинаковых половин
    length = len(input_string)
    half_length = length // 2
    
    # Проверяем, состоит ли строка из двух одинаковых половин
    if length % 2 == 0 and input_string[:half_length] == input_string[half_length:]:
        return input_string[:half_length]  # Возвращаем первую половину
    else:
        return input_string  # Если дубликата нет, возвращаем исходную строку

# Пример использования
f_r = open('Лабораторная работа 3/test.txt', encoding='utf-8')

for input_string  in f_r:

    output_string = remove_duplicate_string(input_string)
    # print("Оригинальная строка:")
    # print(input_string)
    # print("\nСтрока после удаления дубликата:")
    print(output_string)
    