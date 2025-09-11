#the following command should be used in the terminal
#cat software.csv
#Output name,version,status,users
#MailTree,5.34,production,324
#CalDoor,1.25.1,beta,22
#Chatty Chicken,0.34,alpha,4

#Aqui o código está abrindo o arquivo e criando um DictReader para processar nossos dados CSV. Em seguida, ele percorre as linhas para acessar as informações em cada linha usando as chaves, exatamente como faríamos ao acessar os dados no dicionário.

with open('software.csv') as software:
    reader = csv.DictReader(software)
    for row in reader:
      print(("{} has {} users").format(row["name"], row["users"]))