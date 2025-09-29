#!/bin/env/python3        # "shebang": indica ao sistema que o script deve ser executado com Python 3

import sys                # módulo para interagir com argumentos e funções do sistema

logfile = sys.argv[1]     # lê o 1º argumento passado na linha de comando (ex.: ./script.py syslog)
with open(logfile) as f:  # abre o ficheiro em modo leitura
  for line in f:          # percorre cada linha do ficheiro
    print(line.strip())   # imprime a linha, removendo espaços em branco e quebras de linha

logfile = sys.argv[1]      # recebe o nome do ficheiro pela linha de comando
with open(logfile) as f:
  for line in f:
    if "CRON" not in line: # só continua se a linha tiver a palavra "CRON"
      continue             # se não tiver, salta para a próxima linha
    print(line.strip())    # imprime apenas as linhas que contêm "CRON"

pattern = r"USER \((\w+)\)$"   # regex: procura 'USER (nome)' no fim da linha
line = "Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)"
result = re.search(pattern, line)   # aplica a regex à linha
print(result[1])                    # imprime o grupo capturado → 'naughty_user'

logfile = sys.argv[1]      # nome do ficheiro passado na linha de comando (ex.: syslog)
with open(logfile) as f:   # abre o ficheiro
  for line in f:           # percorre linha a linha
    if "CRON" not in line: # ignora linhas que não tenham "CRON"
      continue
    pattern = r"USER \((.+)\)$"   # regex: extrai o que estiver entre 'USER (' e ')'
    result = re.search(pattern, line)
    print(result[1])       # imprime apenas o nome do utilizador encontrado

chmod +x check_cron.py     # dá permissão de execução ao script
./check_cron.py syslog     # executa o script, passando 'syslog' como argumento
