import subprocess


# Вспомогательная функция для запуска основного скрипта и передачи данных через stdin
def run_main_script(input_data):
    process = subprocess.Popen(
        ['python', 'task9.py'],  # Запуск основного скрипта
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

    # Тест 1: N = 1 (2^0 = 1)
    print("\nТест 1: N = 1")
    total_tests += 1
    if check_output("1\n", expected_output="YES"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 2: N = 2 (2^1 = 2)
    print("\nТест 2: N = 2")
    total_tests += 1
    if check_output("2\n", expected_output="YES"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 3: N = 3 (не степень двойки)
    print("\nТест 3: N = 3")
    total_tests += 1
    if check_output("3\n", expected_output="NO"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 4: N = 16 (2^4 = 16)
    print("\nТест 4: N = 16")
    total_tests += 1
    if check_output("16\n", expected_output="YES"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 5: N = 31 (не степень двойки)
    print("\nТест 5: N = 31")
    total_tests += 1
    if check_output("31\n", expected_output="NO"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 6: N = 64 (2^6 = 64)
    print("\nТест 6: N = 64")
    total_tests += 1
    if check_output("64\n", expected_output="YES"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 7: N = 100 (не степень двойки)
    print("\nТест 7: N = 100")
    total_tests += 1
    if check_output("100\n", expected_output="NO"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 8: N = 1024 (2^10 = 1024)
    print("\nТест 8: N = 1024")
    total_tests += 1
    if check_output("1024\n", expected_output="YES"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 9: N = 1351
    print("\nТест 9: N = 1351")
    total_tests += 1
    if check_output("1351\n", expected_output="NO"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 10: N = 2048 (2^11 = 2048)
    print("\nТест 10: N = 2048")
    total_tests += 1
    if check_output("2048\n", expected_output="YES"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Итоги
    print(f"\nРезультаты: {tests_passed}/{total_tests} тестов пройдено.")


# Запуск всех тестов
if __name__ == "__main__":
    run_tests()
