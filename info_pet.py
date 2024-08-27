def coletar_informacoes_pet():

    print("Por favor, insira as informações sobre seu pet.")

    nome = input("Nome do pet: ")

    idade = coleta_informacao(
        mensagem_input="Idade do pet (em anos): ",
        tipo_input=int,
        condicao_input_invalido=lambda idade: idade < 0,
        mensagem_erro="Por favor, insira um número válido para a idade. A idade deve ser numérica e não pode ser negativa",
    )

    peso = coleta_informacao(
        mensagem_input="Peso do pet (em kg): ",
        tipo_input=float,
        condicao_input_invalido=lambda peso: peso < 0,
        mensagem_erro="Por favor, insira um número válido para o peso. O peso deve ser numérico e não pode ser negativo",
    )

    print("\nInformações do pet:")
    print(f"Nome: {nome}")
    print(f"Idade: {idade} {'ano' if idade == 1 else 'anos'}")
    print(f"Peso: {peso} kg")

def coleta_informacao(
    mensagem_input: str,
    tipo_input: type,
    condicao_input_invalido: callable,
    mensagem_erro: str,
) -> type:
    """
    Coleta e valida uma informação do usuário.

    Args:
        mensagem_input (str): Mensagem exibida ao usuário para solicitação de entrada.
        tipo_input (type): Tipo de dado esperado (ex: int, float).
        condicao_input_invalido (callable): Função que verifica se o input digitado é invalido.
        mensagem_erro (str): Mensagem exibida em caso de entrada inválida.

    Returns:
        type: Valor validado e convertido para o tipo especificado.
    """
    while True:
        try:
            valor = tipo_input(input(mensagem_input))
            if condicao_input_invalido(valor):
                print(mensagem_erro)
            else:
                return valor
        except ValueError:
            print(mensagem_erro)

coletar_informacoes_pet()
