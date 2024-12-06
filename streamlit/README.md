# MLSuperHero - Aplicação Streamlit

## Descrição
O **MLSuperHero** é uma aplicação interativa desenvolvida em **Streamlit** para análise e visualização de dados relacionados a super-heróis. A ferramenta permite explorar estatísticas, realizar análises de cluster, fazer previsões de alinhamento e estimar características como peso usando modelos de aprendizado de máquina.

---

## Estrutura do Projeto Streamlit

```
streamlit/
├── .streamlit/                         # Configurações do Streamlit (tema, layout)
├── app.py                              # Arquivo principal para iniciar a aplicação
├── data/                               # Dados usados diretamente pela aplicação
│   ├── raw/                            # Dados brutos
│   ├── processed/                      # Dados tratados
│   └── heroes_informatio.csv           # Dados de heróis
│   └── super_hero_powers.csv           # Dados de poderes
├── models/                             # Modelos treinados para previsões
│   ├── clustering_model.pkl            # Modelo de clusterização
│   ├── clustering_scaler.pkl           # Normalizador de clusterização
│   ├── naive_bayes_alignment.pkl       # Modelo Naive Bayes para alinhamento
│   └── random_forest_weight_regressor.pkl # Modelo Random Forest para regressão de peso
├── pages/                              # Páginas adicionais da aplicação
│   ├── classification.py               # Página de classificação
│   ├── clustering.py                   # Página de clusterização
│   ├── exploration.py                  # Página de exploração de dados
│   ├── instructions.py                 # Página de instruções e guia
│   └── regression.py                   # Página de regressão
├── utils/                              # Funções auxiliares e configurações
│   └── config.py                       # Configurações gerais
├── requirements.txt                    # Dependências necessárias para o Streamlit
└── README.md                           # Este arquivo de documentação
```

---

## Funcionalidades

### 🎯 Exploração de Dados
- Visualize as estatísticas descritivas de variáveis numéricas e categóricas.
- Analise distribuições de características como Altura, Peso e Gênero.
- Filtros interativos para Editora, Alinhamento e Gênero.

### 🔀 Clusterização
- Visualize clusters de super-heróis com gráficos interativos.
- Explore agrupamentos baseados em características como Altura e Peso.
- Modelos de clusterização integrados para análises dinâmicas.

### 🧠 Classificação
- Predição do alinhamento do herói (bom, mau, neutro) usando Naive Bayes.
- Ferramenta para testar novas entradas e verificar resultados.

### 📉 Regressão
- Estimativa do peso do herói baseado em suas características usando Random Forest.
- Integração de sliders para ajustar valores e observar predições.

---

## Pré-requisitos

Certifique-se de ter as seguintes ferramentas instaladas:
- Python 3.8 ou superior
- Pip para gerenciar dependências

---

## Configuração

### 1. Clone o repositório:
```bash
git clone https://github.com/seu_usuario/MLSuperHero.git
cd MLSuperHero/streamlit
```

### 2. Instale as dependências:
```bash
pip install -r requirements.txt
```

### 3. Inicie o aplicativo Streamlit:
```bash
streamlit run app.py
```

---

## Estrutura das Páginas

### 1. Página Principal (`app.py`)
- **Descrição:** Serve como ponto de entrada para o usuário explorar as funcionalidades.

### 2. Páginas Adicionais (`pages/`)
- **Exploração de Dados (`exploration.py`)**: Estatísticas descritivas, filtros e gráficos.
- **Clusterização (`clustering.py`)**: Análise e visualização de clusters.
- **Classificação (`classification.py`)**: Predições de alinhamento com base nos dados.
- **Regressão (`regression.py`)**: Previsões do peso com Random Forest.
- **Instruções (`instructions.py`)**: Guia do usuário e explicações sobre o uso.

---

## Modelos Integrados

Os modelos treinados são armazenados na pasta **`models/`** e usados diretamente pela aplicação:
- **`clustering_model.pkl`**: Modelo para agrupar heróis em clusters.
- **`clustering_scaler.pkl`**: Normalizador para o modelo de clusterização.
- **`naive_bayes_alignment.pkl`**: Classificador para prever alinhamento.
- **`random_forest_weight_regressor.pkl`**: Regressor para estimar o peso.

---

## Personalização

### Configuração do Tema Streamlit
Você pode alterar o tema da interface editando o arquivo **`.streamlit/config.toml`**.

Exemplo:
```toml
[theme]
base="light"
primaryColor="#4CAF50"
secondaryBackgroundColor="#F5F5F5"
```

---

## Exemplos de Uso

1. **Exploração de Dados**:
   - Acesse a página "Exploração" para visualizar estatísticas e gráficos interativos.
2. **Clusterização**:
   - Identifique grupos de heróis com base em características como Altura e Peso.
3. **Classificação**:
   - Teste se um herói é bom, mau ou neutro.
4. **Regressão**:
   - Estime o peso de um herói com base em suas características.

---

## Contribuindo

Contribuições são bem-vindas! Siga os passos:
1. Faça um fork do repositório.
2. Crie um branch para sua feature: `git checkout -b minha-feature`.
3. Envie um pull request.

---

## Licença

Este projeto está licenciado sob a **MIT License** - veja o arquivo **LICENSE** para mais detalhes.
