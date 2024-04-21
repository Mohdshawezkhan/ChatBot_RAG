# ConvoBot

This is a Python application that enables you to load a CSV file and ask questions about its contents using natural language. The application leverages Language Models (LLMs) to generate responses based on the CSV data. The LLM will only provide answers related to the information present in the CSV and also provide normal conversation, it does have some characteristics of a Retrieval-Augmented Generation (RAG) model.
## Preview
<img width="960" alt="upgit" src="https://github.com/Mohdshawezkhan/ConvoBot/assets/103235200/52cb568d-ad39-4a49-a516-63bdac4d2ee6">

## Installation

To install the repository, follow these steps:

1. Clone this repository to your local machine.
2. Install the necessary dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```
3. Additionally, you need to obtain an OpenAI API key and add it to the `.env` file.

## Usage

To use the application, execute the `main.py` file using the Streamlit CLI. Make sure you have Streamlit installed before running the application. Run the following command in your terminal:

```
streamlit run main.py
```
