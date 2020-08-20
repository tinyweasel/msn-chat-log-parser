import os
from bs4 import BeautifulSoup

chat_log_folder = 'chat-logs'
output_folder = 'output-files'

with os.scandir(chat_log_folder) as chat_log_files:
  for chat_log_file in chat_log_files:
    with open(chat_log_file, 'r') as chat_log:
      contents = chat_log.read()
      soup = BeautifulSoup(contents, 'html.parser')

      if not os.path.exists(output_folder):
        os.makedirs(output_folder)
      output_filename = f'{chat_log_file.name}_output.txt'
      with open(os.path.join(output_folder, output_filename), 'a') as chat_log_output:
        messages = soup.find_all('message')

        for message in messages:
          user = message.find('user').get('friendlyname')
          date = message.get('date')
          time = message.get('time')
          print(f'{time} {date}\n{user} - {message.get_text()}\n')

          chat_log_output.write(f'{time} {date}\n')
          chat_log_output.write(f'{user} - {message.get_text()}\n\n')