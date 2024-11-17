# Номер 1.1: Деление чисел, выбрасывает исключение при делении на ноль.
def divide_numbers(a, b):
    if b == 0:
        raise ValueError("Деление на ноль невозможно!")
    return a / b


# Номер 1.2: Проверка, что число положительное, выбрасывает исключение при отрицательном значении.
def validate_positive_number(num):
    if num < 0:
        raise ValueError("Число не должно быть отрицательным!")
    return num


# Номер 2.1: Доступ к элементу списка с обработкой исключения общего типа (Exception).
def safe_list_access(lst, index):
    try:
        return lst[index]
    except Exception as e:
        print(f"Ошибка доступа к списку: {e}")
        return None


# Номер 3.1: Чтение файла с обработчиком исключений общего типа и блоком finally.
def read_file_safe(filepath):
    file = None
    try:
        file = open(filepath, 'r')
        content = file.read()
        return content
    except Exception as e:
        print(f"Ошибка чтения файла: {e}")
        return None
    finally:
        if file:
            file.close()
        print("Файл закрыт.")


# Номер 4.1: Обработка данных с несколькими типами исключений.
def process_data(data, key):
    try:
        value = data[key]
        result = int(value)
        return result
    except KeyError:
        print("Ошибка: Ключ отсутствует в данных.")
    except ValueError:
        print("Ошибка: Значение не может быть преобразовано в число.")
    except TypeError:
        print("Ошибка: Неверный тип данных.")
    finally:
        print("Завершение обработки данных.")


# Номер 5.1: Вычисление скидки с генерацией и обработкой исключений.
def calculate_discount(price, discount):
    try:
        if price < 0 or discount < 0:
            raise ValueError("Цена и скидка не могут быть отрицательными.")
        if discount > 100:
            raise OverflowError("Скидка не может превышать 100%.")
        return price * (1 - discount / 100)
    except ValueError as e:
        print(f"Ошибка значения: {e}")
    except OverflowError as e:
        print(f"Ошибка переполнения: {e}")
    finally:
        print("Попытка расчета скидки завершена.")


# Номер 6.1: Пользовательское исключение: отрицательное число.
class NegativeNumberError(Exception):
    pass


# Номер 6.2: Пользовательское исключение: высокая температура.
class HighTemperatureError(Exception):
    pass


# Номер 6.3: Пользовательское исключение: недопустимая операция.
class InvalidOperationError(Exception):
    pass


# Номер 7.1: Проверка температуры, выбрасывает пользовательское исключение.
def check_temperature(temp):
    try:
        if temp < -50 or temp > 50:
            raise HighTemperatureError("Температура вне допустимого диапазона!")
    except HighTemperatureError as e:
        print(f"Ошибка температуры: {e}")
    finally:
        print("Проверка температуры завершена.")


# Номер 8.1: Демонстрация деления с исключениями.
def demo_divide():
    try:
        print(divide_numbers(10, 0))
    except ValueError as e:
        print(f"Демонстрация исключения: {e}")


# Номер 8.2: Демонстрация проверки положительности числа.
def demo_validate_positive():
    try:
        print(validate_positive_number(-5))
    except ValueError as e:
        print(f"Демонстрация исключения: {e}")


# Номер 8.3: Демонстрация расчета скидки.
def demo_discount():
    calculate_discount(-100, 110)