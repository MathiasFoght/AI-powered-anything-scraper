import streamlit as st
from src.scrape import scrape_website, split_dom_content, clean_body_content, extract_body_content

st.title("Anything scraper with AI")
url = st.text_input("Enter a Website URL: ")

if st.button("Scrape site"):
    st.write("Scraping the website...")

    result = scrape_website(url)
    print(result)
    cleaned_content = clean_body_content(result)
    st.session_state.dom_content = cleaned_content

    # View DOM content that was scraped
    with st.expander("View DOM content:"):
        st.text_area("Dom content", cleaned_content, height=500)

if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse?")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content...")

            dom_batches = split_dom_content(st.session_state.dom_content)


