import subprocess


# Вспомогательная функция для запуска основного скрипта и передачи данных через stdin
def run_main_script(input_data):
    process = subprocess.Popen(
        ['python', 'task4.py'],  # Запуск основного скрипта
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

    # Тест 1: НОД для 2 и 4
    print("\nТест 1: НОД для 2 и 4")
    total_tests += 1
    if check_output("2\n4\n", expected_output="НОД: 2"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 2: НОД для 3 и 9
    print("\nТест 2: НОД для 3 и 9")
    total_tests += 1
    if check_output("3\n9\n", expected_output="НОД: 3"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 3: НОД для 25 и 100
    print("\nТест 3: НОД для 25 и 100")
    total_tests += 1
    if check_output("25\n100\n", expected_output="НОД: 25"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 4: НОД для 8 и 12
    print("\nТест 4: НОД для 8 и 12")
    total_tests += 1
    if check_output("8\n12\n", expected_output="НОД: 4"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 5: НОД для 13 и 7 (простые числа)
    print("\nТест 5: НОД для 13 и 7")
    total_tests += 1
    if check_output("13\n7\n", expected_output="НОД: 1"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 6: НОД для 81 и 27
    print("\nТест 6: НОД для 81 и 27")
    total_tests += 1
    if check_output("81\n27\n", expected_output="НОД: 27"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 7: НОД для 56 и 98
    print("\nТест 7: НОД для 56 и 98")
    total_tests += 1
    if check_output("56\n98\n", expected_output="НОД: 14"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 8: НОД для 144 и 233 (два числа Фибоначчи)
    print("\nТест 8: НОД для 144 и 233")
    total_tests += 1
    if check_output("144\n233\n", expected_output="НОД: 1"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 9: НОД для 2 и 3 (два последовательных простых числа)
    print("\nТест 9: НОД для 2 и 3")
    total_tests += 1
    if check_output("2\n3\n", expected_output="НОД: 1"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 10: НОД для 1000 и 250
    print("\nТест 10: НОД для 1000 и 250")
    total_tests += 1
    if check_output("1000\n250\n", expected_output="НОД: 250"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Итоги
    print(f"\nРезультаты: {tests_passed}/{total_tests} тестов пройдено.")


# Запуск всех тестов
if __name__ == "__main__":
    run_tests()
