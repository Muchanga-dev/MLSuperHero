# streamlit/pages/Clustering.py

import streamlit as st
import pandas as pd
import joblib
from sklearn.decomposition import PCA
import altair as alt
import plotly.express as px
import os
from sklearn.metrics import silhouette_score



# Função para carregar dados
@st.cache_data
def load_data(filepath):
    try:
        df = pd.read_csv(filepath)
        return df
    except FileNotFoundError:
        st.error(f"Arquivo `{filepath}` não encontrado no diretório `data/processed/`.")
        return pd.DataFrame()

# Função para carregar scaler
@st.cache_resource
def load_scaler(filepath):
    try:
        scaler = joblib.load(filepath)
        return scaler
    except FileNotFoundError:
        st.error(f"Scaler `{filepath}` não encontrado em `models/`.")
        return None

# Função para carregar modelo PCA
@st.cache_resource
def load_pca(n_components=2):
    pca = PCA(n_components=n_components)
    return pca

# Função para aplicar PCA
def apply_pca(scaled_features, pca):
    return pca.fit_transform(scaled_features)

# Função para criar gráficos Altair
def create_altair_pca_chart(df):
    return alt.Chart(df).mark_circle(size=60).encode(
        x=alt.X('PCA1:Q', title='Componente Principal 1'),
        y=alt.Y('PCA2:Q', title='Componente Principal 2'),
        color=alt.Color('Cluster:N', legend=alt.Legend(title="Cluster")),
        tooltip=['Height', 'Weight', 'Gender', 'Cluster']
    ).properties(
        title="Visualização dos Clusters usando PCA (Altair)",
        width=700,
        height=500
    ).interactive()

# Função para criar gráficos Plotly
def create_plotly_pca_chart(df):
    return px.scatter(
        df,
        x='PCA1',
        y='PCA2',
        color='Cluster',
        hover_data=['Height', 'Weight', 'Gender', 'Cluster'],
        title="Visualização dos Clusters usando PCA (Plotly)",
        width=700,
        height=500
    )

