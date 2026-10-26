---
name: 01_garimpador_duplo_eu
description: Garimpeiro Unificado Europa para mapear pares de produtos de alto ticket e intenção de compra na Espanha e Alemanha.
---

# Skill: Garimpeiro Unificado Europa (Espanha & Alemanha)
**ID:** `garimpador_duplo_eu`  
**Função:** Encontrar pares de produtos concorrentes diretos e campeões de venda na Amazon Espanha (.es) e mapear simultaneamente o ASIN correspondente na Amazon Alemanha (.de).

## Regras de Operação e Guardrails
1. **Seleção Baseada em Espanha (Facilidade de Auditoria):**
   - Iniciar sempre a análise por categorias de alta demanda na Espanha (`amazon.es`): Cafeteiras, Fritadeiras sem óleo (Airfryers), Aspiradores Robô, Ferramentas (Bricolaje) e Equipamentos Tech/Home Office.
2. **Critérios de Filtro de Qualidade:**
   - Avaliação mínima do produto: $\ge 4.1$ estrelas.
   - Volume relevante de avaliações (idealmente $> 300$ reviews).
   - Preço de referência: mínimo de €80 na Espanha e €100 na Alemanha para assegurar comissão atrativa.
   - Selecionar sempre 2 concorrentes diretos (Produto A vs. Produto B) da mesma faixa de preço.
3. **Mapeamento de ASIN e Links:**
   - Extrair o código ASIN (10 caracteres alfanuméricos) de cada produto.
   - Na maioria das vezes, o ASIN da Amazon é idêntico nos mercados europeus (ES, DE, FR, IT).
   - Ler o arquivo `config_afiliados.json` e construir os links matemáticos de afiliados:
     - **ES:** `https://www.amazon.es/dp/{ASIN}?tag={amazon_es_tag}`
     - **DE:** `https://www.amazon.de/dp/{ASIN}?tag={amazon_de_tag}`
4. **Extração de Reviews Reais (Sem Inventar):**
   - Coletar avaliações reais de compradores (15 mais úteis de 5 estrelas e 10 críticas de 1 a 3 estrelas).
   - Sintetizar:
     - **3 Pontos Fortes Comprovados:** Vantagens reais no uso diário.
     - **2 Defeitos Crônicos / Pontos de Atenção:** Falhas reais mencionadas pelos compradores (evita parecer publicidade forçada e gera autoridade imediata).

## Formato de Saída Obrigatório (Output)
Salvar os dados estritamente no formato JSON em `data/produto_duplo.json` com os seguintes campos:
```json
{
  "slug_es": "nome-produto-a-vs-nome-produto-b",
  "slug_de": "nome-produto-a-vs-nome-produto-b-test",
  "categoria": "Nome da Categoria / Kategorie",
  "data_publicacao": "AAAA-MM-DD",
  "queda_preco_detectada": true,
  "produto_a": {
    "nome": "Modelo Completo",
    "marca": "Marca",
    "asin": "B00XXXXXXX",
    "link_es": "https://www.amazon.es/dp/...",
    "link_de": "https://www.amazon.de/dp/...",
    "specs_tecnicas": {
      "potencia": "...",
      "capacidade": "..."
    },
    "pros": ["Ponto 1", "Ponto 2", "Ponto 3"],
    "contras_reais": ["Defeito 1", "Defeito 2"]
  },
  "produto_b": { ... },
  "veredito_resumo": {
    "es": "Resumo executivo da decisão em espanhol",
    "de": "Kurzfazit auf Deutsch"
  }
}
```
