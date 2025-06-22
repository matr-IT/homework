from functools import wraps


def log(filename=None):
    """decorator fo function logging"""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            func_name = func.__name__
            try:
                result = func(*args, **kwargs)
                success_message = f"{func.__name__} ok"

                if filename:
                    with open(filename, "a") as f:
                        f.write(success_message + "\n")
                else:
                    print(success_message)

                return result

            except Exception as e:
                error_message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"

                if filename:
                    with open(filename, "a") as f:
                        f.write(error_message + "\n")
                else:
                    print(error_message)

                raise

        return wrapper

    return decorator

