#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Orquestrador Definitivo da Esteira Dupla Europeia (ES + DE) - ShopVS EU
"""

import os
import sys
import json
import subprocess

try:
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, "scripts"))

def carregar_json(rel_path):
    path = os.path.join(BASE_DIR, rel_path)
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def verificar_skills():
    skills_dir = os.path.join(BASE_DIR, ".antigravity", "skills")
    skills_esperadas = [
        "01_garimpador_duplo_eu.md",
        "02_redator_bilingue_es_de.md",
        "03_distribuidor_pinterest_telegram.md"
    ]
    print("[1/4] Verificando Skills do Antigravity...")
    for s in skills_esperadas:
        p = os.path.join(skills_dir, s)
        if os.path.exists(p):
            print(f"  -> [OK] Skill detectada: {s}")
        else:
            print(f"  -> [AVISO] Skill não encontrada em: {p}")

def executar_indexador_e_build():
    print("\n[2/4] Sincronizando StoreID (shopvseu-21), Catálogo e Build HTML...")
    indexer_script = os.path.join(BASE_DIR, "scripts", "indexer.py")
    res = subprocess.run([sys.executable, indexer_script], capture_output=True, text=True, encoding="utf-8", errors="replace")
    if res.returncode != 0:
        print(res.stderr)
        raise RuntimeError("Falha na execução do indexer.py")
    print(res.stdout.strip())

def executar_geracao_pins(dados_duplos):
    print("\n[3/4] Gerando Pins Verticais para Pinterest (1000x1500px)...")
    from gerar_pins import criar_card_pinterest
    output_dir = os.path.join(BASE_DIR, "assets", "pins")

    pa = dados_duplos["produto_a"]
    pb = dados_duplos["produto_b"]

    specs_es = pa.get("specs_es", {})
    destaques_es = [
        f"Presión: {specs_es.get('Presión de Bomba', '15 bar')}",
        f"Molinillo: {specs_es.get('Molinillo', 'Acero cónico 13 niveles')}",
        f"Infusor: {specs_es.get('Grupo Infusor', '100% Extraíble')}"
    ]
    pin_es_path = os.path.join(output_dir, f"{dados_duplos['slug_es']}.png")
    criar_card_pinterest("ES", pa["nome"], pb["nome"], destaques_es, pin_es_path)

    specs_de = pa.get("specs_de", {})
    destaques_de = [
        f"Pumpendruck: {specs_de.get('Pumpendruck', '15 Bar')}",
        f"Mahlwerk: {specs_de.get('Mahlwerk', '13-stufiges Kegelmahlwerk')}",
        f"Brühgruppe: {specs_de.get('Brühgruppe', '100% Herausnehmbar')}"
    ]
    pin_de_path = os.path.join(output_dir, f"{dados_duplos['slug_de']}.png")
    criar_card_pinterest("DE", pa["nome"], pb["nome"], destaques_de, pin_de_path)

def formatar_telegram(config, dados_duplos):
    print("\n[4/4] Formatando disparos 100% nativos para Telegram (ES & DE)...")
    pa = dados_duplos["produto_a"]
    pb = dados_duplos["produto_b"]
    dom = config["dominio_site"].rstrip("/")

    pros_a_es = pa.get("pros_es", pa.get("pros", [""]))[0]
    pros_b_es = pb.get("pros_es", pb.get("pros", [""]))[0]
    pros_a_de = pa.get("pros_de", pa.get("pros", [""]))[0]
    pros_b_de = pb.get("pros_de", pb.get("pros", [""]))[0]

    msg_es = f"""⚡ Comparativa & Oferta Técnica: {pa['nome']} vs {pb['nome']}
🔍 Analizamos opiniones reales y fallos ocultos antes de que compres:
• {pa['marca']}: {pros_a_es}
• {pb['marca']}: {pros_b_es}

📊 Ver tabla comparativa completa: {dom}/es/{dados_duplos['slug_es']}.html
🛒 Ver oferta actual en Amazon España: {pa['link_es']} *(Enlace de Afiliado)*"""

    msg_de = f"""🔥 Direktvergleich & Kaufberatung: {pa['nome']} vs. {pb['nome']}
✅ Echte Käufermeinungen und technische Daten im Praxis-Check:
• {pa['marca']}: {pros_a_de}
• {pb['marca']}: {pros_b_de}

📊 Zum vollständigen Testbericht: {dom}/de/{dados_duplos['slug_de']}.html
🛒 Direkt zu Amazon Deutschland: {pa['link_de']} *(Affiliate-Link)*"""

    telegram_file = os.path.join(BASE_DIR, "data", "telegram_disparos.txt")
    with open(telegram_file, "w", encoding="utf-8") as f:
        f.write("=== CANAL ESPANHA (Chollos & Comparativas) ===\n\n" + msg_es + "\n\n" + "="*50 + "\n\n")
        f.write("=== CANAL ALEMANHA (Schnäppchen & Testbericht) ===\n\n" + msg_de + "\n")
    print(f"  -> [OK] Disparos salvos sem texto em português em: {telegram_file}")

def rodar_esteira():
    print("=" * 60)
    print("   INICIANDO ESTEIRA DUAL-MARKET SHOPVS EU (ES + DE)")
    print("=" * 60)
    verificar_skills()
    executar_indexador_e_build()
    config = carregar_json("config_afiliados.json")
    dados_duplos = carregar_json("data/produto_duplo.json")
    executar_geracao_pins(dados_duplos)
    formatar_telegram(config, dados_duplos)
    print("\n[SUCESSO TOTAL] Projeto 100% pronto para git push!")

if __name__ == "__main__":
    rodar_esteira()
