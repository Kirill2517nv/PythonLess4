import subprocess


# Вспомогательная функция для запуска основного скрипта и передачи данных через stdin
def run_main_script(input_data):
    process = subprocess.Popen(
        ['python', 'task8.py'],  # Запуск основного скрипта
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,  # Используем текстовый режим (строки)
        encoding='utf-8'  # Явно указываем кодировку UTF-8
    )

    stdout, stderr = process.communicate(input=input_data)

    if stderr:
        raise Exception(f"Ошибка: {stderr}")

    return stdout.strip()


# Проверка результата на соответствие
def check_output(input_data, expected_output):
    output = run_main_script(input_data)

    if expected_output == output:
        return True
    else:
        print(f"Ожидалось:\n{expected_output}, но получили:\n{output}")
        return False


# Функция для запуска всех тестов
def run_tests():
    tests_passed = 0
    total_tests = 0

    # Тест 1: Разложение 378
    print("\nТест 1: Разложение 378")
    total_tests += 1
    if check_output("378\n", expected_output="2*3*3*3*7"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 2: Разложение 2
    print("\nТест 2: Разложение 2")
    total_tests += 1
    if check_output("2\n", expected_output="2"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 3: Разложение 100
    print("\nТест 3: Разложение 100")
    total_tests += 1
    if check_output("100\n", expected_output="2*2*5*5"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 4: Разложение 7 (простое число)
    print("\nТест 4: Разложение 7")
    total_tests += 1
    if check_output("7\n", expected_output="7"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 5: Разложение 81
    print("\nТест 5: Разложение 81")
    total_tests += 1
    if check_output("81\n", expected_output="3*3*3*3"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 6: Разложение 15
    print("\nТест 6: Разложение 15")
    total_tests += 1
    if check_output("15\n", expected_output="3*5"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 7: Разложение 1000
    print("\nТест 7: Разложение 1000")
    total_tests += 1
    if check_output("1000\n", expected_output="2*2*2*5*5*5"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 8: Разложение 16
    print("\nТест 8: Разложение 16")
    total_tests += 1
    if check_output("16\n", expected_output="2*2*2*2"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 9: Разложение 42
    print("\nТест 9: Разложение 42")
    total_tests += 1
    if check_output("42\n", expected_output="2*3*7"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 10: Разложение 2310
    print("\nТест 10: Разложение 2310")
    total_tests += 1
    if check_output("2310\n", expected_output="2*3*5*7*11"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Итоги
    print(f"\nРезультаты: {tests_passed}/{total_tests} тестов пройдено.")


# Запуск всех тестов
if __name__ == "__main__":
    run_tests()
