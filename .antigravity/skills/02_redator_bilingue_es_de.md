---
name: 02_redator_bilingue_es_de
description: Redator Técnico Bilíngue Espelhado (ES + DE), Indexador de Catálogo e Compilador Estático HTML com padrão Stiftung Warentest / OCU.
---
# Skill: Redator Técnico Bilíngue Espelhado (ES + DE) & Build HTML

**ID:** `redator_bilingue_es_de`  
**Função:** Auditar a qualidade linguística e técnica de `data/produto_duplo.json` e `data/catalogo_produtos.json`, sincronizar o StoreID `shopvseu-21` via `scripts/indexer.py`, compilar as páginas HTML estáticas via `scripts/builder.py` e atualizar o `sitemap.xml`.

## Regras Globais de Compliance e Anti-Ban (Amazon EU)

1. **PROIBIÇÃO ESTRITA DE PREÇO FIXO:** É proibido exibir valores numéricos de preço do produto em Euro no texto (ex: *cuesta 349€* ou *kostet 299€*). Apenas custos estimados de manutenção genéricos são tolerados no veredito, e todos os botões de compra devem usar chamadas dinâmicas:
   - **ES:** `Consultar precio actual y stock en Amazon.es →`
   - **DE:** `Aktuellen Preis auf Amazon.de prüfen →`
   - Todos os links de afiliado devem conter `target="_blank" rel="nofollow noopener sponsored"`.
2. **ZERO CLICHÊS DE IA E ZERO "PORTUNHOL":**
   - Proibido iniciar textos com introduções vagas (*"En el mundo actual..."*, *"In der heutigen..."*).
   - Proibido vazar termos em português nos arquivos JSON ou HTML (usar sempre *Calidad-Precio* em ES e *Preis-Leistungs-Verhältnis* em DE; *Robots Aspiradores* em ES e *Saugroboter* em DE).
   - Em `specs_es` e `specs_de` do `produto_duplo.json`, garantir que os dois produtos tenham exatamente o mesmo número de linhas na mesma ordem para que `scripts/builder.py` monte a tabela comparativa perfeitamente alinhada.
3. **AVISOS LEGAIS OBRIGATÓRIOS (Transparência Europeia & § 5 TMG):**
   - **ES:** *"En calidad de Afiliado de Amazon, obtengo ingresos por las compras adscritas que cumplen los requisitos aplicables."*
   - **DE:** *"Als Amazon-Partner verdiene ich an qualifizierten Verkäufen."*
   - Manter sempre o link funcional para `/legal/` (`Impressum § 5 TMG`) no cabeçalho e rodapé.

## Padrão Editorial por País

### Versão Espanha (`/es/{slug_es}.html`)
- **Tom:** Castelhano nativo da Espanha, analítico, focado em *relación calidad-precio*, facilidade de limpeza/manutenção e durabilidade real.
- **Componentes compilados pelo `builder.py`:**
  1. Cards lado a lado com selo de pontuação (`score_label_es`), ASIN, nota de laboratório, 3 pontos fortes (`pros_es`), botão CTA com `?tag=shopvseu-21` e gaveta modal (*Ver Ficha Técnica Expandida - 6 Parámetros*).
  2. *Veredicto Rápido de Nuestros Ingenieros* (`veredito_resumo.es`).
  3. *Matriz de Especificaciones Técnicas* (cabeçalho `Parámetro`).
  4. *Fallos Crónicos Reportados* (`contras_es`).
  5. Link direto no topo para abrir a disputa pré-selecionada no comparador interativo (`/compare/?cat={categoria_id}&a={id_a}&b={id_b}&lang=es`).

### Versão Alemanha (`/de/{slug_de}.html`)
- **Tom:** *Hochdeutsch* técnico, seco e rigoroso, padrão *Stiftung Warentest*.
- **Vocabulário Nativo Obrigatório:** *Direktvergleich, Technische Daten im Direktvergleich, Kenngröße, Kurzfazit der Prüfredaktion, Bekannte Schwachstellen, Erweiterte technische Datenblätter*.
- **Componentes compilados pelo `builder.py`:**
  1. Cards lado a lado com `score_label_de`, ASIN, `pros_de`, botão CTA para `amazon.de` com `?tag=shopvseu-21` e gaveta modal (`ficha_expandida_de`).
  2. *Kurzfazit der Prüfredaktion* (`veredito_resumo.de`).
  3. *Technische Daten im Direktvergleich* (cabeçalho `Kenngröße`).
  4. *Bekannte Schwachstellen* (`contras_de`).
  5. Link direto no topo para `/compare/?cat={categoria_id}&a={id_a}&b={id_b}&lang=de`.

## Pipeline de Execução Pós-Redação

1. Executar `python scripts/indexer.py` (que sincroniza a tag `shopvseu-21` de `config_afiliados.json` em todos os itens, valida imagens em `assets/products/`, gera `assets/search_index.json` e dispara `scripts/builder.py` preservando o `index.html` interativo da raiz).
2. Atualizar as vitrines regionais (`es/index.html` e `de/index.html`) caso um novo duelo ou categoria precise ser destacado nos cards.
3. Adicionar as novas URLs geradas (`/es/{slug_es}.html` e `/de/{slug_de}.html`) dentro do arquivo `sitemap.xml` na raiz do projeto.
