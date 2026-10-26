---
name: 03_distribuidor_pinterest_telegram
description: Distribuidor Visual Multicanal para Pinterest EU (1000x1500) e alertas Telegram Chollos/Schnäppchen.
---

# Skill: Distribuidor Visual Multicanal (Pinterest EU & Telegram)
**ID:** `distribuidor_pinterest_telegram`  
**Função:** Converter os comparativos publicados em ativos visuais de alta conversão para o Pinterest Europeu e disparos estruturados para canais de Telegram na Espanha e Alemanha.

## Etapa 1: Ativos Visuais para Pinterest EU (1000x1500px)
O Pinterest na Europa funciona como um catálogo visual de compras e pesquisa de intenção. O robô deve executar `scripts/gerar_pins.py` para produzir duas imagens verticais com tipografia limpa e alto contraste:

1. **Pin Espanha (`assets/pins/{slug_es}.png`):**
   - Topo: `COMPARATIVA TÉCNICA 2026: [Produto A] vs [Produto B]`
   - Miolo: Tabela resumida de 3 especificações decisivas.
   - Rodapé CTA: `¿Cuál merece la pena comprar? Leer veredicto completo`
   - Link de destino: `{dominio_site}/es/{slug_es}.html`

2. **Pin Alemanha (`assets/pins/{slug_de}.png`):**
   - Topo: `DIREKTVERGLEICH 2026: [Produto A] vs. [Produto B]`
   - Miolo: 3 itens técnicos decisivos em alemão (*Technische Daten*).
   - Rodapé CTA: `Welches Modell ist besser? Jetzt Testbericht lesen`
   - Link de destino: `{dominio_site}/de/{slug_de}.html`

## Etapa 2: Formatação de Disparos para Telegram

### Canal Espanha (Estilo "Chollos & Comparativas")
```text
⚡ Comparativa & Oferta Técnica: [Produto A] vs [Produto B]
🔍 Analizamos opiniones reales y fallos ocultos antes de que compres:
- [Ponto forte chave A]
- [Ponto forte chave B]

📊 Ver análisis técnico completo: {dominio_site}/es/{slug_es}.html
🛒 Ver precio actual en Amazon España: {link_es} *(Enlace de Afiliado)*
```

### Canal Alemanha (Estilo "Schnäppchen & Testbericht")
```text
🔥 Direktvergleich & Kaufberatung: [Produto A] vs [Produto B]
✅ Echte Käufermeinungen und technische Daten im Praxis-Check:
- [Stärke A]
- [Stärke B]

📊 Zum vollständigen Testbericht: {dominio_site}/de/{slug_de}.html
🛒 Direkt zu Amazon Deutschland: {link_de} *(Affiliate-Link)*
```
