import pytest
import os
from unittest.mock import mock_open, patch
from app.file_operations import read_toml, find_toml, get_config


def test_read_toml_good():
    toml_content = b"""
    fake_api_key = "abcdefg12345678"
    fake_model_name = "seneca-ai"
    """

    with patch("builtins.open", mock_open(read_data=toml_content)):
        result = read_toml("good.toml")

        assert result == {
            "fake_api_key": "abcdefg12345678",
            "fake_model_name": "seneca-ai",
        }


def test_read_toml_raises_ioerror():
    with patch("builtins.open", mock_open()) as mock_file:
        mock_file.side_effect = IOError("File not found")

        with pytest.raises(RuntimeError, match="Error reading TOML file"):
            read_toml("non_existent_file.toml")


def test_find_toml_found():
    with patch("os.path.expanduser", return_value="/mock/home/dir"):
        with patch("os.listdir", return_value=["addcom_config.toml", "other_file.txt"]):
            result = find_toml()
            expected_path = os.path.join("/mock/home/dir", "addcom_config.toml")
            assert result == expected_path


def test_find_toml_not_found():
    with patch("os.path.expanduser", return_value="/mock/home/dir"):
        with patch("os.listdir", return_value=["other_file.txt", "another_file.txt"]):
            result = find_toml()
            assert result is None


def test_get_config_with_valid_toml():
    with patch("app.file_operations.find_toml", return_value="valid_toml_path.toml"):
        mock_toml_data = {
            "fake_api_key": "abcdefg12345678",
            "fake_model_name": "seneca-ai",
        }
        with patch("app.file_operations.read_toml", return_value=mock_toml_data):
            result = get_config()

            assert result == mock_toml_data


def test_get_config_with_no_toml():
    with patch("app.file_operations.find_toml", return_value=None):
        result = get_config()

        assert result is None
