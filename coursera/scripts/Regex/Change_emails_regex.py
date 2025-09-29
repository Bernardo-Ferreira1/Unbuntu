#!/usr/bin/env python3

import re     # Biblioteca para trabalhar com expressões regulares (regex)
import csv    # Biblioteca para ler e escrever arquivos CSV

# Função que verifica se um endereço de email termina com um domínio específico
def contains_domain(address, domain):
  """Retorna True se o endereço de e-mail contém o domínio dado na posição correta, False caso contrário."""
  domain = r'[\w\.-]+@' + domain + '$'   # Regex que procura um email que termina com "@dominio"
  if re.match(domain, address):          # Verifica se o padrão bate com o endereço passado
    return True
  return False

# Função que substitui o domínio antigo por um novo em um endereço de e-mail
def replace_domain(address, old_domain, new_domain):
  """Substitui o domínio antigo pelo novo no endereço recebido."""
  old_domain_pattern = r'' + old_domain + '$'    # Regex que identifica o domínio antigo no final do email
  address = re.sub(old_domain_pattern, new_domain, address)  # Substitui pelo novo domínio
  return address

# Função principal que processa o CSV
def main():
  """Processa a lista de e-mails, substituindo qualquer ocorrência do domínio antigo pelo novo."""
  
  # Define o domínio antigo e o novo
  old_domain, new_domain = 'abc.edu', 'xyz.edu'
  
  # Localização do CSV de entrada e do CSV de saída
  csv_file_location = '/home/[virtual_machine_username]/data/user_emails.csv'
  report_file = '/home/[virtual_machine_username]/data' + '/updated_user_emails.csv'

  # Listas para organizar os dados
  user_email_list = []        # Lista com todos os e-mails dos usuários
  old_domain_email_list = []  # Lista com os e-mails que contêm o domínio antigo
  new_domain_email_list = []  # Lista com os e-mails já atualizados para o novo domínio

  # Abre o arquivo CSV para leitura
  with open(csv_file_location, 'r') as f:
    user_data_list = list(csv.reader(f))   # Converte o CSV em uma lista de listas (cada linha é uma lista)
    
    # Pega apenas a segunda coluna (índice 1), que contém os e-mails, ignorando o cabeçalho
    user_email_list = [data[1].strip() for data in user_data_list[1:]]
    
    # Verifica cada email para ver se tem o domínio antigo
    for email_address in user_email_list:
      if contains_domain(email_address, old_domain):             # Se contiver o domínio antigo...
        old_domain_email_list.append(email_address)              # Guarda na lista de antigos
        replaced_email = replace_domain(email_address, old_domain, new_domain)  # Substitui pelo novo
        new_domain_email_list.append(replaced_email)             # Guarda na lista de novos

    # Identifica em qual índice da linha está a coluna de e-mail
    email_key = ' ' + 'Email Address'               # Nome da coluna (com espaço na frente!)
    email_index = user_data_list[0].index(email_key) # Descobre o índice da coluna "Email Address"

    # Atualiza cada linha do CSV com o novo e-mail (se aplicável)
    for user in user_data_list[1:]:  # Ignora o cabeçalho
      for old_domain, new_domain in zip(old_domain_email_list, new_domain_email_list):
        if user[email_index] == ' ' + old_domain:   # Confere se o e-mail do usuário é o antigo
          user[email_index] = ' ' + new_domain      # Substitui pelo novo

  f.close()  # Fecha o arquivo de entrada (embora o with já cuide disso)

  # Abre um novo arquivo CSV para salvar os resultados
  with open(report_file, 'w+') as output_file:
    writer = csv.writer(output_file)   # Cria um objeto para escrever em CSV
    writer.writerows(user_data_list)   # Escreve todas as linhas (já atualizadas)
    output_file.close()                # Fecha o arquivo de saída

# Executa a função principal
main()
