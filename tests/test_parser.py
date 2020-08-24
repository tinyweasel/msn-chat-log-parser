from click.testing import CliRunner
from parser import parse_chat_logs

# TODO write better test
def test_parse_chat_logs():
  runner = CliRunner()
  logs = runner.invoke(parse_chat_logs, ['--input=chat-logs', '--output=output-files'])
  assert logs.exit_code == 1
