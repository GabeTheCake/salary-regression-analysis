import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def resumo_geral(df):
    return df.describe()

def contagem_experiencia(df):
    # Criar uma nova coluna 'nivel de experiencia' com base no tempo de trabalho
    bins = [-0.01, 2, 5, 10, float('inf')]
    labels = ['Junior', 'Pleno', 'Sênior', 'Especialista']
    df['nivel_de_experiencia'] = pd.cut(df['tempo_de_trabalho'], bins=bins, labels=labels, right = True)

    # Contar o número de funcionários em cada nível de experiência
    df_experiencia = df['nivel_de_experiencia'].value_counts().reset_index()
    df_experiencia.columns = ['nivel_de_experiencia', 'quantidade_funcionarios']

    # Calcular a renda média e mediana para cada nível de experiência
    df_experiencia = df.groupby('nivel_de_experiencia',observed=False).agg(
        quantidade_funcionarios=('renda_anual', 'count'),
        renda_media=('renda_anual', 'mean'),
        renda_mediana=('renda_anual', 'median')
    ).reset_index()
    return df_experiencia

def plotagem(df, df_contagem):
    sns.set_style("whitegrid")
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    sns.boxplot(x='nivel_de_experiencia', y='renda_anual', data=df, ax=axes[0])
    axes[0].set_title('Distribuição de renda por nivel de experiencia')
    axes[0].set_xlabel('Nivel de Experiencia')
    axes[0].set_ylabel('Renda Anual (USD)')
    
    sns.histplot(df['renda_anual'], bins=30, kde=True, ax=axes[1])
    axes[1].set_title('Distribuição da Renda Anual')
    axes[1].set_xlabel('Renda Anual (USD)')
    axes[1].set_ylabel('Frequência')

    sns.barplot(
        data = df_contagem, 
        x='nivel_de_experiencia', 
        y='quantidade_funcionarios', ax=axes[2])
    axes[2].set_title('Contagem de funcionários por nível de experiência')
    axes[2].set_xlabel('Nivel de Experiencia')
    axes[2].set_ylabel('Contagem')

    plt.suptitle("Visualizações principais da análise de renda", fontsize=14)
    plt.tight_layout()
    plt.show()