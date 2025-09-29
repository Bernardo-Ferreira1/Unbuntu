import subprocess  # Importa o módulo subprocess, usado para executar comandos do sistema operacional

# Executa o comando 'date' no terminal e mostra a data/hora atual
subprocess.run(["date"])

# Executa o comando 'sleep 2', que faz o programa "pausar" por 2 segundos
subprocess.run(["sleep", "2"])

# Executa o comando 'ls this_file_does_not_exist'
# Como esse ficheiro não existe, o comando deve falhar e gerar um código de erro
result = subprocess.run(["ls", "this_file_does_not_exist"])

# Mostra o "return code" (código de saída) do comando anterior.
# returncode = 0 significa que o comando foi bem-sucedido
# qualquer outro número (por ex. 2) indica erro
print(result.returncode)

import subprocess                   # importa o módulo 'subprocess' para executar comandos do sistema

# Executa: host 8.8.8.8
# capture_output=True captura stdout e stderr no objecto result (em bytes).
result = subprocess.run(["host", "8.8.8.8"], capture_output=True)

# Re-executa o mesmo comando (sobrescreve 'result').
# Neste caso vamos imprimir o código de saída do comando.
result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
print(result.returncode)           # imprime o código de saída (0 = sucesso, !=0 = erro)

# Executa novamente e imprime a saída padrão (stdout) tal como foi recebida — em bytes.
result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
print(result.stdout)               # exemplo: b'8.8.8.8.in-addr.arpa domain name pointer dns.google.\n'

# Executa novamente, decodifica stdout de bytes para string e faz split() para obter uma lista de palavras.
result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
print(result.stdout.decode().split())  # ex: ['8.8.8.8.in-addr.arpa', 'domain', 'name', 'pointer', 'dns.google.']

# --- Exemplo com 'rm' (comportamento de erro) ---
               
result = subprocess.run(["rm", "does_not_exist"], capture_output=True)
# tenta remover 'does_not_exist' — o ficheiro não existe, logo o comando falha e o erro fica em result.stderr

result = subprocess.run(["rm", "does_not_exist"], capture_output=True)
print(result.returncode)           # imprime o código de saída do 'rm' (por exemplo 1)
result = subprocess.run(["rm", "does_not_exist"], capture_output=True)
print(result.returncode)           # código de saída (não-zero porque houve erro)
print(result.stdout)               # stdout normalmente vazio (b'')
print(result.stderr)               # stderr contém a mensagem de erro em bytes,
                                   # ex: b"rm: cannot remove 'does_not_exist': No such file or directory\n"
# para ler mensagens em texto: print(result.stderr.decode())

my_env = os.environ.copy()  
# Faz uma cópia das variáveis de ambiente atuais do sistema.
# Isto evita alterar diretamente 'os.environ' global.

my_env["PATH"] = os.pathsep.join(["/opt/myapp/", my_env["PATH"]])  
# Modifica a variável de ambiente PATH.
# - 'os.pathsep' é ':' no Linux/macOS e ';' no Windows.
# - Aqui, adicionamos "/opt/myapp/" no início do PATH,
#   garantindo que o sistema procure executáveis primeiro nessa pasta
#   antes de procurar nas pastas já existentes.

result = subprocess.run(["myapp"], env=my_env)  
# Executa o comando 'myapp' usando o ambiente modificado.
# O parâmetro 'env=my_env' substitui as variáveis de ambiente do processo filho
# pelas que definimos em 'my_env'.
# Se 'myapp' existir em /opt/myapp/, será encontrado e executado.