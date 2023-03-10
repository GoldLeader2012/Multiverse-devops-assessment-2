#    This function capitalizes the first_name and last_name fields in each row of a list of lists.

def capitalize_names(data):
    capitalized_data = []
    for row in data:
        capitalized_row = [row[0].capitalize(), row[1].capitalize(), row[2]]
        capitalized_data.append(capitalized_row)
    return capitalized_data