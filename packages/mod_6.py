# This function writes the cleansed data to a new CSV file called clean_results.csv.

def write_clean_data(data):
    with open('clean_results.csv', mode='w') as file:
        for row in data:
            row_str = ','.join(row)
            file.write(row_str + '\n')