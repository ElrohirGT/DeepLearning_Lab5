import warnings

def new_representation(num):
    try:
        num = float(num)
        hex_repr = float.hex(num)
    except ValueError:
        raise ValueError("Invalid input. Please provide a valid floating-point number.")
    return hex_repr

def hex_to_float(hex_str):
    return float.fromhex(hex_str)

def compare_numbers(num1_hex, operator_hex, num2_hex):
    operators = {
        "3c": "<",
        "3e": ">",
        "3c3d": "<=",
        "3e3d": ">=",
        "3d3d": "==",
        "213d": "!="
    }

    try:
        num1 = hex_to_float(num1_hex)
        num2 = hex_to_float(num2_hex)
        operator = operators.get(operator_hex)
        if not operator:
            raise ValueError("Invalid operator. Supported operators are: '<', '>', '<=', '>=', '==', '!='")
    except ValueError:
        raise ValueError("Invalid input. Please provide valid numbers.")

    return eval(f"{num1} {operator} {num2}")
    
def calculate_coincidences_percentage(list1, list2):

    if len(list1) != len(list2):
        warnings.warn("List are of different size.", UserWarning)
        #    raise ValueError("Both lists should have the same length.")
        
    max_length = max(len(list1), len(list2))
    dummy_word = None
    
    if len(list1) < max_length:
        list1 = list1 + [dummy_word] * (max_length - len(list1))
    if len(list2) < max_length:
        list2 = list2 + [dummy_word] * (max_length - len(list2))

    total_elements = len(list1)
    coincidences = sum(1 for x, y in zip(list1, list2) if x == y)
    percentage = (coincidences / total_elements) * 100

    return percentage

def compare_lists_by_percentage(list1, list2, min_percentage):
    percentage_coincidences = calculate_coincidences_percentage(list1, list2)
    return percentage_coincidences >= min_percentage
