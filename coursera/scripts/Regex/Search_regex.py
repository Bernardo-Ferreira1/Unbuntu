#!/usr/bin/env python3

import re

# =============================================================================
# EXEMPLO 1: Extrair número de processo de um log
# =============================================================================

# String de log do sistema
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"

# Regex para encontrar padrão [número] - \d+ significa "um ou mais dígitos"
# Os parênteses () criam um grupo de captura para extrair só o número
regex = r"\[(\d+)\]"

# Procura o padrão regex na string log
result = re.search(regex, log)

# result[1] acessa o primeiro grupo de captura (o número dentro dos parênteses)
print(result[1])
# Saída: 12345


# =============================================================================
# EXEMPLO 2: Pesquisas básicas com regex
# =============================================================================

# Procura o padrão "aza" na string "plaza"
result = re.search(r"aza", "plaza")
print(result)
# Saída: <re.Match object; span=(2, 5), match='aza'>

# Procura "aza" em "bazaar" - encontra na posição 1-4
result = re.search(r"aza", "bazaar")
print(result)
# Saída: <re.Match object; span=(1, 4), match='aza'>

# Procura "aza" em "maze" - não encontra, retorna None
result = re.search(r"aza", "maze")
print(result)
# Saída: None


# =============================================================================
# EXEMPLO 3: Âncoras e caracteres especiais
# =============================================================================

# ^ significa "início da string" - procura "x" no início de "xenon"
print(re.search(r"^x", "xenon"))
# Saída: <re.Match object; span=(0, 1), match='x'>

# . significa "qualquer caractere único" - procura p + qualquer caractere + ng
print(re.search(r"p.ng", "penguin"))
# Saída: <re.Match object; span=(0, 4), match='peng'>

# Outro exemplo do coringa . 
print(re.search(r"p.ng", "penguin"))
# Saída: <re.Match object; span=(0, 4), match='peng'>

# re.IGNORECASE faz busca case-insensitive - encontra "Pang" apesar do P maiúsculo
print(re.search(r"p.ng", "Pangaea", re.IGNORECASE))
# Saída: <re.Match object; span=(0, 4), match='Pang'>

# Procura "Python" ou "python" (primeira letra pode ser maiúscula ou minúscula)
print(re.search(r"[Pp]ython", "Python"))  
# Saída: <re.Match object; span=(0, 6), match='Python'>

# Procura qualquer letra minúscula [a-z] seguida da palavra "way"
print(re.search(r"[a-z]way", "The end of the highway"))  
# Aqui encontra "hway" (o 'h' é minúsculo e está antes de "way")
# Saída: <re.Match object; span=(18, 22), match='hway'>

print(re.search(r"[a-z]way", "What a way to go"))  
# Não encontra nada porque "way" não tem letra minúscula antes
# Saída: None

# Procura a palavra "cloud" seguida de uma letra ou número ([a-zA-Z0-9])
print(re.search("cloud[a-zA-Z0-9]", "cloudy"))  
# Aqui encontra "cloudy"
# Saída: <re.Match object; span=(0, 6), match='cloudy'>

print(re.search("cloud[a-zA-Z0-9]", "cloud9"))  
# Aqui encontra "cloud9"
# Saída: <re.Match object; span=(0, 6), match='cloud9'>

# Procura o primeiro caractere que NÃO seja uma letra (negado com ^ dentro de [])
print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces."))  
# O primeiro caractere não-letra é o espaço após "This"
# Saída: <re.Match object; span=(4, 5), match=' '>

# Procura o primeiro caractere que NÃO seja uma letra OU espaço
print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces."))  
# O primeiro caractere que não é letra nem espaço é o ponto final "."
# Saída: <re.Match object; span=(29, 30), match='.'>

# Procura "cat" ou "dog" (operador | significa "ou")
print(re.search(r"cat|dog", "I like cats."))  
# Encontra "cat" dentro da palavra "cats"
# Saída: <re.Match object; span=(7, 10), match='cat'>

print(re.search(r"cat|dog", "I love dogs!"))  
# Encontra "dog" dentro da palavra "dogs"
# Saída: <re.Match object; span=(7, 10), match='dog'>

print(re.search(r"cat|dog", "I like both dogs and cats."))  
# Encontra o primeiro que aparece → "dog"
# Saída: <re.Match object; span=(12, 15), match='dog'>

# (linhas repetidas, mesma explicação e resultados)
print(re.search(r"cat|dog", "I like cats."))  
# Saída: <re.Match object; span=(7, 10), match='cat'>

