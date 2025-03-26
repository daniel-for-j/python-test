from return_sublist import return_sublist

def return_sublist_total(data: dict[str, list[str]] | list[tuple[str, list[str]]], col_name: str) -> float | None:
    # Reuse the previously defined function to get the sublist
    sublist = return_sublist(data, col_name)
    
    # If no sublist found, return None
    if sublist is None:
        return None
    
    # Check if all entries are convertible to float and sum them
    try:
        total = sum(float(value) for value in sublist)
        return total
    except ValueError:
        # If any value can't be converted to float
        return None
data = {'Age': ['23', '45', '30', '28'], 'Name': ['Alice', 'Bob', 'Charlie', 'Diana'], 'Salary': ['5000', '7000', '4500', '6000']}
print(return_sublist_total(data, 'Age'))
