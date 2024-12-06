import streamlit as st


def app():
    c1,c2,c3=st.columns([1,4,1])
    c2.title("Aplicação de Super-Heróis com Machine Learning")
    c2.subheader("Instruções de Uso")

    c2.markdown("""
    ## Bem-vindo à Aplicação de Super-Heróis!

    Esta aplicação permite explorar dados sobre super-heróis, visualizar resultados de agrupamento 
    (clustering), classificar o alinhamento (bom ou mau) com base em atributos de heróis, 
    e prever o peso de um herói dado suas características.

    ### Navegação
    Utilize a barra lateral para acessar as diferentes seções do aplicativo:
    - **Instruções**: Esta página, com informações sobre o uso da aplicação.
    - **Exploração de Dados**: Visualize estatísticas, dados brutos e filtre por critérios.
    - **Resultados do Clustering**: Veja o agrupamento de heróis com base em seus poderes.
    - **Classificação do Alinhamento**: Forneça atributos de um herói para prever seu alinhamento.
    - **Previsão de Peso**: Insira características para prever o peso do herói.

    ### Dicas
    - Use as caixas de seleção para filtrar os dados na exploração.
    - Experimente diferentes valores nos modelos de classificação e regressão para ver como muda a previsão.
   
    ### Contato
    Para dúvidas ou melhorias, entre em contato com o desenvolvedor:
    [muchangarmando@gmail.com](mailto:muchangarmando@gmail.com)
""")

app()