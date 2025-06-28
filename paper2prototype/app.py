import streamlit as st
from main import get_arxiv_abstract, summary

st.set_page_config(page_title="arXiv Paper to a Prototype", page_icon=":plant:", layout="centered")
st.title("arXiv Paper to a Prototype :plant:")

paper_input = st.text_input("Enter the arXiv paper ID or URL:", placeholder="e.g. 2301.00001 or https://arxiv.org/abs/2301.00001")
if st.button("Generate Code Prototype") and paper_input:
    with st.spinner("Reading paper..."):
        info = get_arxiv_abstract(paper_input)
        if info:
            st.subheader(info["title"])
            st.markdown(f"[Read on arXiv]({info['url']})")
            st.write(info("summary"))
            st.markdown("----")
            st.subheader("AI Generated Code Prototype")
            code = get_code_suggestion(info["summary"])
            st.code(code, language="python")
        else:
            st.error("Paper not found or invalid ID.")
            