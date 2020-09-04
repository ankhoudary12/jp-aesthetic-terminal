import click.testing
import pytest

from jp_aesthetic_terminal import console


@pytest.fixture
def mock_fancy_print(mocker):
    mock = mocker.patch("jp_aesthetic_terminal.console.fancy_print")
    mock.return_value = True
    return mock


@pytest.fixture
def runner(mock_fancy_print, mock_requests_get):
    return click.testing.CliRunner().invoke(
        console.main, "--iterations 1 --time_to_sleep 0"
    )


def test_main_succeeds(runner, mock_requests_get, mock_fancy_print):
    result = runner
    assert result.exit_code == 0


def test_main_invokes_requests_get(runner, mock_requests_get):
    runner
    assert mock_requests_get.called


def test_main_uses_jp_wikipedia_org(runner, mock_requests_get):
    runner
    args, _ = mock_requests_get.call_args
    assert "ja.wikipedia.org" in args[0]


def test_main_fails_on_request_error(mock_requests_get):
    mock_requests_get.side_effect = Exception("Boom")
    result = click.testing.CliRunner().invoke(
        console.main, "--iterations 1 --time_to_sleep 0"
    )
    assert result.exit_code == 1


@pytest.mark.e2e
def test_main_succeeds_in_production_env():
    result = click.testing.CliRunner().invoke(
        console.main, "--iterations 1 --time_to_sleep 0"
    )
    assert result.exit_code == 0
