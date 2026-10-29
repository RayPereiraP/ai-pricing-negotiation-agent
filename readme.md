# 🤝 AI B2B Negotiation & Pricing Agent

Mini-aplicação analítica desenvolvida em Python para capacitar executivos de vendas em negociações B2B no ecossistema de delivery. 

## 🎯 Caso de Uso
Quando restaurantes de alto volume (Key Accounts) exigem redução de taxas de comissão, o executivo comercial frequentemente precisa escalar a decisão para a diretoria. Este agente de IA processa a proposta em tempo real, calculando imediatamente a **ZOPA (Zona Possível de Acordo)** e a **BATNA (Melhor Alternativa em Caso de Não Acordo)** com base nas médias regionais e custos operacionais, garantindo que o vendedor feche o contrato com a margem ideal.

## 🛠️ Tecnologias e Implementação
- **Framework:** Python / Streamlit (Rápida prototipação de UI B2B).
- **IA Generativa:** OpenAI API (`gpt-4o-mini`) focada em lógica microeconômica.
- **Ambiente:** Desenvolvido assistido por IA (Cursor IDE).

## 🚀 Como testar localmente
1. Clone o repositório.
2. Instale as dependências: `pip install -r requirements.txt`
3. Exporte sua chave de API: `export OPENAI_API_KEY="sk-..."`
4. Rode a aplicação: `streamlit run src/main.py`