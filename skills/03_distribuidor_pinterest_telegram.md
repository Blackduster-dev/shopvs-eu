---
name: 03_distribuidor_pinterest_telegram
description: Distribuidor Visual Multicanal para Pinterest EU (1000x1500px via Pillow) e alertas nativos para Telegram (Chollos ES & Schnäppchen DE).
---
# Skill: Distribuidor Visual Multicanal (Pinterest EU & Telegram)

**ID:** `distribuidor_pinterest_telegram`  
**Função:** Converter os comparativos publicados em ativos visuais verticais (1000x1500px) para o Pinterest Europeu e gerar os textos de disparo 100% nativos para os canais de Telegram na Espanha e Alemanha.

## Etapa 1: Ativos Visuais para Pinterest EU (1000x1500px)

O script `scripts/gerar_pins.py` (acionado diretamente ou via `scripts/pipeline_master.py`) utiliza a biblioteca `Pillow` para renderizar os cartões verticais de alta conversão na pasta `assets/pins/`:

1. **Pin Espanha (`assets/pins/{slug_es}.png`):**
   - **Badge Superior:** `LABORATORIO DE COMPARATIVAS TÉCNICAS · EUROPA`
   - **Título:** `COMPARATIVA TÉCNICA 2026: [Produto A] VS. [Produto B]`
   - **Destaques Centrais:** 3 especificações técnicas extraídas de `specs_es` (sem textos em português).
   - **Botão CTA:** `VER VEREDICTO Y PRECIOS ACTUALES`
   - **URL de Destino no Pinterest ES:** `https://shopvs-eu.pages.dev/es/{slug_es}.html`

2. **Pin Alemanha (`assets/pins/{slug_de}.png`):**
   - **Badge Superior:** `EUROPÄISCHES TESTLABOR · DIREKTVERGLEICH`
   - **Título:** `DIREKTVERGLEICH 2026: [Produto A] VS. [Produto B]`
   - **Destaques Centrais:** 3 especificações técnicas extraídas de `specs_de` em alemão puro.
   - **Botão CTA:** `JETZT TESTBERICHT & PREISE PRÜFEN`
   - **URL de Destino no Pinterest DE:** `https://shopvs-eu.pages.dev/de/{slug_de}.html`

## Etapa 2: Formatação de Disparos para Telegram (`data/telegram_disparos.txt`)

Gerar e salvar os disparos em `data/telegram_disparos.txt` puxando os campos `pros_es[0]` e `pros_de[0]` de cada produto e garantindo que o link da Amazon contenha `?tag=shopvseu-21`:

### Canal Espanha (Estilo "Chollos & Comparativas")
```text
⚡ Comparativa & Oferta Técnica: {produto_a.nome} vs {produto_b.nome}

🔎 Analizamos opiniones reales y fallos ocultos antes de que compres:
• {produto_a.marca}: {produto_a.pros_es[0]}
• {produto_b.marca}: {produto_b.pros_es[0]}

📊 Ver tabla comparativa completa: https://shopvs-eu.pages.dev/es/{slug_es}.html
🛒 Ver oferta actual en Amazon España: {produto_a.link_es} *(Enlace de Afiliado)*
```

### Canal Alemanha (Estilo "Schnäppchen & Testbericht")
```text
⚡ Direktvergleich & Kaufberatung: {produto_a.nome} vs. {produto_b.nome}

🔎 Echte Käufermeinungen und technische Daten im Praxis-Check:
• {produto_a.marca}: {produto_a.pros_de[0]}
• {produto_b.marca}: {produto_b.pros_de[0]}

📊 Zum vollständigen Testbericht: https://shopvs-eu.pages.dev/de/{slug_de}.html
🛒 Direkt zu Amazon Deutschland: {produto_a.link_de} *(Affiliate-Link)*
```

## Etapa 3: Orquestração Completa e Deploy

Sempre que um novo duelo for processado, executar a esteira completa na raiz do repositório:
```bash
python scripts/pipeline_master.py
git add .
git commit -m "Add comparison & assets: {slug_es}"
git push origin main
```
