import pandas as pd

def salvar_dados(df):
    caminho = 'data/income_tratado.csv'
    df.to_csv(caminho, index=False)
    resposta = f"Dados salvos com sucesso em: {caminho}"
    return resposta