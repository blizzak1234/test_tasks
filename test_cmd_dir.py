# Тест-кейс №1 'Проверка вывода полных путей файлов и каталогов в указанных каталогах с подкаталогами с помощью команды dir"
# Шаги:
# 1. Запустить командную строку виндоус
# 2. Запустить команду dir с аргументами /s /b <полный путь к каталогу>
# 3. Сравнить полученный результат с действительным наполнением указанного каталога
#
# Ожидаемый результат:
# Результат, полученный через dir совпадает с реальным наполнением указанного каталога

import pytest
from subprocess import getoutput
from pathlib import Path

# получаем список каталогов и файлов командой dir
def get_files_list_from_command(dir_path):
    command = 'dir /s /b ' + dir_path
    output = subprocess.getoutput(command)
    split_out = output.splitlines()
    return split_out

# получаем список каталогов и файлов при помощи библиотеки зфердши
def get_reference_list_using_python(dir_path):
    p = list()
    for filepath in pathlib.Path(dir_path).glob('**/*'):
        p.append(str(filepath.absolute()))
    return p

# указываем тестовые каталоги (тест позволяет использовать несколько каталогов одновременно)
@pytest.mark.parametrize('dir', [
    'D:\\Downloads\\Kasp_test',
])
# тест, сравнивающий результаты, полученные используя разные команды получения каталогов
def test_command(dir):
    command_output = get_files_list_from_command(dir)
    print(command_output)
    python_output = get_reference_list_using_python(dir)
    print(python_output)
    assert command_output == python_output
