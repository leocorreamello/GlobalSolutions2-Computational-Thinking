![Green Flow](~Logo.png)

# Projeto de Análise de Dados de Países

## Introdução

Este projeto tem como objetivo analisar e apresentar dados estatísticos de diferentes países, com foco especial em informações sobre a produção de energia. A partir de um banco de dados contendo informações sobre população, PIB, produção total de energia, produção de energia nuclear e produção de energia eólica, o projeto oferece uma série de funções para realizar análises estatísticas como média, variância e correlação entre variáveis.

O projeto foi desenvolvido em Python, utilizando um dicionário para armazenar os dados dos países e uma estrutura modular de código que permite fácil manutenção e extensão. Os dados apresentados foram inspirados em fontes públicas de estatísticas globais e visam dar uma visão sobre os fatores que podem influenciar a adoção de energias limpas por cada país.

## Funcionalidades

O sistema inclui uma interface simples para consulta e análise dos dados, permitindo ao usuário selecionar diferentes opções de análise através do terminal. As principais funcionalidades oferecidas são:

- **Apresentar dados**: Permite visualizar os dados de um determinado indicador (como PIB ou produção de energia eólica) para todos os países.
- **Consultar dados por país**: Permite visualizar todos os dados disponíveis de um país específico.
- **Análise estatística**: Inclui funções para calcular média, variância, média ponderada e correlação entre variáveis selecionadas.

## Estrutura do Projeto

O projeto está dividido em dois módulos principais:

1. **main.py** - Responsável pela interface com o usuário, onde ocorre a interação principal. Recebe as entradas do usuário para selecionar as funções desejadas e exibe os resultados obtidos.
2. **functions.py** - Contém as funções de análise e manipulação de dados. Este módulo é responsável pelo cálculo das estatísticas como média, variância, média ponderada e correlação entre variáveis.
3. **countries_data.json** - Dicionário utilizado para os dados feito a mão.

## Fontes Utilizadas

<a href="https://www.bing.com/ck/a?!&&p=d8aad64dba69dc1f1876ee88dd6e1962985ce88cd7e5d8ef3d74453214c49c2eJmltdHM9MTczMTU0MjQwMA&ptn=3&ver=2&hsh=4&fclid=002cfa02-4b38-66b7-0f8f-ee054ae167c7&psq=popula%c3%a7%c3%a3o+dos+paises&u=a1aHR0cHM6Ly9wdC53aWtpcGVkaWEub3JnL3dpa2kvTGlzdGFfZGVfcGElQzMlQURzZXNfcG9yX3BvcHVsYSVDMyVBNyVDMyVBM28&ntb=1">Lista de países por população – Wikipédia</a>

<a href="https://www.bing.com/ck/a?!&&p=0f45d6205681c9981162fb1d2d613f96fe2dbd87c89a7092f2d4be64333696daJmltdHM9MTczMTU0MjQwMA&ptn=3&ver=2&hsh=4&fclid=002cfa02-4b38-66b7-0f8f-ee054ae167c7&psq=pib+dos+pa%c3%adses&u=a1aHR0cHM6Ly9wdC53aWtpcGVkaWEub3JnL3dpa2kvTGlzdGFfZGVfcGElQzMlQURzZXNfcG9yX1BJQl9ub21pbmFs&ntb=1">Lista de países por PIB nominal – Wikipédia</a>

<a href="https://www.bing.com/ck/a?!&&p=c976093ff367af5ad0fb736dd46fc089e71065085f600c4343596392fbc25ffcJmltdHM9MTczMTU0MjQwMA&ptn=3&ver=2&hsh=4&fclid=002cfa02-4b38-66b7-0f8f-ee054ae167c7&psq=Energia+ecologica+produzida+pelos+paises&u=a1aHR0cHM6Ly9leGFtZS5jb20vZWNvbm9taWEvb3MtMTAtcGFpc2VzLWxpZGVyZXMtZW0tZW5lcmdpYS1saW1wYS1uby1tdW5kby8&ntb=1">As 10 potências mundiais em energia limpa - Exame</a>

<article>
        <h2>Integrantes</h2>
                <h3><img src="https://avatars.githubusercontent.com/u/129889380?v=4" width="50px" alt="Pedro Guidotte Icon">  Pedro Guidotte | RM556630<a href="https://github.com/peguidotte" target="_blank" style="font-style: italic">  /GitHub <i class="fab fa-github"></i></a>
                <a href="https://www.linkedin.com/in/pedro-guidotte/" target="_blank" style="font-style: italic">  /LinkedIn<i class="fab fa-linkedin"></i></a></h3>
                <h3><img src="https://avatars.githubusercontent.com/u/158540749?v=4)" width="50px" alt="Gabriel Vara Icon">  Gabriel Vara | RM555355<a href="https://github.com/gabrielvara" target="_blank" style="font-style: italic"> 
 /GitHub <i class="fab fa-github"></i></a>
                <a href="https://www.linkedin.com/in/gabriel-vara" target="_blank" style="font-style: italic">  /LinkedIn <i class="fab fa-linkedin"></i></a></h3>
                <h3><img src="https://avatars.githubusercontent.com/u/158527393?v=4" width="50px" alt="Leonardo Correa Icon">  Leonardo Correa | RM555573<a href="https://github.com/leocorreamello" target="_blank" style="font-style: italic">  /GitHub <i class="fab fa-github"></i></a>
                <a href="https://www.linkedin.com/in/leocorreamello/" target="_blank" style="font-style: italic">  /LinkedIn <i class="fab fa-linkedin"></i></a></h3>
    </article>
