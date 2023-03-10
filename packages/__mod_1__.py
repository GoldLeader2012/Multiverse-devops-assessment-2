#     This function reads data from a CSV file and returns a list of lists, where each inner list represents a row in the CSV file. Empty lines are ignored.


def read_csv_file(file_path):
    data = []
    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                row = line.split(",")
                data.append(row)
    return data
