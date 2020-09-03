# MSN Chat log parser

This parser uses Beautiful Soup to convert MSN Messenger chat logs from XML to a more readable text file.
If the input and output folder and print boolean aren't set, it will prompt the user to enter them.

## Usage

### To print chat logs to console
`pipenv run python parser.py --input-folder=<input_folder> --output-folder=<output_folder> --print-output`


### To output formatted text files without printing to console

`pipenv run python parser.py --input-folder=<input_folder> --output-folder=<output_folder> --no-print`

### To run tests

`pipenv run pytest`

#### TODO

* Create functions to read/write to file
