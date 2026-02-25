import streamlit as st
from src.scrape import scrape_website, split_dom_content, clean_body_content, extract_body_content
from src.llm import parse_with_openai

st.title("Anything scraper with AI")
url = st.text_input("Enter a Website URL: ")

# Start scraping
if st.button("Scrape site"):
    st.write("Scraping the website...")

    result = scrape_website(url)
    print(result)
    # Clean the data
    cleaned_content = clean_body_content(result)
    st.session_state.dom_content = cleaned_content

    # View DOM content that was scraped
    with st.expander("View DOM content:"):
        st.text_area("Dom content", cleaned_content, height=500)

# Parse the data with LLM-analysis
if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse?")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content...")

            # Split the data into batches
            dom_batches = split_dom_content(st.session_state.dom_content)
            try:
                result = parse_with_openai(dom_batches, parse_description)
                st.write(result)
            except RuntimeError as exc:
                st.error(str(exc))
