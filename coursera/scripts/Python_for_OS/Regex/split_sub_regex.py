#!/usr/bin/env python3

# re.split(r"[.?!]", ...)
# [ .?! ] → divide a string em qualquer ocorrência de ponto (.), interrogação (?) ou exclamação (!)
print(re.split(r"[.?!]", "One sentence. Another one? And the last one!"))
# Divide a frase em partes:
# ['One sentence', ' Another one', ' And the last one', '']
# (repara que sobra uma string vazia no fim porque havia um delimitador no final)


# re.split(r"([.?!])", ...)
# Os parênteses criam um GRUPO DE CAPTURA → os separadores também são mantidos no resultado
print(re.split(r"([.?!])", "One sentence. Another one? And the last one!"))
# ['One sentence', '.', ' Another one', '?', ' And the last one', '!', '']
# Agora vemos cada frase + o separador (., ?, !)


# re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", ...)
# [\w.%+-]+ → parte inicial do email (nome do utilizador)
# @        → o arroba literal
# [\w.-]+  → parte do domínio
# Troca o padrão encontrado por "[REDACTED]"
print(re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an email for go_nuts95@my.example.com"))
# "Received an email for [REDACTED]"


# re.sub com grupos e substituição
# ^([\w .-]*), ([\w .-]*)$  
# ^ e $ → início e fim da string (garante que toda a string tem este formato)
# ([\w .-]*) → primeiro grupo: nome antes da vírgula
# , (vírgula) → separador
# ([\w .-]*) → segundo grupo: nome depois da vírgula
#
# r"\2 \1" → reordena os grupos (2 primeiro, depois 1)
print(re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada"))
# Saída: "Ada Lovelace"