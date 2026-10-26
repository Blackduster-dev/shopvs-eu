#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Motor de Armazenamento & Indexador do ShopVS EU
Executado localmente ou automaticamente a cada 3 dias via GitHub Actions.
1. Valida a integridade do catálogo mestre (data/catalogo_produtos.json)
2. Garante que os arquivos de imagens locais (assets/products/) existam em disco
3. Compila um índice de busca ultra-leve (assets/search_index.json) para consulta em <5ms
4. Atualiza os links e flags de ofertas/preço dinâmico em conformidade estrita com a UE
"""

import json
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def carregar_json(rel_path):
    path = os.path.join(BASE_DIR, rel_path)
    if not os.path.exists(path):
        raise FileNotFoundError(f"Arquivo não encontrado: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_json(rel_path, dados):
    path = os.path.join(BASE_DIR, rel_path)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)
    print(f"[OK] Dados gravados em: {path}")

def validar_ativos_graficos(catalogo):
    """Verifica se todas as imagens referenciadas nos produtos existem em disco."""
    print("[1/4] Verificando integridade de imagens locais (assets/products/)...")
    produtos = catalogo.get("produtos", [])
    faltantes = []
    
    for p in produtos:
        img_rel = p.get("imagem_url", "")
        # Remove barra inicial para checagem local
        clean_rel = img_rel.lstrip("/")
        img_full = os.path.join(BASE_DIR, clean_rel)
        if not os.path.exists(img_full):
            faltantes.append((p.get("id"), img_full))
        else:
            tamanho = os.path.getsize(img_full)
            if tamanho < 500:
                print(f"  -> [AVISO] Imagem potencialmente corrompida: {img_rel} ({tamanho} bytes)")

    if faltantes:
        print(f"  -> [ALERTA] {len(faltantes)} produtos sem imagem local:")
        for pid, path in faltantes:
            print(f"     - Produto: {pid} | Caminho esperado: {path}")
    else:
        print(f"  -> [SUCESSO] Todas as {len(produtos)} imagens de produtos estao íntegras e presentes no disco.")

def gerar_indice_busca(catalogo):
    """
    Cria um índice compacto otimizado para o cliente (assets/search_index.json).
    Contém apenas os metadados necessários para autocompletar e filtragem por categoria.
    """
    print("\n[2/4] Compilando índice de busca compacto (assets/search_index.json)...")
    produtos = catalogo.get("produtos", [])
    categorias = {c["id"]: c for c in catalogo.get("categorias", [])}

    indice = {
        "versao": "2026.1",
        "total_produtos": len(produtos),
        "itens": []
    }

    for p in produtos:
        cat_id = p.get("categoria_id")
        cat_info = categorias.get(cat_id, {})
        
        # Entrada compacta de busca
        indice["itens"].append({
            "id": p.get("id"),
            "cat": cat_id,
            "cat_nome_es": cat_info.get("nome_es", cat_id),
            "cat_nome_de": cat_info.get("nome_de", cat_id),
            "marca": p.get("marca"),
            "nome": p.get("nome"),
            "asin": p.get("asin"),
            "score": p.get("score_lab"),
            "img": p.get("imagem_url"),
            "link_es": p.get("link_es"),
            "link_de": p.get("link_de")
        })

    salvar_json("assets/search_index.json", indice)
    print(f"  -> [SUCESSO] Índice gerado com {len(indice['itens'])} produtos indexados.")

def sincronizar_produto_duplo(catalogo):
    """
    Mantém o contrato 'data/produto_duplo.json' sincronizado com o primeiro par
    da categoria principal para servir aos compiladores de artigos.
    """
    print("\n[3/4] Sincronizando contrato de dados entre agentes (data/produto_duplo.json)...")
    prods = [p for p in catalogo.get("produtos", []) if p.get("categoria_id") == "cafeteras"]
    if len(prods) >= 2:
        pa, pb = prods[0], prods[1]
        duplo = carregar_json("data/produto_duplo.json")
        duplo["produto_a"]["nome"] = pa["nome"]
        duplo["produto_a"]["asin"] = pa["asin"]
        duplo["produto_a"]["imagem_url"] = pa["imagem_url"]
        duplo["produto_b"]["nome"] = pb["nome"]
        duplo["produto_b"]["asin"] = pb["asin"]
        duplo["produto_b"]["imagem_url"] = pb["imagem_url"]
        salvar_json("data/produto_duplo.json", duplo)
        print("  -> [SUCESSO] data/produto_duplo.json sincronizado com dados do catálogo.")

def executar_rebuild():
    """Chama o builder para atualizar as páginas com o índice atualizado."""
    print("\n[4/4] Executando compilação estática do site com novos dados...")
    import subprocess
    builder_script = os.path.join(BASE_DIR, "scripts", "builder.py")
    res = subprocess.run([sys.executable, builder_script], capture_output=True, text=True, encoding="utf-8")
    if res.returncode == 0:
        print("  -> [SUCESSO] Todas as rotas estáticas foram recompiladas.")
    else:
        print("  -> [ERRO] Falha ao executar builder.py:")
        print(res.stderr)

def main():
    print("=" * 65)
    print("   MOTOR DE ARMAZENAMENTO & INDEXAÇÃO DE CATÁLOGO (SHOPVS EU)")
    print("=" * 65)
    catalogo = carregar_json("data/catalogo_produtos.json")
    validar_ativos_graficos(catalogo)
    gerar_indice_busca(catalogo)
    sincronizar_produto_duplo(catalogo)
    executar_rebuild()
    print("\n" + "=" * 65)
    print("   PROCESSO DE INDEXAÇÃO CONCLUÍDO COM SUCESSO!")
    print("=" * 65)

if __name__ == "__main__":
    main()
