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
                # Если 3 значения, значит 1 словло "Дата", 2 слово "рождения", 3  слово "**.**.****"
                if len(line.split()) == 3:
                    lico += line.split()[2][6:] + ';;' + '\n'
                # Если 2 значения, значит 1 слово "Дата", 2 слово "рождения", а 3 слово - "дата рождения" не указано
                if len(line.split()) == 2:
                    lico += ';;' + '\n'
                    # Обработка случая, когда не указана дата рождения
                    with open('внимание.txt', 'w', encoding='windows-1251') as file_attension:
                        result = f'У {debug} не указана дата рождения!'
                        file_attension.write(result)

    print(lico)
    file_result.write(lico)