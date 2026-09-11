RESET = "\033[0m"
AZUL = "\033[94m"
CIANO = "\033[96m"
VERDE = "\033[92m"
NEGRITO = "\033[1m"


def mostrar_cabecalho():
	print(f"{AZUL}{NEGRITO}+{'=' * 46}+{RESET}")
	print(f"{AZUL}{NEGRITO}|{RESET}             CALCULO DA HOSPEDAGEM              {AZUL}{NEGRITO}|{RESET}")
	print(f"{AZUL}{NEGRITO}+{'=' * 46}+{RESET}")


def calcular_hospedagem(preco, quantidade, desconto):
	valor_total = preco * quantidade
	valor_final = valor_total - desconto
	return valor_total, valor_final


def mostrar_resumo(preco, quantidade, desconto, valor_total, valor_final):
	print(f"{CIANO}{NEGRITO}  RESUMO DA RESERVA{RESET}")
	print("  Hospede: Maria")
	print(f"  Preco da diaria: R$ {preco:.2f}")
	print(f"  Quantidade de diarias: {quantidade}")
	print(f"  Valor total: R$ {valor_total:.2f}")
	print(f"  Desconto: R$ {desconto:.2f}")
	print(f"  Valor final: {VERDE}R$ {valor_final:.2f}{RESET}")
	print(f"  Diferenca: {valor_total:.2f} - {desconto:.2f} = {valor_final:.2f}")


def main():
	preco = 180.00
	quantidade = 3
	desconto = 50.00

	mostrar_cabecalho()
	valor_total, valor_final = calcular_hospedagem(preco, quantidade, desconto)
	mostrar_resumo(preco, quantidade, desconto, valor_total, valor_final)
	print(f"{AZUL}{NEGRITO}+{'=' * 46}+{RESET}")


if __name__ == "__main__":
	main()
