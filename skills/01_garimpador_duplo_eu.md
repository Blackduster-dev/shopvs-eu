---
name: 01_garimpador_duplo_eu
description: Garimpeiro Unificado Europa para mapear pares de produtos de alto ticket na Espanha e Alemanha, alimentando o catálogo dinâmico e os duelos bilíngues do ShopVS EU.
---
# Skill: Garimpeiro Unificado Europa (Espanha & Alemanha)

**ID:** `garimpador_duplo_eu`  
**Função:** Encontrar pares de produtos concorrentes diretos e campeões de venda na Amazon Espanha (`.es`), mapear simultaneamente o ASIN na Amazon Alemanha (`.de`) e alimentar os arquivos `data/produto_duplo.json` e `data/catalogo_produtos.json` no formato 100% bilíngue (Castelhano e Hochdeutsch), sem nenhum texto em português.

## Regras de Operação e Guardrails

1. **Seleção Baseada em Categorias do Catálogo:**
   - Priorizar as categorias ativas do `ShopVS EU` (`cafeteras`, `freidoras_aire`, `aspiradoras_robot`) ou criar uma nova categoria estruturada em `data/catalogo_produtos.json`.
2. **Critérios de Filtro de Qualidade:**
   - Avaliação mínima do produto: $\ge 4.1$ estrelas e alto volume de avaliações ($> 300$ reviews).
   - Preço de referência: mínimo de €80 na Espanha e €100 na Alemanha para assegurar comissão atrativa.
   - Selecionar sempre 2 concorrentes diretos (Produto A vs. Produto B) da mesma categoria e faixa de preço.
   - **Proibição de Preço Fixo:** Nunca salvar valores numéricos em Euro nas especificações ou prós/contras.
3. **Mapeamento de ASIN, Imagens e StoreID Global (`shopvseu-21`):**
   - Extrair o código ASIN (10 caracteres alfanuméricos) de cada produto.
   - Ler `config_afiliados.json` (StoreID ativo: `shopvseu-21` via Amazon EU Global Earning) e montar os links:
     - **ES:** `https://www.amazon.es/dp/{ASIN}?tag=shopvseu-21`
     - **DE:** `https://www.amazon.de/dp/{ASIN}?tag=shopvseu-21`
   - Salvar a imagem oficial do produto (alta resolução, idealmente 500x500px em fundo branco puro ou transparente) em `assets/products/{id_produto}.png`.
4. **Extração de Reviews Reais e Tradução Técnica Nativa (Zero Português):**
   - Coletar avaliações reais de compradores (5 estrelas vs. 1 a 3 estrelas) e sintetizar:
     - **3 Pontos Fortes Comprovados (`pros_es` e `pros_de`):** Vantagens técnicas e práticas reais.
     - **2 Defeitos Crônicos / Pontos de Atenção (`contras_es` e `contras_de`):** Falhas reais mencionadas pelos donos (gera autoridade estilo *Stiftung Warentest* / *OCU*).

## Formato de Saída Obrigatório (Contratos JSON)

O agente DEVE atualizar dois arquivos JSON mantendo a codificação UTF-8 intacta:

### Saída 1: `data/produto_duplo.json` (Para compilação dos artigos HTML via `builder.py`)
```json
{
  "slug_es": "marca-modelo-a-vs-marca-modelo-b",
  "slug_de": "marca-modelo-a-vs-marca-modelo-b-test",
  "categoria_es": "Nome da Categoria em Espanhol",
  "categoria_de": "Nome da Categoria em Alemão",
  "data_publicacao": "2026-10-26",
  "queda_preco_detectada": true,
  "produto_a": {
    "id": "marca_modelo_a",
    "nome": "Nome Completo do Modelo A",
    "marca": "Marca A",
    "asin": "B00XXXXXXX",
    "imagem_url": "/assets/products/marca_modelo_a.png",
    "link_es": "https://www.amazon.es/dp/B00XXXXXXX?tag=shopvseu-21",
    "link_de": "https://www.amazon.de/dp/B00XXXXXXX?tag=shopvseu-21",
    "score_lab": "9.2",
    "score_label": "TESTSIEGER · SEHR GUT",
    "score_label_es": "TESTSIEGER · SOBRESALIENTE",
    "score_label_de": "TESTSIEGER · SEHR GUT",
    "specs_es": {
      "Parámetro 1": "Valor técnico em espanhol",
      "Parámetro 2": "Valor técnico em espanhol"
    },
    "specs_de": {
      "Kenngröße 1": "Valor técnico em alemão",
      "Kenngröße 2": "Valor técnico em alemão"
    },
    "ficha_expandida_es": {
      "Parámetro Avanzado 1": "Detalhe técnico em espanhol (total 6 parâmetros)"
    },
    "ficha_expandida_de": {
      "Erweiterter Parameter 1": "Detalhe técnico em alemão (total 6 parâmetros)"
    },
    "pros_es": ["Ponto forte 1 em ES", "Ponto forte 2 em ES", "Ponto forte 3 em ES"],
    "contras_es": ["Defeito real 1 em ES", "Defeito real 2 em ES"],
    "pros_de": ["Ponto forte 1 em DE", "Ponto forte 2 em DE", "Ponto forte 3 em DE"],
    "contras_de": ["Defeito real 1 em DE", "Defeito real 2 em DE"]
  },
  "produto_b": {
    "id": "marca_modelo_b",
    "nome": "Nome Completo do Modelo B",
    "marca": "Marca B",
    "asin": "B00YYYYYYY",
    "imagem_url": "/assets/products/marca_modelo_b.png",
    "link_es": "https://www.amazon.es/dp/B00YYYYYYY?tag=shopvseu-21",
    "link_de": "https://www.amazon.de/dp/B00YYYYYYY?tag=shopvseu-21",
    "score_lab": "8.4",
    "score_label": "GUT (2.1) · COMPACTA",
    "score_label_es": "GUT (2.1) · COMPACTA",
    "score_label_de": "GUT (2.1) · KOMPAKT",
    "specs_es": {},
    "specs_de": {},
    "ficha_expandida_es": {},
    "ficha_expandida_de": {},
    "pros_es": [],
    "contras_es": [],
    "pros_de": [],
    "contras_de": []
  },
  "veredito_resumo": {
    "es": "Resumo executivo técnico em espanhol (3 linhas) sem preço fixo.",
    "de": "Kurzfazit auf Deutsch (3 Zeilen) ohne statische Preisangaben."
  }
}
```

### Saída 2: `data/catalogo_produtos.json` (Para a Busca da Home e Comparador `/compare/`)
Adicionar ou atualizar os dois produtos dentro do array `"produtos"` de `data/catalogo_produtos.json`, usando as chaves padronizadas da categoria (`presion`, `molinillo`, `infusor`, `potencia`, `capacidad`, `succion`, etc.) tanto no objeto `"specs"` (em espanhol) quanto em `"specs_de"` (em alemão), além de `"score_badge_es"`, `"score_badge_de"`, `"pros_es"`, `"contras_es"`, `"pros_de"` e `"contras_de"`.
