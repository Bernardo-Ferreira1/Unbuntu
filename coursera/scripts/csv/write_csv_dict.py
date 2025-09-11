#Aqui o código cria uma lista de dicionários com os dados que queremos armazenar. Neste exemplo, queremos armazenar dados sobre os usuários de nossa empresa e os departamentos em que trabalham. Portanto, aqui temos nossa lista de dicionários e cada um contém as chaves: nome, nome de usuário e departamento. Agora queremos escrever esse Arquivo CSV. Portanto, primeiro definimos a lista de chaves que queremos gravar no arquivo e, em seguida, abrimos o arquivo para gravação. Em seguida, criamos o DictWriter, passando as chaves que identificamos anteriormente, e chamamos dois métodos diferentes no gravador. O método writeheader() criará a primeira linha do Arquivo CSV com base nas chaves que passamos, e o método writerows() transformará a lista de dicionários em linhas nesse arquivo.
#the following command should be used in the terminal
#cat by_department.csv  

users = [ {"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"}, 
 {"name": "Lio Nelson", "username": "lion", "department": "User Experience Research"}, 
  {"name": "Charlie Grey", "username": "greyc", "department": "Development"}]
keys = ["name", "username", "department"]
with open('by_department.csv', 'w') as by_department:
    writer = csv.DictWriter(by_department, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)