#A função file_date cria um novo arquivo no diretório de trabalho atual, verifica a data em que o arquivo foi modificado e retorna apenas a parte da data do registro de data e hora no formato aaaa-mm-dd. Preencha as lacunas para criar um arquivo chamado "newfile.txt" e verifique a data em que ele foi modificado.

import os
import datetime

def file_date(filename):
  # Create the file in the current directory
  with open(filename,"w") as file:
    pass
  timestamp = os.path.getmtime(filename)
  # Convert the timestamp into a readable format, then into a string
  timestamp=datetime.datetime.fromtimestamp(timestamp)
  # Return just the date portion 
  # Hint: how many characters are in “yyyy-mm-dd”? 
  return ("{}".format(timestamp))

print(file_date("newfile.txt")) 
# Should be today's date in the format of yyyy-mm-dd