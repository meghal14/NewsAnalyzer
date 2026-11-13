import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel
from typing import Optional, List

load_dotenv()

# Page Configuration
st.set_page_config(
    page_title="PromptPearl - News Analyzer",
    page_icon="📰",
    layout="centered"
)

# Initialize Model
@st.cache_resource
def get_model():
    return init_chat_model(
        "openai/gpt-oss-20b",
        model_provider="groq"
    )

model = get_model()

# Pydantic Model
class News_Analyzer(BaseModel):
    headline: str
    date: Optional[str] = None
    category: str
    location: Optional[str] = None
    summary: str
    sentiment: List[str]

parser = PydanticOutputParser(pydantic_object=News_Analyzer)

# Prompt Template
prompt = PromptTemplate.from_template("""
Extract News Information from the given paragraph.

{format_instructions}

News Description:
{paragraph}
""")

# UI Design
st.title("📰 PromptPearl")
st.subheader("AI-Powered News Analyzer")

st.write("Convert lengthy news paragraphs into structured information using AI.")

st.divider()

news_input = st.text_area(
    "Enter News Description",
    placeholder="Paste your news article here...",
    height=200
)

if st.button("✨ Analyze News", use_container_width=True):

    if not news_input.strip():
        st.warning("Please enter a news paragraph first.")

    else:
        with st.spinner("Analyzing your news..."):

            try:
                final_prompt = prompt.invoke({
                    "paragraph": news_input,
                    "format_instructions": parser.get_format_instructions()
                })

                response = model.invoke(final_prompt)

                result = parser.parse(response.content)

                st.success("News Analyzed Successfully!")

                st.divider()

                st.subheader("📌 Analysis Results")

                st.write("**Headline:**", result.headline)

                col1, col2 = st.columns(2)

                with col1:
                    st.metric("Category", result.category)

                with col2:
                    st.metric("Location", result.location or "Not specified")

                st.write("**Date:**", result.date or "Not specified")

                st.write("**Summary:**")
                st.info(result.summary)

                st.write("**Sentiment:**")

                for sentiment in result.sentiment:
                    st.write(f"• {sentiment}")

                with st.expander("View Structured JSON"):
                    st.json(result.model_dump())

            except Exception as e:
                st.error(f"Something went wrong: {e}")

st.divider()

st.caption("Built with ❤️ using LangChain, Groq, Pydantic & Streamlit")
