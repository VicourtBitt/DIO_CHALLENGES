import sys
from CleanTerminalModule import clean_terminal

_operacoes_feitas = []
_saldo_total = 0
_SAQUES_MAX = 3
_VALOR_SAQUES = 500.00


def sistema_bancario():
    global _saldo_total
    _lista_de_operacoes = {
        "saque" : lambda:_sacar(),
        "deposito" : lambda:_depositar(),
        "extrato" : lambda:_ver_extrato(),
        "sair" : lambda:sys.exit("Saindo do sistema"),
        "erro" : lambda:print("Algum erro ocorreu, tente novamente.")
}
    print("Seja bem vindo ao sistema bancário VicourtBitt. ")

    while True:
        _operacao_bancaria = input("Digite o que deseja realizar [Saque]-[Deposito]-[Extrato]-[Sair]: ") 
        try:
            _comando = _lista_de_operacoes[_operacao_bancaria.lower()]
            _comando()
        except (KeyError, ValueError):
            clean_terminal()
            _comando = _lista_de_operacoes["erro"]
            _comando()

        

def _verificar_valor(operacao=str):
        """Função responsável pela verificação do valor"""
        clean_terminal()
        while True:
            print(f"A operação é {operacao}")
            _valor_operacao = input("Digite o valor que deseja inserir/sacar: R$")

            if _valor_operacao.lower() == "sair":
                return "falsy"

            try:
                _valor_operacao = float(_valor_operacao)
                if _valor_operacao < 0:
                    raise ValueError
                
            except ValueError:
                clean_terminal()
                print("O valor a ser depositado precisa ser um número positivo e real.")
                continue
            break
        return (operacao, _valor_operacao)


def _sacar():
    """Função para sacar valores"""
    global _SAQUES_MAX, _VALOR_SAQUES, _saldo_total
    _a_sacar = _verificar_valor
    _sacando = _a_sacar(operacao="Saque")
    if "falsy" in _sacando:
        ...
    else:
        if _SAQUES_MAX == 0:
            print("Você já atingiu o limite de saques diários. Cancelando operação.")
        
        elif (_VALOR_SAQUES - (_sacando[1])) < 0:
            print("Você já atingiu o limite de valor diário a ser sacado.")
            print(f"Te restam R${_VALOR_SAQUES} para hoje.")
        
        elif (_saldo_total - (_sacando[1])) < 0:
            print("Você não possui saldo suficiente.")

        else:
            _SAQUES_MAX -= 1
            _VALOR_SAQUES -= _sacando[1]
            _operacoes_feitas.append(_sacando)
            _saldo_total -= _operacoes_feitas[-1][1]


def _depositar():
    """Função responsável pelo depósito"""
    global _saldo_total
            
    _a_depositar = _verificar_valor
    _depositando = _a_depositar(operacao="Depósito")
    if "falsy" in _depositando:
        ...
    else:
        _operacoes_feitas.append(_depositando)
        _saldo_total += _operacoes_feitas[-1][1]
    

def _ver_extrato():
    """Função para exibir cada operação realizada."""
    global _saldo_total

    clean_terminal()
    print("============EXTRATO============")
    for n, (op, vl) in enumerate(_operacoes_feitas):
        print(f"{n}. {op} de R${vl:.2f}")
    print("===============================")

    print('\n')
    print(f"Seu saldo total é R${_saldo_total:.2f}")


sistema_bancario()