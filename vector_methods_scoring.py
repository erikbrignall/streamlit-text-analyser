# python -m streamlit run vector_methods_scoring.py

import pandas as pd
import streamlit as st
# LANGUAGE DETECTION
import textstat
import language_tool_python

st.set_page_config(page_title='Text Assessment Estimation - DEMO')

st.title('Methods Assessment - VECTOR DEMO')
st.write('The following is a demo for text quality scoring.')
textstring = st.text_input('Methods text')

if textstring:

  st.subheader('Language Detected:')
  
  st.subheader('Word Count:')
  
  st.subheader('Readability: (Flesch Reading Ease Score)')
  ease = textstat.flesch_reading_ease(textstring)
  st.write(ease)
  st.subheader('Grammar errors:')
  tool = language_tool_python.LanguageToolPublicAPI('en')

  matches = tool.check(textstring)
  st.write(len(matches))
  st.write(matches)
