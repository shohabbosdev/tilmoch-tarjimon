import streamlit as st
import requests

st.set_page_config(page_title="Tilmoch tarjimon", layout="centered", page_icon='⚠️')

st.header("Tilmoch tarjima 🖲")

col1, col2 = st.columns(2)

inputText = col1.text_area("Tarjima matn kiriting", height=300)


tarjima = st.button("Tarjima qilish", type='primary')
if tarjima:
    text = inputText.replace('\n',' ')
    col2.text_area('Result',text)
