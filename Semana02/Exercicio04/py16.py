import csv

html_output = ''
names = []

with open('patrons.csv', 'r') as data_file:
    csv_data = csv.reader(data_file)

    print(list(csv_data))

import csv

html_output = ''
names = []

with open('patrons.csv', 'r') as data_file:
    csv_data = csv.reader(data_file)

    for line in csv_data:
        print(line)

import csv

html_output = ''
names = []

with open('patrons.csv', 'r') as data_file:
    csv_data = csv.reader(data_file)

    next(csv_data)
    next(csv_data)

    for line in csv_data:
        names.append(f"{line[0]} {line[1]}")

for name in names:
    print(name)

import csv

html_output = ''
names = []

with open('patrons.csv', 'r') as data_file:
    csv_data = csv.reader(data_file)

    next(csv_data)
    next(csv_data)

    for line in csv_data:
        if line[0] == 'No Reward':
            break
        names.append(f"{line[0]} {line[1]}")

html_output += f'<p>There are currently {len(names)} public contributors. Thank you!</p>'
html_output += '\n<ul>'

for name in names:
    html_output += f'\n\t<li>(name)</li>'

print(html_output)

import csv

html_output = ''
names = []

with open('patrons.csv', 'r') as data_file:
    csv_data = csv.DictReader(data_file)

    for item in csv_data:
        print(item)

html_output += f'<p>There are currently {len(names)} public contributors. Thank you!</p>'
html_output += '\n<ul>'

for name in names:
    html_output += f'\n\t<li>(name)</li>'

print(html_output)