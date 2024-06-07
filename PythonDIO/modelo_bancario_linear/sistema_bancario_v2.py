# Built-in Python Modules
import sys

# Self-Made Python Modules
from CleanTerminalModule import clean_terminal


def _menu_de_selecao():
    """This is a function that only calls an input. It'll return
    the input to the 'bank_system()' function."""
    _selecao = "Escolha uma das seguintes operações: \
                \n[Deposito] - [Saque] - [Extrato]\
                \n[NovoUsuario]-[NovaConta]-[Sair]\
                \n>>> "
    return input(_selecao)


def _deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato.append((f"Saque", {valor}))
    else:
        print("O valor informado é inválido. Insira um número real e positivo.")

    clean_terminal()
    return saldo, extrato


def _saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    _acima_saldo = valor > saldo
    _acima_limite = valor > limite
    _acima_saques = numero_saques >= limite_saques

    if _acima_saldo:
        print("Você não possui saldo o suficiente. Deposite antes de sacar novamente.")

    elif _acima_limite:
        print("Você já atingiu o limite. Para sacar novamente retorne amanhã.")

    elif _acima_saques:
        print("Você já atingiu o limite diário de saques. Tente novamente amanhã.")

    elif valor > 0:
        saldo -= valor
        extrato.append((f"Saque", {valor}))
        numero_saques += 1

    else:
        print("O valor inserido é invalido, insira um valor real ou positivo.")

    clean_terminal()
    return saldo, extrato


def _ver_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    for n, (op, vl) in enumerate(extrato):
        print(f"{n}. {op} de R${vl}")
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")
    print('\n')


def criar_usuario(usuarios):
    _cpf = input("CPF (somente número): ")
    _usuario_registrado = _filtrar_registros(_cpf, usuarios)

    if _usuario_registrado == True:
        print("Este CPF já está vinculado a outro usuário.")
        return

    nome = input("Nome completo: ")
    data_nascimento = input("Data de nascimento (dd-mm-aaaa): ")
    endereco = input("Endereço (rua, bairro, cidade e estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": _cpf, "endereco": endereco})


def _filtrar_registros(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def _criar_conta_bancaria(agencia, numero_conta, usuarios):
    _cpf = input("CPF do usuário: ")
    _usuario = _filtrar_registros(_cpf, usuarios)

    if _usuario:
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": _usuario}

    print("Usuário informado não reconhecido. Cancelando criação de conta.")


def bank_system():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    _saldo_total = 0
    _LIMITE_SAQUE = 500
    _extrato = []
    _qtd_saques = 0
    _usuarios = []
    _contas = []

    while True:
        _escolha = _menu_de_selecao()

        if _escolha.lower() == "deposito":
            clean_terminal()
            valor = float(input("Informe o valor do depósito: R$"))


            _saldo_total, _extrato = _deposito(_saldo_total, valor, _extrato)

        elif _escolha.lower() == "saque":
            clean_terminal()
            valor = float(input("Informe o valor do saque: R$"))

            _saldo_total, _extrato = _saque(
                saldo=_saldo_total,
                valor=valor,
                extrato=_extrato,
                limite=_LIMITE_SAQUE,
                numero_saques=_qtd_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif _escolha.lower() == "extrato":
            clean_terminal()
            _ver_extrato(_saldo_total, extrato=_extrato)

        elif _escolha.lower() == "novousuario":
            clean_terminal()
            criar_usuario(_usuarios)

        elif _escolha.lower() == "novaconta":
            clean_terminal()
            numero_conta = len(_contas) + 1
            conta = _criar_conta_bancaria(AGENCIA, numero_conta, _usuarios)

            if conta:
                _contas.append(conta)

        elif _escolha.lower() == "sair":
            break

        else:
            print("Operação não reconhecida, tente novamente.")

bank_system()()