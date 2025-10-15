#A função create_python_script cria um novo script Python no diretório de trabalho atual, adiciona a linha de comentários declarada pela variável 'comments' e retorna o tamanho do novo arquivo. Preencha as lacunas para criar um script chamado "program.py".

def create_python_script(filename):
  comments = "# Start of a new Python program"
  with open("filename","w") as filee:
    filesize = filee.write(comments)
  return(filesize)

print(create_python_script("program.py"))