# Multiverse-devops-assessment-2
App.py Notes:
1. Read the data from the original CSV file using read_csv_file.
2. Remove any duplicate entries from the data using remove_duplicates.
3. Ignore any empty lines in the data using ignore_empty_lines.
4. Capitalize the first name and last name fields in the data using capitalize_names.
5. Validate the third answer field in the data using validate_answer_3.
6. Write the cleaned data to a new CSV file using write_clean_data.
7. Output the cleaned data to the command line using output.


Mod 1 notes: 
This function opens the file at the given path and reads it line by line. Each line is stripped of leading and trailing whitespace, split by comma delimiter, and then appended to the data list as a new inner list. Finally, the function returns the data list.


Mod 2 notes: 
This function takes a list of lists as input, where each inner list represents a row of data. It creates a new list unique_data to hold the unique rows, and a set user_ids to keep track of which User Ids have already been seen. It then loops through each row of the input data and checks if its User Id has already been seen. If not, it appends the row to the unique_data list and adds the User Id to the user_ids set. Finally, it returns the unique_data list.


Mod 3 notes:
This function is similar to the one I provided earlier for reading a CSV file, but it also checks if each line is empty before attempting to split it into a list. If the line is not empty, it proceeds as before to split the line into a list of values and append it to the data list.


Mod 4 notes: 
This function takes a list of lists as input, where each inner list represents a row of data. It creates a new list capitalized_data to hold the capitalized rows, and then loops through each row of the input data. For each row, it creates a new list capitalized_row with the first_name and last_name fields capitalized using the capitalize() method of strings. It then appends the capitalized_row to the capitalized_data list. Finally, it returns the capitalized_data list.


Mod 5 notes: 
This function takes a list of lists as input, where each inner list represents a row of data. It creates a new list validated_data to hold the validated rows, and then loops through each row of the input data. For each row, it checks if the third field is a digit using the isdigit() method of strings, and if it is, it checks if the value is between 1 and 10 using an if statement. If the value is valid, it appends the entire row to the validated_data list. If the value is invalid, it skips the row.

To use this function, first call the read_csv_file() function from Ticket #1 to read in the CSV file and create a list of lists. Then call the capitalize_names() function from Ticket #4 to capitalize the first_name and last_name fields in each row. Finally, call the validate_answer_3() function with the resulting list of lists as the argument. For example:


Mod 6 notes: 
This function takes the cleansed data as input, which is a list of lists where each inner list represents a row of data. It then opens a new file called 'clean_results.csv' in write mode using the open() function with the 'w' mode argument. It then loops through each row in the data, converts it to a string using the join() method of strings with ',' as the delimiter, and writes the resulting string to the file followed by a newline character.

To use this function, call the read_csv_file() function from Ticket #1 to read in the CSV file and create a list of lists. Then call the remove_duplicates() function from Ticket #2 to remove any duplicate entries. Next, call the ignore_empty_lines() function from Ticket #3 to ignore any empty lines. Then call the capitalize_names() function from Ticket #4 to capitalize the first_name and last_name fields in each row. Finally, call the validate_answer_3() function from Ticket #5 to validate the third answer field, and pass the resulting list of lists to the write_clean_data() function to output it to a new CSV file:


Mod 7 notes:
This code checks that the row has a length of 4 (which includes the valid answer 3), that the answer is a digit, and that the answer is within the valid range of 1 to 10. If these conditions are all met, the row is outputted with capitalized first and last names.