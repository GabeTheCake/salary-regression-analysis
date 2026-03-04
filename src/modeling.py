from sklearn.linear_model import LinearRegression

def modelo_regressao(df):
    X = df[["idade", "tempo_de_trabalho"]]
    y = df["renda_anual"]

    modelo = LinearRegression()
    modelo.fit(X, y)

    return modelo
