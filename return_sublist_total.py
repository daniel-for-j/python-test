import return_sublist

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
