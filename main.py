from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication
import sys
from server_cliente import *

from telainicial import *
from telacadastro import *
from telaconta import *
from telaextrato import *
from teladeposito import *
from telasacar import *
from telatransferir import *


class Ui_Main(QtWidgets.QWidget):
    """
    Essa classe representa as telas do banco

    - - -
    Atributos
    _________
        Qtstack: return function
            cria o layout para as telas

        stack0 - stack6: return function
            cria uma tela
        
        telaInicial: class
            adiciona a tela inicial a uma stack

        telaConta: class
            adiciona a tela conta a uma stack

        telaCadastro: class
            adiciona a tela cadastro a uma stack

        telaDeposito: class
            adiciona a tela deposito a uma stack

        telaSacar: class
            adiciona a tela sacar a uma stack

        telaTransferir: class
            adiciona a tela transferir a uma stack

        telaExtrato: class
            adiciona a tela extrato a uma stack
    """
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(640, 480)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()
        self.stack5 = QtWidgets.QMainWindow()
        self.stack6 = QtWidgets.QMainWindow()

        self.telaInicial = TelaInicial()
        self.telaInicial.setupUi(self.stack0)

        self.telaConta = TelaConta()
        self.telaConta.setupUi(self.stack1)

        self.telaCadastro = TelaCadastro()
        self.telaCadastro.setupUi(self.stack2)
        
        self.telaDeposito = TelaDeposito()
        self.telaDeposito.setupUi(self.stack3)

        self.telaSacar = TelaSacar()
        self.telaSacar.setupUi(self.stack4)

        self.telaTransferir = TelaTransferir()
        self.telaTransferir.setupUi(self.stack5)

        self.telaExtrato = TelaExtrato()
        self.telaExtrato.setupUi(self.stack6)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)
        self.QtStack.addWidget(self.stack6)

