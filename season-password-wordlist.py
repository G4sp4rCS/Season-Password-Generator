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

def generate_passwords_with_months(yearInit, yearEnd):
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    special_chars = ['!', '@', '#', '$', '%', '^', '&', '*']
    years = list(range(yearInit, yearEnd + 1))
    for month in months:
        for year in years:
            for special_char in special_chars:
                print(f'{month}{year}')
                print(f'{month}{year}{special_char}')
                print(f'{month.capitalize()}{year}')
                print(f'{month.capitalize()}{year}{special_char}')


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Usage: python3 script.py yearInit yearEnd seasons-or-months')
        sys.exit(1)
    yearInit = int(sys.argv[1])
    yearEnd = int(sys.argv[2])
    seasons_or_months = sys.argv[3]
    if seasons_or_months == 'seasons':
        generate_passwords(yearInit, yearEnd)
    elif seasons_or_months == 'months':
        generate_passwords_with_months(yearInit, yearEnd)
    else:
        print('Invalid option')
        sys.exit(1)