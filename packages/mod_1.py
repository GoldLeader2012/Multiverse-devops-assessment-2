# This function reads data from a CSV file and returns a list of lists, where each inner list represents a row in the CSV file.

def read_csv_file(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            row = line.strip().split(',')
            data.append(row)
    return data