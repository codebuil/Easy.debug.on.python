returns="\x1bc\x1b[43;30mhello world...\n"


def propertys(func):

    return func


@propertys
def my_function():
    return returns


print(my_function())

