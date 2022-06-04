import operator

grades = [
    ('Alice', 'Wooding', 89),
    ('Bob', 'Johnson', 86),
    ('Cindy', 'Letterman', 93),
    ('David', 'Moor', 86),
    ('Eddie', 'Williams', 91)
    ]


def sort_grade(grades):
    grades.sort(key=operator.itemgetter(2),reverse=True)
    output = []
    for first,last,grade in grades:
        output.append(f'{last:12s}{first:10s}{grade:.1f}')
    return '\n'.join(output)

print(sort_grade(grades))

