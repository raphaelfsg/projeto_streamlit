import streamlit as st

with st.form(key="include_cliente"):
    input_name = st.text_input(label="Insira o seu nome")
    input_age = st.number_input(label="Insira a sua idade")
    input_occupation = st.selectbox("Selecione a sua profissão", ["Desenvolvedor", "Designer", "Orientador"])
    input_button_submit = st.form_submit_button("Enviar")