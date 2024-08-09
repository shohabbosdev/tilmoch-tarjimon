import streamlit as st
import requests

st.set_page_config(page_title="Tilmoch tarjimon", layout="centered", page_icon='⚠️')

language_lists = {
    "Inglizcha":"eng_Latn",
    "O'zbekcha":"uzn_Latn",
    "Ruscha":"rus_Cyrl",
    "Ўзбекча":"uzn_Cyrl",
    "Qoraqalpoqcha":"kaa_Latn"
}

st.header("Tilmoch tarjima 🖲")
api_token = st.secrets['token']

col1, col2 = st.columns(2)

selectSourceList1 = col1.selectbox(label="Yuqorida kiritilgan matn tili", options=language_lists, key='selected1')

selectTargetList1 = col2.selectbox(label="Tarjima qilinadigan til", options=language_lists,placeholder="Tanlang...", key='selected2')


inputText = col1.text_area("Tarjima matn kiriting", height=300)

url = "https://websocket.tahrirchi.uz/translate"
headers = {
    "Authorization": api_token,
    "Content-Type": "application/json"
}
data = {
    "text": {
        "texts": [
            inputText.replace("\n", "")
        ]
    },
    "source_lang": language_lists[selectSourceList1],
    "target_lang": language_lists[selectTargetList1],
}
tarjima = st.button("Tarjima qilish", type='primary')
if tarjima:
      response = requests.post(url, json=data, headers=headers)
      if response.status_code == 200:
            col2.text_area("Natija",response.json()['sentences'][-1]['translated'], height=300)
                  
      else:
            st.error(f"Xatolik kodi: {response.status_code}")