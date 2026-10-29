import streamlit as st
from openai import OpenAI
import json
import os

# Configuração da Interface (Estética Dark Mode nativa do Streamlit)
st.set_page_config(page_title="AI B2B Negotiator", layout="centered")
st.title("🤝 Agente de Inteligência e Negociação B2B")
st.markdown("Análise de propostas de restaurantes parceiros para definição de limites comerciais.")

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY", "SUA_CHAVE_AQUI"))

def analyze_proposal(restaurant_name, proposed_fee, market_avg_fee):
    prompt = f"""
    Você é um estrategista comercial sênior de um app de delivery. 
    Analise a proposta do restaurante e retorne ESTRITAMENTE um JSON.
    
    Dados:
    - Restaurante: {restaurant_name}
    - Taxa proposta pelo restaurante: {proposed_fee}%
    - Média do mercado local: {market_avg_fee}%
    - Custo operacional mínimo da plataforma: 12%
    
    Calcule e defina:
    1. ZOPA (Zona Possível de Acordo): O intervalo entre o custo mínimo (12%) e a média do mercado.
    2. BATNA (Melhor Alternativa): O que fazer se eles não aceitarem a taxa mínima.
    3. MASA (Melhor Acordo Sem Alternativa): Ponto de ruptura comercial.
    4. Argumento: Um parágrafo curto de persuasão para o vendedor usar.

    Formato de Saída (JSON):
    {{
        "zopa_range": "X% a Y%",
        "batna_strategy": "estratégia",
        "masa_limit": "limite",
        "sales_pitch": "argumento"
    }}
    """
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        response_format={"type": "json_object"},
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )
    return json.loads(response.choices[0].message.content)

# Formulário de Entrada
with st.form("negotiation_form"):
    rest_name = st.text_input("Nome do Restaurante", "Burger House Alpha")
    prop_fee = st.number_input("Taxa Proposta pelo Parceiro (%)", min_value=1.0, max_value=30.0, value=8.0)
    mkt_fee = st.number_input("Média Praticada na Região (%)", min_value=1.0, max_value=30.0, value=18.0)
    submit = st.form_submit_button("Gerar Estratégia de Negociação")

if submit:
    with st.spinner("Analisando limites comerciais e cenários..."):
        result = analyze_proposal(rest_name, prop_fee, mkt_fee)
        
        st.subheader("📊 Resultados da Análise")
        col1, col2, col3 = st.columns(3)
        col1.metric("ZOPA", result["zopa_range"])
        col2.metric("MASA (Ruptura)", result["masa_limit"])
        col3.metric("Taxa Proposta", f"{prop_fee}%", f"{prop_fee - mkt_fee}% vs Mercado", delta_color="inverse")
        
        st.info(f"**BATNA (Alternativa):** {result['batna_strategy']}")
        st.success(f"**Pitch de Vendas Sugerido:** {result['sales_pitch']}")