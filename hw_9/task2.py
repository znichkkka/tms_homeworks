import csv

def find_bad_marks(source_file: str) -> None:
    with open(source_file, 'r', encoding='utf-8') as file:
        file_reader: csv.DictReader[str] = csv.DictReader(file, delimiter=',')

        for row in file_reader:
            if int(row['оценка']) < 3:
                print(row['ФИО'])


file_name: str = 'students.csv'
find_bad_marks(file_name)
