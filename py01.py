RESET = "\033[0m"
AZUL = "\033[94m"
CIANO = "\033[96m"
VERDE = "\033[92m"
AMARELO = "\033[93m"
NEGRITO = "\033[1m"

nome_usuario = input("Digite seu nome: ")
nome = "Python"
mensagem = "Matematica calcula um resultado; expressao representa esse calculo em texto."
texto = "2 + 3 * 4"
matematica = 2 + 3 * 4
expressao = texto + " = " + str(matematica)
expressao1 = f"{texto} = {matematica}"
texto_parenteses = "(2 + 3) * 4"
matematica_parenteses = (2 + 3) * 4
expressao_parenteses = f"{texto_parenteses} = {matematica_parenteses}"

print(f"{VERDE}{NEGRITO}Bem-vindo(a), {nome_usuario}!{RESET}")
print()
print(f"{AZUL}{NEGRITO}+{'=' * 46}+{RESET}")
print(f"{AZUL}{NEGRITO}|{RESET}              {CIANO}PYTHON LAB{RESET}                 {AZUL}{NEGRITO}|{RESET}")
print(f"{AZUL}{NEGRITO}+{'=' * 46}+{RESET}")
print(f"{AMARELO}  Linguagem:{RESET} {nome}")
print(f"{AMARELO}  Mensagem:{RESET}  Ola, {nome_usuario}!")
print(f"  {mensagem}")
print()
print(f"{CIANO}{NEGRITO}  CALCULO{RESET}")
print(f"  Matematica: {texto} = {VERDE}{matematica}{RESET}")
print(f"  Com parenteses: {texto_parenteses} = {VERDE}{matematica_parenteses}{RESET}")
print("  E o resultado calculado pelo Python.")
print()
print(f"{CIANO}{NEGRITO}  FORMATACAO{RESET}")
print(f"  Expressao em texto: {expressao}")
print("  E a conta escrita como texto, sem calcular automaticamente.")
print(f"  Com f-string:       {expressao1}")
print(f"  Com parenteses:     {expressao_parenteses}")
print(f"{AZUL}{NEGRITO}+{'=' * 46}+{RESET}")
