file_name = input('Введите название файла: ')

lico = ''

with open("provereno.txt", "w", encoding='windows-1251') as file_result:
    with open(file_name) as file:
        for line in file:
            if 'Фамилия:' in line:
                lico += line.split()[1] + ';'
            if 'Имя:' in line:
                lico += line.split()[1] + ';'
            if 'Отчество:' in line:
                lico += line.split()[1] + ';'
            if 'Дата рождения:' in line:
                lico += line.split()[2][6:] + ';;' + '\n'
    #print(lico)
    file_result.write(lico)
