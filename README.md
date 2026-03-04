# 📊 Análise de Renda vs Experiência

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange)
![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-purple)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

Projeto de Data Analytics que investiga o impacto dos anos de experiência profissional na renda anual, utilizando análise exploratória, testes estatísticos e modelagem preditiva.
O objetivo é simular um cenário real de apoio à decisão em políticas salariais e planejamento de carreira.

Este projeto foi desenvolvido como parte de um portfólio para demonstrar habilidades em **Python, análise de dados, estatística e visualização**.

---

## 🎯 Perguntas de Negócio

* Como o nível de experiência impacta a renda anual?
* Existe uma relação direta entre anos de experiência e crescimento salarial?
* Como a experiência impacta o crescimento salarial?

---

## 🧠 Técnicas Utilizadas

* Limpeza e preparação de dados
* Engenharia de features
* Estatística descritiva
* Análise de correlação
* Teste de hipótese
* Regressão linear
* Visualização de dados

---

## 🛠️ Tecnologias e Bibliotecas

* Python 3
* Pandas
* NumPy
* Matplotlib
* Seaborn
* SciPy
* Scikit-learn
* Streamlit (para dashboard)

---

## 📁 Estrutura do Projeto

```
Projeto 6 - Analise de salarios/
│
├── data/
│   ├── income.csv
│   ├── income_tratado.csv
|   └── source.txt
│
├── notebooks/
│   └── analise_renda_experiencia.ipynb
│
├── src/
│   ├── load_data.py
│   ├── feature_engineering.py
│   ├── analysis.py
│   ├── statistics.py
│   ├── modeling.py
│   ├── save_data.py
│   └── conclusion.py
│
├── app.py
├── main.py
├── requirements.txt
└── README.md
```

---

## ▶️ Como Executar o Projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2. Criar ambiente virtual

```bash
python -m venv venv
```

### 3. Ativar o ambiente

**Windows**

```bash
venv\Scripts\activate
```

**Linux / Mac**

```bash
source venv/bin/activate
```

### 4. Instalar dependências

```bash
pip install -r requirements.txt
```

---

## 🔎 Executar análise no terminal

```bash
python main.py
```

---

## 🌐 Executar o dashboard interativo (Streamlit)

```bash
streamlit run app.py
```

---

## 📈 Principais Insights

* Foi identificada correlação forte (r > 0.80) entre experiência e renda.
* O modelo de regressão linear explicou aproximadamente 65% da variabilidade salarial.
* O teste t indicou diferença estatisticamente significativa (p < 0.05) entre profissionais juniores e experientes.

---

## 📊 Resultados do Modelo
* R²: 0.65
* MAE: $3.300
* Correlação entre experiência e renda: 0.83

---

## 📚 Notebook da Análise

O notebook com toda a análise exploratória e estatística está disponível em:

```
notebooks/analise_renda_experiencia.ipynb
```

---

## 🚀 Possíveis Melhorias Futuras

* Adicionar novos datasets
* Implementar modelos de machine learning mais robustos
* Deploy do dashboard online
* Criação de um pipeline automatizado de dados

---

## 👤 Autor

**Gabriel**
📊 Data Analytics | Data Science | Python
🌎 Interesse em oportunidades remotas e internacionais

---

## 📄 Licença

Este projeto está sob a licença MIT.
