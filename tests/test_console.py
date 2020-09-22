"""Test suite for console.py!"""
import click.testing
from click.testing import CliRunner
import pytest
from pytest_mock import MockFixture
from unittest.mock import Mock


from jp_aesthetic_terminal import console


@pytest.fixture
def mock_fancy_print(mocker: MockFixture) -> Mock:
    """Fixture for mocking the fancy print function."""
    mock = mocker.patch("jp_aesthetic_terminal.console.fancy_print")
    mock.return_value = True
    return mock


@pytest.fixture
def runner(mock_fancy_print: Mock, mock_requests_get: Mock) -> CliRunner:
    """Fixture for running command-line interface."""
    return click.testing.CliRunner().invoke(
        console.main, "--iterations 1 --time_to_sleep 0"
    )


def test_main_succeeds(
    runner: CliRunner, mock_requests_get: Mock, mock_fancy_print: Mock
) -> None:
    """It exits with code of 0."""
    result = runner
    assert result.exit_code == 0


def test_main_invokes_requests_get(runner: CliRunner, mock_requests_get: Mock) -> None:
    """It invokes requests get."""
    runner
    assert mock_requests_get.called


def test_main_uses_jp_wikipedia_org(runner: CliRunner, mock_requests_get: Mock) -> None:
    """It calls the Japanese page."""
    runner
    args, _ = mock_requests_get.call_args
    assert "ja.wikipedia.org" in args[0]


def test_main_fails_on_request_error(mock_requests_get: Mock) -> None:
    """It fails on request error."""
    mock_requests_get.side_effect = Exception("Boom")
    result = click.testing.CliRunner().invoke(
        console.main, "--iterations 1 --time_to_sleep 0"
    )
    assert result.exit_code == 1


@pytest.mark.e2e
def test_main_succeeds_in_production_env() -> None:
    """It exits with status code 0 (end-to-end)."""
    result = click.testing.CliRunner().invoke(
        console.main, "--iterations 1 --time_to_sleep 0"
    )
    assert result.exit_code == 0
