import streamlit as st

st.set_page_config(page_title="ISO 11855", page_icon="🦈", layout="wide")

st.write("# ISO 11855 example application")

st.sidebar.success("Select a demo above.")

st.markdown(
    """  
    ISO 11855 standard is applicable to water based embedded surface heating 
    and cooling systems in residential, commercial and industrial buildings.
    """
)