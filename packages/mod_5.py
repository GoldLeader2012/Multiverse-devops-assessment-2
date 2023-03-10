# This function validates the third answer field in each row of a list of lists. Any rows with an invalid value are ignored.

def validate_answer_3(data):
    validated_data = []
    for row in data:
        if row[3].isdigit() and 1 <= int(row[3]) <= 10:
            validated_data.append(row)
    return validated_data

