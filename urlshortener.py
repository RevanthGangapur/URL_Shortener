import pyshorteners
import streamlit as st

long_url = st.text_input("Enter url:").strip()
tiny= pyshorteners.Shortener()
is_clicked = st.button("submit")
if long_url.startswith("http://") or long_url.startswith("https://"):
    short_url = tiny.tinyurl.short(long_url)
    st.write("Shortened url:", f"{short_url}")
else:
    if is_clicked:
        st.write("Invalid URL. Please enter a full URL starting with http:// or https://")