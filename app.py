import streamlit as st
import pandas as pd
import plotly.express as px

from src.load_data import carregar_dados
from src.feature_engineering import aplicar_features
from src.analysis import contagem_experiencia

# Configuração da página
st.set_page_config(
    page_title="Portfolio | Análise de Renda",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilização Customizada (CSS)
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .insight-card {
        background-color: #e1f5fe;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #0288d1;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

def safe_metric(value, format_str):
    return format_str.format(value) if pd.notnull(value) else "Sem dados"

def main(df):
    df = aplicar_features(df)
    df_contagem = contagem_experiencia(df)

    # --- SIDEBAR ---
    st.sidebar.title("Filtros de Análise")
    st.sidebar.markdown("Use os filtros abaixo para refinar os dados visualizados.")
    
    # Filtro de Experiência
    niveis = st.sidebar.multiselect(
        "Nível de Experiência",
        options=sorted(df_contagem['nivel_de_experiencia'].dropna().unique()),
        default=sorted(df_contagem['nivel_de_experiencia'].dropna().unique())
    )
    
    # Filtro de Idade
    idade_min, idade_max = int(df['idade'].min()), int(df['idade'].max())
    filtro_idade = st.sidebar.slider("Faixa Etária", idade_min, idade_max, (idade_min, idade_max))

    # Aplicando filtros
    df_filtered = df[
        (df['nivel_de_experiencia'].isin(niveis)) & 
        (df['idade'].between(filtro_idade[0], filtro_idade[1]))
    ]

    # --- CORPO PRINCIPAL ---
    st.title("📊 Dashboard de Análise de Renda e Experiência")
    
    # Seção de Contexto
    st.markdown("""
        Este dashboard apresenta uma análise profunda sobre a estrutura remuneratória. 
        O objetivo é responder a perguntas estratégicas sobre carreira, senioridade e retorno financeiro sobre o tempo investido.
    """)

    # Linha 1: Métricas Principais
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Renda Média", safe_metric(df_filtered['renda_anual'].mean(), "R$ {:,.2f}"))
    with col2:
        st.metric("Idade Média", safe_metric(df_filtered['idade'].mean(), "{:.1f} anos"))
    with col3:
        st.metric("Tempo Médio Trampo", safe_metric(df_filtered['tempo_de_trabalho'].mean(), "{:.1f} anos"))
    with col4:
        st.metric("Amostras", len(df_filtered))

    st.markdown("---")

    # --- SEÇÃO DE PERGUNTAS E RESPOSTAS (INSIGHTS) ---
    st.subheader("💡 Conclusões da Análise")
    
    with st.container():
        # Pergunta 1
        st.markdown("**Como o nível de experiência impacta a renda anual dos funcionários?**")
        st.write("""
            O impacto é direto e escalonável. Observa-se que a transição entre níveis (ex: Sênior para Especialista) 
            apresenta saltos significativos na mediana salarial, indicando que a especialização técnica é o maior 
            alavancador de renda nesta base de dados.
        """)
        
        # Pergunta 2
        st.markdown("**Qual a relação entre tempo de experiência e crescimento salarial?**")
        st.write("""
            Existe uma correlação positiva clara, porém não linear. O crescimento é mais acentuado nos primeiros 10 anos, 
            estabilizando em patamares elevados após a maturidade profissional. O tempo de casa atua como um validador 
            de senioridade que reflete no bônus de renda anual.
        """)
        
        # Pergunta 3
        st.markdown("**Vale mais contratar profissionais experientes ou investir em juniores?**")
        st.write("""
            **Depende do objetivo:** Profissionais experientes (Especialistas/Sêniores) entregam maior valor imediato e 
            possuem uma renda por ano trabalhada mais estável. Investir em juniores é financeiramente eficiente para 
            operações de volume, mas o retorno sobre o 'crescimento salarial' sugere que a retenção de talentos que 
            sobem de nível é mais barata do que contratar novos especialistas no mercado.
        """)

    st.markdown("---")

    # Linha 2: Gráficos Principais
    st.subheader("Visualização dos Dados")
    c1, c2 = st.columns(2)
    ordem = ['Junior', 'Pleno', 'Sênior', 'Especialista']

    with c1:
        st.markdown("##### Distribuição de Renda por Nível")
        fig_box = px.box(
            df_filtered, 
            x='nivel_de_experiencia', 
            y='renda_anual',
            category_orders={'nivel_de_experiencia': ordem},
            color='nivel_de_experiencia',
            points="all",
            labels={'nivel_de_experiencia': 'Nível', 'renda_anual': 'Renda Anual (USD)'},
            template="plotly_white"
        )
        st.plotly_chart(fig_box, width='stretch')

    with c2:
        st.markdown("##### Relação Idade vs. Renda")
        fig_scatter = px.scatter(
            df_filtered, 
            x='idade', 
            y='renda_anual',
            category_orders={'nivel_de_experiencia': ordem},
            color='nivel_de_experiencia',
            size='tempo_de_trabalho',
            labels={'idade': 'Idade', 'renda_anual': 'Renda Anual (USD)', 'nivel_de_experiencia': 'Nível'},
            template="plotly_white"
        )
        st.plotly_chart(fig_scatter, width='stretch')

    # Linha 3: Análise de Eficiência e Tempo
    c3, c4 = st.columns([1, 1])

    with c3:
        st.markdown("##### Média de Renda por Tempo de Carreira")
        df_tempo = df_filtered.groupby('tempo_de_trabalho')['renda_anual'].mean().reset_index()
        fig_line = px.line(
            df_tempo,
            x='tempo_de_trabalho',
            y='renda_anual',
            markers=True,
            labels={'tempo_de_trabalho': 'Anos de Experiência', 'renda_anual': 'Média de Renda'},
            template="plotly_white",
            color_discrete_sequence=['#2ecc71']
        )
        st.plotly_chart(fig_line, width='stretch')

    with c4:
        st.markdown("##### Concentração da Força de Trabalho (Proporção)")
        fig_hist = px.histogram(
            df_filtered,
            x='proporcao_trabalho',
            nbins=20,
            color_discrete_sequence=['#3498db'],
            labels={'proporcao_trabalho': 'Proporção (Trabalho/Idade)'},
            template="plotly_white",
            marginal="rug"
        )
        st.plotly_chart(fig_hist, width='stretch')

    # Seção de Dados Brutos
    with st.expander("Visualizar Base de Dados Filtrada"):
        st.dataframe(df_filtered.style.highlight_max(axis=0, subset=['renda_anual']), width='stretch')

    st.sidebar.markdown("---")
    st.sidebar.info("Desenvolvido para Portfolio de Análise de Dados.")

@st.cache_data
def carregar_dados_cache():
    return carregar_dados()

if __name__ == "__main__":
    df = carregar_dados_cache()
    main(df)