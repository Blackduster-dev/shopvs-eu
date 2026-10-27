#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Orquestrador Definitivo da Esteira Dupla Europeia (ES + DE) - ShopVS EU
Suporta compilação, pins e disparos em lote para todos os duelos do catálogo.
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

def obter_lista_duelos():
    duelos_path = os.path.join(BASE_DIR, "data", "duelos.json")
    if os.path.exists(duelos_path):
        return carregar_json("data/duelos.json")
    d = carregar_json("data/produto_duplo.json")
    return d if isinstance(d, list) else [d]

def verificar_pauta_mercado():
    print("[0/4] Verificando Pauta de Mercado (Ponto 0)...")
    pauta_path = os.path.join(BASE_DIR, "data", "pauta_mercado.json")
    if not os.path.exists(pauta_path):
        print("  -> [AVISO] data/pauta_mercado.json não encontrado. Execute a Skill 00 para pesquisar novas pautas.")
        return False
    try:
        pauta = carregar_json("data/pauta_mercado.json")
        status = pauta.get("status_pauta", "")
        cat = pauta.get("analise_macro", {}).get("categoria_id", "")
        print(f"  -> [OK] Pauta detectada: Categoria '{cat}' (Status: {status})")
        return True
    except Exception as e:
        print(f"  -> [ERRO] data/pauta_mercado.json corrompido: {e}")
        return False

def verificar_skills():
    skills_dir = os.path.join(BASE_DIR, ".antigravity", "skills") if os.path.exists(os.path.join(BASE_DIR, ".antigravity", "skills")) else os.path.join(BASE_DIR, "skills")
    skills_esperadas = [
        "00_pesquisador_mercado_eu.md",
        "01_garimpador_duplo_eu.md",
        "02_redator_bilingue_es_de.md",
        "03_distribuidor_pinterest_telegram.md"
    ]
    print("[1/4] Verificando Skills da Esteira Antigravity...")
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

def executar_geracao_pins(lista_duelos):
    print(f"\n[3/4] Gerando Pins Verticais para Pinterest (1000x1500px) [{len(lista_duelos)} duelos]...")
    from gerar_pins import criar_card_pinterest
    output_dir = os.path.join(BASE_DIR, "assets", "pins")

    for d in lista_duelos:
        pa = d["produto_a"]
        pb = d["produto_b"]

        # Destaques ES dinâmicos
        specs_es = pa.get("specs_es", {})
        destaques_es = [f"{k}: {v}" for k, v in list(specs_es.items())[:3]]
        if len(destaques_es) < 3:
            destaques_es = pa.get("pros_es", ["Prestaciones avanzadas", "Calidad comprobada", "Alta durabilidad"])[:3]
        pin_es_path = os.path.join(output_dir, f"{d['slug_es']}.png")
        criar_card_pinterest("ES", pa["nome"], pb["nome"], destaques_es, pin_es_path)

        # Destaques DE dinâmicos
        specs_de = pa.get("specs_de", {})
        destaques_de = [f"{k}: {v}" for k, v in list(specs_de.items())[:3]]
        if len(destaques_de) < 3:
            destaques_de = pa.get("pros_de", ["Hervorragende Leistung", "Geprüfte Qualität", "Hohe Langlebigkeit"])[:3]
        pin_de_path = os.path.join(output_dir, f"{d['slug_de']}.png")
        criar_card_pinterest("DE", pa["nome"], pb["nome"], destaques_de, pin_de_path)

def formatar_telegram(config, lista_duelos):
    print(f"\n[4/4] Formatando disparos 100% nativos para Telegram (ES & DE) [{len(lista_duelos)} duelos]...")
    dom = config.get("dominio_site", "https://shopvs-eu.pages.dev").rstrip("/")
    blocos_es = []
    blocos_de = []

    for d in lista_duelos:
        pa = d["produto_a"]
        pb = d["produto_b"]

        pros_a_es = pa.get("pros_es", pa.get("pros", ["Excelente rendimiento"]))[0]
        pros_b_es = pb.get("pros_es", pb.get("pros", ["Excelente rendimiento"]))[0]
        pros_a_de = pa.get("pros_de", pa.get("pros", ["Hervorragende Leistung"]))[0]
        pros_b_de = pb.get("pros_de", pb.get("pros", ["Hervorragende Leistung"]))[0]

        msg_es = f"""⚡ Comparativa & Oferta Técnica: {pa['nome']} vs {pb['nome']}
🔍 Analizamos opiniones reales y fallos ocultos antes de que compres:
• {pa['marca']}: {pros_a_es}
• {pb['marca']}: {pros_b_es}

📊 Ver tabla comparativa completa: {dom}/es/{d['slug_es']}.html
🛒 Ver oferta actual en Amazon España: {pa['link_es']} *(Enlace de Afiliado)*"""
        blocos_es.append(msg_es)

        msg_de = f"""🔥 Direktvergleich & Kaufberatung: {pa['nome']} vs. {pb['nome']}
✅ Echte Käufermeinungen und technische Daten im Praxis-Check:
• {pa['marca']}: {pros_a_de}
• {pb['marca']}: {pros_b_de}

📊 Zum vollständigen Testbericht: {dom}/de/{d['slug_de']}.html
🛒 Direkt zu Amazon Deutschland: {pa['link_de']} *(Affiliate-Link)*"""
        blocos_de.append(msg_de)

    telegram_file = os.path.join(BASE_DIR, "data", "telegram_disparos.txt")
    with open(telegram_file, "w", encoding="utf-8") as f:
        f.write("=== CANAL ESPAÑA (Chollos & Comparativas) ===\n\n")
        f.write("\n\n" + "-"*40 + "\n\n".join(blocos_es))
        f.write("\n\n" + "="*50 + "\n\n")
        f.write("=== CANAL DEUTSCHLAND (Schnäppchen & Testbericht) ===\n\n")
        f.write("\n\n" + "-"*40 + "\n\n".join(blocos_de))
        f.write("\n")
    print(f"  -> [OK] Disparos salvos sem texto em português em: {telegram_file}")

def rodar_esteira():
    print("=" * 60)
    print("   INICIANDO ESTEIRA DUAL-MARKET SHOPVS EU (ES + DE)")
    print("=" * 60)
    verificar_pauta_mercado()
    verificar_skills()
    executar_indexador_e_build()
    config = carregar_json("config_afiliados.json")
    lista_duelos = obter_lista_duelos()
    executar_geracao_pins(lista_duelos)
    formatar_telegram(config, lista_duelos)
    print("\n[SUCESSO TOTAL] Projeto 100% pronto para git push!")

if __name__ == "__main__":
    rodar_esteira()
