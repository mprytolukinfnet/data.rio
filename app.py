import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Explicação do Objetivo e Motivação
st.title("Dashboard de Turismo - Data.Rio")
st.write("""
    **Objetivo**: O objetivo deste dashboard é permitir a visualização e análise interativa dos dados turísticos do portal Data.Rio. 
    A aplicação facilita o processo de filtragem, exploração e personalização dos dados, proporcionando insights valiosos para decisões no setor de turismo.
    
    **Motivação**: A escolha de dados turísticos se deve à importância crescente do turismo sustentável e à necessidade de ferramentas que 
    ajudem a analisar informações do setor para otimização de recursos e planejamento estratégico.
""")

# 2. Realizar Upload de Arquivo CSV
st.header("Upload de Arquivo CSV")
uploaded_file = st.file_uploader("Faça o upload do arquivo CSV de turismo", type="csv")

@st.cache_data
def load_data(file):
    return pd.read_csv(filepath_or_buffer=file, skipinitialspace = True, quotechar = '"', on_bad_lines="skip", parse_dates=['created', 'modified'])

if uploaded_file:
    progress = st.progress(0)
    with st.spinner('Carregando dados...'):
        data = load_data(uploaded_file)
        progress.progress(50)
        st.write("Dados carregados com sucesso:")
        st.dataframe(data.head())
        progress.progress(60)

# 3. Filtro de Dados e Seleção
st.header("Filtrar e Selecionar Dados")
filtered_data = None
if uploaded_file:
    # Filtros usando checkboxes
    owners = data['owner'].unique()
    types = data['type'].unique()

    col_owners, col_types = st.columns(2)
    
    def select_all_owners():
        bool_val = st.session_state.all_owners
        owner_checks = [s for s in st.session_state if s.startswith("owner_")]
        for c in owner_checks:
            st.session_state[c] = bool_val

    with col_owners:
        st.write("Proprietários:")
        st.checkbox("Selecionar/Desselecionar todos", value=True, key=f'all_owners', on_change=select_all_owners)
        selected_owners = [owner for owner in owners if st.checkbox(owner, value=True, key=f'owner_{owner}')]

    def select_all_types():
        bool_val = st.session_state.all_types
        owner_checks = [s for s in st.session_state if s.startswith("type_")]
        for c in owner_checks:
            st.session_state[c] = bool_val
    
    with col_types:
        st.write("Tipos:")
        st.checkbox("Selecionar/Desselecionar todos", value=True, key=f'all_types', on_change=select_all_types)
        selected_types = [type_ for type_ in types if st.checkbox(type_, value=True, key=f'type_{type_}')]

    # Aplicar filtros se houver seleções
    if selected_owners and selected_types:
        filtered_data = data[(data['owner'].isin(selected_owners)) & (data['type'].isin(selected_types))]
        st.write("Dados filtrados:")
        st.dataframe(filtered_data)
    else:
        st.write("Selecione pelo menos um proprietário e um tipo para visualizar os dados.")

# 4. Desenvolver Serviço de Download de Arquivos
st.header("Baixar Dados Filtrados")
if uploaded_file:
    if filtered_data is not None:
        st.download_button(
            label="Baixar CSV filtrado",
            data=filtered_data.to_csv(index=False),
            file_name="dados_filtrados.csv",
            mime="text/csv"
        )
    else:
        st.write("Selecione pelo menos um proprietário e um tipo para baixar os dados.")
else:
    st.write("Faça o Upload de um arquivo para baixar os dados.")

# 5. Utilizar Barra de Progresso e Spinners
# Foi implementado spinner em todas as funções que carregam dados e visualizações, além de uma barra de progresso.

# 6. Utilizar Color Picker
st.header("Personalizar Dashboard")
background_color = st.color_picker("Escolha a cor de fundo", "#FFFFFF")
font_color = st.color_picker("Escolha a cor da fonte", "#000000")
st.markdown(f"""
    <style>
    h1, h2, h3, p, .e1i5pmia3, .stApp {{
        background-color: {background_color};
        color: {font_color};
    }}
    </style>
    """, unsafe_allow_html=True)

# 7. Utilizar Funcionalidade de Cache
# Já foi implementado no decorador @st.cache_data no carregamento de dados

# 8. Persistir Dados Usando Session State
# Foi implementada a persistência de dados usando Session State nos filtros de dados.
# As opções de "Selecionar/Deselecionar todos" utiliza o Session State para marcar/desmarcar todas as opções. 

# 9. Criar Visualizações de Dados - Tabelas
st.header("Tabela de Dados Interativa")
with st.spinner('Carregando dados...'):
    if uploaded_file:
        st.dataframe(filtered_data)
        progress.progress(70)

# 10. Criar Visualizações de Dados - Gráficos Simples
st.header("Gráficos Simples")
with st.spinner('Carregando dados...'):
    if uploaded_file:
        st.subheader("Gráfico de Barras - Contagem por Proprietário")
        fig_bar = px.bar(filtered_data, x='owner', y='id', title="Contagem de Registros por Proprietário")
        st.plotly_chart(fig_bar)

        st.subheader("Gráfico de Pizza - Tipos de Dados")
        fig_pie = px.pie(filtered_data, names='type', title="Distribuição dos Tipos de Dados")
        st.plotly_chart(fig_pie)
        progress.progress(80)

# 11. Criar Visualizações de Dados - Gráficos Avançados
st.header("Gráficos Avançados")
with st.spinner('Carregando dados...'):
    if uploaded_file:
        st.subheader("Histograma - Data de Criação")
        fig_hist = px.histogram(filtered_data, x='created', title="Distribuição das Datas de Criação")
        st.plotly_chart(fig_hist)

        st.subheader("Scatter Plot - Tipo x Data de Criação")
        fig_scatter = px.scatter(filtered_data, x='created', y='type', title="Scatter Plot de Tipos e Data de Criação")
        st.plotly_chart(fig_scatter)
        progress.progress(90)

# 12. Exibir Métricas Básicas
st.header("Métricas Básicas")
with st.spinner('Carregando dados...'):
    if uploaded_file:
        st.metric("Total de Registros", len(filtered_data))
        st.metric("Data mais Antiga", filtered_data['created'].min().strftime('%Y-%m-%d %X'))
        st.metric("Data mais Recente", filtered_data['created'].max().strftime('%Y-%m-%d %X'))
        progress.progress(100)
