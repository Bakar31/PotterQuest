import os
import gradio as gr
from pathlib import Path
from typing import Union
from langchain import VectorDBQA
from langchain.llms import HuggingFaceHub
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores.faiss import FAISS
from langchain import PromptTemplate

os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"
index_path = 'index/'

def load_document_store(path: Union[str, Path]) -> FAISS:
    embeddings = HuggingFaceEmbeddings()
    document_store = FAISS.load_local(path, embeddings)
    return document_store


examples = [
    "Why harry potter is famous?", 
    "How would you sneak into Hogwarts without being detected?",
    "Who is the most badass wizard in the world?",
    "Why are the Dursleys so mean to Harry?", 
    'What position does Harry play in Quidditch?', 
    "Who is harry potter's best friend?",
    'Whom do Harry and Ron accidentally lock in the bathroom with the troll?',
    'In what house is Malfoy?', 
    'Who is professor dumboldore?', 
    'To whom does the invisibility cloak belong originally?', 
    'Which teacher is trying to steal the Sorcerer’s Stone?', 
    'Who is Fluffy?', 
    'Who decides where the children will be housed at Hogwarts?', 
    "Where do Harry and the Dursleys go for Dudley's birthday?",
    'In what house did the Sorting Hat almost put Harry?',
    'What subject does Professor McGonagall teach?', 
    'What did Dobby catch that set him free from Mr. Malfoy?', 
    "The Hogwarts motto is “Draco dormiens nunquan titillandus.” What does it mean?", 
    "How many presents did Dudley Dursley receive on his birthday in total?", 
    "What was the Fat Lady’s password to get into the Gryffindor common room?", 
    "When Harry, Ron and Hermione make Polyjuice Potion, who steals the ingredients from Professor Snape’s office?",
    "What two creatures are Hippogriffs a mix of?",  
    "What is Draco Malfoy’s mother’s name?",
    "Which of Voldemort’s Horcruxes do Harry and Dumbledore track down—but it turns out to be a fake?",
    "What is Professor Snape’s Patronus?", 
    "who killed dumboldore?",
    'What was the last horcrux?'
]

def ask(question, repo_id = "google/flan-ul2"):

    if len(question) == 0:
        return ""
    
    document_store = load_document_store(index_path)
    chain = VectorDBQA.from_chain_type(
        llm=HuggingFaceHub(repo_id = repo_id),
        chain_type="stuff",
        vectorstore=document_store,
        return_source_documents=True
    )

    response = chain(question)
    return response["result"].strip()


demo = gr.Blocks()

with demo:
    gr.Markdown("# PotterQuest: Your One-Line Wizardry Encyclopedia")
    with gr.Row():
        with gr.Column():
            question = gr.Textbox(lines=2, label="Question")
            with gr.Row():
                clear = gr.Button("Clear")
                btn = gr.Button("Submit", variant="primary")
        with gr.Column():
            answer = gr.Textbox(lines=2, label="Answer")
    btn.click(ask, [question], answer)
    clear.click(lambda _: "", question, question)
    gr.Examples(examples, question)
    gr.Markdown("💻 Checkout the source code on [GitHub](https://github.com/Bakar31/PotterQuest).")
demo.launch()
