from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Annie's Pub Tour", page_icon="🍺", layout="wide")
html = Path(__file__).with_name("galway-pub-crawl.html").read_text(encoding="utf-8")
components.html(html, height=3200, scrolling=True)