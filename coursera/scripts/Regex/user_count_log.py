import re              # importa o módulo de expressões regulares (regex)
import sys             # importa o módulo sys para aceder aos argumentos do programa

logfile = sys.argv[1]  # lê o primeiro argumento da linha de comando (nome do ficheiro de log)

usernames = {}         # dicionário vazio para guardar utilizadores e o nº de vezes que aparecem

with open(logfile) as f:        # abre o ficheiro em modo leitura
  for line in f:                # percorre cada linha do ficheiro
    if "CRON" not in line:      # ignora linhas que não contenham "CRON"
      continue

    pattern = r"USER \((\w+)\)$"   # regex para apanhar o nome de utilizador no fim da linha
    result = re.search(pattern, line)  # tenta encontrar correspondência na linha

    if result is None:          # se não encontrou nada, salta para a próxima linha
      continue

    name = result[1]            # extrai o grupo capturado → o nome do utilizador
    # adiciona +1 ao contador desse utilizador no dicionário
    # se ainda não existir, usernames.get(name, 0) devolve 0 como valor inicial
    usernames[name] = usernames.get(name, 0) + 1

print(usernames)   # imprime o dicionário final {utilizador: nº de ocorrências}