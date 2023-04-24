import pylambdic
from pydantic import BaseModel
import pytest


class Input(BaseModel):
    name: str
    age: int


class Output(BaseModel):
    message: str


@pytest.fixture
def valid_func():
    @pylambdic.handler
    def my_function(event: Input) -> Output:
        return Output(message=f"Hello, {event.name}!")

    return my_function


def test_handler_with_valid_input(valid_func):

    event = {"name": "John", "age": 30}
    expected_output = {"statusCode": 200, "message": "Hello, John!"}
    assert valid_func(event, None) == expected_output


def test_handler_with_invalid_input(valid_func):
    event = {"name": 123}
    assert valid_func(event, None)["statusCode"] == 400


def test_handler_with_invalid_output(valid_func):
    @pylambdic.handler
    def invalid_output(event: Input) -> Output:
        return {"invalid": "output"}

    event = {"name": "John", "age": 30}
    assert invalid_output(event, None)["statusCode"] == 500


def test_handler_with_missing_return_type_annotation():
    @pylambdic.handler
    def my_function(event: Input):
        return Output(message=f"Hello, {event.name}!")

    event = {"name": "John", "age": 30}
    expected_output = {"statusCode": 200, "body": {"message": "Hello, John!"}}
    assert my_function(event, None) == expected_output


def test_handler_with_missing_input_type_annotation():
    with pytest.raises(
        ValueError, match="Unable to infer input type from function signature"
    ):

        @pylambdic.handler
        def my_function(event):
            return Output(message=f"Hello, {event.name}!")

        event = {"name": "John", "age": 30}
        my_function(event, None)


def test_handler_with_multiple_input_types():
    with pytest.raises(ValueError, match="Only 1 argument allowed"):

        @pylambdic.handler
        def my_function(event: Input, other_event: Input) -> Output:
            return Output(message=f"Hello, {event.name}!")

        event = {"name": "John", "age": 30}
        my_function(event, None)
