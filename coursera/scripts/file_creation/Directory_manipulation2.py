#A função parent_directory retorna o nome do diretório que está localizado logo acima do diretório de trabalho atual. Lembre-se de que "..." é um alias de caminho relativo que significa "ir até o diretório pai". Preencha as lacunas para concluir essa função.

import os
def parent_directory():
  # Create a relative path to the parent 
  # of the current working directory 
  relative_parent = os.path.join(os.getcwd(), "..")

  # Return the absolute path of the parent directory
  return os.path.abspath(relative_parent)

print(parent_directory())