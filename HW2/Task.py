# Задание 1.
# Условие:
# Дополнить проект тестами, проверяющими команды вывода списка файлов 
# (l) и разархивирования с путями (x).
# *Задание 2. *
# • Установить пакет для расчёта crc32
# sudo apt install libarchive-zip-perl
# • Доработать проект, добавив тест команды расчёта хеша (h). 
# Проверить, что хеш совпадает с рассчитанным командой crc32.

import Homework
import CRC

falderin = '/home/user/tst'
falderout = '/home/user/out'


def test_1_find_text_in_command():
    '''
    Задание выполненное на семинаре
    '''
    assert Homework.find_text_in_command(f'cd {falderin}; 7z a {falderout}/arh1',
                                   'Everything is Ok'), 'test1 FAIL'


def test_2_find_text_in_command():
    assert Homework.find_text_in_command(f'ls {falderout}',
                                   'arh1.7z'), 'test2 FAIL'


def test_3_find_text_in_command():
    temp = CRC.crc32(f'{falderout}/arh1.7z').lower()
    assert Homework.find_text_in_command(f'crc32 {falderout}/arh1.7z',
                                   temp), 'test3 FAIL'