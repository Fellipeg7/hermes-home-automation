<div align="center">

# Hermes Home Automation

**Assistente IA residencial** — controle de ar-condicionado, monitor de rede e automação de presença em um único dashboard web.

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-18-61DAFB?style=for-the-badge&logo=react&logoColor=black)
![LG ThinQ](https://img.shields.io/badge/LG%20ThinQ-Integrado-A50034?style=for-the-badge&logo=lg&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Licença](https://img.shields.io/badge/Licen%C3%A7a-MIT-yellow?style=for-the-badge)

</div>

## Sobre

Esse é o meu projeto de automação residencial: um assistente de IA que junta o controle dos dispositivos inteligentes da minha casa em um lugar só, sem precisar ficar abrindo um app diferente pra cada coisa. A API é feita com FastAPI (leve e rápida) e o dashboard com React, e ele cuida de três coisas principais: o controle do ar-condicionado LG ThinQ, o monitoramento dos dispositivos conectados na rede local e automações baseadas na presença dos moradores.

## Funcionalidades

- **Controle de ar-condicionado (LG ThinQ)** — ligar/desligar, ajuste de temperatura, modos de operação, velocidade do ventilador e Jet Mode.
- **Monitor de rede local** — detecta os dispositivos conectados, identifica quem está em casa e alerta quando aparece um dispositivo novo.
- **Automação de presença** — regras automáticas acionadas pela presença ou ausência dos moradores.
- **Dashboard web** — interface responsiva com atualizações em tempo real (WebSockets) construída com React.
- **Health check integrado** — endpoint `/health` pra monitorar o serviço e orquestrar com o Docker.

## Stack tecnológica

| Camada            | Tecnologia                                          |
| ----------------- | --------------------------------------------------- |
| Backend           | Python 3.11+, FastAPI, Uvicorn, WebSockets          |
| Frontend          | React 18, Vite                                      |
| Integrações       | LG ThinQ (ar-condicionado), aiohttp, scan de rede   |
| Infraestrutura    | Docker, Docker Compose                              |

## Como executar

### Pré-requisitos

- Python 3.11 ou superior
- (Opcional) Docker e Docker Compose

### Backend (local)

```bash
# 1. Clone o repositório
git clone https://github.com/Fellipeg7/hermes-home-automation.git
cd hermes-home-automation

# 2. Crie e ative um ambiente virtual
python -m venv .venv
source .venv/bin/activate    # Linux / macOS
# .venv\Scripts\activate     # Windows

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Configure as variáveis de ambiente
cp .env.example .env

# 5. Inicie o servidor de desenvolvimento
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

A documentação interativa da API fica em **http://localhost:8000/docs**.

### Com Docker

```bash
docker compose up --build
```

## Estrutura do projeto

```
hermes-home-automation/
├── src/
│   ├── __init__.py          # Pacote da aplicação
│   └── main.py              # Aplicação FastAPI e health check
├── frontend/                # Dashboard React (em breve)
├── requirements.txt         # Dependências do backend
├── .env.example             # Exemplo de variáveis de ambiente
├── docker-compose.yml       # Orquestração dos serviços (em breve)
└── README.md
```

## Screenshots

> Em breve — vou colocar capturas de tela do dashboard, do painel de controle do ar-condicionado e do monitor de rede.

## Roadmap

- [x] Estrutura inicial do projeto (FastAPI + health check)
- [ ] Integração com LG ThinQ (controle do ar-condicionado)
- [ ] Monitor de rede local (presença por dispositivo)
- [ ] Automação de presença e regras personalizadas
- [ ] Dashboard React com atualizações em tempo real
- [ ] Docker Compose completo (API + frontend)
- [ ] Autenticação e controle de acesso

## Contribuindo

Curte a ideia? Contribuições são bem-vindas. Abre uma *issue* pra gente discutir a mudança ou manda um *pull request* com melhorias. Dá uma olhada no roadmap pra ver onde dá pra ajudar.

## Licença

Distribuído sob a licença **MIT**. Mais detalhes no arquivo `LICENSE`.
