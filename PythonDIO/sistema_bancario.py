import sys
from CleanTerminalModule import clean_terminal

operacoes_feitas = []
saldo_total = 0
SAQUES_MAX = 3
VALOR_SAQUES = 500.00


def sistema_bancario():
    global saldo_total
    lista_de_operacoes = {
        "saque" : lambda:sacar(),
        "deposito" : lambda:depositar(),
        "extrato" : lambda:ver_extrato(),
        "sair" : lambda:sys.exit("Saindo do sistema"),
        "erro" : lambda:print("Algum erro ocorreu, tente novamente.")
}
    print("Seja bem vindo ao sistema bancário VicourtBitt. ")

    while True:
        operacao_bancaria = input("Digite o que deseja realizar [Saque]-[Deposito]-[Extrato]-[Sair]: ") 
        
        try:
            comando = lista_de_operacoes[operacao_bancaria.lower()]
            comando()
        except (KeyError, ValueError):
            clean_terminal()
            comando = lista_de_operacoes["erro"]
            comando()

        

def verificar_valor(operacao=str):
        """Função responsável pela verificação do valor"""
        clean_terminal()
        while True:
            print(f"A operação é {operacao}")
            valor_operacao = input("Digite o valor que deseja inserir/sacar: R$")

            if valor_operacao.lower() == "sair":
                return "falsy"

            try:
                valor_operacao = float(valor_operacao)
                if valor_operacao < 0:
                    raise ValueError
                
            except ValueError:
                clean_terminal()
                print("O valor a ser depositado precisa ser um número positivo e real.")
                continue
            break
        return (operacao, valor_operacao)


def sacar():
    """Função para sacar valores"""
    global SAQUES_MAX, VALOR_SAQUES, saldo_total
    a_sacar = verificar_valor
    sacando = a_sacar(operacao="Saque")
    if "falsy" in sacando:
        ...
    else:
        if SAQUES_MAX == 0:
            print("Você já atingiu o limite de saques diários. Cancelando operação.")
        
        elif (VALOR_SAQUES - (sacando[1])) < 0:
            print("Você já atingiu o limite de valor diário a ser sacado.")
            print(f"Te restam R${VALOR_SAQUES} para hoje.")
        
        elif (saldo_total - (sacando[1])) < 0:
            print("Você não possui saldo suficiente.")

        else:
            SAQUES_MAX -= 1
            VALOR_SAQUES -= sacando[1]
            operacoes_feitas.append(sacando)
            saldo_total -= operacoes_feitas[-1][1]


def depositar():
    """Função responsável pelo depósito"""
    global saldo_total
            
    a_depositar = verificar_valor
    depositando = a_depositar(operacao="Depósito")
    if "falsy" in depositando:
        ...
    else:
        operacoes_feitas.append(depositando)
        saldo_total += operacoes_feitas[-1][1]
    

def ver_extrato():
    """Função para exibir cada operação realizada."""
    global saldo_total

    clean_terminal()
    print("============EXTRATO============")
    for n, (op, vl) in enumerate(operacoes_feitas):
        print(f"{n}. {op} de R${vl:.2f}")
    print("===============================")

    print('\n')
    print(f"Seu saldo total é R${saldo_total:.2f}")



sistema_bancario()