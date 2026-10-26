#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Orquestrador da Esteira Dupla Europeia (ES + DE)
Executa sequencialmente o fluxo:
1. Sincronização de tags e indexação via indexer.py
2. Verificação das skills do Antigravity
3. Compilação estática dos artigos bilíngues (ES e DE)
4. Geração dos ativos visuais (Pins 1000x1500px para Pinterest)
5. Preparação dos disparos bilíngues para Telegram
"""

import os
import sys
import json
import subprocess

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, "scripts"))

def carregar_config():
    cfg_path = os.path.join(BASE_DIR, "config_afiliados.json")
    if not os.path.exists(cfg_path):
        raise FileNotFoundError(f"Arquivo não encontrado: {cfg_path}")
    with open(cfg_path, "r", encoding="utf-8") as f:
        return json.load(f)

def verificar_skills():
    skills_dir = os.path.join(BASE_DIR, ".antigravity", "skills")
    skills_esperadas = [
        "01_garimpador_duplo_eu.md",
        "02_redator_bilingue_es_de.md",
        "03_distribuidor_pinterest_telegram.md"
    ]
    print("[1/5] Verificando Skills do Antigravity...")
    for s in skills_esperadas:
        p = os.path.join(skills_dir, s)
        if not os.path.exists(p):
            raise FileNotFoundError(f"Skill obrigatória ausente: {p}")
        print(f"  -> [OK] Skill detectada: {s}")

def executar_indexacao_e_build():
    print("\n[2/5] Executando sincronização de tags e compilação editorial...")
    import indexer
    indexer.main()

def executar_geracao_pins(dados_duplos):
    print("\n[3/5] Gerando ativos visuais verticais para Pinterest (1000x1500px)...")
    from gerar_pins import criar_card_pinterest
    output_dir = os.path.join(BASE_DIR, "assets", "pins")

    pa = dados_duplos["produto_a"]
    pb = dados_duplos["produto_b"]

    specs_es = pa.get("specs_es", {})
    destaques_es = [
        f"Presión: {specs_es.get('Presión de Bomba', '15 bar')}",
        f"Molinillo: {specs_es.get('Molinillo', 'Acero cónico')}",
        f"Limpieza: {specs_es.get('Grupo Infusor', '100% Extraíble')}"
    ]
    pin_es_path = os.path.join(output_dir, f"{dados_duplos['slug_es']}.png")
    criar_card_pinterest("ES", pa["nome"], pb["nome"], destaques_es, pin_es_path)

    specs_de = pa.get("specs_de", {})
    destaques_de = [
        f"Pumpendruck: {specs_de.get('Pumpendruck', '15 Bar')}",
        f"Mahlwerk: {specs_de.get('Mahlwerk', 'Edelstahl-Kegel')}",
        f"Brühgruppe: {specs_de.get('Brühgruppe', '100% Herausnehmbar')}"
    ]
    pin_de_path = os.path.join(output_dir, f"{dados_duplos['slug_de']}.png")
    criar_card_pinterest("DE", pa["nome"], pb["nome"], destaques_de, pin_de_path)

def formatar_telegram(config, dados_duplos):
    print("\n[4/5] Formatando disparos para canais do Telegram (ES & DE)...")
    pa = dados_duplos["produto_a"]
    pb = dados_duplos["produto_b"]
    dom = config["dominio_site"]

    pro_es_a = pa.get("pros_es", ["Grupo infusor extraíble"])[0]
    pro_es_b = pb.get("pros_es", ["Diseño compacto"])[0]

    pro_de_a = pa.get("pros_de", ["Herausnehmbare Brühgruppe"])[0]
    pro_de_b = pb.get("pros_de", ["Kompaktes Design"])[0]

    msg_es = f"""⚡ Comparativa & Oferta Técnica: {pa['nome']} vs {pb['nome']}
🔍 Analizamos opiniones reales y fallos ocultos antes de que compres:
- {pro_es_a}
- {pro_es_b}

📊 Ver análisis técnico completo: {dom}/es/{dados_duplos['slug_es']}.html
🛒 Ver precio actual en Amazon España: {pa['link_es']} *(Enlace de Afiliado)*"""

    msg_de = f"""🔥 Direktvergleich & Kaufberatung: {pa['nome']} vs. {pb['nome']}
✅ Echte Käufermeinungen und technische Daten im Praxis-Check:
- {pro_de_a}
- {pro_de_b}

📊 Zum vollständigen Testbericht: {dom}/de/{dados_duplos['slug_de']}.html
🛒 Direkt zu Amazon Deutschland: {pa['link_de']} *(Affiliate-Link)*"""

    telegram_file = os.path.join(BASE_DIR, "data", "telegram_disparos.txt")
    with open(telegram_file, "w", encoding="utf-8") as f:
        f.write("=== CANAL ESPANHA (Chollos & Comparativas) ===\n\n" + msg_es + "\n\n" + "="*50 + "\n\n")
        f.write("=== CANAL ALEMANHA (Schnäppchen & Testbericht) ===\n\n" + msg_de + "\n")
    print(f"  -> [OK] Disparos formatados e salvos em: {telegram_file}")

def rodar_esteira():
    print("=" * 60)
    print("   INICIANDO ESTEIRA DUAL-MARKET SHOPVS EU (ES + DE)")
    print("=" * 60)
    
    config = carregar_config()
    verificar_skills()
    executar_indexacao_e_build()
    
    dados_path = os.path.join(BASE_DIR, "data", "produto_duplo.json")
    if not os.path.exists(dados_path):
        raise FileNotFoundError(f"Dados do produto ausentes: {dados_path}")
    with open(dados_path, "r", encoding="utf-8") as f:
        dados_duplos = json.load(f)

    executar_geracao_pins(dados_duplos)
    formatar_telegram(config, dados_duplos)

    print("\n[5/5] Resumo da Operação:")
    print(f"  -> Vitrine Raiz: {config['dominio_site']}/")
    print(f"  -> Artigo Espanha: {config['dominio_site']}/es/{dados_duplos['slug_es']}.html")
    print(f"  -> Artigo Alemanha: {config['dominio_site']}/de/{dados_duplos['slug_de']}.html")
    print(f"  -> Impressum / Legal: {config['dominio_site']}/legal/")
    print("\n[SUCESSO] Todo o ecossistema ShopVS EU está pronto e sincronizado!")

if __name__ == "__main__":
    rodar_esteira()
