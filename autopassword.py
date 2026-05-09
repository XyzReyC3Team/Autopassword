# ==============================
#        XyzReyC3Team
# ==============================

import os
import random

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def logo():
    limpar()
    print("""
██╗  ██╗██╗   ██╗███████╗██████╗ ███████╗██╗   ██╗ ██████╗██████╗ ███████╗
╚██╗██╔╝╚██╗ ██╔╝╚══███╔╝██╔══██╗██╔════╝╚██╗ ██╔╝██╔════╝╚════██╗██╔════╝
 ╚███╔╝  ╚████╔╝   ███╔╝ ██████╔╝█████╗   ╚████╔╝ ██║      █████╔╝█████╗
 ██╔██╗   ╚██╔╝   ███╔╝  ██╔══██╗██╔══╝    ╚██╔╝  ██║     ██╔═══╝ ██╔══╝
██╔╝ ██╗   ██║   ███████╗██║  ██║███████╗   ██║   ╚██████╗███████╗███████╗
╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚══════╝   ╚═╝    ╚═════╝╚══════╝╚══════╝

                        XyzReyC3Team pt-br
""")

while True:
    logo()

    print("[1] Gerar senha + LETRAS")
    print("[2] Gerar senha + NÚMEROS")
    print("[3] Gerar senha + LETRAS + NÚMEROS")
    print("[4] Sair")

    opcao = input("\nEscolha: ")

    if opcao == "1":
        letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        senha = ""

        tamanho = int(input("\nTamanho da senha: "))

        for i in range(tamanho):
            senha += random.choice(letras)

        print("\nSenha gerada:")
        print(senha)

        input("\nENTER para continuar...")

    elif opcao == "2":
        numeros = "0123456789"
        senha = ""

        tamanho = int(input("\nTamanho da senha: "))

        for i in range(tamanho):
            senha += random.choice(numeros)

        print("\nSenha gerada:")
        print(senha)

        input("\nENTER para continuar...")

    elif opcao == "3":
        caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        senha = ""

        tamanho = int(input("\nTamanho da senha: "))

        for i in range(tamanho):
            senha += random.choice(caracteres)

        print("\nSenha gerada:")
        print(senha)

        input("\nENTER para continuar...")

    elif opcao == "4":
        print("\nSaindo...")
        break

    else:
        print("\nOpção inválida.")
        input("\nENTER para continuar...")