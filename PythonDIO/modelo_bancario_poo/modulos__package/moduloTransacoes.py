from abc import ABC, abstractmethod

class RegistroTransacao(ABC):
    @property
    @abstractmethod
    def valor_transacao(self):
        pass

    @property
    @abstractmethod
    def registro_transacao(self):
        pass

class Historico:
    def __init__(self):
        self._registro_transacoes = []

    @property
    def registro_transacoes(self):
        return self._registro_transacoes
    
    def adicionar_transacao(self, transacao_adicionar):
        self._registro_transacoes.append(
            {
                'Natureza': transacao_adicionar.__class__.__name__,
                "Valor": transacao_adicionar.valor,
            }
        )


class DepositoConta(RegistroTransacao):
    def __init__(self, valor_deposito):
        self._valor_deposito = valor_deposito

    @property
    def valor_transacao(self):
        return self._valor_saque
    
    def registrar_transacao(self, conta):
        transacao_feita = conta.depositar(self.valor_transacao)

        if transacao_feita:
            conta.historico.adicionar_transacao(self)


class SaqueConta(RegistroTransacao):
    def __init__(self, valor_saque):
        self._valor_saque = valor_saque

    @property
    def valor_transacao(self):
        return self._valor_saque
    
    def registrar_transacao(self, conta):
        transacao_feita = conta.sacar(self.valor_transacao)

        if transacao_feita:
            conta.historico.adicionar_transacao(self)