class Main(QMainWindow, Ui_Main):
    """
    Essa classe representa uma conta bancária básica

    - - -
    Atributes
    _________
        Todos os parametros anteriores
        server: class
            conecta o cliente ao servidor
    
    Methods
    -------
    sair():
        sai do banco
    
    BotaoVoltarTelaInicial():
        volta para tela inicial
    
    BotaoParaTelaConta():
        leva para a tela conta

    BotaoParaTelaCadastro():
        leva para tela cadastro

    BotaoParaTelaDeposito():
        leva a tela deposito

    BotaoParaTelaSacar():
        leva a tela sacar

    BotaoParaTelaTransferir():
        leva a tela transferir

    BotaoParaTelaHistorico():
        leva a tela historico e puxa do banco de dados o extrato

    request_server(request):
        envia uma mensagem para o servidor, recebe outra do servidor e retorna o resultado

    BotaoCadastrar():
        solicita uma solicitação para cadastrar ao servidor

    BotaoLogin():
        solicita uma solicitação para logar ao servidor

    BotaoDepositar(self):
        solicita uma solicitação para depositar ao servidor

    BotaoSacar(self):
        solicita uma solicitação para sacar ao servidor
    
    BotaoTransferir():
        solicita uma solicitação para transferir ao servidor

    concatenar(string):
        formata a mensagem enviada pelo servidor
    
    concatenarHis(string):
        formata a mensagem do historico
    """
    def __init__(self):
        super(Main, self).__init__(None)
        self.setupUi(self)
        
        self.server = server_cliente()

        self.telaInicial.btnCadastrar.clicked.connect(self.BotaoParaTelaCadastro)
        self.telaInicial.btnLogin.clicked.connect(self.BotaoLogin)
        self.telaInicial.btnSair.clicked.connect(self.sair)

        self.telaCadastro.btnCadastrar.clicked.connect(self.BotaoCadastrar)
        self.telaCadastro.btnVoltar.clicked.connect(self.BotaoVoltarTelaInicial)

        self.telaConta.btnDepositar.clicked.connect(self.BotaoParaTelaDeposito)
        self.telaConta.btnSacar.clicked.connect(self.BotaoParaTelaSacar)
        self.telaConta.btnTransferir.clicked.connect(self.BotaoParaTelaTransferir)
        self.telaConta.btnExtrato.clicked.connect(self.BotaoParaTelaHistorico)
        self.telaConta.btnVoltar.clicked.connect(self.BotaoVoltarTelaInicial)
        self.telaConta.btnSair.clicked.connect(self.sair)

        self.telaDeposito.btnDepositar.clicked.connect(self.BotaoDepositar)
        self.telaDeposito.btnVoltar.clicked.connect(self.BotaoParaTelaConta)
        self.telaDeposito.btnSair.clicked.connect(self.sair)

        self.telaSacar.btnSacar.clicked.connect(self.BotaoSacar)
        self.telaSacar.btnVoltar.clicked.connect(self.BotaoParaTelaConta)
        self.telaSacar.btnSair.clicked.connect(self.sair)

        self.telaTransferir.btnTransferir.clicked.connect(self.BotaoTransferir)
        self.telaTransferir.btnVoltar.clicked.connect(self.BotaoParaTelaConta)
        self.telaTransferir.btnSair.clicked.connect(self.sair)

        self.telaExtrato.btnVoltar.clicked.connect(self.BotaoParaTelaConta)
        self.telaExtrato.btnSair.clicked.connect(self.sair)

    def sair(self):
        """
        Sai do servidor
        """
        self.request_server('sair')
        sys.exit()

    def BotaoVoltarTelaInicial(self):
        """
        Volta para primeira tela
        """
        self.QtStack.setCurrentIndex(0)

    def BotaoParaTelaConta(self):
        """
        Verifica o login do usuário e conecta na conta
        """
        solicit = f'login*{self.user}*{self.passw}'
        flag = self.request_server(solicit)
        if flag[0]:
            self.numero = flag[3]
            self.telaConta.labelConta.setText(f'Olá, {flag[1]}!\nSaldo: R$ {flag[2]}\nNúmero da Conta: {flag[3]}')
            self.QtStack.setCurrentIndex(1)

    def BotaoParaTelaCadastro(self):
        """
        Entra na tela cadastro
        """
        self.QtStack.setCurrentIndex(2)

    def BotaoParaTelaDeposito(self):
        """
        Entra na tela deposito
        """
        self.QtStack.setCurrentIndex(3)

    def BotaoParaTelaSacar(self):
        """
        Entra na tela Sacar
        """
        self.QtStack.setCurrentIndex(4)

    def BotaoParaTelaTransferir(self):
        """
        Entra na tela Transferir
        """
        self.QtStack.setCurrentIndex(5)

    def BotaoParaTelaHistorico(self):
        """
        Entra na tela historico e adiciona o historico na campo da tela
        """
        solicit = f'get_historico*{self.numero}'
        flag = self.request_server(solicit)
        noti = self.concatenarHis(flag)
        self.telaExtrato.labelExtrato.setText(noti)
        self.QtStack.setCurrentIndex(6)
    
    def request_server(self, request):
        """
        Envia uma mensagem para o servidor, e recebe outra mensagem retornando algo

        Parameters
        ----------
        request: list
            lista com o metodo que o usuário solicitou e informações do usuário
        """
        self.server.send(request.encode())
        recv = self.server.recv(2048)
        flag = recv.decode()
        flag = flag.replace("(", "").replace(")", "").replace("[", "").replace("]", "").replace(",", "").replace("'", '').split()
        return flag
    
    def concatenar(self, string):
        """
        Forma a mensagem enviada pelo servidor

        Parametros
        ----------
        string: str
            mensagem enviada pelo servidor
        """
        noti = ''
        for i in range(1,len(string)):
            noti += string[i] + " "
        return noti

    def BotaoCadastrar(self):
        """
        Envia uma solicitação ao servidor para cadastrar e recebe os campos de cadastro do usuário
        """
        nome = self.telaCadastro.lineEditNome.text()
        sobrenome = self.telaCadastro.lineEditSobrenome.text()
        cpf = (self.telaCadastro.lineEditCPF.text())
        usuario = self.telaCadastro.lineEditUser.text()
        senha = self.telaCadastro.lineEditSenha.text()
        if nome != '' and cpf != '' and usuario != '' and senha != '':
            if cpf.isdigit() and len(cpf) == 11:
                solicit = f'add_conta*{usuario}*{senha}*{nome}*{sobrenome}*{cpf}'
                flag = self.request_server(solicit)
                noti = self.concatenar(flag)
                self.request_server(solicit)
                self.telaCadastro.lineEditNome.setText("")
                self.telaCadastro.lineEditSobrenome.setText("")
                self.telaCadastro.lineEditCPF.setText("")
                self.telaCadastro.lineEditUser.setText("")
                self.telaCadastro.lineEditSenha.setText("")
                QMessageBox.information(None, 'Cadastro', noti)
            else:
                QMessageBox.information(None, 'Cadastro', 'O CPF não existe')
        else:
            QMessageBox.information(None, 'Cadastro', 'Todos os dados devem estar preenchidos!')

    def BotaoLogin(self):
        """
        Envia uma solicitação ao servidor para logar e recebe os campos de login do usuário
        """
        usuario = self.telaInicial.lineEditUser.text()
        senha = self.telaInicial.lineEditSenha.text()
        if usuario != '' and senha != '':
            solicit = f'login*{usuario}*{senha}'
            flag = self.request_server(solicit)
            if flag[0]:
                self.user = usuario
                self.passw = senha
                self.numero = flag[3]
                self.telaConta.labelConta.setText(f'Olá, {flag[1]}!\nSaldo: R$ {flag[2]}\nNúmero da Conta: {flag[3]}')
                self.QtStack.setCurrentIndex(1)
            else:
                noti = self.concatenar(flag)
                QMessageBox.information(None, 'Login', noti)
        else:
            QMessageBox.information(None, 'Login', 'Todos os dados devem ser preenchidos.')
        self.telaInicial.lineEditUser.setText("")
        self.telaInicial.lineEditSenha.setText("")

    def BotaoDepositar(self):
        """
        Envia uma solicitação ao servidor para depositar e recebe os campos de valor para depositar
        """
        valor = self.telaDeposito.lineEditDepositar.text()
        if valor != '':
            if valor.replace('.','').isdigit():
                solicit = f'depositar*{self.numero}*{float(valor)}'
                flag = self.request_server(solicit)
                noti = self.concatenar(flag)
                QMessageBox.information(None, 'Deposito', noti)
            else:
                QMessageBox.information(None, 'Deposito', 'Informe somente números.')
        else:
            QMessageBox.information(None, 'Deposito', 'Todos os espaços devem ser preenchidos.')
        self.telaDeposito.lineEditDepositar.setText('')

    def BotaoSacar(self):
        """
        Envia uma solicitação ao servidor para sacar e recebe os campos de valor para sacar
        """
        valor = self.telaSacar.lineEditSacar.text()
        if valor != '':
            if valor.replace('.','').isdigit():
                solicit = f'sacar*{self.numero}*{valor}'
                flag = self.request_server(solicit)
                noti = self.concatenar(flag)
                if flag[0]:
                    QMessageBox.information(None, 'Saque', noti)
                else:
                    QMessageBox.information(None, 'Saque', 'Saldo insuficiente.')
            else:
                QMessageBox.information(None, 'Saque', 'Informe somente números.') 
        else:
            QMessageBox.information(None, 'Saque', 'Informe um valor.') 
        self.telaSacar.lineEditSacar.setText('')

    def BotaoTransferir(self):
        """
        Envia uma solicitação ao servidor para transferir e recebe os campos de valor para transferir e o número da conta de destino
        """
        valor = self.telaTransferir.lineEditTransferir.text()
        numero = self.telaTransferir.lineEditConta.text()
        if valor != '' and numero != '':
            if valor.replace('.','').isdigit() and numero.replace('.','').isdigit():
                solicit = f'transferir*{self.numero}*{numero}*{valor}'
                self.request_server(solicit)
                QMessageBox.information(None, 'Transferir', 'Transferências realizada com sucesso.')
            else:
                QMessageBox.information(None, 'Transferir', 'Informe somente números.')
        else:
            QMessageBox.information(None, 'Transferir', 'Todos os dados devem ser preenchidos')
        self.telaTransferir.lineEditTransferir.setText('')
        self.telaTransferir.lineEditConta.setText('')
    
    def concatenarHis(self, string):
        """
        Formata a mensagem enviada pelo servidor do extrato

        Parameters
        ----------
        string: list
            mensagem do historico
        """
        noti = ''
        for i in range(len(string)):
            noti += string[i] + ' '
        noti = noti.split('\\n')
        a = ''
        for i in noti:
            a += i + '\n'
        return a

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())