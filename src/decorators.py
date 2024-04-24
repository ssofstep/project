from datetime import datetime
from functools import wraps
from typing import Any, Callable


def log(filename: str | None = None) -> Callable[[Any], Any]:
    """
    Декоратор, который будет логировать вызов функции и ее результат в файл или в консоль"""

    def wrapper(function: Callable[[Any], Any]) -> Callable[[Any], Any]:
        @wraps(function)
        def inner(*args: Any, **kwargs: Any) -> Any:
            data = str(datetime.now())[:-7]
            if filename:
                with open(filename, "a", encoding="UTF-8") as file:
                    try:
                        result = function(*args, **kwargs)
                    except Exception as error:
                        file.write(
                            f"{data} {function.__name__} error: {type(error).__name__} Inputs: {args}, {kwargs}\n"
                        )
                    else:
                        file.write(f"{data} {function.__name__} ok\n")
                        return result
            else:
                try:
                    result = function(*args, **kwargs)
                except Exception as error:
                    print(f"{data} {function.__name__} error: {type(error).__name__} Inputs: {args}, {kwargs}")
                    return f"{data} {function.__name__} error: {type(error).__name__} Inputs: {args}, {kwargs}"
                else:
                    print(f"{data} {function.__name__} ok")
                    return (result, f"{data} {function.__name__} ok")

        return inner

    return wrapper
