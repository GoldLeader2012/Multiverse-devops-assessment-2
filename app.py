from packages.__mod_1__ import read_csv_file
from packages.__mod_2__ import remove_duplicates
from packages.__mod_3__ import capitalize_names
from packages.__mod_4__ import validate_answer_3
from packages.__mod_5__ import write_clean_data
from packages.__mod_6__ import output

data = read_csv_file("results.csv")
no_duplicates_data = remove_duplicates(data)
no_empty_lines_data = no_duplicates_data
capitalized_data = capitalize_names(no_empty_lines_data)
validated_data = validate_answer_3(capitalized_data)
write_clean_data(validated_data)
output(validated_data)
