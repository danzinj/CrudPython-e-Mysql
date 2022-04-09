import mysql.connector

mybanco = mysql.connector.connect(host="localhost", user="root", password="",  database='bdempresa')
cursor = mybanco.cursor(dictionary=True)



class Cadastros:



    def programa(self):
        while True:
            print('\n1 Cadastrar Usuario  \n2 Listar Usuarios \n3 Deletar usuario \n4 Atualizar Dados do Usuario\n')
            console = input("Digite a opção que deseja utilizar: ")
            if console == '1':
                self.cadastrarUser()
            elif console == '2':
                self.ListarUser()
            elif console == '3':
                self.DeletarUser()
            elif console == '4':
                self.AtualizarUser()
            else:
                raise ValueError("Opção Invalida!!")


    def cadastrarUser(self):
        Nome = input('Digite seu nome completo: ')
        Cpf = input('Digite seu cpf: ')
        Telefone = input("Digite seu telefone: ")
        DataNascimento = input("Data de nascimento: ")
        Cargo = input("Digite seu cargo: ")
        Email = input("Digite um email para cadastro: ")
        cursor.execute(f"INSERT INTO cadastros (NomeCompleto, Cpf, Telefone, DataNascimento, Cargo, Email) VALUES('{Nome}', '{Cpf}', '{Telefone}', '{DataNascimento}', '{Cargo}', '{Email}' )")
        print('Usuario adicionado com sucesso!!')
        mybanco.commit()


    def ListarUser(self):
        cursor.execute("SELECT * from cadastros")
        usuarios = cursor.fetchall()
        print("Usuarios cadastrados/\n")
        print(usuarios)


    def DeletarUser(self):
        cpf = input("Digite o cpf cadastrado para deletar o usuario: ")
        cursor.execute(f"DELETE from cadastros WHERE Cpf='{cpf}' ")
        print("Usuario deletado com sucesso")
        mybanco.commit()


    def AtualizarUser(self):
        NomeCompleto = input("Digite o Nome Completo do Funcionario")
        cargo = input("Digite o novo cargo do Funcionario")
        cursor.execute(f"UPDATE cadastros SET  cargo = {cargo} WHERE NomeCompleto={NomeCompleto}")
        print("Cargo Alterado com Sucesso!")
        mybanco.commit()


if __name__ == '__main__':
    rodarPrograma = Cadastros()
    rodarPrograma.programa()
