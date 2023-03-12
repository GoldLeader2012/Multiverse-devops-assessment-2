"""
The code imports the four functions from a module called __modules__ located in the packages directory. It then sets the input file path to "results.csv" and the output file path to "clean_results.csv".

The read_csv() function is called with the input file path, which returns the data as a list of lists. The remove_duplicates() function is then called with the data, which removes duplicate rows based on the first column. The resulting unique data is stored in a variable called unique_data.

The clean_data() function is called with the unique data, which performs data cleaning by capitalizing the names in the second and third columns and filtering answer 3 to be between 1 and 10. The resulting cleaned data is stored in a variable called cleaned_data.

The write_csv() function is then called with the output file path and the cleaned data, which writes the cleaned data to a new CSV file.

Finally, the code opens the output file and reads each line, printing it to the console without the newline character. This allows us to see the cleaned data in a human-readable format.

Overall, the code reads a CSV file, removes duplicates, cleans the data, writes the cleaned data to a new CSV file, and prints the cleaned data to the console.
"""

from packages.__modules__ import read_csv, remove_duplicates, clean_data, write_csv


# Set the input and output file paths
input_file = "results.csv"
output_file = "clean_results.csv"

# Read in the data from the input file
data = read_csv(input_file)

# Remove duplicates from the data
unique_data = remove_duplicates(data)

# Clean the data by capitalizing names and filtering answer 3 to be between 1 and 10
cleaned_data = clean_data(unique_data)

# Write the cleaned data to the output file
write_csv(output_file, cleaned_data)

# Print out the cleaned data to the console
with open(output_file, "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())