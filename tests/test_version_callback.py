import pytest
from typer import Exit
from app.callbacks import version_callback


# def test_version_callback(capfd):
#     """
#     Test version callback function with flag provided
#     """
#     # Check that function raises an Exit exception upon completion
#     with pytest.raises(Exit):
#         version_callback(provided=True)

#     # Capture the output
#     captured = capfd.readouterr()

#     # Check if the version was printed correctly
#     assert captured.out.strip() == __version__


def test_version_callback_without_flag(capfd):
    """
    Test version callback function when the version flag is not provided.
    """
    # Ensure function doesn't raise an unexpected Exit exception
    try:
        version_callback(provided=False)
    except Exit:
        pytest.fail("version_callback() raised unexpected Exit")

    # Capture the output
    captured = capfd.readouterr()

    # Check if the version was NOT printed
    assert captured.out.strip() == ""
