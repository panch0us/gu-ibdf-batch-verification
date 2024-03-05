import os

# Если файл есть в дирректории с программой - удаляем" (файл хранит ошибки от предыдущего запуска программы)
try:
    os.remove('внимание.txt')
except OSError:
    pass

file_name = input('Введите название файла: ')

lico = ''

def split_line(lico, line):
    if len(line.split()) == 1:
        lico += ';'
    if len(line.split()) == 2:
        lico += line.split()[1] + ';'
    if len(line.split()) == 3:
        lico += line.split()[1] + ' ' + line.split()[2] + ';'
    if len(line.split()) == 4:
        lico += line.split()[1] + ' ' + line.split()[2] + ' ' + line.split()[3] + ';'
    return lico, line

def attension(message: str) -> None:
    """Возращает информацию в файле для пользователя об отсутствии Ф, И, О или Даты рождения"""
    with open('внимание.txt', 'a', encoding='windows-1251') as file_attension:
        file_attension.write(f'{debug} - {message}\n')


with open("provereno.txt", "w", encoding='windows-1251') as file_result:
    with open(file_name) as file:
        for line in file:
            print(line)
            if 'Фамилия:' in line:
                lico, line = split_line(lico, line)
                # Запоминаем фамилию для её отображения на случай ошибки
                debug = line.split()[1]
            if 'Имя:' in line:
                lico, line = split_line(lico, line)
            if 'Отчество:' in line:
                lico, line = split_line(lico, line)
            if 'Дата рождения:' in line:
                # Ожидаем, что первое слово "Дата", второе слово "рождения", третье  слово "ДД.ММ.ГГГГ"
                # и что год рождения == 4 символам
                if len(line.split()) == 3 and len(line.split()[2][6:]) == 4:
                    lico += line.split()[2][6:] + ';;' + '\n'
                else:
                    lico += ';;' + '\n'
                    attension('неверная дата рождения!\n')

    #print(lico)
    file_result.write(lico)