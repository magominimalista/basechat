import streamlit as st
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain_community.document_loaders import CSVLoader
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

# Configurar página do Streamlit
st.set_page_config(
    page_title="E-mail manager", page_icon=":bird:"
)

# Função para carregar documentos do CSV
def load_documents_from_csv(file_path):
    try:
        loader = CSVLoader(file_path=file_path)
        documents = loader.load()
        return documents
    except Exception as e:
        st.warning(f"Erro ao carregar documentos do CSV: {e}")
        return []

# Carregar documentos do CSV
csv_file_path = "knowledge_base.csv"
documents = load_documents_from_csv(csv_file_path)

if documents:
    # Inicializar embeddings do OpenAI
    embeddings = OpenAIEmbeddings()

    # Inicializar banco de dados FAISS com os documentos e embeddings
    db = FAISS.from_documents(documents, embeddings)

    # Configurar modelo de linguagem ChatOpenAI
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")

    # Template de prompt para modelo de resposta
    template = """
    Você é um assistente virtual de um freelancer full stack em programação com foco na web.....
    Sua funnnção será responder e-mails que recebo de potenciais clientes.
    Vou te passar algumas perguntas e respostas que tenho recebido de clientes e potenciais clientes.

    Siga todas as regras abaixo:
    1/ Você deve iniciar as respostas com um Olá, tudo bem?

    2/ Suas respostas devem ser similares ou até identicas as respostas passadas em termos de comprimento, 
    tom de voz, argumentos lógicos e demais detalhes.

    3/ Algumas respostas pode conter links ou conteúdos irrelevantes. 
    Preste atenção ao conteúdo útil da mensagem.

    4/ Ao final notifique que se ainda tiver ficado dúvidas poderá entrar em contato comigo pelo Whatsapp
    no número 55 84 99962-2586 ou pelo link https://wa.me/5584999622586.

    Atensiosamente,

    Philipe Cairon (Mago Minimalista)

    Aqui está uma pergunta recebida de um novo cliente.
    {message}

    Aqui está uma resposta enviada a um de nossos clientes.
    Isso servirá de base para que você compreenda meus serviços de forma a atender bem o meu público.
    {best_practice}

    Escreva a melhor resposta que eu deveria enviar para este potencial cliente:
    """

    prompt = PromptTemplate(
        input_variables=["message", "best_practice"],
        template=template
    )

    # Configurar cadeia de modelo de linguagem LLMChain
    chain = LLMChain(llm=llm, prompt=prompt)

# Função para recuperar informações similares usando Faiss
def retrieve_info(query):
    if documents:
        similar_response = db.similarity_search(query, k=3)
        return [doc.page_content for doc in similar_response]
    else:
        return []

# Função para gerar resposta com base na mensagem do cliente
def generate_response(message):
    if documents:
        best_practice = retrieve_info(message)
        response = chain.run(message=message, best_practice=best_practice)
        return response
    else:
        return "Não é possível gerar uma resposta pois o CSV está vazio ou não pôde ser carregado."

# Função principal do Streamlit
def main():
    st.header("E-mail do cliente")
    message = st.text_area("E-mail do cliente")

    if st.button("Gerar resposta") and message:
        st.info("Gerando um e-mail baseado nas melhores práticas...")
        result = generate_response(message)
        st.write(result)

if __name__ == '__main__':
    main()
