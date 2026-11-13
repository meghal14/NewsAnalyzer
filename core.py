from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel
from langchain_core.output_parsers import PydanticOutputParser
from typing import List, Optional

load_dotenv()

model = init_chat_model("openai/gpt-oss-20b", model_provider = "groq")


class News_Analyzer(BaseModel):
    headline : str
    date : Optional[str]
    category : str
    location : Optional[str]
    summary : str
    sentiment : list[str]

parser = PydanticOutputParser(pydantic_object=News_Analyzer)

print("-----Welcome to PromptPerl-----")

prompt = PromptTemplate.from_template("""
        Extract News Information {format_instructions}
        News Description: {paragraph}
        """)

para = input("Enter News Detail: ")

final_prompt = prompt.invoke({"paragraph": para,
                            "format_instructions":parser.get_format_instructions})

response = model.invoke(final_prompt)

print(response.content)