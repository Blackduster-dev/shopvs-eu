#!/usr/bin/env python3

# -*- coding: utf-8 -*-

"""

Motor de Armazenamento & Indexador do ShopVS EU

1. Lê as tags oficiais em config_afiliados.json e injeta em todos os produtos do catálogo

2. Valida imagens locais em assets/products/

3. Compila assets/search_index.json

4. Dispara o builder.py sem destruir a Home interativa

"""



import json

import os

import sys

import subprocess



BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



def carregar_json(rel_path):

    path = os.path.join(BASE_DIR, rel_path)

    with open(path, "r", encoding="utf-8") as f:

        return json.load(f)



def salvar_json(rel_path, dados):

    path = os.path.join(BASE_DIR, rel_path)

    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:

        json.dump(dados, f, ensure_ascii=False, indent=2)

    print(f"[OK] Gravado: {rel_path}")



def sincronizar_tags_afiliado(config, catalogo, duplo):

    print("[1/4] Sincronizando Tags de Afiliado da Amazon (ES e DE)...")

    tag_es = config.get("amazon_es_tag", "teste-es-21")

    tag_de = config.get("amazon_de_tag", "teste-de-21")



    for p in catalogo.get("produtos", []):

        asin = p["asin"]

        p["link_es"] = f"https://www.amazon.es/dp/{asin}?tag={tag_es}"

        p["link_de"] = f"https://www.amazon.de/dp/{asin}?tag={tag_de}"



    for key in ["produto_a", "produto_b"]:

        if key in duplo:

            asin = duplo[key]["asin"]

            duplo[key]["link_es"] = f"https://www.amazon.es/dp/{asin}?tag={tag_es}"

            duplo[key]["link_de"] = f"https://www.amazon.de/dp/{asin}?tag={tag_de}"



    salvar_json("data/catalogo_produtos.json", catalogo)

    salvar_json("data/produto_duplo.json", duplo)



def validar_ativos_graficos(catalogo):

    print("[2/4] Verificando imagens em assets/products/...")

    for p in catalogo.get("produtos", []):

        img_full = os.path.join(BASE_DIR, p.get("imagem_url", "").lstrip("/"))

        if not os.path.exists(img_full):

            print(f"  -> [ALERTA] Imagem ausente: {img_full}")

    print("  -> [OK] Verificação de imagens concluída.")



def gerar_indice_busca(catalogo):

    print("[3/4] Compilando assets/search_index.json...")

    categorias = {c["id"]: c for c in catalogo.get("categorias", [])}

    indice = {

        "versao": "2026.2",

        "total_produtos": len(catalogo.get("produtos", [])),

        "itens": []

    }

    for p in catalogo.get("produtos", []):

        cat_info = categorias.get(p["categoria_id"], {})

        indice["itens"].append({

            "id": p["id"],

            "cat": p["categoria_id"],

            "cat_nome_es": cat_info.get("nome_es", ""),

            "cat_nome_de": cat_info.get("nome_de", ""),

            "marca": p["marca"],

            "nome": p["nome"],

            "asin": p["asin"],

            "score": p["score_lab"],

            "img": p["imagem_url"],

            "link_es": p["link_es"],

            "link_de": p["link_de"]

        })

    salvar_json("assets/search_index.json", indice)



def main():

    config = carregar_json("config_afiliados.json")

    catalogo = carregar_json("data/catalogo_produtos.json")

    duplo = carregar_json("data/produto_duplo.json")



    sincronizar_tags_afiliado(config, catalogo, duplo)

    validar_ativos_graficos(catalogo)

    gerar_indice_busca(catalogo)



    print("[4/4] Compilando páginas de artigos (ES e DE)...")

    builder_script = os.path.join(BASE_DIR, "scripts", "builder.py")

    subprocess.run([sys.executable, builder_script], check=True)

    print("\n[SUCESSO] Catálogo, tags e páginas 100% sincronizados!")



if __name__ == "__main__":

    main()
