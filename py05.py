RESET = "\033[0m"
AZUL = "\033[94m"
CIANO = "\033[96m"
VERDE = "\033[92m"
VERMELHO = "\033[91m"
AMARELO = "\033[93m"
NEGRITO = "\033[1m"

LEITORES = ('Daniela', 'Roberta', 'Joana')
LIVROS = ('Python', 'Java', 'C++')
OPCOES = ('sair', 'continuar')


def mostrar_cabecalho():
    print(f"{AZUL}{NEGRITO}+{'=' * 46}+{RESET}")
    print(f"{AZUL}{NEGRITO}|{RESET}              SISTEMA DA BIBLIOTECA             {AZUL}{NEGRITO}|{RESET}")
    print(f"{AZUL}{NEGRITO}+{'=' * 46}+{RESET}")


def autenticar_leitor():
    leitor = input("Digite o nome do leitor: ")

    if leitor in LEITORES:
        print(f"{VERDE}Leitor encontrado com sucesso!{RESET}")
        return leitor

    print(f"{VERMELHO}Leitor nao encontrado. Acesso negado.{RESET}")
    return None


def verificar_livro():
    livro = input("Digite o nome do livro: ")

    if livro in LIVROS:
        print(f"{VERDE}Livro disponivel para emprestimo!{RESET}")
        return livro

    print(f"{VERMELHO}Livro nao encontrado na biblioteca.{RESET}")
    return None


def controlar_sessao():
    opcao = input("Digite 'sair' ou 'continuar' para encerrar a sessao: ")

    if opcao == OPCOES[0]:
        print(f"{AMARELO}Sessao encerrada. Ate logo!{RESET}")
    else:
        print(f"{CIANO}A sessao continuara.{RESET}")


def mostrar_resumo(leitor, livro):
    print()
    print(f"{CIANO}{NEGRITO}  RESUMO DO ATENDIMENTO{RESET}")
    print(f"  Leitor: {leitor}")
    print(f"  Livro selecionado: {livro}")
    print("  Status: consulta autorizada")


def main():
    mostrar_cabecalho()
    leitor = autenticar_leitor()

    if leitor is None:
        return

    livro = verificar_livro()

    if livro is None:
        return

    mostrar_resumo(leitor, livro)
    controlar_sessao()
    print(f"{AZUL}{NEGRITO}+{'=' * 46}+{RESET}")


if __name__ == "__main__":
    main()
