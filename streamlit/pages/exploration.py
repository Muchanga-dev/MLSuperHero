import streamlit as st
import pandas as pd
import altair as alt

@st.cache_data
def load_data():
    try:
        df = pd.read_csv('../data/processed/merged_data_cleaned.csv')
        return df
    except FileNotFoundError:
        st.error("Arquivo `merged_data_cleaned.csv` não encontrado no diretório `data/processed/`.")
        return pd.DataFrame()

def app():
    st.sidebar.header("Exploração de Dados")
    
    # Carregar os dados
    with st.spinner('Carregando dados...'):
        df = load_data()
    
    if not df.empty:
        # Configuração da Barra Lateral
        st.sidebar.header("Filtros - Heróis")
        
        # Filtros na Barra Lateral
        publishers = sorted(df['Publisher'].dropna().unique())
        alignments = sorted(df['Alignment'].dropna().unique())
        genders = sorted(df['Gender'].dropna().unique())
        
        selected_publishers = st.sidebar.multiselect(
            "Escolha Editora(s)",
            options=["Todos"] + publishers,
            default="Todos"
        )
        selected_alignments = st.sidebar.multiselect(
            "Escolha Alinhamento(s)",
            options=["Todos"] + alignments,
            default="Todos"
        )
        selected_genders = st.sidebar.multiselect(
            "Escolha Gênero(s)",
            options=["Todos"] + genders,
            default="Todos"
        )
        
        # Aplicação dos Filtros
        filtered_df = df.copy()
        if "Todos" not in selected_publishers:
            filtered_df = filtered_df[filtered_df['Publisher'].isin(selected_publishers)]
        if "Todos" not in selected_alignments:
            filtered_df = filtered_df[filtered_df['Alignment'].isin(selected_alignments)]
        if "Todos" not in selected_genders:
            filtered_df = filtered_df[filtered_df['Gender'].isin(selected_genders)]
        
        # Mostrar dados filtrados na barra lateral
        st.sidebar.write(f"Total de Heróis Encontrados: **{len(filtered_df)}**")
        #if st.sidebar.checkbox("Mostrar Tabela de Dados Filtrados"):
        #    st.sidebar.dataframe(filtered_df)
        
        # Tabela de Estatísticas Descritivas para Variáveis Numéricas
        st.subheader("📊 Estatísticas Descritivas de Variáveis Altura e Peso")
        numeric_columns = filtered_df.select_dtypes(include=['float64', 'int64']).columns
        if not numeric_columns.empty:
            stats_table = filtered_df[numeric_columns].describe().T
            stats_table['missing'] = filtered_df[numeric_columns].isnull().sum()
            stats_table['unique'] = [filtered_df[col].nunique() for col in numeric_columns]
            stats_table = stats_table.rename(columns={
                "mean": "Média",
                "std": "Desvio Padrão",
                "min": "Mínimo",
                "25%": "Percentil 25",
                "50%": "Mediana",
                "75%": "Percentil 75",
                "max": "Máximo"
            })
            st.dataframe(stats_table)
        else:
            st.warning("Nenhuma variável numérica disponível para exibir estatísticas descritivas.")
        
        # Gráfico de Distribuição de Altura e Peso
        st.subheader("Distribuição de Altura e Peso")
        if not filtered_df.empty:
            height_weight_chart = alt.Chart(filtered_df).mark_circle(size=60).encode(
                x=alt.X('Height:Q', title='Altura (cm)'),
                y=alt.Y('Weight:Q', title='Peso (kg)'),
                color='Alignment:N',
                tooltip=['Publisher', 'Alignment', 'Height', 'Weight']
            ).properties(title="Altura vs Peso", height=600).interactive()
            st.altair_chart(height_weight_chart, use_container_width=True)
            
            # Mostrar tabela 
            st.sidebar.markdown("#### Dados Filtrados")
            st.sidebar.success(f"Total de Heróis Filtrados: **{len(filtered_df)}**")
            if st.sidebar.checkbox("Mostrar Tabela de Dados Filtrados"):
                st.dataframe(filtered_df)
            
            # Botão para baixar os dados filtrados
            def convert_df_to_csv(dataframe):
                return dataframe.to_csv(index=False).encode('utf-8')
            
            csv_data = convert_df_to_csv(filtered_df)
            st.sidebar.download_button(
                label="📥 Baixar Dados Filtrados",
                data=csv_data,
                file_name='dados_filtrados.csv',
                mime='text/csv'
            )
        else:
            st.warning("Nenhum dado disponível para visualização.")
app()