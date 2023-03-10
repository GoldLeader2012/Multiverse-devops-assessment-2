# Open the clean_results.csv file for reading
def output():
    with open('clean_results.csv', 'r') as f:
        lines = f.readlines()
        # Output the header row
        header = lines[0].strip().split(',')
        print('{:<10} {:<15} {:<15} {:<15}'.format(*header))
        # Output the data rows
        for line in lines[1:]:
            row = line.strip().split(',')
            if len(row) == 4 and row[3].isdigit() and 1 <= int(row[3]) <= 10:  # Only output valid rows
                user_id, first_name, last_name, answer = row
                print('{:<10} {:<15} {:<15} {:<15}'.format(user_id, first_name.capitalize(), last_name.capitalize(), answer))

                