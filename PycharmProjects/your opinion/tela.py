from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import mysql.connector


def harry1():
    tela4.close()
    harry1t.show()


def harry2():
    tela4.close()
    harry2t.show()


def harry3():
    tela4.close()
    harry3t.show()


def jojo():
    tela4.close()
    jojot.show()


def jujutsu():
    tela4.close()
    jujutsut.show()


# ainda não exite, def lookism():

def voltarlivros():
    harry1t.close()
    tela4.show()

def avaliar():
    #harry1t.close()
    avaliart.show()

def troca():
    tela.close()
    tela2.show()


def troca2():
    tela2.close()
    tela3.show()


def login():
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="yvy1kmv*zxq7GNM8eyw",
        database="organizae"
    )
    email = tela2.email.text()
    senha = tela2.senha.text()

    cursor = conexao.cursor()
    sql = "SELECT * FROM usuarios WHERE email = %s AND senha = %s"
    valores = (email, senha)
    cursor.execute(sql, valores)
    resultado = cursor.fetchone()

    if resultado:
        tela2.close()
        tela4.show()
    else:
        QMessageBox.about(tela2, 'Atenção', 'Usuário e/ou senha incorretos.')


#   user = tela.usuario.text()
# if user == '' or password == '':
#     QMessageBox.about(tela, 'Atenção', 'Preencha os campos solicitados!')
# elif user == 'admin' and password == '123':
#   QMessageBox.about(tela, ' Usuário OK', 'Usuário Aceito')
#  tela.close()
# else:
#   QMessageBox.about(tela, 'Atenção', 'Usuário e/ou senha incorretos.')

def cadastro():
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="yvy1kmv*zxq7GNM8eyw",
        database="organizae"
    )

    cursor = conexao.cursor()

    nome = tela3.nome.text()
    email = tela3.email.text()
    senha = tela3.senha.text()
    # data = tela3.nascimento.text()

    sql = "INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)"
    valores = (nome, email, senha)
    cursor.execute(sql, valores)
    conexao.commit()

    if conexao.commit:
        tela3.close()
        tela2.show()
    else:
        QMessageBox.about(tela3, 'Atenção', 'Não foi possivel se conectar com o banco')


app = QtWidgets.QApplication([])
tela = uic.loadUi("principal.ui")
tela2 = uic.loadUi("entrar.ui")
tela3 = uic.loadUi("cadastro.ui")
tela4 = uic.loadUi("pagina-livros.ui")

harry1t = uic.loadUi("descriçãoharry01.ui")
harry2t = uic.loadUi("descriçãoharry02.ui")
harry3t = uic.loadUi("descriçãoharry03.ui")
jojot = uic.loadUi("descriçãoJojo.ui")
jujutsut = uic.loadUi("descriçãojujutsu.ui")
# aqui será o lookism, porém ele ainda não existe lookism = uic.loadUi("pagina-livros.ui")

avaliart = uic.loadUi("Widget.ui")

tela.acessar.clicked.connect(troca)
tela2.login.clicked.connect(login)
tela2.cads.clicked.connect(troca2)
tela3.cadastro.clicked.connect(cadastro)

tela4.harrydesc1.clicked.connect(harry1)
# tela4.harry02.clicked.connect(harry2)
# tela4.harry03.clicked.connect(harry3)
# tela4.jujutsuKaisen.clicked.connect(jujutsu)
# tela4.Jojoadventures.clicked.connect(jojo)
# samerda de lookism tmnc, tela4.harry01.clicked.connect(harry1)

harry1t.batata.clicked.connect(voltarlivros)
harry1t.botaoavaliar.clicked.connect(avaliar)

tela.show()
app.exec()

# qual o problema? os bagulho estão como qlabel e deveriam ser botoes
