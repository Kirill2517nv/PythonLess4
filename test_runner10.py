import subprocess


# Вспомогательная функция для запуска основного скрипта и передачи данных через stdin
def run_main_script(input_data):
    process = subprocess.Popen(
        ['python', 'task10.py'],  # Запуск основного скрипта
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

    if expected_output in output:
        return True
    else:
        print(f"Ожидалось:\n{expected_output}, но получили:\n{output}")
        return False


# Функция для запуска всех тестов
def run_tests():
    tests_passed = 0
    total_tests = 0

    # Тест 1: Перевод из двоичной в десятичную (1010 -> 10)
    print("\nТест 1: 1010 (2) -> 10 (10)")
    total_tests += 1
    if check_output("1010\n2\n10\n",
                    expected_output="10"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 2: Перевод из десятичной в двоичную (10 -> 1010)
    print("\nТест 2: 10 (10) -> 1010 (2)")
    total_tests += 1
    if check_output("10\n10\n2\n",
                    expected_output="1010"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 3: Перевод из десятичной в шестнадцатеричную (255 -> FF)
    print("\nТест 3: 255 (10) -> FF (16)")
    total_tests += 1
    if check_output("255\n10\n16\n",
                    expected_output="FF"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 4: Перевод из шестнадцатеричной в десятичную (FF -> 255)
    print("\nТест 4: FF (16) -> 255 (10)")
    total_tests += 1
    if check_output("FF\n16\n10\n",
                    expected_output="255"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 5: Перевод из восьмеричной в десятичную (77 -> 63)
    print("\nТест 5: 77 (8) -> 63 (10)")
    total_tests += 1
    if check_output("77\n8\n10\n",
                    expected_output="63"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 6: Перевод из десятичной в восьмеричную (63 -> 77)
    print("\nТест 6: 63 (10) -> 77 (8)")
    total_tests += 1
    if check_output("63\n10\n8\n",
                    expected_output="77"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 7: Перевод из двоичной в шестнадцатеричную (10111011 -> BB)
    print("\nТест 7: 10111011 (2) -> BB (16)")
    total_tests += 1
    if check_output("10111011\n2\n16\n",
                    expected_output="BB"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 8: Перевод из шестнадцатеричной в двоичную (BB -> 10111011)
    print("\nТест 8: BB (16) -> 10111011 (2)")
    total_tests += 1
    if check_output("BB\n16\n2\n",
                    expected_output="10111011"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 9: Перевод из шестнадцатеричной в восьмеричную (1F -> 37)
    print("\nТест 9: 1F (16) -> 37 (8)")
    total_tests += 1
    if check_output("1F\n16\n8\n",
                    expected_output="37"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 10: Перевод из восьмеричной в шестнадцатеричную (37 -> 1F)
    print("\nТест 10: 37 (8) -> 1F (16)")
    total_tests += 1
    if check_output("37\n8\n16\n",
                    expected_output="1F"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 11: Перевод из троичной в десятеричную (120 -> 15)
    print("\nТест 11: 120 (3) -> 15 (10)")
    total_tests += 1
    if check_output("120\n3\n10\n",
                    expected_output="15"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Итоги
    print(f"\nРезультаты: {tests_passed}/{total_tests} тестов пройдено.")


# Запуск всех тестов
if __name__ == "__main__":
    run_tests()
