import streamlit as st

st.title("Project team")

with st.form(key="include_cliente", clear_on_submit=True):
    input_name = st.text_input(label="Insira o seu nome")
    input_age = st.number_input(label="Insira a sua idade", format="%d", step=1)
    input_occupation = st.selectbox("Selecione a sua profissão", ["Desenvolvedor", "Designer", "Orientador"])
    input_social = st.text_input(label="Insira o endereço de sua rede social")
    input_button_submit = st.form_submit_button("Enviar")

if input_button_submit:
    