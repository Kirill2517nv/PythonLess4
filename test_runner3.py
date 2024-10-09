import subprocess


# Вспомогательная функция для запуска основного скрипта и передачи данных через stdin
def run_main_script(input_data):
    process = subprocess.Popen(
        ['python', 'task3.py'],  # Запуск основного скрипта
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

    if output in expected_output:
        return True
    else:
        print(f"Ожидалось:\n{expected_output}, но получили:\n{output}")
        return False


# Функция для запуска всех тестов
def run_tests():
    tests_passed = 0
    total_tests = 0

    # Тест 1: Преобразование 1
    print("\nТест 1: Преобразование 1")
    total_tests += 1
    if check_output("1\n", expected_output="I"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 2: Преобразование 4
    print("\nТест 2: Преобразование 4")
    total_tests += 1
    if check_output("4\n", expected_output="IV"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 3: Преобразование 9
    print("\nТест 3: Преобразование 9")
    total_tests += 1
    if check_output("9\n", expected_output="IX"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 4: Преобразование 58
    print("\nТест 4: Преобразование 58")
    total_tests += 1
    if check_output("58\n", expected_output="LVIII"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 5: Преобразование 199
    print("\nТест 5: Преобразование 199")
    total_tests += 1
    if check_output("199\n", expected_output="CXCIX"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 6: Преобразование 3999
    print("\nТест 6: Преобразование 3999")
    total_tests += 1
    if check_output("3999\n", expected_output="MMMCMXCIX"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 7: Преобразование 2024
    print("\nТест 7: Преобразование 2024")
    total_tests += 1
    if check_output("2024\n", expected_output="MMXXIV"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 8: Преобразование 1000
    print("\nТест 8: Преобразование 1000")
    total_tests += 1
    if check_output("1000\n", expected_output="M"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 9: Преобразование 500
    print("\nТест 9: Преобразование 500")
    total_tests += 1
    if check_output("500\n", expected_output="D"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 10: Преобразование 2000
    print("\nТест 10: Преобразование 2000")
    total_tests += 1
    if check_output("2000\n", expected_output="MM"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Итоги
    print(f"\nРезультаты: {tests_passed}/{total_tests} тестов пройдено.")


# Запуск всех тестов
if __name__ == "__main__":
    run_tests()
