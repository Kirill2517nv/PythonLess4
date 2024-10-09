import subprocess


# Вспомогательная функция для запуска основного скрипта и передачи данных через stdin
def run_main_script(input_data):
    process = subprocess.Popen(
        ['python', 'task6.py'],  # Запуск основного скрипта
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,  # Используем текстовый режим (строки)
        encoding='utf-8'  # Явно указываем кодировку UTF-8
    )

    stdout, stderr = process.communicate(input=input_data)

    if stderr:
        raise Exception(f"Ошибка: {stderr}")

    return stdout


# Проверка результата на соответствие
def check_output(input_data, expected_output):
    output = run_main_script(input_data)

    if expected_output in output:
        return True
    else:
        print(f"Ожидалось:\n{expected_output}, но получили:\n{output}")
        return False


# Функция для запуска всех тестов
def run_tests():
    tests_passed = 0
    total_tests = 0

    # Тест 1: Сокращение дроби 8/4
    print("\nТест 1: Сокращение дроби 8/4")
    total_tests += 1
    if check_output("8\n4\n", expected_output="2 1"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 2: Сокращение дроби 6/9
    print("\nТест 2: Сокращение дроби 6/9")
    total_tests += 1
    if check_output("6\n9\n", expected_output="2 3"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 3: Сокращение дроби 10/100
    print("\nТест 3: Сокращение дроби 10/100")
    total_tests += 1
    if check_output("10\n100\n", expected_output="1 10"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 4: Сокращение дроби 24/36
    print("\nТест 4: Сокращение дроби 24/36")
    total_tests += 1
    if check_output("24\n36\n", expected_output="2 3"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 5: Сокращение дроби 7/13 (простая дробь)
    print("\nТест 5: Сокращение дроби 7/13")
    total_tests += 1
    if check_output("7\n13\n", expected_output="7 13"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 6: Сокращение дроби 1/1
    print("\nТест 6: Сокращение дроби 1/1")
    total_tests += 1
    if check_output("1\n1\n", expected_output="1 1"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 7: Сокращение дроби 100/200
    print("\nТест 7: Сокращение дроби 100/200")
    total_tests += 1
    if check_output("100\n200\n", expected_output="1 2"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 8: Сокращение дроби 11/121
    print("\nТест 8: Сокращение дроби 11/121")
    total_tests += 1
    if check_output("11\n121\n", expected_output="1 11"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 9: Сокращение дроби 9/27
    print("\nТест 9: Сокращение дроби 9/27")
    total_tests += 1
    if check_output("9\n27\n", expected_output="1 3"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 10: Сокращение дроби 81/243
    print("\nТест 10: Сокращение дроби 81/243")
    total_tests += 1
    if check_output("81\n243\n", expected_output="1 3"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Итоги
    print(f"\nРезультаты: {tests_passed}/{total_tests} тестов пройдено.")


# Запуск всех тестов
if __name__ == "__main__":
    run_tests()