print(re.search(r"cat|dog", "I love dogs!"))  
# Saída: <re.Match object; span=(7, 10), match='dog'>

print(re.search(r"cat|dog", "I like both dogs and cats."))  
# Saída: <re.Match object; span=(12, 15), match='dog'>

# findall devolve TODAS as ocorrências em vez de apenas a primeira
print(re.findall(r"cat|dog", "I like both dogs and cats."))  
# Aqui devolve uma lista com ['dog', 'cat']
# Saída: ['dog', 'cat']

# "Py.*n"
# Py → começa por "Py"
# .* → qualquer número de caracteres (inclusive nenhum), de qualquer tipo
# n  → termina com "n"
print(re.search(r"Py.*n", "Pygmalion"))  
# Encontra "Pygmalion" inteiro (de Py até n final)
# Saída: <re.Match object; span=(0, 9), match='Pygmalion'>

print(re.search(r"Py.*n", "Python Programming"))  
# Encontra "Python Programmin" (de Py até o último "n" que puder)
# Saída: <re.Match object; span=(0, 17), match='Python Programmin'>


# "Py[a-z]*n"
# Py → começa por "Py"
# [a-z]* → zero ou mais letras minúsculas (não aceita maiúsculas aqui!)
# n → termina com "n"
print(re.search(r"Py[a-z]*n", "Python Programming"))  
# Encontra "Python" (de Py até n, só com letras minúsculas no meio)
# Saída: <re.Match object; span=(0, 6), match='Python'>

print(re.search(r"Py[a-z]*n", "Pyn"))  
# Encontra "Pyn" (porque depois de Py não há letras minúsculas, só o n direto)
# Saída: <re.Match object; span=(0, 3), match='Pyn'>


# "o+l+"
# o+ → um ou mais 'o'
# l+ → um ou mais 'l'
print(re.search(r"o+l+", "goldfish"))  
# Encontra "ol" (um 'o' e um 'l')
# Saída: <re.Match object; span=(1, 3), match='ol'>

print(re.search(r"o+l+", "woolly"))  
# Encontra "ooll" (dois 'o' seguidos de dois 'l')
# Saída: <re.Match object; span=(1, 5), match='ooll'>

print(re.search(r"o+l+", "boil"))  
# Não encontra nada (há 'o' mas não seguido imediatamente de 'l')
# Saída: None


# "p?each"
# p? → zero ou um 'p' (opcional)
# each → seguido de "each"
print(re.search(r"p?each", "To each their own"))  
# Encontra "each" (sem 'p' antes, porque p é opcional)
# Saída: <re.Match object; span=(3, 7), match='each'>

print(re.search(r"p?each", "I like peaches"))  
# Encontra "peach" (o 'p' está presente desta vez)
# Saída: <re.Match object; span=(7, 12), match='peach'>

# "." em regex significa "qualquer caractere" (exceto quebra de linha)
# ".com" → qualquer caractere seguido de "com"
print(re.search(r".com", "welcome"))  
# Encontra "lcom" (o 'l' + "com")
# Saída: <re.Match object; span=(3, 7), match='lcom'>


# "\." → o ponto literal "." (porque "." sozinho significa "qualquer caractere")
# "\.com" → procura exatamente ".com"
print(re.search(r"\.com", "welcome"))  
# Não encontra nada porque não existe ".com" no texto
# Saída: None

print(re.search(r"\.com", "mydomain.com"))  
# Encontra ".com" no final
# Saída: <re.Match object; span=(8, 12), match='.com'>


# "\w*" → zero ou mais caracteres alfanuméricos (inclui letras, números e "_")
print(re.search(r"\w*", "This is an example"))  
# O regex começa no início da string: "This" é a maior sequência de \w no começo
# Saída: <re.Match object; span=(0, 4), match='This'>

print(re.search(r"\w*", "And_this_is_another"))  
# Desde o início, encontra toda a sequência contínua de \w → "And_this_is_another"
# Saída: <re.Match object; span=(0, 19), match='And_this_is_another'>

# "A.*a"
# A → começa com 'A'
# .* → qualquer sequência de caracteres (inclusive nenhum)
# a → termina com 'a' (mas como não tem ^ nem $, pode terminar antes do fim da string)
print(re.search(r"A.*a", "Argentina"))  
# Encontra "Argentina" (do A inicial até o 'a' final)
# Saída: <re.Match object; span=(0, 9), match='Argentina'>

