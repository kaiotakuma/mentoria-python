import datetime


def calculate_time(function):
    def wrapper(*args, **kwargs):
        initial_time = datetime.datetime.now()
        print(f"Ini: {initial_time}")
        result = function(*args, **kwargs)
        end_time = datetime.datetime.now()
        print(f"End: {end_time}")
        print(f"The execution time was: {end_time - initial_time} s.")
        return result

    return wrapper
