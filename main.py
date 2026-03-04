from src.statistics import matriz_correlacao, teste_junior_vs_especialista
from src.modeling import modelo_regressao
from src.load_data import carregar_dados
from src.analysis import contagem_experiencia, plotagem
from src.feature_engineering import aplicar_features
from src.save_data import salvar_dados
from src.conclusion import conclusao

def main():
    # Introdução
    print("Perguntas centrais da análise:")
    print(" - Como o nível de experiência impacta a renda anual dos funcionários?")
    print(" - Qual a relação entre tempo de experiência e crescimento salarial?")
    print(" - Como a experiência impacta o crescimento salarial?")
    print('-' * 80)

    # Carregar os dados
    df = carregar_dados()

    # Aplicar as features
    df = aplicar_features(df)

    # Análise de contagem por nível de experiência
    df_contagem = contagem_experiencia(df)
    print(df_contagem)
    print('-' * 80)

    # Analises estatísticas
    corr = matriz_correlacao(df)
    print("Top correlações com renda anual:\n")
    print(corr.drop('renda_anual').head(4))

    stat, p = teste_junior_vs_especialista(df)
    print("\nTeste estatístico (Especialista vs Junior)")
    print(f"p-valor: {p:.6g}")
    if p < 0.05:
        print("Diferença estatisticamente significativa entre os grupos.")
    else:
        print("Diferença NÃO significativa entre os grupos.")

    modelo = modelo_regressao(df)
    print("\nModelo de regressão:")
    print(f"Cada ano adicional de experiência aumenta a renda em média ${modelo.coef_[1]:,.2f}.")
    print('-' * 80)

    # Visualizações
    print("Gerando visualizações da análise...")
    print('-' * 80)
    plotagem(df, df_contagem)
    
    # Salvar os dados tratados
    caminho = salvar_dados(df)
    print(caminho)
    print('-' * 80)

    #Conclusão
    conclusao()

if __name__ == "__main__":
    main()
