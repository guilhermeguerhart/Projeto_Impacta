RESET = "\033[0m"
AZUL = "\033[94m"
CIANO = "\033[96m"
VERDE = "\033[92m"
AMARELO = "\033[93m"
NEGRITO = "\033[1m"


def mostrar_cabecalho():
	print(f"{AZUL}{NEGRITO}+{'=' * 46}+{RESET}")
	print(f"{AZUL}{NEGRITO}|{RESET}             RESERVA DE INGRESSOS              {AZUL}{NEGRITO}|{RESET}")
	print(f"{AZUL}{NEGRITO}+{'=' * 46}+{RESET}")


def coletar_dados():
	nome_cliente = input("Nome do cliente: ")
	evento = input("Nome do evento: ")
	quantidade = int(input("Quantidade de ingressos: "))
	preco = float(input("Preco do ingresso: "))
	percentual_desconto = float(input("Percentual de desconto (em %): "))
	return nome_cliente, evento, quantidade, preco, percentual_desconto


def calcular_reserva(quantidade, preco, percentual_desconto):
	subtotal = preco * quantidade
	desconto = subtotal * (percentual_desconto / 100)
	total = subtotal - desconto
	return subtotal, desconto, total


def mostrar_resumo(nome_cliente, evento, quantidade, preco, percentual_desconto, subtotal, desconto, total):
	print()
	print(f"{CIANO}{NEGRITO}  RESUMO DA RESERVA{RESET}")
	print(f"  Cliente: {nome_cliente}")
	print(f"  Evento: {evento}")
	print(f"  Quantidade: {quantidade}")
	print(f"  Preco unitario: R$ {preco:.2f}")
	print(f"  Subtotal: R$ {subtotal:.2f}")
	print(f"  Desconto ({percentual_desconto:.2f}%): R$ {desconto:.2f}")
	print(f"  Total: {VERDE}R$ {total:.2f}{RESET}")


def main():
	mostrar_cabecalho()
	dados = coletar_dados()
	nome_cliente, evento, quantidade, preco, percentual_desconto = dados
	subtotal, desconto, total = calcular_reserva(quantidade, preco, percentual_desconto)
	mostrar_resumo(nome_cliente, evento, quantidade, preco, percentual_desconto, subtotal, desconto, total)
	print(f"{AZUL}{NEGRITO}+{'=' * 46}+{RESET}")
	print(f"{VERDE}Reserva realizada com sucesso!{RESET}")


if __name__ == "__main__":
	main()
