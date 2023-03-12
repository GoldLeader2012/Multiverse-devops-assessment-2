"""
Brief explanation of each function:

read_csv(file_path):
This function takes a file path as input and reads the file using the 'open()' function. It reads each line in the file and strips the newline character. If the line is not an empty string, it splits the line by comma and appends the resulting list to the data list. Finally, it returns the data list.

remove_duplicates(data):
This function takes a list of lists as input and removes duplicate rows based on the first column. It creates a set of user_ids to keep track of the unique user IDs and appends the rows to the unique_data list only if the user ID is not in the set.

clean_data(data):
This function takes a list of lists as input and performs data cleaning. It loops through each row and capitalizes the second and third columns. It also converts the fifth column to an integer and appends the row to the cleaned_data list if the value is between 1 and 10. If there is an error while converting the fifth column to an integer, it continues to the next row.

write_csv(file_path, data):
This function takes a file path and a list of lists as input and writes the cleaned data to a new CSV file. It opens the file in write mode and loops through each row in the data list. It joins the row using a comma delimiter and writes the resulting string to the file, followed by a newline character.

Overall, the code reads a CSV file, removes duplicates, cleans the data, and writes the cleaned data to a new CSV file.

"""

def read_csv(file_path):
    data = []
    with open(file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            if line.strip() != "":
                data.append(line.strip().split(","))
    return data


def remove_duplicates(data):
    unique_data = []
    user_ids = set()
    for row in data:
        if row[0] not in user_ids:
            unique_data.append(row)
            user_ids.add(row[0])
    return unique_data


def clean_data(data):
    cleaned_data = []
    for row in data:
        try:
            row[2] = row[2].capitalize()
            row[1] = row[1].capitalize()
            answer_3 = int(row[5])
            if answer_3 >= 1 and answer_3 <= 10:
                cleaned_data.append(row)
        except ValueError:
            continue
    return cleaned_data


def write_csv(file_path, data):
    with open(file_path, "w") as file:
        for row in data:
            file.write(",".join(row) + "\n")

