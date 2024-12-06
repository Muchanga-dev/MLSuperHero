
# app.py
import streamlit as st
from utils.config import Conf_pagina

# Definição das páginas
instructions_page = st.Page("pages/instructions.py", title="Instruções", icon="📝")
exploration_page = st.Page("pages/exploration.py", title="Exploração de Dados", icon="🔍")
clustering_page = st.Page("pages/clustering.py", title="Clustering", icon="🔀")
classification_page = st.Page("pages/classification.py", title="Classificação do Alinhamento", icon="📊")
regression_page = st.Page("pages/regression.py", title="Previsão de Peso", icon="📈")


# Configuração inicial da página
Conf_pagina("assets/icon.png")
st.logo("assets/logo.png")

# Definição da navegação
navigation = st.navigation([
    instructions_page,
    exploration_page,
    clustering_page,
    classification_page,
    regression_page
])

# Executa a página selecionada
navigation.run()

