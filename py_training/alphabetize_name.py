people = [
    ('Joe', 'Biden', 'president@usa.gov'),
    ('Emmanuel', 'Macron', 'president@france.gov'),
    ('Justin', 'Trudeau', 'primeminister@canada.gov'),
    ('Angela', 'Merkel', 'primeminister@germany.gov'),
    ('Jacinda', 'Ardern', 'primeminister@newzealand.gov')
    ]

def alphabetize_name(people):
    for person in sorted(people,key=lambda x: (x[1],x[0])):
        print(f'{person[1]},{person[0]}:{person[2]}')
#---------------------------------------------------------
import operator
def alphabetize_name2(people):
    for person in sorted(people,key=operator.itemgetter(1,0)):
        print(f'{person[1]},{person[0]}:{person[2]}')


alphabetize_name(people)
print('-'*50)
alphabetize_name2(people)