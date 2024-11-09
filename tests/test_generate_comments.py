import pytest
from app.core.api import generate_comments


@pytest.fixture
def test_parameters():
    """
    Fixture to provide realistic parameters for the generate_comments function
    """
    file_path = "examples/sample.py"
    content = """
                def generate_fibonacci(limit):
                fibonacci_sequence = [0, 1]
                while True:
                    next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
                    if next_number > limit:
                        break
                    fibonacci_sequence.append(next_number)
                return fibonacci_sequence

                limit = 100
                fibonacci_numbers = generate_fibonacci(limit)
                print(fibonacci_numbers)
                """

    return file_path, content


@pytest.fixture
def mock_openai_client(mocker):
    """
    Fixture to mock the OpenAI client and its responses
    """
    mock_client = mocker.MagicMock()
    mocker.patch("app.core.api.OpenAI", return_value=mock_client)
    return mock_client


##############################################################################


def test_generate_comments_no_api_key(test_parameters):
    """
    Test that the function raises an error if no API key is provided or found
    """
    file_path, content = test_parameters

    with pytest.raises(RuntimeError, match="API key must be provided"):
        generate_comments(file_path, content, None, None, None, None, False)


def test_generate_comments_with_api_key(test_parameters, mocker, mock_openai_client):
    """
    Test that the function generates expected output when valid file path and API key are provided
    """
    file_path, content = test_parameters

    commented_code = """
                    def generate_fibonacci(limit):
                        # Initialize the Fibonacci sequence with the first two numbers
                        fibonacci_sequence = [0, 1]
                        # Generate Fibonacci numbers until the next number exceeds the given limit
                        while True:
                            # Calculate the next number in the sequence
                            next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
                            # Stop generating if the next number exceeds the limit
                            if next_number > limit:
                                break
                            # Append the next number to the sequence
                            fibonacci_sequence.append(next_number)
                        return fibonacci_sequence

                    """

    # Replicate the OpenAI client response structure using mock objects
    mock_response = mocker.MagicMock()
    mock_response.choices = [
        mocker.MagicMock(message=mocker.MagicMock(content=commented_code))
    ]
    # Set the result of the mock chat completion to the mock response
    mock_openai_client.chat.completions.create.return_value = mock_response

    result = generate_comments(
        file_path, content, None, "test_api_key", None, None, False
    )

    assert result == commented_code


def test_generate_comments_api_error(mock_openai_client, test_parameters):
    """
    Test that the function raises a RuntimeError if the API call fails
    """
    file_path, content = test_parameters

    # Simulate an API error
    mock_openai_client.chat.completions.create.side_effect = Exception("Invalid API key")

    with pytest.raises(
        RuntimeError, match="Error occurred while trying to generate comments"
    ):
        generate_comments(file_path, content, None, "invalid_api_key", None, None, False)
