from src.decorators import log


@log(filename="file_log.txt")
def file_success(a, b):
    return a + b

@log(filename="file_log.txt")
def file_error(a, b):
    raise ValueError("Test error")

@log()
def console_success(x, y):
    return x * y

@log()
def console_error():
    raise TypeError("Console error")