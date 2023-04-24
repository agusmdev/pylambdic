import inspect
from typing import Any, Callable, get_type_hints
from pydantic import ValidationError
from functools import wraps


def handler(func: Callable[..., Any]) -> Callable[..., Any]:
    f_signature = inspect.signature(func).parameters
    type_hints = get_type_hints(func)
    input_type = None
    output_type = type_hints.pop("return", None)
    has_context = "context" in f_signature
    type_hints.pop("context", None)

    if len(type_hints) > 1:
        raise ValueError(
            f"Only 1 argument allowed (without including context), you gave {len(type_hints)} arguments"
        )

    try:
        input_type = list(type_hints.values())[0]
    except IndexError:
        raise ValueError("Unable to infer input type from function signature")

    @wraps(func)
    def wrapper(event: dict, context: Any) -> dict:
        try:
            input_data = input_type(**event)
        except ValidationError as exc:
            return {"statusCode": 400, "body": f"Invalid input: {exc}"}

        if has_context:
            output_data = func(input_data, context)
        else:
            output_data = func(input_data)

        if not output_type:
            return {"statusCode": 200, "body": output_data}

        try:
            response_body = (
                output_type(**output_data).dict()
                if not isinstance(output_data, output_type)
                else output_data.dict()
            )
        except ValidationError as exc:
            return {"statusCode": 500, "body": f"Invalid output: {exc}"}

        return {"statusCode": 200, **response_body}

    return wrapper
