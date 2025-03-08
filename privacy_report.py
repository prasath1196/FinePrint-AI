import streamlit as st
from crawl import extract_data
from report_ui import report_markdown

# User Input
st.title("What Am I Agreeing To? 🤔")
url = st.text_input("Enter Terms of Use URL", key='url')

if st.button("Generate Report"):
    if url:
        extracted_data = extract_data(url)
        print(extracted_data)

        st.title("📜 Terms of Service Report")  
        st.write("🔎 This report summarizes key insights extracted from the Terms of Service.")
        st.html(report_markdown(extracted_data))

    else:
        st.error("⚠️ Please enter a valid URL!")
