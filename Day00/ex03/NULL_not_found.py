from types import NoneType


def NULL_not_found(object: any) -> int:
    """
    This Python function checks the type of an object and prints a corresponding message based on the
    type.
    
    :param object: The code you provided is a function called `NULL_not_found` that takes an object as
    input and checks its type to determine a specific string format to print along with the object and
    its type. If the type of the object is not recognized, it prints "Type not Found" and returns 1
    :type object: any
    :return: The function `NULL_not_found` returns an integer value. If the type of the input object is
    recognized and processed within the function, it returns 0. If the type of the input object is not
    found in the defined conditions, it prints "Type not Found" and returns 1.
    """
    str_format = ""

    if isinstance(object, NoneType):
        str_format = "Nothing:"
    elif isinstance(object, float):
        str_format = "Cheese:"
    elif isinstance(object, bool):
        str_format = "Fake:"
    elif isinstance(object, int):
        str_format = "Zero:"
    elif isinstance(object, str) and object == "":
        str_format = "Empty:"
    else:
        print("Type not Found")
        return 1
    
    print(str_format, object, type(object))
    return 0
