import csv as csv

with open('user.csv', newline='') as userfile:
    reader= csv.DictReader(userfile)

    for row in reader:

        email = row(['email'])
        first_name = (row['first_name'])
        gender = row (['ga_gender'])
        print(gender)
    