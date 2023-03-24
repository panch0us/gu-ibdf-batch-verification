file_name = input('Введите название файла: ')

lico = ''

def split_line(lico, line):
    if len(line.split()) == 1:
        lico += ';'
    if len(line.split()) == 2:
        lico += line.split()[1] + ';'
    if len(line.split()) == 3:
        lico += line.split()[1] + line.split()[1] + ';'
    return lico, line

with open("provereno.txt", "w", encoding='windows-1251') as file_result:
    with open(file_name) as file:
        for line in file:
            print(line)
            if 'Фамилия:' in line:
                lico, line = split_line(lico, line)
            if 'Имя:' in line:
                lico, line = split_line(lico, line)
            if 'Отчество:' in line:
                lico, line = split_line(lico, line)
            if 'Дата рождения:' in line:
                lico += line.split()[2][6:] + ';;' + '\n'

    #print(lico)
    file_result.write(lico)