import numpy as np

def aplicar_features(df):

    # Renomear as colunas para português
    df_Portugues = df.rename(columns={'age': 'idade', 'experience' : 'tempo_de_trabalho', 'income': 'renda_anual'})

    # Criando novas colunas para análise
    tempo = df_Portugues['tempo_de_trabalho'].replace(0, np.nan)

    df_Portugues['renda_por_ano_de_experiencia'] = df_Portugues['renda_anual'] / tempo
    df_Portugues['renda_por_idade'] = df_Portugues['renda_anual'] / df_Portugues['idade']
    df_Portugues['proporcao_trabalho'] = df_Portugues['tempo_de_trabalho'] / df_Portugues['idade'] 
    df_Portugues['idade_inicio_carreira'] = df_Portugues['idade'] - df_Portugues['tempo_de_trabalho']
    df_Portugues['log_renda'] = np.log(df_Portugues['renda_anual'])

    return df_Portugues