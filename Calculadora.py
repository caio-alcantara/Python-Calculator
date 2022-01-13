# Um programa que mostra na tela um menu com opções básicas de uma calculadora.
# Por fim, essa calculadora irá realizar operações de soma, subtração, multiplicação e divisão
# com quaisquer dois números digitados pelo usuário.
# O programa também conta com um sistema de validação de entrada de dados.

from time import sleep


def menuCalculadora():
    """
    Esta função imprime na tela um menu de uma calculadora simples.
    :return:
    """
    funcoes = ['ADIÇÃO', 'SUBTRAÇÃO', 'MULTIPLICAÇÃO', 'DIVISÃO [N1/N2]', 'SAIR DA CALCULADORA']
    print('-' * 32)
    print(f"{'CALCULADORA PYTHON':^30}")
    print('-' * 32)
    for index, item in enumerate(funcoes):
        print(f"{f'[{index+1}]':>9} {item}")
    print('-' * 32)


def leiaValor(text):
    """
    Esta função lê e valida o input de um float, a fim de que, caso o usuário digite algo inválido, seja retornada
    uma mensagem de erro, e o usuário seja possibilitado de digitar o valor novamente.
    :param text: Texto que será exibido no input.
    :return: O valor, já tratado, digitado pelo usuário.
    """
    valor = 0
    while True:
        try:
            valor = float(input(text))
        except (ValueError, TypeError):
            print("\33[31mVocê não digitou um valor válido. Tente novamente!\33[m")
            continue
        else:
            break
    return valor


def leiaOperacao(text):
    """
    Esta função lê e valida o input de um usuário, sendo que esse input só pode ser de um número de 1 a 5.
    :param text: Texto que será exibido no input.
    :return: O valor, já tratado, digitado pelo usuário.
    """
    operation = 0
    while True:
        try:
            operation = int(input(text))
            while operation == 0 or operation > 5:
                print("\33[31mVocê não digitou um valor válido. Tente novamente!\33[m")
                continue
        except (ValueError, TypeError):
            print("\33[31mVocê não digitou um valor válido. Tente novamente!\33[m")
            continue
        finally:
            break
    return operation


def textoComLinha(text):
    """
    Esta função imprime na tela um texto formatado com "-" que irão se adaptar ao tamanho do texto.
    :param text: Texto que se quer colocar nessa formatação
    Ex: -------------------
        ENCERRANDO PROGRAMA
        -------------------
    :return:
    """
    print('-' * len(text))
    print(text)
    print('-' * len(text))


# Programa principal

print("Bem-vindo à Calculadora Python. Digite dois \33[32mvalores\33[m e escolha uma \33[33moperação\33[m para começar!"
      )

while True:

    menuCalculadora()

    num1 = leiaValor("Digite o primeiro valor: ")
    num2 = leiaValor("Digite o segundo valor: ")
    operacao = leiaOperacao("Qual operação você deseja realizar com esses dois números? [\33[32m1, 2, 3, 4\33[m "
                            "\33[33m(5 para sair)\33[m] ")

    if operacao == 1:
        sleep(0.3)
        textoComLinha(f"{num1} + {num2} = {num1 + num2:.2f}")
        sleep(0.3)

    if operacao == 2:
        sleep(0.3)
        textoComLinha(f"{num1} - {num2} = {num1 - num2:.2f}")
        sleep(0.3)

    if operacao == 3:
        sleep(0.3)
        textoComLinha(f"{num1} * {num2} = {num1 * num2:.2f}")
        sleep(0.3)

    if operacao == 4:
        sleep(0.3)
        try:
            textoComLinha(f"{num1} / {num2} = {num1 / num2:.2f}")
        except ZeroDivisionError:
            textoComLinha("Não é possível dividir por ZERO.")
        sleep(0.3)

    if operacao == 5:
        textoComLinha("ENCERRANDO PROGRAMA")
        break
