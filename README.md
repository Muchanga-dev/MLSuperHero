# MLSuperHero - Projeto de Análise, Visualização de Dados e aprendizado de máquina

## Descrição Geral
O **MLSuperHero** é um projeto que combina **análise de dados**, **aprendizado de máquina** e **visualizações interativas** para explorar informações relacionadas a super-heróis. A partir de um conjunto de dados detalhado sobre características e poderes de super-heróis, o projeto aborda tarefas como **clusterização**, **classificação** e **regressão**, além de fornecer uma aplicação interativa desenvolvida com **Streamlit**.

---
![Imagem](assets/image.png)

## Estrutura do Projeto

```
MLSuperHero/
├── data/                                   # Dados brutos e processados
├── notebooks/                              # Notebooks Jupyter para experimentação
│   ├── exploration.ipynb                   # Análise exploratória
│   ├── classification.ipynb                # Classificação (Naive Bayes)
│   ├── regression.ipynb                    # Regressão (Random Forest)
│   └── clustering.ipynb                    # Clusterização (KMeans)
├── streamlit/                              # Aplicação Streamlit interativa
│   ├── app.py                              # Arquivo principal do app
│   ├── pages/                              # Páginas individuais do app
│   ├── models/                             # Modelos treinados usados no app
│   └── README.md                           # Documentação específica do Streamlit
├── requirements.txt                        # Dependências do projeto
├── LICENSE                                 # Licença do projeto
└── README.md                               # Este arquivo de documentação
```

---

## Notebooks do Projeto

### **1. Exploration.ipynb**
Realiza uma análise exploratória inicial dos dados de super-heróis.

#### Principais Tarefas:
- Leitura e exibição dos dados.
- Identificação e tratamento de valores ausentes.
- Visualizações de distribuições e correlações entre variáveis.
- Salvamento dos dados processados para uso nos próximos notebooks.

---

### **2. Classification.ipynb**
Foco no treinamento de um modelo **Naive Bayes** para prever o alinhamento dos heróis (bom, mau ou neutro).

#### Etapas:
1. **Processamento dos Dados**:
   - Transformação de colunas booleanas e nominais.
   - Seleção de colunas relevantes com base em correlações.
2. **Treinamento do Modelo**:
   - Treinamento de um modelo Naive Bayes.
3. **Avaliação do Modelo**:
   - Métricas como acurácia e matriz de confusão.
4. **Salvamento do Modelo**:
   - Exportação do modelo treinado para uso na aplicação Streamlit.

---

### **3. Regression.ipynb**
Prevê o peso dos super-heróis utilizando algoritmos de **regressão**.

#### Etapas:
1. **Carregamento e Preparação dos Dados**:
   - Seleção de colunas com alta correlação com o peso.
2. **Treinamento do Modelo**:
   - Treinamento de um modelo Random Forest.
3. **Avaliação do Modelo**:
   - Métricas como erro absoluto médio e coeficiente de determinação.
4. **Discussão**:
   - Interpretação dos resultados e importância das features.

---

### **4. Clustering.ipynb**
Agrupa os super-heróis com base em características e poderes utilizando **KMeans**.

#### Etapas:
1. **Preparação dos Dados**:
   - Seleção e padronização de colunas para clustering.
2. **Número Ideal de Clusters**:
   - Métodos como Elbow e Silhouette.
3. **Criação dos Clusters**:
   - Aplicação do algoritmo KMeans.
4. **Visualização dos Resultados**:
   - PCA para redução de dimensionalidade e gráficos 2D.
5. **Salvamento dos Resultados e Modelos**:
   - Dados com rótulos de cluster prontos para uso no Streamlit e os Modelos Treinados.

---

## Aplicação Streamlit

O projeto também inclui uma aplicação interativa para explorar os dados e modelos treinados. Para mais detalhes sobre a aplicação, consulte o arquivo [README.md do Streamlit](streamlit/README.md).

---

## Configuração do Ambiente

### 1. Clone o repositório:
```bash
git clone https://github.com/Muchanga-dev/MLSuperHero.git
cd MLSuperHero/
```

### 2. Instale as dependências:
```bash
pip install -r requirements.txt
```

---

## Licença

Este projeto está licenciado sob a **MIT License**. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
