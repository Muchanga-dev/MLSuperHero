# pages/regression.py

import streamlit as st
import pandas as pd
import joblib

def app():
    c1,c2,c3=st.columns([2,4,2])
    c2.title("Previsão de Peso (Regressão)")

    # Colunas usadas no treinamento da regressão
    # ['Gender_Male', 'Height', 'Gender_Female'] -> target = Weight
    features = ['Gender_Male', 'Height', 'Gender_Female']

    @st.cache_resource
    def load_model():
        try:
            model = joblib.load('./models/random_forest_weight_regressor.pkl')
            return model
        except FileNotFoundError:
            st.error("Modelo `random_forest_weight_regressor.pkl` não encontrado em `models/`.")
            return None

    model = load_model()

    if model is not None:
        c2.warning("Insira as características do herói para prever o peso:")

        gender = c2.selectbox("Gênero", ["Masculino", "Feminino"])
        height_val = c2.slider("Altura (cm)", 50, 300, 175)

        # Converter gênero em variáveis dummies:
        # Se Masculino: Gender_Male=1, Gender_Female=0
        # Se Feminino: Gender_Male=0, Gender_Female=1
        gender_male = 1 if gender == "Masculino" else 0
        gender_female = 1 if gender == "Feminino" else 0

        input_data = pd.DataFrame([{
            'Gender_Male': gender_male,
            'Height': height_val,
            'Gender_Female': gender_female
        }], columns=features)

        if c2.button("Prever Peso"):
            try:
                predicted_weight = model.predict(input_data)[0]
                c2.success(f"O peso previsto é: **{predicted_weight:.2f} kg**")
            except Exception as e:
                st.error(f"Erro na previsão: {e}")
app()