#Read a CSV File
import csv

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    #Print a CSV File
    print(csv_reader)

    for line in csv_reader:
        print(line)
        
    #Skip the First Line
    for line in csv_reader:
        print(line[2])

#Write to a New File
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('new_names.csv', 'w') as new_file:   
        csv_writer = csv.writer(new_file, delimiter='\t')

        for line in csv_reader:
            csv_writer.writerow(line)

#Read a CSV With the Correct Delimiter
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')

    for line in csv_reader:
        print(line)

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter='\t')

    for line in csv_reader:
        print(line)
    
    for line in csv_reader:
        print(line['email'])

#Using the Dictionary Writer
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('new_names.csv', 'w') as new_file:   
        fieldnames = ['first_name', 'last_name', 'email']
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

        csv_writer.writeheader()

        for line in csv_reader:
            csv_writer.writerow(line)

#Removing an Email
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('new_names.csv', 'w') as new_file:   
        fieldnames = ['first_name', 'last_name']
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

        csv_writer.writeheader()

        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line)

    

