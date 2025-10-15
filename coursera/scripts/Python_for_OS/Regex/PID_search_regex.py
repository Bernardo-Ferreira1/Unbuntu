#!/usr/bin/env python3

import re

# String de log com um número dentro de colchetes
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"

# Regex explicado:
# \[    → colchete de abertura literal "["
# (\d+) → grupo de captura:
#           \d → dígito (0–9)
#           +  → um ou mais dígitos
# \]    → colchete de fecho literal "]"
regex = r"\[(\d+)\]"

# Procura o padrão na string "log"
result = re.search(regex, log)
# Aqui encontra "[12345]" e captura só "12345" no grupo (result[1])
# result[1] → '12345'

# Outro exemplo: a string também tem números dentro de colchetes
result = re.search(regex, "A completely different string that also has numbers [34567]")
# Encontra "[34567]" e captura "34567"
# result[1] → '34567'

# Aqui temos colchetes, mas o conteúdo é "cage", não são dígitos
result = re.search(regex, "99 elephants in a [cage]")
# O padrão exige (\d+) → um ou mais dígitos, mas temos letras.
# Portanto, não há match → result = None
# Se tentasses result[1], daria erro, porque não existe grupo capturado.


# Função para extrair o PID (número dentro de colchetes, se existir)
def extract_pid(log_line):
    regex = r"\[(\d+)\]"
    result = re.search(regex, log_line)
    if result is None:
        return ""   # Se não encontrou, devolve string vazia
    return result[1]  # Se encontrou, devolve o grupo capturado (só o número)

print(extract_pid(log))  
# Saída: 12345

print(extract_pid("99 elephants in a [cage]"))  
# Como não há números dentro dos colchetes, regex não encontra nada
# Saída: ""
