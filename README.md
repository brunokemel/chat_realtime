Chat em Tempo Real com Autenticação JWT e Persistência em PostgreSQL

🚧 Projeto em construção — sugestões para melhorias são bem-vindas. Mais funcionalidades serão adicionadas em breve.

Este repositório contém um sistema de chat em tempo real, com autenticação de usuários via JWT e persistência de mensagens em PostgreSQL.

🛠️ Tecnologias Utilizadas

Python: Linguagem principal do projeto

FastAPI: Framework web para APIs

PostgreSQL: Banco de dados para armazenamento das mensagens e usuários

WebSockets: Comunicação em tempo real entre clientes

📁 Estrutura do Repositório

app/ — Código-fonte da aplicação

Chat.txt — Arquivo com informações ou dados relacionados ao chat

requirements.txt — Dependências Python

package.json — Configuração de ferramentas ou bibliotecas JS (se aplicável)

🔑 Funcionalidades

Autenticação de usuários com JWT

Chat em tempo real via WebSocket

Persistência das mensagens no PostgreSQL

Histórico de mensagens (em desenvolvimento)

Suporte a múltiplas salas de chat (em desenvolvimento)

⚙️ Pré-requisitos

Python 3.10+

PostgreSQL

Node.js (caso utilize scripts JS auxiliares)

Como Executar Localmente
# Clone o repositório
git clone https://github.com/brunokemel/chat_realtime.git
cd chat_realtime

# Crie e ative um ambiente virtual (recomendado)
python -m venv venv
# Linux/macOS
source venv/bin/activate
# Windows
venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt

# Configure o PostgreSQL
# - Crie um banco de dados e usuário
# - Atualize as configurações de conexão no arquivo de configuração

# Execute a aplicação
uvicorn app.main:app --reload
