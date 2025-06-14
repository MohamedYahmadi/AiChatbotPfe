from flask import jsonify
from langchain_ollama import OllamaLLM
from prompts import ANSWER_UNRELATED_QUESTION
from langchain_core.prompts import ChatPromptTemplate

model = OllamaLLM(model="qwen3:8b", temperature=0.1)


def answer_unrelated_question(question):

    response_template = ChatPromptTemplate.from_template(ANSWER_UNRELATED_QUESTION)

    response_chain = response_template | model

    response = response_chain.invoke({
        "question": question
    })

    return jsonify({
        "response": clean_data(response).strip()
    })

def clean_data(response):
    return response.replace("<think>", "").replace("</think>", "")