# News Analyzer

News Analyzer is a simple Generative AI application that analyzes news content and generates a structured summary with important information.

## Features

- Accepts news content as input.
- Analyzes news using a Large Language Model (LLM).
- Generates structured information from unstructured news text.
- Provides an easy-to-use interface built with Streamlit.

## Technologies Used

- Python
- LangChain
- Groq API
- LLM (GPT-OSS)
- Streamlit
- UV

## Installation

1. Clone the repository:

```bash
git clone https://github.com/meghal14/NewsAnalyzer.git
```

2. Navigate to the project folder:

```bash
cd NewsAnalyzer
```

3. Create and activate a virtual environment.

4. Install the dependencies:

```bash
uv sync
```

5. Create a `.env` file in the root directory and add your Groq API key:

```env
GROQ_API_KEY=your_api_key
```

## Run the Application

```bash
streamlit run UI-NewsAnalyzer.py
```

## Purpose

This project was developed to learn and explore Generative AI, prompt engineering, and structured output generation using Large Language Models.
