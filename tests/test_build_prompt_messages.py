import pytest
from app.core.api import build_prompt_messages


@pytest.fixture
def test_data():
    """
    Fixture to provide the content and context for testing the build_prompt_messages function
    """
    content = """
    def generate_fibonacci(limit):
        fibonacci_sequence = [0, 1]
        while True:
            next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
            if next_number > limit:
                break
            fibonacci_sequence.append(next_number)
        return fibonacci_sequence
    """
    context = """
    def generate_prime_numbers(limit):
    # Initialize an empty list to store prime numbers
    primes = []

    # Iterate over the range from 2 to the given limit
    for num in range(2, limit):
        # Assume the number is prime
        is_prime = True

        # Check if the number is divisible by any number from 2 to (num - 1)
        for i in range(2, num):
            # If the number is divisible, it's not prime
            if num % i == 0:
                is_prime = False
                break

        # If the number is still prime, add it to the list
        if is_prime:
            primes.append(num)

    # Return the list of prime numbers
    return primes
    """
    return content, context


##############################################################################


def test_build_prompt_messages_no_context(test_data):
    """
    Test that the function builds the correct prompt when no context is provided
    """
    content, _ = test_data
    result = build_prompt_messages(content, None)

    # Check the system prompt
    assert result[0]["role"] == "system"
    assert "You are a coding assistant." in result[0]["content"]

    # Check the user content
    assert result[-1]["role"] == "user"
    assert result[-1]["content"] == content


def test_build_prompt_messages_with_context(test_data):
    """
    Test that the function builds the correct prompt when context is provided
    """
    content, context = test_data
    result = build_prompt_messages(content, context)

    # Check the system prompt
    assert result[0]["role"] == "system"
    assert "You are a coding assistant." in result[0]["content"]

    # Check if context is included in the prompt
    assert result[1]["role"] == "user"
    assert f"Example:\n{context}" in result[1]["content"]

    # Check the user message
    assert result[-1]["role"] == "user"
    assert result[-1]["content"] == content


def test_build_prompt_messages_empty_content():
    """
    Test that the function handles empty content string correctly
    """
    with pytest.raises(
        ValueError,
        match="It seems that the specified file is empty, please provide code to comment",
    ):
        build_prompt_messages("", None)
