# Задание 1.

# Условие:
# Написать функцию на Python, которой передаются в качестве параметров команда и текст. 
# Функция должна возвращать True, если команда успешно выполнена и текст найден в её выводе 
# и False в противном случае. Передаваться должна только одна строка, разбиение вывода 
# использовать не нужно.

import subprocess
import sys

def find_text(command, text):
    """
    Функция для поиска текста в выводе команды 
    """
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding="utf-8")
    result_out = result.stdout
    if text in result_out:
        print('TRUE')
    else:
        print('FAIL')

if __name__ == '__main__':
    """
    Программа принимает аргументы через командную строку
    example: python3 hw.py 'ls' 'venv'
    Если не будет задан один из параметров, либо NULL
    То в функцию будут переданы следующие параметры:
    command: 'cat /etc/os-release', text: 'jammy'
    """
    try:
        arguments = sys.argv
        command = arguments[1]
        text = arguments[2]
        find_text(command, text)
    except:
        find_text('cat /etc/os-release', 'jammy')