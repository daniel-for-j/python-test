file_path = input("Type in File Path:")
def load_data_as_dict(file_path):
    data_dict = {}
    current_column = None

    file = open(file_path, 'r')
    for line in file:
        line = line.strip()
        if not line:
            continue
        if line.startswith('COLUMN'):
            # Extract column name after 'COLUMN'
            current_column = line.split(' ', 1)[1]
            data_dict[current_column] = []
        elif line == 'END':
            break
        else:
            if current_column:
                data_dict[current_column].append(line)
    return data_dict

   