def app():

    dash=1
    # Carregar dados e scaler
    with st.spinner('Carregando dados...'):
        df = load_data('data/processed/clustered_data.csv')
        scaler = load_scaler('./models/clustering_scaler.pkl')

    if df.empty or scaler is None:
        st.warning("Dados ou scaler não carregados corretamente. Verifique os arquivos.")
        st.stop()

    # Recuperar as features do scaler
    try:
        features = scaler.feature_names_in_
    except AttributeError:
        st.error("O scaler não possui o atributo `feature_names_in_`. Certifique-se de que está usando um scaler compatível.")
        st.stop()

    # Verificar se todas as features estão presentes no DataFrame
    missing_features = [feat for feat in features if feat not in df.columns]
    if missing_features:
        st.sidebar.warning(f"As seguintes features estão faltando no DataFrame e serão preenchidas com zeros: {', '.join(missing_features)}")
        for feat in missing_features:
            df[feat] = 0  # Preencher com zero ou outro valor adequado

    # Garantir que a ordem das colunas corresponda às features do scaler
    df_features = df[features]

    # Aplicar o scaler nas features
    try:
        scaled_features = scaler.transform(df_features)
    except ValueError as e:
        st.error(f"Erro ao aplicar o scaler: {e}")
        st.stop()

    # Aplicar PCA
    pca = load_pca(n_components=2)
    reduced_features = apply_pca(scaled_features, pca)

    # Adicionar as componentes PCA ao DataFrame
    df['PCA1'] = reduced_features[:, 0]
    df['PCA2'] = reduced_features[:, 1]

    # Verificar se a coluna 'Cluster' existe
    if 'Cluster' not in df.columns:
        st.sidebar.warning("A coluna 'Cluster' não está presente no DataFrame. Por favor, execute a clusterização primeiro.")
        st.stop()

    # Adicionar Visão Geral dos Clusters
    if st.sidebar.toggle("Visão Geral dos Clusters", key='show_overview_clusters'):
        dash=0
        st.subheader("📋 Visão Geral dos Clusters")
        cluster_summary = df.groupby('Cluster')[features].mean().reset_index()
        st.dataframe(cluster_summary)


    if st.sidebar.toggle("📥 Baixar Dados por clusters"):
      dash=0
      # Seleção de Cluster para Detalhes na Barra Lateral
      st.subheader("🔍 Seleção de Clusters para Detalhes")
      clusters_selected = st.sidebar.multiselect(
          "Selecione os Clusters para visualizar:",
        options=sorted(df['Cluster'].unique()),
        default=sorted(df['Cluster'].unique())[:2],
        key='clusters_selected_multiselect'
        )
      
      cluster_subset_multi = df[df['Cluster'].isin(clusters_selected)]
    
      st.write(f"Clusters selecionados: **{', '.join(map(str, clusters_selected))}** com **{len(cluster_subset_multi)}** heróis.")
      st.dataframe(cluster_subset_multi)

      # Botão para download dos dados filtrados
      def convert_df_to_csv(df):
           return df.to_csv(index=False).encode('utf-8')

      csv = convert_df_to_csv(cluster_subset_multi)

      st.download_button(
          label="📥 Baixar Dados Filtrados",
          data=csv,
          file_name='dados_filtrados_clusters.csv',
          mime='text/csv',
         )

    if st.sidebar.toggle("Distribuição dos Clusters"):
       dash=0
       # Gráfico de Dispersão PCA com Opção de Escolha de Técnica
       st.subheader("📊 Distribuição dos Clusters")

       visualization_type = st.sidebar.radio("Escolha a técnica de visualização:", ["Altair", "Plotly"], key='visualization_type_selectbox')

       if visualization_type == "Altair":
          pca_chart = create_altair_pca_chart(df)
          st.altair_chart(pca_chart, use_container_width=True)

       elif visualization_type == "Plotly":
          fig = create_plotly_pca_chart(df)
          st.plotly_chart(fig, use_container_width=True)

       # Gráfico de Distribuição por Cluster
       cluster_counts = df['Cluster'].value_counts().reset_index()
       cluster_counts.columns = ['Cluster', 'Count']

    if st.sidebar.toggle("Distribuição de Altura vs Peso dos Heróis"):
       dash=0
       # Gráfico de Dispersão Altura vs Peso
       st.subheader("📐 Distribuição de Altura vs Peso dos Heróis")

       scatter_chart = alt.Chart(df).mark_circle(size=60).encode(
            x=alt.X('Height:Q', title='Altura (cm)'),
            y=alt.Y('Weight:Q', title='Peso (kg)'),
            color=alt.Color('Cluster:N', legend=alt.Legend(title="Cluster")),
            tooltip=['Height', 'Weight', 'Gender', 'Cluster']
         ).properties(
            title="Altura vs Peso dos Heróis por Cluster",
            height=600
         ).interactive()

       st.altair_chart(scatter_chart, use_container_width=True)

       if st.checkbox("Visualizar a Tabela"):
         st.dataframe(df)

    if st.sidebar.toggle("Distribuição por Gênero por Clusters"):
       dash=0
       # Gráfico de Distribuição de Gênero dentro dos Clusters Selecionados
       st.subheader("👥 Distribuição por Gênero dentro dos Clusters Selecionados")

       # Garantir que haja clusters selecionados antes de continuar
       if 'Cluster' in df.columns:
          clusters_selected = st.sidebar.multiselect(
          "Selecione os Clusters para visualizar a distribuição por gênero:",
          options=sorted(df['Cluster'].unique()),
          default=sorted(df['Cluster'].unique())[:2]
          )

       if clusters_selected:
          # Filtrar os dados com base nos clusters selecionados
          cluster_subset_multi = df[df['Cluster'].isin(clusters_selected)]
        
          # Calcular distribuição de gênero
          gender_counts = cluster_subset_multi['Gender'].value_counts().reset_index()
          gender_counts.columns = ['Gênero', 'Quantidade']

          # Gráfico de barras para distribuição de gênero
          st.bar_chart(gender_counts.set_index('Gênero'))
          st.dataframe(gender_counts)

       else:
         st.warning("Por favor, selecione pelo menos um cluster para visualizar a distribuição por gênero.")
    
    # Dashboard Resumido
    if dash == 1:
      st.subheader("📈 Principais Métricas dos Clusters")

      # Cálculos adicionais
      total_clusters = df['Cluster'].nunique()
      total_herois = len(df)
      herois_no_maior_cluster = df['Cluster'].value_counts().iloc[0]
      maior_cluster_percentual = (herois_no_maior_cluster / total_herois) * 100
      herois_no_menor_cluster = df['Cluster'].value_counts().iloc[-1]
      menor_cluster_percentual = (herois_no_menor_cluster / total_herois) * 100
      media_herois_por_cluster = total_herois / total_clusters
      variaveis_treinadas = len(features)
      desvio_padrao_tamanho_clusters = df['Cluster'].value_counts().std()
      diversidade_genero = df['Gender'].nunique()
      tamanho_total_dados = df.size

      # Layout em colunas
      col1, col2, col3 = st.columns(3)
      with col1:
        st.metric("Total de Clusters", total_clusters)
        st.metric("Variáveis Treinadas", variaveis_treinadas)
        st.metric("Desvio Padrão dos Tamanhos", f"{desvio_padrao_tamanho_clusters:.2f}")
      with col2:
        st.metric("Total de Heróis", total_herois)
        st.metric("Média de Heróis por Cluster", f"{media_herois_por_cluster:.2f}")
        st.metric("Diversidade de Gêneros", diversidade_genero)
      with col3:
        st.metric("Heróis no Maior Cluster", herois_no_maior_cluster)
        st.metric("Maior Cluster (%)", f"{maior_cluster_percentual:.2f}%")
        st.metric("Heróis no Menor Cluster", herois_no_menor_cluster)
        st.metric("Menor Cluster (%)", f"{menor_cluster_percentual:.2f}%")

     
      # Cálculo da distribuição
      cluster_distribution = df['Cluster'].value_counts().reset_index()
      cluster_distribution.columns = ['Cluster', 'Quantidade']
      cluster_distribution['Percentual (%)'] = (cluster_distribution['Quantidade'] / total_herois * 100).round(2)

      # Mostrar tabela opcionalmente
      if st.checkbox("Mostrar tabela completa de distribuição de clusters", key='show_cluster_table'):
        st.subheader("📋 Tabela Completa de Distribuição")
        st.dataframe(cluster_distribution, use_container_width=True)

app()
