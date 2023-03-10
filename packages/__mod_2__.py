# This function removes duplicates from a list of lists based on the User Id field.


def remove_duplicates(data):
    unique_data = []
    user_ids = set()
    for row in data:
        user_id = row[0]
        if user_id not in user_ids:
            unique_data.append(row)
            user_ids.add(user_id)
    return unique_data
