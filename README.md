# MSN Chat log parser

MSN Messenger allowed you to download any chat logs you had saved. Unfortunately they came tangled in a mess of XML. This parser uses Beautiful Soup to print them in a more readable manner.

Currently it expects the XML files to be stored in a folder called `chat-logs`.

## Usage

`pipenv run python parser.py --input=<input_folder> --output=<output_folder>`

### TODO

* Add tests
* Add more docstrings