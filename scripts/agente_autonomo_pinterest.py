#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Agente Autônomo Pinterest EU:
1. Calcula o Score de Rentabilidade (EV) de produtos (Alto Giro vs. High-Ticket)
2. Valida cada URL da Amazon e foto oficial de estúdio via requisição HTTP real (Anti-404)
3. Minera palavras-chave de alta mostrabilidade por idioma
4. Aciona o Motor de Design de Marketing com Fotos Oficiais (Skill 03)
5. Gera o CSV de agendamento para os 30 dias do mês
"""

import os
import csv
import json
import urllib.request
import urllib.parse
from datetime import datetime, timedelta

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PINS_DIR = os.path.join(BASE_DIR, "assets", "pins", "mes_atual")
CSV_OUT = os.path.join(BASE_DIR, "data", "pinterest_bulk_30dias.csv")

STORE_ID = "shopvseu-21"
CDN_BASE = "https://shopvs-eu.pages.dev/assets/pins/mes_atual"

HEADERS_HTTP = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "Accept-Language": "es-ES,es;q=0.9,de-DE;q=0.8,en-GB;q=0.7"
}

def calcular_ev_produto(preco_eur, comissao_pct, vendas_mensais_estimadas, efeito_carrinho=1.35):
    """
    Calcula o Valor Esperado (EV) do produto combinando margem unitária + velocidade de giro + efeito carrinho.
    Permite que produtos de alta rotatividade (ticket médio/baixo) compitam de igual para igual com High-Ticket.
    """
    comissao_direta = preco_eur * (comissao_pct / 100.0)
    score_ev = comissao_direta * (vendas_mensais_estimadas / 100.0) * efeito_carrinho
    return round(score_ev, 2)

def validar_url_http(url, timeout=8):
    """Testa se o link do produto ou da foto oficial responde 200 OK e não está quebrado."""
    try:
        req = urllib.request.Request(url, headers=HEADERS_HTTP, method="HEAD")
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status in (200, 301, 302)
    except Exception:
        # Fallback com GET leve caso o servidor bloqueie HEAD
        try:
            req_get = urllib.request.Request(url, headers=HEADERS_HTTP, method="GET")
            with urllib.request.urlopen(req_get, timeout=timeout) as resp:
                return resp.status == 200
        except Exception:
            return False

def buscar_tags_alta_mostrabilidade(termo_base, idioma_mkt):
    """
    Consulta sugestões reais de busca (Autocomplete) para enriquecer a coluna Keywords
    com os termos que mais aparecem para os usuários naquele idioma.
    """
    gl_map = {"DE": "de", "ES": "es", "FR": "fr", "IT": "it", "UK": "uk"}
    hl_map = {"DE": "de", "ES": "es", "FR": "fr", "IT": "it", "UK": "en"}
    gl = gl_map.get(idioma_mkt, "es")
    hl = hl_map.get(idioma_mkt, "es")

    query = urllib.parse.quote(termo_base)
    url = f"https://suggestqueries.google.com/complete/search?client=firefox&gl={gl}&hl={hl}&ds=sh&q={query}"
    try:
        req = urllib.request.Request(url, headers=HEADERS_HTTP)
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            sugestoes = data[1][:8] if len(data) > 1 else []
            if sugestoes:
                return ", ".join(sugestoes)
    except Exception:
        pass
    return f"{termo_base}, {termo_base} 2026, {termo_base} test, amazon {gl}"

def filtrar_e_rankear_catalogo(produtos):
    """Ordena o catálogo pelo maior potencial de lucro (EV) antes de montar a grade mensal."""
    rankeados = []
    for p in produtos:
        preco_est = float(p.get("preco_medio_eur", 150.0))
        comissao_est = float(p.get("comissao_pct", 6.0))
        giro_est = float(p.get("giro_mensal_score", 300.0))
        p["ev_score"] = calcular_ev_produto(preco_est, comissao_est, giro_est)
        rankeados.append(p)
    return sorted(rankeados, key=lambda x: x["ev_score"], reverse=True)

if __name__ == "__main__":
    print("[Agente Autônomo] Módulo de Cálculo EV, Validação HTTP e Extração de Tags pronto.")