print(re.search(r"A.*a", "Azerbaijan"))  
# Encontra "Azerbaija" (do A inicial até o penúltimo 'a'; o último 'n' fica de fora)
# Saída: <re.Match object; span=(0, 9), match='Azerbaija'>

print(re.search(r"^A.*a$", "Australia"))  
# ^ → início da string
# A → tem de começar por 'A'
# .* → qualquer sequência
# a → tem de terminar com 'a'
# $ → fim da string
# Aqui a string toda cumpre o padrão
# Saída: <re.Match object; span=(0, 9), match='Australia'>


# Regex para nomes de variáveis em Python (simplificado):
pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
# ^ → início da string
# [a-zA-Z_] → o primeiro caractere tem de ser letra ou "_"
# [a-zA-Z0-9_]* → os seguintes podem ser letras, números ou "_"
# $ → fim da string

print(re.search(pattern, "_this_is_a_valid_variable_name"))  
# Começa com "_", segue só com letras/números/_, válido
# Saída: <re.Match object; span=(0, 30), match='_this_is_a_valid_variable_name'>

print(re.search(pattern, "this isn't a valid variable"))  
# Tem espaços e apóstrofo → não casa com o padrão
# Saída: None

print(re.search(pattern, "my_variable1"))  
# Começa com letra, resto letras/números/_ → válido
# Saída: <re.Match object; span=(0, 12), match='my_variable1'>

print(re.search(pattern, "2my_variable1"))  
# Começa com número → inválido para nomes de variáveis
# Saída: None

def rearrange_name(name):
    result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
    if result == None:
        return name
    return "{} {}".format(result[2], result[1])
rearrange_name("Hopper, Grace M.")

# "[a-zA-Z]{5}"
# [a-zA-Z] → qualquer letra (maiúscula ou minúscula)
# {5} → exatamente 5 repetições consecutivas
print(re.search(r"[a-zA-Z]{5}", "a ghost"))  
# A string tem "ghost" (5 letras), regex encontra
# Saída: <re.Match object; span=(2, 7), match='ghost'>

print(re.search(r"[a-zA-Z]{5}", "a scary ghost appeared"))  
# O primeiro conjunto de 5 letras que aparece é "scary"
# Saída: <re.Match object; span=(2, 7), match='scary'>

print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared"))  
# Encontra TODOS os conjuntos de 5 letras consecutivas
# Resultado: ['scary', 'ghost', 'appea']  
# (atenção: "appea" é só as 5 primeiras letras de "appeared")

print(re.findall(r"\b[a-zA-Z]{5}\b", "A scary ghost appeared"))  
# \b → delimita "fronteira de palavra"
# [a-zA-Z]{5} → palavra de exatamente 5 letras
# Resultado: ['scary', 'ghost']  
# ("appeared" tem 8 letras, por isso não entra)


# "\w{5,10}"
# \w → letra, número ou "_"
# {5,10} → entre 5 e 10 caracteres consecutivos
print(re.findall(r"\w{5,10}", "I really like strawberries"))  
# Encontra: ['really', 'like', 'strawberri']  
# ("strawberries" tem 11 letras → só capta os primeiros 10 = "strawberri")

print(re.findall(r"\w{5,}", "I really like strawberries"))  
# \w{5,} → 5 ou mais caracteres
# Resultado: ['really', 'strawberries']


# "s\w{,20}"
# s → começa com 's'
# \w{,20} → até 20 caracteres a seguir (zero a 20)
print(re.search(r"s\w{,20}", "I really like strawberries"))  
# Encontra "strawberries" (13 caracteres no total, cabe dentro do limite 20)
# Saída: <re.Match object; span=(14, 26), match='strawberries'>



# =============================================================================
# EXPLICAÇÃO DAS SAÍDAS:
# 
# <re.Match object; span=(X, Y), match='TEXT'> 
# - span=(X, Y): indica a posição onde o padrão foi encontrado (início, fim)
# - match='TEXT': mostra o texto que casou com o padrão
#
# None: significa que o padrão não foi encontrado na string
# =============================================================================

# =============================================================================
# RESUMO DOS METACARACTERES USADOS:
# r"..."       - raw string (recomendado para regex)
# \d+         - um ou mais dígitos
# [...]       - conjunto de caracteres
# (\d+)       - grupo de captura
# ^           - início da string  
# .           - qualquer caractere único
# re.IGNORECASE - busca case-insensitive
# =============================================================================

