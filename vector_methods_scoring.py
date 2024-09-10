# python -m streamlit run vector_methods_scoring.py

import pandas as pd
import streamlit as st
# LANGUAGE DETECTION
#from lingua import LanguageDetectorBuilder
#from lingua import Language, LanguageDetectorBuilder
# reading ease score
import textstat

#@st.cache
#def load_detector():
#    return LanguageDetectorBuilder.from_all_languages().build()

#detector = load_detector()

#st.title("Language Detection App")

#text = st.text_area("Enter text to detect language:")
#if text:
#    result = detector.detect_language_of(text)
#    st.write(f"Detected language: {result}")

st.set_page_config(page_title='Text Assessment Estimation - DEMO')

st.image('TR-logo.png')
st.title('Methods Assessment - VECTOR DEMO')
st.write('The following is a demo for text quality scoring.')
vehicle_name = st.text_input('Methods text')

st.subheader('Language Detected:')

st.subheader('Word Count:')

st.subheader('Readability: (Flesch Reading Ease Score)')

st.subheader('Grammar errors:')
