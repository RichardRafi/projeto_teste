# Análise estatística da base de dados de pessoas com diabetes nos EUA

Este projeto de estatística tem como objetivo explorar e analisar dados estatísticos relacionados ao diabetes nos Estados Unidos, utilizando um grande conjunto de dados coletados pelo Behavioral Risk Factor Surveillance System (BRFSS) em 2015. A análise busca identificar padrões e fatores associados ao diabetes, com foco em características socioeconômicas, comportamentos de risco e condições de saúde, para contribuir no combate à prevalência dessa doença e apoiar estratégias de saúde pública.

O diabetes é uma das doenças crônicas mais prevalentes nos Estados Unidos, afetando milhões de pessoas e causando sérias complicações de saúde, como doenças cardíacas, perda de visão, amputações e problemas renais. Em 2018, cerca de 34,2 milhões de americanos foram diagnosticados com diabetes e outros 88 milhões apresentavam pré-diabetes, sendo que grande parte dessas pessoas não tinham conhecimento de sua condição.

Os custos associados ao diabetes são alarmantes, com despesas anuais estimadas em cerca de $400 bilhões, considerando diagnósticos de diabetes, pré-diabetes e casos não diagnosticados. A doença também afeta desproporcionalmente indivíduos de baixa renda e menor escolaridade, destacando a necessidade de intervenções direcionadas.

![Imagem](imagens/diabetes.jpg)

Os objetivos específicos incluem:

1. Identificar os fatores de risco associados ao diabetes:

A análise pretende examinar como fatores como idade, renda, escolaridade, hábitos de vida (como alimentação, consumo de álcool, tabagismo e atividade física) e condições de saúde impactam o risco de diabetes.

2. Compreender as disparidades socioeconômicas e demográficas:

Avaliar como o diabetes varia entre diferentes grupos socioeconômicos e demográficos, como renda, raça, nível de educação e localização, para entender melhor como essas desigualdades afetam a prevalência da doença.



## Organização do projeto

```
├── .gitignore         <- Arquivos e diretórios a serem ignorados pelo Git
├── ambiente.yml       <- O arquivo de requisitos para reproduzir o ambiente de análise
├── LICENSE            <- Licença de código aberto (MIT)
├── README.md          <- README principal para desenvolvedores que usam este projeto.
|
├── dados              <- Arquivos de dados para o projeto.
|
|
├── notebooks          <- Jupyter Notebook.
│
|   └──src             <- Código-fonte para uso neste projeto.
|      │
|      ├── __init__.py  <- Torna um módulo Python
|      ├── config.py    <- Configurações básicas do projeto
|      └── estatistica.py  <- Funções criadas para este projeto.
|
├── referencias        <- Dicionários de dados.
|
├── imagens         <- Imagens utilizadas no projeto

```

## Configuração do ambiente

1. Faça o clone do repositório que será criado a partir deste modelo.

    ```bash
    git clone ENDERECO_DO_REPOSITORIO
    ```

2. Crie um ambiente virtual para o seu projeto utilizando o gerenciador de ambientes de sua preferência.


```bash
conda env export > ambiente.yml
```

## Um pouco mais sobre a base

[Clique aqui](referencias/01_dicionario_de_dados.md) para ver o dicionário de dados da base utilizada

## Resumo dos principais resultados

Com base nos gráficos apresentados:

1. Diabetes por variáveis categóricas:
   
- Pressão Alta, Colesterol Alto e Problemas Cardíacos: Pessoas com essas condições apresentam uma alta associação com o diagnóstico de diabetes. Por exemplo, cerca de 75% dos indivíduos com problemas cardíacos têm diabetes.
- Atividade Física e Consumo de Frutas e Legumes: Há uma menor prevalência de diabetes entre pessoas que praticam atividade física e consomem frutas e legumes regularmente.
- Sem Dinheiro para Consultas: Há uma maior prevalência de diabetes entre pessoas que relatam dificuldade em pagar consultas médicas.
- Dificuldade para Andar: Pessoas com dificuldades de locomoção apresentam uma alta prevalência de diabetes.
- Gênero e Plano de Saúde: Não há uma diferença tão significativa na prevalência de diabetes entre homens e mulheres, e também não há para aqueles que tem plano de saúde ou não.
- Pessoas com diabetes tem uma tendência de piora em seu estado de saúde, sendo que mais de 70% das pessoas que declararam ter saúde Aceitável ou Ruim, tem a doença.
- A renda e nível de ensino superiores tendem a ter menor quantidade de pessoas com diabetes, já que elas tem maior acesso a prevenção e/ou tratamento dos que tem uma renda, ou nível de estudo inferior.
- Pessoas com idades mais avançadas são mais propensas a ter diabetes, já que há um aumento expressivo da porcentagem na faixa das pessoas entre 45-49 anos.

2. Distribuição de SaudeGeral por nível de ensino:

- As pessoas que estão na faixa de ensino do Secundário para Faculdade + tem uma melhor qualidade de saúde do que da faixa do Sem Estudo para Secundário Incompleto
- Isto influencia na questão da Faixa da Renda, pessoas que estão na faixa de ensino do Secundário para Faculdade + tem melhor renda que os demais, o que facilitaria o acesso ao tratamento médico do que os outros níveis.

3. Coeficiente de Spearman:

- Os resultados apresentados no Coeficiente de Spearman mostram a correlação entre as variáveis categóricas, e nela podemos tirar algumas conclusões, como o fato de uma pessoa com diabetes ter uma correlação significantemente alta em relação a saúde geral (0.41), Pressão Alta (0.38) e Colesterol Alto (0.29), isso pode ser considerado em outras colunas, como Pressão Alta x Faixa Idade por exemplo.

- Falando de valores negativos, podemos tirar conclusões, como por exemplo, pessoas que praticam atividade física são menos propensas a ter dificuldades de andar (-0.27) e ter uma melhor saúde geral (-0.27), e pessoas com Faixa de Renda superior ou inferior, tendem a influenciar na saúde geral, na qual vimos no 2º tópico dos resultados, e etc.
