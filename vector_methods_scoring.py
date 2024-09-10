# python -m streamlit run vector_methods_scoring.py

import pandas as pd
import streamlit as st
# LANGUAGE DETECTION
import textstat
import language_tool_python
from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException

st.set_page_config(page_title='Text Assessment Estimation - DEMO')

st.title('Methods Assessment - VECTOR DEMO')
st.write('The following is a demo for text quality scoring.')
textstring = st.text_area('Methods text')

if textstring:

  st.subheader('Language Detected:')
  # Ensure consistent results
  DetectorFactory.seed = 0

  try:
        language = detect(textstring)
        st.write(f"Detected language: {language}")
  except LangDetectException:
        st.write("Could not detect the language. Please enter more text.")
  
  st.subheader('Word Count:')
  def word_count(text):
    words = text.split()
    return len(words)

  # Example usage
  count = word_count(textstring)
  st.write(count)

  
  st.subheader('Readability: (Flesch Reading Ease Score)')
  ease = textstat.flesch_reading_ease(textstring)
  st.write(ease)
  st.subheader('Grammar errors:')
  tool = language_tool_python.LanguageToolPublicAPI('en')

  matches = tool.check(textstring)
  st.write(len(matches))
  st.write(matches)
