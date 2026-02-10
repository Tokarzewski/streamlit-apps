import streamlit as st
from language_constants import LANGUAGES, LANGUAGE_PAGES, DEFAULT_LANGUAGE

st.set_page_config(page_title="ISO 11855", page_icon="🦈", layout="wide")

# Initialize language in session state
if "language" not in st.session_state:
    st.session_state.language = DEFAULT_LANGUAGE

# Language selector in sidebar
st.sidebar.header("🌐 Language")
language_list = list(LANGUAGES.values())
language_codes = list(LANGUAGES.keys())
current_index = language_codes.index(st.session_state.language)

selected_lang_display = st.sidebar.selectbox(
    "Select language",
    options=language_list,
    index=current_index,
    key="language_selector",
    label_visibility="collapsed"
)
selected_code = language_codes[language_list.index(selected_lang_display)]
st.session_state.language = selected_code

# Navigate to selected language page
st.switch_page(LANGUAGE_PAGES[st.session_state.language])

st.write("# ISO 11855 example application")

st.sidebar.success("Select a header from above.")

st.markdown(
    """  
    ISO 11855 standard is applicable to water based embedded surface heating 
    and cooling systems in residential, commercial and industrial buildings.
    """
)