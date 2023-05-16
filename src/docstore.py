from pathlib import Path
from typing import Union
from langchain.text_splitter import TokenTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores.faiss import FAISS

from process import get_book_chapters

def build_document_store(
    index_save_path: Union[str, Path], chunk_size: int = 150, chunk_overlap: int = 10, overwrite: bool = False):
    index_save_path = Path(index_save_path)

    if index_save_path.exists() and not overwrite:
        raise Exception(f"{index_save_path} already exists. Set overwrite=True to overwrite.")

    docs = []
    text_splitter = TokenTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    for book_number in range(1, 8):
        chapters = get_book_chapters(book_number)
        text_list = list(chapters.values())
        metadata_list = [{"book": book_number, "chapter": name} for name in chapters.keys()]
        docs.extend(text_splitter.create_documents(texts=text_list, metadatas=metadata_list))

    embeddings = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-mpnet-base-v2')
    print(f"Embedding {len(docs)} documents...")
    document_store = FAISS.from_documents(docs, embeddings)
    print(f"Saving index at {index_save_path}")
    document_store.save_local(index_save_path)

    return document_store


def load_document_store(path: Union[str, Path]) -> FAISS:
    embeddings = HuggingFaceEmbeddings()
    document_store = FAISS.load_local(path, embeddings)
    return document_store