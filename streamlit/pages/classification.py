# pages/classification.py

import streamlit as st
import pandas as pd
import joblib

def app():
    c1,c2,c3=st.columns([2,4,2])
    c2.title("Classificação do Alinhamento")
    # Colunas usadas no treinamento da classificação
    features = ['Invisibility', 'Natural Weapons', 'Power Suit', 'Insanity', 'Super Strength', 'Weight']
    target = 'Alignment'  # Bom/Mau

    @st.cache_resource
    def load_model():
        try:
            model = joblib.load('./models/naive_bayes_alignment.pkl')
            return model
        except FileNotFoundError:
            st.error("Modelo `naive_bayes_alignment.pkl` não encontrado em `models/`.")
            return None

    model = load_model()

    if model is not None:

        c2.warning("Insira os valores das features para prever o alinhamento (Bom/Mau):")

        # Supondo que as colunas exceto 'Weight' sejam binárias (0 ou 1)
        invisibility = c2.checkbox("Invisibilidade")
        natural_weapons = c2.checkbox("Armas Naturais")
        power_suit = c2.checkbox("Traje de Poder")
        insanity = c2.checkbox("Insanidade")
        super_strength = c2.checkbox("Super Força")
        weight_val = c2.number_input("Peso (kg)", value=100.0, min_value=0.0, max_value=2000.0, step=1.0)

        # Preparar os dados de entrada para a previsão
        input_data = pd.DataFrame([{
            'Invisibility': 1 if invisibility else 0,
            'Natural Weapons': 1 if natural_weapons else 0,
            'Power Suit': 1 if power_suit else 0,
            'Insanity': 1 if insanity else 0,
            'Super Strength': 1 if super_strength else 0,
            'Weight': weight_val
        }], columns=features)

        if c2.button("Prever Alinhamento"):
            try:
                # Fazer a previsão
                prediction = model.predict(input_data)[0]
                
                # Mapear a previsão para as categorias correspondentes
                if isinstance(prediction, (int, float)):
                    alignment = "Bom" if prediction == 1 else "Mau"
                elif isinstance(prediction, str):
                    alignment = "Bom" if prediction.lower() == "good" else "Mau"
                else:
                    alignment = "Indefinido"

                c2.success(f"Alinhamento previsto: **{alignment}**")
            except Exception as e:
                c2.error(f"Erro na previsão: {e}")

app()