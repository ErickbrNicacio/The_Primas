from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import mysql.connector

# Função para cadastrar um usuário no banco de dados
def cadastrar_usuario():
    # Estabelecer conexão com o banco de dados
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="yvy1kmv*zxq7GNM8eyw",
        database="organizae"
    )

    # Criar um cursor para executar as consultas SQL
    cursor = conexao.cursor()

    # Solicitar informações do usuário
    nome = input("Digite o nome do usuário: ")
    senha = input("Digite a idade do usuário: ")
    email = input("Digite o email do usuário: ")

    # Inserir os dados do usuário no banco de dados
    sql = "INSERT INTO usuarios (nome, senha, email) VALUES (%s, %s, %s)"
    valores = (nome, senha, email)
    cursor.execute(sql, valores)

    # Efetivar as mudanças no banco de dados
    conexao.commit()

    # Fechar a conexão com o banco de dados
    cursor.close()
    conexao.close()

    print("Usuário cadastrado com sucesso!")

# Função para exibir os usuários cadastrados
def exibir_usuarios():
    # Estabelecer conexão com o banco de dados
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="yvy1kmv*zxq7GNM8eyw",
        database="organizae"
    )

    # Criar um cursor para executar as consultas SQL
    cursor = conexao.cursor()

    # Recuperar os usuários do banco de dados
    sql = "SELECT * FROM usuarios"
    cursor.execute(sql)
    usuarios = cursor.fetchall()

    # Exibir os usuários cadastrados
    print("Usuários cadastrados:")
    for usuario in usuarios:
        print(f"Nome: {usuario[1]}, Idade: {usuario[2]}, Email: {usuario[3]}")

    # Fechar a conexão com o banco de dados
    cursor.close()
    conexao.close()

# Função principal
def main():
    while True:
        print("\n----- Sistema de Cadastro -----")
        print("1. Cadastrar usuário")
        print("2. Exibir usuários cadastrados")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            exibir_usuarios()
        elif opcao == "3":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Digite novamente.")

if __name__ == "__main__":
       main()
else: print("pão")