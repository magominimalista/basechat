# Chatbase

Este projeto é um gerenciador de e-mails desenvolvido com Streamlit, FAISS, LangChain e OpenAI. Ele responde automaticamente aos e-mails recebidos de potenciais clientes com base nas melhores práticas.

## Vídeo Demonstrativo
Assista ao vídeo demonstrativo do projeto no YouTube:

[Assista ao vídeo no YouTube](https://youtu.be/eyjU0RUVJRI)


## Requisitos

- Python 3.8 ou superior
- Conta na OpenAI para obter a chave da API

## Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/magominimalista/basechat.git
    cd basechat
    ```

2. Crie um ambiente virtual e ative-o:

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

4. Crie um arquivo `.env` na raiz do projeto e adicione sua chave da API OpenAI:

    ```env
    OPENAI_API_KEY=your_openai_api_key
    ```

5. Certifique-se de ter um arquivo CSV chamado `knowledge_base.csv` na raiz do projeto. Este CSV deve conter as perguntas e respostas que você recebeu de clientes e potenciais clientes.

## Executando o Projeto

1. Para iniciar a aplicação, execute:

    ```bash
    streamlit run main.py
    ```

2. Acesse o Streamlit no seu navegador através do endereço exibido no terminal, geralmente `http://localhost:8501`.

## Estrutura do Projeto

- `main.py`: Contém o código principal do Streamlit.
- `requirements.txt`: Lista de todas as dependências do projeto.
- `.env`: Arquivo para armazenar variáveis de ambiente, como a chave da API OpenAI.

## Utilização

1. Na interface do Streamlit, insira o e-mail recebido do cliente na área de texto.
2. Clique no botão "Gerar resposta".
3. A aplicação irá gerar uma resposta baseada nas melhores práticas armazenadas no CSV.

## Notas

- Certifique-se de que o arquivo CSV `knowledge_base.csv` esteja formatado corretamente e acessível na raiz do projeto.
- Para evitar problemas de carregamento, valide o caminho do arquivo CSV e o conteúdo.

## Contribuição
Contribuições são bem-vindas! Se deseja contribuir para o projeto, siga estes passos:

1. Fork o projeto.
2. Crie uma branch para sua feature (git checkout -b feature/nova-feature).
3. Commit suas mudanças (git commit -am 'Adicionar nova feature').
4. Push para a branch (git push origin feature/nova-feature).
5. Abra um Pull Request.

## Autor
- Nome: Philipe Cairon (Mago Minimalista)
- Email: magominimalista@gmail.com
