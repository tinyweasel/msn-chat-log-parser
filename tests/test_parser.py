from click.testing import CliRunner
from parser import format_message, parse_chat_logs

# TODO mock Beautiful soup
def test_format_message():
    # message_to_format = "test"
    # formatted_message = format_message(message_to_format)

    # assert formatted_message == "test"
    pass


def test_parse_chat_logs():
    runner = CliRunner()
    logs = runner.invoke(
        parse_chat_logs,
        ["--input-folder=tests/test-logs", "--output-folder=test-output-files", "--print-output"],
    )
    assert logs.exit_code == 0
    assert logs.output == "22:46:40 06/07/2007\nJohn - Hello\n\n22:46:41 06/07/2007\nJeff - I am part of a test\n\nFinished parsing.\n"