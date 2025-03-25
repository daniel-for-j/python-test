def return_sublist(data: dict[str, list[str]] | list[tuple[str, list[str]]], col_name: str) -> list[str] | None:
    # Check if data is dictionary
    if isinstance(data, dict):
        return data.get(col_name, None)

    # Check if data is list of tuples
    if isinstance(data, list):
        for key, values in data:
            if key == col_name:
                return values
    
    # If not found or wrong type, return None
    return None
