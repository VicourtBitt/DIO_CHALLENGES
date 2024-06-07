import moduloTransacoes
import moduloClientes
from moduloClientes import CadastroCliente
from moduloTransacoes import Historico, SaqueConta

class Conta:
    def __init__(self, numero_conta, cliente):
        self._saldo_conta = 0
        self._numero_conta = numero_conta
        self._agencia_banco = "0001"
        self._cliente = cliente
        self._historico_conta = Historico

    @property
    def saldo_conta(self):
        return self._saldo_conta

    @property
    def numero_conta(self):
        return self._numero_conta
    
    @property
    def agencia_banco(self):
        return self._agencia_banco
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico_conta(self):
        return self._historico_conta

    @classmethod
    def criar_nova_conta(cls, cliente, numero_conta):
        return cls(cliente, numero_conta)
    
    def sacar_valor(self, valor_a_sacar):
        saldo_a_sacar = self.saldo_conta
        limite_saldo_atual = valor_a_sacar > saldo_a_sacar

        if limite_saldo_atual:
            print("Você não possui saldo suficiente para completar esta operação.")
        
        if valor_a_sacar > 0:
            self.saldo_conta -= valor_a_sacar
            print("Saque feito com sucesso! Valor retirado da sua conta.")
            return True
        
        else:
            print("Operação não finalizada, saldo insucifiente ou valor inválido.")
        return False
    
    def depositar_valor(self, valor_a_depositar):
        if valor_a_depositar > 0:
            self.saldo_conta += valor_a_depositar
            print("O valor foi depositado com sucesso.")

        else:
            print("O deposito não foi realizado. Valor informado não é válido.")
            return False
        return True


class ContaCorrente(Conta):
    def __init__(self, numero_conta, cliente, limite_valor= 750, limite_diario_saque=4):
        super().__init__(numero_conta, cliente)
        self.limite_valor = limite_valor
        self.limite_diario_saque = limite_diario_saque

    def sacar_valor(self, valor_a_sacar):
        qtd_saques_atuais = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == SaqueConta.__name__]
        )
    
        passou_limite_valor = valor_a_sacar > self.limite_valor
        passou_limite_diario = qtd_saques_atuais > self.limite_diario_saque

        if passou_limite_diario:
            print("Você passou o limite diário de saques")
        
        elif passou_limite_valor:
            print("Você passou o limite diário de valores a retirar.")

        else:
            return super().sacar(valor_a_sacar)

    def __str__(self):
        return f"Agência do Banco: {self.agencia_banco}\n\
                Conta: {self.numero_conta}\n\
                Titular da Conta: {self.cliente.nome}"
    