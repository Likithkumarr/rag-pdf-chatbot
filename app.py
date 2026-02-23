from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama

from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

loader = PyPDFLoader("docs/attention-is-all-you-need-Paper.pdf")
documents = loader.load()

splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
docs = splitter.split_documents(documents)

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

vectordb = Chroma.from_documents(docs, embeddings)
retriever = vectordb.as_retriever()

llm = Ollama(model="tinyllama")

prompt = ChatPromptTemplate.from_template("""
Answer using ONLY this context:

{context}

Question: {input}
""")

doc_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, doc_chain)

while True:
    q = input("Ask: ")
    if q == "exit":
        break
    res = rag_chain.invoke({"input": q})
    print(res["answer"])