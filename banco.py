import mysql.connector as mysql
from random import randint
import datetime
import threading

class Banco():
    """
    Essa classe representa uma conta bancária básica

    - - -
    Atributes
    _________
        conexao: return function
            conecta a classe no banco de dados
        sinc: return function
            recebe uma thread
        cursor: return function
            server como uma variavel para trabalhar com o banco de dados pelo python
        nome: str
            nome do usuário
        usuario: str
            usuario para login da conta
        senha: str
            senha do usuário
        num: int
            numero da conta do usuário
        cpf: str
            cpf do usuário
        saldo: float
            saldo da conta do usuário
        limite: float
            limite da conta do usuário

    Methods
    -------
    add_conta(usuario, senha, nome, sobrenome, cpf, saldo = 0.0, limite = 1000.0):
        Adiciona uma conta no banco de dadosd

    login(usuario, senha):
        verifica se os campos digitados batem com o que consta no banco de dados

    verificarUsuario(usuario, senha, UserPassword = True):
        Verifica a existência do usuário

    verificarCPF(cpf):
        Verifica se o CPF já existe no banco de dados

    verificarNumero(numero):
        Verifica se o número da conta existe

    get_saldo(numero):
        Retorna o saldo da conta

    set_saldo(numero, valor, flag = True):
        Define um saldo para conta

    get_historico(numero):
        Retorna o historico da conta

    set_historico(numero):
        Define uma nova mensagem para o histórico do usuário

    depositar(numero, valor, frase = True):
        Deposita um valor na conta
    
    sacar(numero, valor, frase = True):
        Saca um valor da conta
    """

    def __init__(self):
        self.conexao = mysql.connect(host='localhost', db='pooii', user='root', password='', autocommit=True)
        sql = """CREATE TABLE IF NOT EXISTS cliente(id int AUTO_INCREMENT PRIMARY KEY NOT NULL, cpf varchar(11) NOT NULL, nome varchar(10) NOT NULL, sobrenome varchar(10) NOT NULL, usuario varchar(12) NOT NULL, senha varchar(200) NOT NULL, numero int(100) NOT NULL, saldo float NOT NULL, limite float NOT NULL, historico varchar(1000) NOT NULL);"""
        self.cursor = self.conexao.cursor()
        self.sinc = threading.Lock()
        self.cursor.execute(sql)

    def add_conta(self, usuario, senha, nome, sobrenome, cpf, saldo = 0.0, limite = 1000.0):
        """
        Adiciona uma conta ao banco

        Parameters
        ----------
        usuario: str
            recebe o user para login da pessoa
        senha: str
            recebe a senha em hash para adicionar no banco de dados
        nome: str
            recebe o nome do usuario
        sobrenome: str
            recebe o sobrenome do usuario
        cpf: str
            recebe o cpf do usuario
        saldo: float, padrao
            cria numa conta com saldo nulo
        limite: float, padrao
            cria um limite para conta de tamanho fixo
        """

        if not self.verificarCPF(cpf):
            if not self.verificarUsuario(usuario):
                data = datetime.datetime.today().strftime("%d/%m/%y %H:%M")
                while True:
                    numero = randint(100, 999)
                    if not self.verificarNumero(numero):
                        self.numero = numero
                        break
                query = f'INSERT INTO cliente(cpf, nome, sobrenome, usuario, senha, numero, saldo, limite, historico) VALUES ("{cpf}", "{nome}", "{sobrenome}", "{usuario}", MD5("{senha}"), {numero}, {saldo}, {limite}, "Data de de abertura: {data}\n")'
                self.sinc.acquire()
                self.cursor.execute(query)
                self.sinc.release()
                return True, "Cadastro realizado com sucesso."
            else:
                return False, 'CPF já estar cadastrado.'
    
    def login(self, usuario, senha):
        """
        Conecta um usuario ao banco

        Parameters
        ----------
        usuario: str
            recebe o user para login da pessoa
        senha: str
            recebe a senha em hash para verificar no banco de dados     
        """

        flag = self.verificarUsuario(usuario, senha, False)
        if flag:
            self.cursor.execute(f'select nome, saldo, numero from cliente where usuario = "{usuario}"')
            resul = self.cursor.fetchall()
            return True, resul
        else:
            return False, "Senha ou Usuário incorretos."

    def verificarUsuario(self, usuario, senha = None, UserPassword = True):
        """
        Verifica se o usuário existe.

        Parameters
        ----------
        usuario: str
            recebe o usuário para verificar no banco de dados
        senha: str
            recebe a senha em hash para verificar no banco de dados
        UserPassword: bool
            confere se a verificação ocorre quando o usuário está conectado ou não    
        """
        if UserPassword:
            self.cursor.execute(f'SELECT usuario FROM cliente WHERE usuario = "{usuario}"')
            exists = self.cursor.fetchall()
            if exists:
                return True  
            return False
        else:
            self.cursor.execute(f'SELECT usuario, senha FROM cliente WHERE usuario = "{usuario}" and senha = MD5("{senha}")')
            if self.cursor.fetchall():
                return True, 'Existe.'
            return False, 'Usuário ou senha não encontrado.'
    
    def verificarCPF(self, cpf):
        """
        Verifica se o CPF existe.

        Parameters
        ----------
        cpf: str
            recebe o hash do CPF do usuário para verificar no banco de dados   
        """
        self.cursor.execute(f'SELECT cpf FROM cliente WHERE cpf = "{cpf}"')
        exists = self.cursor.fetchall()
        if exists:
            return True
        return False

    def verificarNumero(self, numero):
        """
        Verifica se o número da conta existe.

        Parameters
        ----------
        numero: int
            recebe o numero da conta para verificar no banco de dados   
        """
        self.cursor.execute(f'SELECT numero FROM cliente WHERE numero = "{numero}"')
        exists = self.cursor.fetchall()
        if exists:
            return True
        return False
    
    def get_saldo(self, numero):
        """
        Retorna o saldo da conta.

        Parameters
        ----------
        numero: int
            recebe o numero da conta para verificar no banco de dados   
        """
        self.cursor.execute(f'select saldo, limite from cliente where numero = {numero}')
        flag = self.cursor.fetchall()
        if flag:
            return flag
        return False
    
    def set_saldo(self, numero, valor, flag = True):
        """
        Altera o saldo da conta.

        Parameters
        ----------
        numero: int
            recebe o numero da conta para verificar no banco de dados 
        valor: float
            valor para alterar o saldo da conta
        flag: bool
            bandeira para definir se o método será usado em sacar ou depositar  
        """
        saldo = self.get_saldo(numero)
        if flag: 
            valor += saldo[0][0]
        else:
            valor = saldo[0][0] - valor
        self.cursor.execute(f'update cliente set saldo = {valor} where numero = {numero}')
    
    def get_historico(self, numero):
        """
        Retorna o historico da conta.

        Parameters
        ----------
        numero: int
            recebe o numero da conta para verificar no banco de dados   
        """
        self.cursor.execute(f'select historico from cliente where numero = {numero}')
        flag = self.cursor.fetchall()
        return flag

    def set_historico(self, numero, his):
        """
        Retorna o historico da conta.

        Parameters
        ----------
        numero: int
            recebe o numero da conta para verificar no banco de dados
        his: str
            recebe o histórico anterior
        """
        flag = self.get_historico(numero)
        his = flag[0][0] + his
        self.cursor.execute(f'update cliente set historico = "{his}" where numero = {numero}')

    def depositar(self,  numero, valor, frase=True):
        """
        Deposita um valor na conta.

        Parameters
        ----------
        numero: int
            recebe o numero da conta para verificar no banco de dados
        valor: float
            recebe um valor para depositar
        frase: bool
            bandeira para definir se o método adicionará mensagem de deposito ou não
        """
        valor = float(valor)
        flag = self.get_saldo(numero)
        if flag[0][1] < valor or valor <= 0 or flag[0][0] + valor > flag[0][1]:
            return False, "Não foi possível fazer o deposito."
        else:
            self.sinc.acquire()
            self.set_saldo(numero, valor)
            data = datetime.datetime.now().strftime("%d/%m/%y %H:%M")
            if frase:
                his = f"Deposito: R$ {valor:.2f} - Data: {data}\n"
                self.set_historico(numero, his)
            self.sinc.release()
            return True, "Deposito realizado com sucesso."

    def sacar(self, numero, valor, frase=True):
        """
        Saca um valor na conta.

        Parameters
        ----------
        numero: int
            recebe o numero da conta para verificar no banco de dados
        valor: float
            recebe um valor para depositar
        frase: bool
            bandeira para definir se o método adicionará mensagem de saque ou não
        """
        valor = float(valor)
        flag = self.get_saldo(numero)
        if valor > flag[0][0] or valor <= 0:
            return False, "Valor maior que o saldo ou valor menor que 0."
        else:
            self.sinc.acquire()
            self.set_saldo(numero, valor, False)
            data = datetime.datetime.now().strftime("%d/%m/%y %H:%M")
            if frase:
                his = f"Saque: R$ {valor:.2f} - Data: {data}\n"
                self.set_historico(numero, his)
            self.sinc.release()
            return True, "Saque realizado com sucesso."

    def transferir(self, numero, destino, valor):
        """
        Transfere um valor de uma conta a outra.

        Parameters
        ----------
        numero: int
            recebe o numero da conta para verificar no banco de dados
        destino: int
            recebe um numero de outra conta para verificar no banco de dados
        valor: float
            valor para enviar na transferência
        """
        valor = float(valor)
        retirou = self.sacar(numero, valor, False)
        if retirou:
            self.depositar(destino, valor, False)
            data = datetime.datetime.now().strftime("%d/%m/%y %H:%M")
            his = f"Enviou: R$ Valor: {valor:.2f} de {destino} - Data: {data}\n"
            self.sinc.acquire()
            self.set_historico(numero, his)
            his = f"Recebeu: R$ {valor:.2f} de conta: {numero} - Data: {data}\n"
            self.set_historico(destino, his)
            self.sinc.release()
            return True, "Transferencia realizada com sucesso."
        else:
            return False, "Não foi possivel finalizar a transferencia."
