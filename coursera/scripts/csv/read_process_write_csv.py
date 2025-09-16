#!/usr/bin/env python3
import csv

def read_employees(csv_file_location):
    """
    LÊ E CONVERTE DADOS DE FUNCIONÁRIOS DE UM ARQUIVO CSV PARA UMA LISTA DE DICIONÁRIOS.
    
    Esta função é responsável por:
    1. Ler um arquivo CSV contendo informações dos funcionários
    2. Converter cada linha em um dicionário Python
    3. Retornar uma lista com todos os registros processados
    
    Args:
        csv_file_location (str): Caminho para o arquivo CSV com dados dos funcionários
        
    Returns:
        list: Lista de dicionários, onde cada dicionário representa um funcionário
              Exemplo: [{'Name': 'John', 'Department': 'IT'}, {...}]
    """
    # Define um dialeto personalizado para o CSV
    # skipinitialspace=True: Ignora espaços iniciais nos campos
    # strict=True: Levanta exceção para erros no formato do CSV
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    
    # Abre o arquivo CSV e cria um leitor de dicionário
    # DictReader converte cada linha em um dicionário onde as chaves são os cabeçalhos
    employee_file = csv.DictReader(open(csv_file_location), dialect='empDialect')
    
    # Lista para armazenar todos os funcionários processados
    employee_list = []
    
    # Itera sobre cada linha/registro do arquivo CSV
    for data in employee_file:
        # Adiciona o dicionário do funcionário à lista
        employee_list.append(data)
    
    return employee_list


def process_data(employee_list):
    """
    PROCESSA OS DADOS DOS FUNCIONÁRIOS PARA CONTAR PESSOAS POR DEPARTAMENTO.
    
    Esta função:
    1. Extrai todos os departamentos da lista de funcionários
    2. Conta quantos funcionários existem em cada departamento
    3. Retorna um dicionário com os resultados
    
    Args:
        employee_list (list): Lista de dicionários com dados dos funcionários
        
    Returns:
        dict: Dicionário onde as chaves são nomes de departamentos e os valores
              são as contagens de funcionários
              Exemplo: {'IT': 5, 'HR': 3, 'Finance': 2}
    """
    # Lista para armazenar todos os departamentos (com duplicatas)
    department_list = []
    
    # Itera sobre cada funcionário na lista
    for employee_data in employee_list:
        # Adiciona o departamento do funcionário atual à lista
        # employee_data['Department'] acessa o valor da chave 'Department' no dicionário
        department_list.append(employee_data['Department'])
    
    # Dicionário para armazenar a contagem final por departamento
    department_data = {}
    
    # Usa set(department_list) para obter departamentos únicos (sem duplicatas)
    # Itera sobre cada departamento único
    for department_name in set(department_list):
        # Conta quantas vezes o departamento aparece na lista original
        # department_list.count(department_name) retorna a frequência
        department_data[department_name] = department_list.count(department_name)
    
    return department_data


def write_report(dictionary, report_file):
    """
    GERA UM RELATÓRIO EM TEXTO COM A CONTAGEM DE FUNCIONÁRIOS POR DEPARTAMENTO.
    
    Esta função:
    1. Cria/abre um arquivo de texto para escrita
    2. Escreve os resultados ordenados por nome do departamento
    3. Formata cada linha como: Departamento:Quantidade
    
    Args:
        dictionary (dict): Dicionário com contagem por departamento
        report_file (str): Caminho do arquivo de relatório a ser criado
        
    Returns:
        None: A função cria um arquivo físico com os resultados
    """
    # Abre o arquivo em modo "w+" (write plus) que:
    # - Cria o arquivo se não existir
    # - Sobrescreve se já existir
    # - Permite leitura e escrita
    with open(report_file, "w+") as f:
        
        # Itera sobre as chaves do dicionário ordenadas alfabeticamente
        # sorted(dictionary) retorna uma lista ordenada dos departamentos
        for k in sorted(dictionary):
            # Escreve cada linha no formato: Departamento:Quantidade
            # Exemplo: "IT:5"
            f.write(str(k) + ':' + str(dictionary[k]) + '\n')
        
        # Fecha o arquivo (embora o 'with' já faça isso automaticamente)
        f.close()


# =============================================================================
# FLUXO DE EXECUÇÃO SUGERIDO:
# 1. Ler dados: employee_list = read_employees('employees.csv')
# 2. Processar: department_count = process_data(employee_list)
# 3. Gerar relatório: write_report(department_count, 'report.txt')
# =============================================================================

# =============================================================================
# EXEMPLO DE ARQUIVO CSV DE ENTRADA (employees.csv):
# Name,Department,Position,Salary
# John Doe,IT,Developer,50000
# Jane Smith,HR,Manager,60000
# Bob Johnson,IT,Analyst,45000
# Alice Brown,Finance,Accountant,55000
#
# EXEMPLO DE ARQUIVO DE SAÍDA (report.txt):
# Finance:1
# HR:1
# IT:2
# =============================================================================

# =============================================================================
# MELHORIAS POSSÍVEIS:
# 1. Adicionar tratamento de erros (try-except) para leitura de arquivo
# 2. Validar se a coluna 'Department' existe no CSV
# 3. Usar context manager para abrir o arquivo CSV também
# 4. Adicionar logging para debug
# 5. Permitir diferentes formatos de saída (JSON, XML, etc.)
# =============================================================================