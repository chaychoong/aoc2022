# get input from file_name and returns a list
def get_input_as_list(file_name) -> list:
    with open(file_name) as f:
        return f.read().splitlines()
