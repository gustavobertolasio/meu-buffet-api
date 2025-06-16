# 🎉 Meu Buffet

API desenvolvida com [FastAPI](https://fastapi.tiangolo.com/) para gerenciamento de buffets e serviços relacionados. Estruturada para ser escalável, segura e de fácil manutenção, com carregamento dinâmico de rotas e documentação automática.

---

## 📦 Tecnologias e bibliotecas utilizadas

- **Python 3.11.9** 
- **FastAPI** – Framework principal para construção da API
- **Uvicorn** – Servidor ASGI leve e rápido para desenvolvimento e produção
- **SQLAlchemy** – ORM para interação com bancos de dados relacionais
- **Passlib[bcrypt]** – Utilizado para hashing seguro de senhas
- **Python-Jose[cryptography]** – Para geração e verificação de tokens JWT
- **python-dotenv** – Carregamento automático de variáveis de ambiente do `.env`
- **python-multipart** – Necessário para suporte a formulários com upload de arquivos

---

## 📁 Organização do projeto

meu-buffet-api/

├── main.py # Arquivo principal da aplicação

├── .env # Variáveis de ambiente

├── models/ # Modelos SQLAlchemy

├── routes/ # Rotas organizadas em módulos

│ ├── init.py

│ ├── auth.py

│ └── service.py

├── database/ # Conexão e setup do banco

├── schemas/ # Schemas (Pydantic) para validação

└── utils/ # Funções auxiliares (ex: autenticação, segurança)

## 🚀 Como executar localmente

1. **Clone o repositório:**

```
git clone https://github.com/gustavobertolasio/meu-buffet-api.git
cd meu-buffet-api
```

2. **Crie e ative um ambiente virtual:**

```
python -m venv .venv
source .venv/bin/activate      # Linux/macOS
.\.venv\Scripts\activate       # Windows
```

3. **Instale as dependências:**

```
pip install -r requirements.txt
```

4. **Configure o arquivo .env:**

```
DATABASE_URL=sqlite:///./buffet.db
SECRET_KEY=sua-chave-secreta
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

5. **Execute o servidor:**

```
uvicorn main:app --reload
```

## 🚀 Roteamento

A API está configurada para descobrir e registrar automaticamente todas as rotas definidas em arquivos dentro da pasta routes/.


### Como adicionar uma nova rota:

1. **Crie um novo arquivo dentro de routes/, por exemplo evento.py:**

```
from fastapi import APIRouter

router = APIRouter(prefix="/eventos", tags=["eventos"])

@router.get("/")
def listar_eventos():
    return {"eventos": []}

```

2. **Pronto! A rota /eventos já estará disponível e documentada automaticamente no Swagger (/docs).**


## 🚀 Documentação interativa
Acesse a documentação automática em:

- http://localhost:8000/docs (Swagger UI)

- http://localhost:8000/redoc (ReDoc)