RESET = "\033[0m"
AZUL = "\033[94m"
CIANO = "\033[96m"
VERDE = "\033[92m"
VERMELHO = "\033[91m"
NEGRITO = "\033[1m"

IDADE_MINIMA = 17


def mostrar_cabecalho():
    print(f"{AZUL}{NEGRITO}+{'=' * 46}+{RESET}")
    print(f"{AZUL}{NEGRITO}|{RESET}             CONTROLE DE ACESSO               {AZUL}{NEGRITO}|{RESET}")
    print(f"{AZUL}{NEGRITO}+{'=' * 46}+{RESET}")


def verificar_idade(idade):
    return idade >= IDADE_MINIMA


def verificar_ingresso():
    ingresso = input("Voce possui o ingresso? (sim/nao): ")
    return ingresso.lower() == "sim"


def mostrar_resultado(idade, possui_ingresso):
    print()
    print(f"{CIANO}{NEGRITO}  RESULTADO DA VERIFICACAO{RESET}")
    print(f"  Idade informada: {idade}")
    print(f"  Idade minima: {IDADE_MINIMA}")

    if possui_ingresso:
        print(f"  Ingresso: {VERDE}confirmado{RESET}")
        print(f"{VERDE}Acesso liberado! Divirta-se no nosso evento!{RESET}")
    else:
        print(f"  Ingresso: {VERMELHO}nao confirmado{RESET}")
        print("Voce nao possui o ingresso. Compre um ingresso para entrar.")


def main():
    mostrar_cabecalho()
    idade = int(input("Digite a sua idade: "))

    if not verificar_idade(idade):
        print(f"{VERMELHO}Acesso negado! Voce precisa ter 17 anos ou mais para entrar.{RESET}")
        return

    possui_ingresso = verificar_ingresso()
    mostrar_resultado(idade, possui_ingresso)


if __name__ == "__main__":
    main()
