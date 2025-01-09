import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy.stats import (
    levene,
    ttest_ind, 
    mannwhitneyu
)


        
def analise_levene(dataframe, alfa=0.05, centro="mean"):
    print("Teste de Levene")
    
    estatistica_levene, valor_p_levene = levene(
        *[dataframe[coluna] for coluna in dataframe.columns], 
        center=centro, 
        nan_policy="omit"
    )
        
    print(f"{estatistica_levene=:.3f}")
    if valor_p_levene > alfa:
        print(f"Variâncias iguais (valor p: {valor_p_levene:.3f})")
    else:
        print(f"Ao menos uma variância é diferente (valor p: {valor_p_levene:.3f})")


def analise_ttest_ind(
    dataframe,
    alfa=0.05,
    variancias_iguais=True,
    alternativa="two-sided",
):
    print("Teste T de Student")
    estatistica_ttest, valor_p_ttest = ttest_ind(
        *[dataframe[coluna] for coluna in dataframe.columns], 
        equal_var=variancias_iguais,
        alternative=alternativa,
        nan_policy="omit"
    )
        
    print(f"{estatistica_ttest=:.3f}")
    if valor_p_ttest > alfa:
        print(f"Não podemos rejeitar a hipótese nula (valor p: {valor_p_ttest:.3f})")
    else:
        print(f"Rejeitamos a hipótese nula (valor p: {valor_p_ttest:.3f})")


def analise_mannwhitneyu(
    dataframe,
    alfa=0.05,
    alternativa="two-sided",
):
    print("Teste Mann-Whitney")
    estatistica_mw, valor_p_mw = mannwhitneyu(
        *[dataframe[coluna] for coluna in dataframe.columns],
        nan_policy="omit",
        alternative=alternativa
    )

    
    print(f"{estatistica_mw=:.3f}")
    if valor_p_mw > alfa:
        print(f"Não podemos rejeitar a hipótese nula (valor p: {valor_p_mw:.3f})")
    else:
        print(f"Rejeitamos a hipótese nula (valor p: {valor_p_mw:.3f})")


def remove_outliers(dados, largura_bigodes=1.5):
    """
    Remove outliers de um conjunto de dados com base no IQR (Intervalo Interquartil).

    Parâmetros:
    dados (pandas.Series ou pandas.DataFrame): Conjunto de dados para processar.
    largura_bigodes (float): Multiplicador do IQR para definir os limites dos bigodes.

    Retorno:
    pandas.Series ou pandas.DataFrame: Dados sem os outliers.
    """
    q1 = dados.quantile(0.25)  # Primeiro quartil (25%)
    q3 = dados.quantile(0.75)  # Terceiro quartil (75%)
    iqr = q3 - q1              # Intervalo interquartil (IQR)
    
    # Filtra os dados dentro dos limites
    dados_sem_outliers = dados[
        (dados >= q1 - largura_bigodes * iqr) & (dados <= q3 + largura_bigodes * iqr)
    ]
    return dados_sem_outliers

