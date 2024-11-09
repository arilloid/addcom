import pytest
from typer import Exit
from app.core.callbacks import version_callback
from app import __version__


def test_version_callback(capfd):
    """
    Test version callback function with flag provided and version set
    """
    # Check that function raises an Exit exception upon completion
    with pytest.raises(Exit):
        version_callback(provided=True)

    # Capture the output
    captured = capfd.readouterr()

    # Check if the version was printed correctly
    assert captured.out.strip() == __version__


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


def test_version_callback_without_version_defined(mocker, capfd):
    """
    Test version callback function when the version is not defined
    """
    mocker.patch("app.core.callbacks.__version__", None)
    with pytest.raises(Exit):
        version_callback(provided=True)

    # Capture the output
    captured = capfd.readouterr()

    # Check that it prints a fallback message instead of the version
    assert "version not defined" in captured.out.strip()
