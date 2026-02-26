from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

template = (
    "Role: You are tasked with extracting specific information from the following text content: {dom_content}. "
    
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

OPENAI_MODEL = os.getenv("OPENAI_MODEL")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI(
    model=OPENAI_MODEL,
    api_key=OPENAI_API_KEY,
    temperature=0,
)

def is_openai_configured():
    if not OPENAI_API_KEY:
        raise RuntimeError(
            "OPENAI_API_KEY is missing. Please set it in your environment variables."
        )


def parse_with_openai(batches, parse_description):
    is_openai_configured()
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    parsed_content = []

    for i, batch in enumerate(batches, start=1):
        try:
            response = chain.invoke({
                "dom_content": batch,
                "parse_description": parse_description
            })
        except Exception as exc:
            raise RuntimeError(
                "Error during OpenAI API call. Check your internet, API key or the model:" + str(exc)
            ) from exc
        print(f"Parsed batch {i} of {len(batches)}")
        parsed_content.append(response.content if hasattr(response, "content") else str(response))

    return "\n".join(parsed_content)
