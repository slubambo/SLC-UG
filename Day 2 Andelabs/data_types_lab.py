def data_types_lab(single_argument):
    if isinstance(single_argument, str):
        return len(single_argument)
    elif isinstance(single_argument, type(None)):
        return "No Value"
    elif isinstance(single_argument, bool):
        return single_argument
    elif isinstance(single_argument, int):
        if single_argument < 100 : return "less than 100"
        elif single_argument > 100 : return "more than 100"
        elif single_argument == 100 : return "equal to 100"
    elif isinstance(single_argument, list):
        if len(single_argument) >= 3:
            return single_argument[2]
        else: return None
