import json

with open('countries_data.json', 'r') as file:
    dados_paises = json.load(file)

unidades = {
    "Population": "milhões de pessoas",
    "GDP": "bilhões de dólares",
    "Total Energy Production": "bilhões de kWh",
    "Nuclear Energy Production": "bilhões de kWh",
    "Wind Energy Production": "bilhões de kWh"
}


def apresenta_dado(dado):
    unidade = unidades.get(dado, "")
    print(f"\nValores de {dado} para todos os países ({unidade}):")
    for pais, info in dados_paises.items():
        valor = info.get(dado)
        if valor is not None:
            print(f"{pais}: {valor:.2f} {unidade}")
        else:
            print(f"{pais}: Dados de {dado} não disponíveis.")
    print("\n")


def apresenta_pais(pais):
    info = dados_paises.get(pais)
    if info:
        print(f"\nDados para {pais}:")
        for dado, valor in info.items():
            unidade = unidades.get(dado, "")
            print(f"{dado}: {valor:.2f} {unidade}")
    else:
        print("\n*** País não encontrado. ***\n")


def calcular_media(dado):
    valores = [info[dado] for info in dados_paises.values() if dado in info]
    unidade = unidades.get(dado, "")
    if valores:
        media = sum(valores) / len(valores)
        print(f"Média de {dado}: {media:.2f} {unidade}")
    else:
        print("\n*** Dados não disponíveis para o cálculo. ***\n")


def calcular_variancia(dado):
    valores = [info[dado] for info in dados_paises.values() if dado in info]
    unidade = unidades.get(dado, "")
    if valores:
        media = sum(valores) / len(valores)
        variancia = sum((x - media) ** 2 for x in valores) / len(valores)
        print(f"Variância de {dado}: {variancia:.2f} {unidade}²")
    else:
        print("\n*** Dados não disponíveis para o cálculo. ***\n")


def calcular_media_ponderada(dado, ponderador):
    valores = [(info[dado], info[ponderador]) for info in dados_paises.values() if dado in info and ponderador in info]
    unidade = unidades.get(dado, "")
    if valores:
        numerador = sum(valor * peso for valor, peso in valores)
        denominador = sum(peso for _, peso in valores)
        media_ponderada = numerador / denominador
        print(f"Média ponderada de {dado} (ponderado por {ponderador}): {media_ponderada:.2f} {unidade}")
    else:
        print("\n*** Dados não disponíveis para o cálculo. ***\n")


def calcular_correlacao(var1, var2):
    dados = [(info[var1], info[var2]) for info in dados_paises.values() if var1 in info and var2 in info]
    unidade1 = unidades.get(var1, "")
    unidade2 = unidades.get(var2, "")
    if dados:
        media_var1 = sum(x[0] for x in dados) / len(dados)
        media_var2 = sum(x[1] for x in dados) / len(dados)

        covariancia = sum((x[0] - media_var1) * (x[1] - media_var2) for x in dados) / len(dados)
        variancia_var1 = sum((x[0] - media_var1) ** 2 for x in dados) / len(dados)
        variancia_var2 = sum((x[1] - media_var2) ** 2 for x in dados) / len(dados)

        correlacao = covariancia / ((variancia_var1 ** 0.5) * (variancia_var2 ** 0.5))
        print(f"Correlação entre {var1} ({unidade1}) e {var2} ({unidade2}): {correlacao:.2f}")
    else:
        print("\n*** Dados insuficientes para cálculo da correlação. ***\n")


print(f"*********************************************************\n" +
      f"* Bem-vindo ao programa de análise de dados de energia! *"
      f"\n*********************************************************")

while True:
    print(f"\nQual opção você deseja escolher?\n"
          f"1 - Apresenta dado para todos os países\n"
          f"2 - Apresenta dados de um país\n"
          f"3 - Calcular média de um dado\n"
          f"4 - Calcular variância de um dado\n"
          f"5 - Calcular média ponderada de um dado\n"
          f"6 - Calcular correlação entre duas variáveis\n"
          f"7 - Sair\n")

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        dado = input(
            "Digite o dado que você deseja visualizar\n(ex.: Population, GDP, Total Energy Production, Nuclear Energy Production, Wind Energy Production): ")
        apresenta_dado(dado)
    elif opcao == 2:
        print("\nPaíses disponíveis: ", ", ".join(dados_paises.keys()))
        pais = input("Digite o país que você deseja visualizar: ")
        apresenta_pais(pais)
    elif opcao == 3:
        dado = input(
            "Digite o dado que você deseja calcular a média\n(ex.: Population, GDP, Total Energy Production, Nuclear Energy Production, Wind Energy Production): ")
        calcular_media(dado)
    elif opcao == 4:
        dado = input(
            "Digite o dado que você deseja calcular a variância\n(ex.: Population, GDP, Total Energy Production, Nuclear Energy Production, Wind Energy Production): ")
        calcular_variancia(dado)
    elif opcao == 5:
        dado = input(
            "Digite o dado que você deseja calcular a média ponderada\n(ex.: Population, GDP, Total Energy Production, Nuclear Energy Production, Wind Energy Production): ")
        ponderador = input("Digite o ponderador (ex.: Population, GDP): ")
        calcular_media_ponderada(dado, ponderador)
    elif opcao == 6:
        var1 = input(
            "Digite a primeira variável\n(ex.: Population, GDP, Total Energy Production, Nuclear Energy Production, Wind Energy Production): ")
        var2 = input("Digite a segunda variável: ")
        calcular_correlacao(var1, var2)
    elif opcao == 7:
        print("Saindo...")
        break
    else:
        print("\n*** Opção inválida. Tente novamente. ***\n")