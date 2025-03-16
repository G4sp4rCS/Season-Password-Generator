# Season password wordlist generator
'''
La idea es la siguiente: Tenemos todas las estaciones en inglés'
winter fall spring summer
tenemos caracteres especiales: !@#$%^%*   '
Tenemos los años que queremos poner en la lista desde el que vos desees hasta el que vos desees'
'entonces la idea sería armar un script para usar así: python3 generate 2020 2025'
y que te genere: winter2020 Winter2020 Winter2020! Winter2020@ y va iterando con todas las combinaciones posibles''
'''''

import sys

def generate_passwords(yearInit, yearEnd):
    seasons = ['winter', 'fall', 'spring', 'summer']
    special_chars = ['!', '@', '#', '$', '%', '^', '&', '*']
    years = list(range(yearInit, yearEnd + 1))

    for season in seasons:
        for year in years:
            for special_char in special_chars:
                print(f'{season}{year}')
                print(f'{season}{year}{special_char}')
                print(f'{season.capitalize()}{year}')
                print(f'{season.capitalize()}{year}{special_char}')

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python3 generate.py <year_init> <year_end>')
        sys.exit(1)

    yearInit = int(sys.argv[1])
    yearEnd = int(sys.argv[2])

    generate_passwords(yearInit, yearEnd)
    # Guardar archivo en un txt en el directorio actual
    # python3 generate.py 2020 2025 > passwords.txt