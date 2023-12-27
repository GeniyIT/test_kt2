import csv

def read_csv(file_path):
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]
    return data

csv_file_path = 'your_csv_file.csv'
grades_data = read_csv(csv_file_path)

def calculate_average(data, column_name):
    values = [float(row[column_name]) for row in data]
    average = sum(values) / len(values)
    return average

final_average = calculate_average(grades_data, 'Final')
print(f'Average Final Grade: {final_average}')