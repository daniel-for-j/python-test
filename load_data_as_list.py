file_path = input("Type in File Path:")
def load_data_as_tuples(file_path):
    result = []
    current_column = None
    current_values = []

    file = open(file_path, 'r') 
    for line in file:
        line = line.strip()
        if not line:
            continue
        if line.startswith('COLUMN'):
            if current_column is not None:
                result.append((current_column, current_values))
            current_column = line.split(' ', 1)[1]
            current_values = []
        elif line == 'END':
            if current_column is not None:
                result.append((current_column, current_values))
            break
        else:
            if current_column:
                current_values.append(line)


