from functions import (
    demo_divide,
    demo_validate_positive,
    demo_discount,
    check_temperature,
    process_data,
    read_file_safe,
    safe_list_access
)

if __name__ == "__main__":
    # Номер 9.1: Вызов демонстрационных функций
    print("Демонстрация исключений:")

    demo_divide()
    demo_validate_positive()
    demo_discount()

    print("Пример доступа к элементу списка:")
    print(safe_list_access([1, 2, 3], 5))

    print("Пример чтения файла:")
    print(read_file_safe("nonexistent_file.txt"))

    print("Пример обработки данных:")
    process_data({"a": "10"}, "b")

    print("Пример проверки температуры:")
    check_temperature(100)