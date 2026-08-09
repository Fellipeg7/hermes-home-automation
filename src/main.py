"""Hermes Home Automation — API principal.

Assistente IA residencial: controle de ar-condicionado (LG ThinQ),
monitor de rede local e automação de presença.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Hermes Home Automation API",
    description=(
        "API do assistente IA residencial: controle de ar-condicionado, "
        "monitor de rede e automação de presença."
    ),
    version="0.1.0",
)

# Permite que o dashboard React (dev server) consuma a API.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root() -> dict:
    """Informações básicas do serviço."""
    return {
        "service": "hermes-home-automation",
        "status": "online",
        "docs": "/docs",
    }


@app.get("/health")
def health() -> dict:
    """Health check para orquestração e monitoramento."""
    return {"status": "ok", "version": app.version}
