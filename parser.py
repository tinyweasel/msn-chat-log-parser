"""
Formats MSN chat logs from XML to a more readable text file
"""

import os
from bs4 import BeautifulSoup
import click


@click.command()
@click.option("--input", help="A folder of MSN chat logs in XML format")
@click.option("--output", help="A folder to save the formatted chat log text files")
def parse_chat_logs(input_folder, output_folder):
    """A function that takes a folder of chat logs and formats them for readability.

    Args:
      input_folder: A folder containing XML MSN chat logs.
      output_folder: A folder to contain the output text files. Will be created if not exists.

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
                        user = message.find("user").get("friendlyname")
                        date = message.get("date")
                        time = message.get("time")
                        print(f"{time} {date}\n{user} - {message.get_text()}\n")

                        chat_log_output.write(f"{time} {date}\n")
                        chat_log_output.write(f"{user} - {message.get_text()}\n\n")


if __name__ == "__main__":
    click.echo("Parsing chat logs...")
    parse_chat_logs()  # pylint: disable=no-value-for-parameter
