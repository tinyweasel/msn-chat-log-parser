from bs4 import BeautifulSoup
from click.testing import CliRunner

from parser import format_message, parse_chat_logs


def test_parse_chat_logs_prints_chat_logs_to_console():
    runner = CliRunner()
    logs = runner.invoke(
        parse_chat_logs,
        ["--input-folder=tests/test-logs", "--output-folder=tests/test-output-files", "--print-output"],
    )
    assert logs.exit_code == 0
    assert logs.output == "22:46:40 06/07/2007\nJohn - Hello\n\n22:46:41 06/07/2007\nJeff - I am part of a test\n\nFinished parsing.\n"

def test_parse_chat_logs_does_not_print_logs():
    runner = CliRunner()
    logs = runner.invoke(
        parse_chat_logs,
        ["--input-folder=tests/test-logs", "--output-folder=tests/test-output-files", "--no-print"],
    )
    assert logs.exit_code == 0
    assert logs.output == "Finished parsing.\n"
