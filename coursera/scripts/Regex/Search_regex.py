#!/usr/bin/env python3

#Essa expressão regular corresponde a uma string entre colchetes seguida de um ou mais dígitos. Em seguida, ele usa a função re.search() para pesquisar o registro da string em busca de uma correspondência com a expressão regular. A função re.search() retorna um objeto Match se uma correspondência for encontrada, ou None se nenhuma correspondência for encontrada. a função re.search() retorna um objeto Match porque a string log contém uma correspondência para a expressão regular. O objeto Match tem um método group() que retorna os grupos capturados da correspondência. Nesse caso, o único grupo capturado é o número, que é retornado pela expressão result[1].

import re
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])