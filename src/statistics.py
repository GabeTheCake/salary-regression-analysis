from scipy.stats import ttest_ind

def matriz_correlacao(df):
    corr = df.corr(numeric_only=True)
    corr = corr["renda_anual"].sort_values(ascending=False)
    return corr

def teste_junior_vs_especialista(df):
    jun = df[df["nivel_de_experiencia"] == "Junior"]["renda_anual"]
    esp = df[df["nivel_de_experiencia"] == "Especialista"]["renda_anual"]

    stat, p = ttest_ind(esp, jun, equal_var=False)
    return stat, p