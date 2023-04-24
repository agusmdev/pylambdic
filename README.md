# pylambdic

pylambdic is a Python package that simplifies the process of validating input and output for AWS Lambda handlers using Pydantic. It automatically validates the input and output types of your Lambda function using Pydantic models, making it easier to ensure your function is working with the correct data.

## Features

- Automatic input and output validation using Pydantic models.
- Simplified error handling for invalid input and output data.
- Support for AWS Lambda context object.
- Easy integration with existing AWS Lambda functions.

## Installation

Install pylambdic using pip:

```bash
pip install pylambdic
```

## Usage

To use pylambdic, simply import the `handler` decorator and apply it to your AWS Lambda function. You should also define your input and output types using Pydantic models.

Here's an example of how to use pylambdic:

```python
from pydantic import BaseModel
import pylambdic

class InputModel(BaseModel):
    name: str
    age: int

class OutputModel(BaseModel):
    message: str

@pylambdic.handler
def my_lambda_handler(input_data: InputModel) -> OutputModel:
    return OutputModel(message=f"Hello {input_data.name}, you are {input_data.age} years old.")
```

In this example, the `my_lambda_handler` function expects an input event with `name` and `age` fields, and returns a response with a `message` field. pylambdic will automatically validate the input and output data against the `InputModel` and `OutputModel` Pydantic models.

If the input data is invalid, the Lambda function will return a 400 status code with a descriptive error message. If the output data is invalid, it will return a 500 status code with a descriptive error message.

You can also use the context object provided by AWS as follows:

```python

from pydantic import BaseModel
import pylambdic

class InputModel(BaseModel):
    name: str
    age: int

class OutputModel(BaseModel):
    message: str
    request_id: str

@pylambdic.handler
def my_lambda_handler(input_data: InputModel, context) -> OutputModel:
    message = f"Hello {input_data.name}, you are {input_data.age} years old."
    request_id = context.aws_request_id
    return OutputModel(message=message, request_id=request_id)
```


## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests for consideration.