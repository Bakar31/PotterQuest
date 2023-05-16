# PotterQuest: Your One-Line Wizardry Encyclopedia

## Unveiling Harry Potter's Secrets with Single-Line Answer

## Overview:

The world of Harry Potter is filled with captivating stories, intricate details, and a vast array of characters and events. `PotterQuest` offers a streamlined approach to explore and uncover the secrets hidden within the Harry Potter series. It aims to provide users with a comprehensive and efficient tool for answering Harry Potter-related questions using a single-line response. By leveraging the power of the open-source Large Language Model and a vector database, PotterQuest extracts answers from the rich content of the Harry Potter books. It has achieved impressive results without relying on any fancy external APIs. With a single-line answer, users can quickly find relevant information for their queries, allowing them to delve deeper into the magical universe created by **J.K. Rowling**. The project utilizes the *Gradio* framework to provide a user-friendly frontend for easy interaction.

## Objectives:

- Develop a question-answering system specifically tailored to Harry Potter-related queries.
- Provide users with an intuitive interface to input questions and receive concise answers.
- Optimize the system to achieve accurate and relevant responses while maintaining efficiency.
- Utilize open-source resources and Langchain, to avoid reliance on external APIs.

## My Approach:

### Data Preprocessing:
The text version Harry Potter books undergo standard preprocessing techniques to prepare them for conversion into a vector database. This step ensures that the text is cleaned and formatted appropriately.

### Vector Database Creation:
The preprocessed Harry Potter books are transformed into a vector database. This process involves encoding the textual information into numerical vectors using the open-source **Hugging Face** embedding model. By representing the books in vector form, efficient retrieval of relevant information becomes possible.

### Question-Answering Chain:
LangChain, a powerful language processing framework, is employed for question-answering against the vector database created in the previous step. The `google/flan-ul2` model is used to power this step. Users can pose their queries related to the Harry Potter universe, and LangChain will search the vector database to extract concise, one-line answers.

### User-Friendly Frontend with Gradio:
To enhance the user experience and facilitate interaction, the project utilizes the Gradio framework. Gradio provides an intuitive frontend where users can input their questions and receive instant answers in a user-friendly format. The integration of Gradio ensures a seamless and accessible experience for users of the PotterQuest system.

## Conclusion:
The PotterQuest project successfully creates a powerful and efficient tool for exploring the magical world of Harry Potter. By leveraging open-source Hugging Face models and implementing a vector database with Langchain, PotterQuest provides users with single-line answers to their Harry Potter-related questions. PotterQuest is an excellent example of how open-source technology can be used to solve complex problems. With its streamlined approach and comprehensive coverage of the books, PotterQuest aims to be the go-to encyclopaedia for all fans of the Harry Potter series, offering quick and accurate insights into its secrets and intricacies without the need for a fancy API.
