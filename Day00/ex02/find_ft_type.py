def all_thing_is_obj(object: any) -> int:
    """
    The function `all_thing_is_obj` checks the type of an input object and prints a formatted message
    based on the type.
    
    :param object: The `object` parameter in the `all_thing_is_obj` function can be of any data type.
    The function checks the type of the object and prints a message based on the type of the object. If
    the object is an integer, it prints "Type not found".
    :type object: any
    :return: The function `all_thing_is_obj` will always return the integer value 42.
    """
    str_format = ""

    if isinstance(object, int):
        str_format = "Type not found"
    elif isinstance(object, str) and (object == "Brian" or object == "Toto"):
        str_format = f"{object} is in the kitchen : {type(object)}"
    else:
        str_format = f"{type(object).__name__.title()} : {type(object)}"
    
    print(str_format)
    return 42
