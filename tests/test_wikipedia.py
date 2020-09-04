import click
import pytest

from jp_aesthetic_terminal import wikipedia


def test_random_page_uses_ja_language(mock_requests_get):
    wikipedia.random_page()
    args, _ = mock_requests_get.call_args
    assert "ja.wikipedia.org" in args[0]


# def test_random_page_handles_validation_errors(mock_requests_get):
#     mock_requests_get.return_value.__enter__.return_value.json.return_value = None
#     with pytest.raises(click.ClickException):
#         wikipedia.random_page()
