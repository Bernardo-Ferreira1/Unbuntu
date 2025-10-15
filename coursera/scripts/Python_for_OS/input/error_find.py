#!/usr/bin/env python3
import sys
import os
import re

# Função para procurar erros dentro de um ficheiro de log
def error_search(log_file):
        # Pede ao utilizador para introduzir o erro a procurar (ex: "CRON ERROR appeared")
        error = input("What is the error? ")

        # Lista que vai armazenar todas as linhas do log que contenham o erro
        returned_errors = []

        # Abre o ficheiro de log em modo leitura com codificação UTF-8
        with open(log_file, mode='r', encoding='UTF-8') as file:
                # Lê todas as linhas do log
                for log in file.readlines():
                        # Define os padrões de erro a procurar, começando com "error"
                        error_patterns = ["error"]

                        # Divide a string do erro inserido em palavras individuais
                        # e adiciona-as como padrões adicionais
                        for i in range(len(error.split(' '))):
                                error_patterns.append(r"{}".format(error.split(' ')[i].lower()))

                        # Verifica se TODAS as palavras/padrões definidos estão presentes na linha
                        if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
                                # Se sim, adiciona a linha à lista de erros encontrados
                                returned_errors.append(log)

        # Devolve a lista de linhas com erros
        return returned_errors


# Função para guardar os erros encontrados num ficheiro
def file_output(returned_errors):
        # Cria (ou substitui) o ficheiro errors_found.log na pasta home do utilizador
        with open(os.path.expanduser('~') + '/data/errors_found.log', 'w') as file:
                # Escreve cada linha de erro encontrada no ficheiro
                for error in returned_errors:
                        file.write(error)


# Programa principal
if __name__ == "__main__":
        # O ficheiro de log a analisar é passado como argumento ao script
        log_file = sys.argv[1]

        # Procura erros dentro do ficheiro de log
        returned_errors = error_search(log_file)

        # Escreve os erros encontrados no ficheiro errors_found.log
        file_output(returned_errors)

        # Termina o programa sem erros
        sys.exit(0)
