"""
Formats MSN chat logs from XML to a more readable text file
"""

import os
from typing import IO
from bs4 import BeautifulSoup
import click


def format_message(message: BeautifulSoup) -> str:
    time = message.get("time")
    date = message.get("date")
    user = message.find("user").get("friendlyname")
    return f"{time} {date}\n{user} - {message.get_text()}\n"


@click.command()
@click.option(
    "--input-folder",
    prompt="Input folder",
    help="A folder of MSN chat logs in XML format",
)
@click.option(
    "--output-folder",
    prompt="Output folder (will be created if doesn't exist)",
    help="A folder to save the formatted chat log text files",
)
@click.option(
    "--print-output/--no-print",
    prompt="Print output to console?",
    help="Boolean to select whether chat logs will be printed to console",
    default=False,
)
def parse_chat_logs(input_folder: str, output_folder: str, print_output: bool) -> IO[str]:
    """A function that takes a folder of chat logs and formats them for readability.

    Args:
      input_folder: A folder containing XML MSN chat logs.
      output_folder: A folder to contain the output text files. Will be created if not exists.
      print_output: A boolean to set whether to print output to console.

    Returns:
      A folder of formatted chat logs.

    """
    with os.scandir(input_folder) as chat_log_files:
        for chat_log_file in chat_log_files:
            with open(chat_log_file, "r") as chat_log:
                contents = chat_log.read()
                soup = BeautifulSoup(contents, "html.parser")

                if not os.path.exists(output_folder):
                    os.makedirs(output_folder)
                output_filename = f"{chat_log_file.name}_output.txt"
                with open(
                    os.path.join(output_folder, output_filename), "a"
                ) as chat_log_output:
                    messages = soup.find_all("message")

                    for message in messages:
                        formatted_message = format_message(message)
                        if print_output:
                            print(formatted_message)
                        chat_log_output.write(f"{formatted_message}\n")
    click.echo("Finished parsing.")


if __name__ == "__main__":
    click.echo("Parsing chat logs...")
    parse_chat_logs()  # pylint: disable=no-value-for-parameter
