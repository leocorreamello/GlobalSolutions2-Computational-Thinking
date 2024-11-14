import json
from functions import *

with open('countries_data.json', 'r') as file:
    dados_paises = json.load(file)

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
        dado = input("Digite o dado que você deseja visualizar\n(ex.: Population, GDP, Total Energy Production, Nuclear Energy Production, Wind Energy Production): ")
        apresenta_dado(dado, dados_paises)
    elif opcao == 2:
        print("Países disponíveis:" + ", ".join(dados_paises.keys()))
        pais = input("Digite o país que você deseja visualizar: ")
        apresenta_pais(pais, dados_paises)
    elif opcao == 3:
        dado = input("Digite o dado que você deseja calcular a média\n(ex.: Population, GDP, Total Energy Production, Nuclear Energy Production, Wind Energy Production): ")
        calcular_media(dado, dados_paises)
    elif opcao == 4:
        dado = input("Digite o dado que você deseja calcular a variância\n(ex.: Population, GDP, Total Energy Production, Nuclear Energy Production, Wind Energy Production): ")
        calcular_variancia(dado, dados_paises)
    elif opcao == 5:
        dado = input("Digite o dado que você deseja calcular a média ponderada\n(ex.: Population, GDP, Total Energy Production, Nuclear Energy Production, Wind Energy Production): ")
        ponderador = input("Digite o ponderador (ex.: Population, GDP): ")
        calcular_media_ponderada(dado, ponderador, dados_paises)
    elif opcao == 6:
        var1 = input("Digite a primeira variável\n(ex.: Population, GDP, Total Energy Production, Nuclear Energy Production, Wind Energy Production): ")
        var2 = input("Digite a segunda variável: ")
        calcular_correlacao(var1, var2, dados_paises)
    elif opcao == 7:
        print("Saindo...")
        break
    else:
        print("\n*** Opção inválida. Tente novamente. ***\n")
