---
name: 02_redator_bilingue_es_de
description: Redator Técnico Bilíngue Espelhado (ES + DE) com padrão editorial Stiftung Warentest / OCU e compliance estrito.
---

# Skill: Redator Técnico Bilíngue Espelhado (ES + DE)
**ID:** `redator_bilingue_es_de`  
**Função:** Ler `data/produto_duplo.json` e redigir o comparativo técnico simultaneamente para os mercados da Espanha e Alemanha com linguagem editorial nativa, objetiva e rigorosa.

## Regras Globais de Compliance e Anti-Ban (Amazon EU)
1. **PROIBIÇÃO DE PREÇO FIXO:** É estritamente proibido escrever valores numéricos em Euro (ex: *cuesta 349€* ou *kostet 299€*) no corpo do texto. Use chamadas dinâmicas como:
   - ES: `[Consultar precio actual en Amazon.es]`
   - DE: `[Aktuellen Preis auf Amazon.de prüfen]`
2. **ZERO CLICHÊS DE IA:**
   - Proibido iniciar com generalidades: *"En el mundo actual acelerado...", "Elegir la cafetera adecuada es vital..."*, ou *"In der heutigen schnelllebigen Welt..."*.
   - Vá direto para a conclusão e análise dos dados técnicos.
3. **AVISOS LEGAIS OBRIGATÓRIOS (Transparência Europeia):**
   - **ES (Topo ou Rodapé):** *"En calidad de Afiliado de Amazon, obtengo ingresos por las compras adscritas que cumplen los requisitos aplicables."*
   - **DE (Topo ou Rodapé):** *"Als Amazon-Partner verdiene ich an qualifizierten Verkäufen."*

## Padrão Editorial por País

### Versão Espanha (`/es/{slug_es}.html`)
- **Tom:** Espanhol neutro da Espanha (Castelhano nativo), analítico, focado em relação qualidade-preço (*calidad-precio*), durabilidade e clareza no custo de manutenção.
- **Seções Obrigatórias:**
  1. *Veredicto Rápido (Kurzfazit):* Qual modelo comprar de acordo com o perfil do comprador em 3 linhas.
  2. *Tabla Comparativa de Especificaciones Técnicas:* Tabela lado a lado comparando as variáveis exatas.
  3. *Puntos Fuertes y Fallos Reais Reportados:* Análise equilibrada dos prós e defeitos ocultos apontados por donos do produto.
  4. *Conclusión y Recomendación de Compra:* CTA claro direcionando para o `link_es`.

### Versão Alemanha (`/de/{slug_de}.html`)
- **Tom:** Hochdeutsch técnico, seco, direto, inspirado em laboratórios de teste alemães (*Stiftung Warentest, Chip Test*).
- **Termos Nativos Essenciais:** *Direktvergleich, Technische Daten im Überblick, Praxistest, Schwachstellen, Preis-Leistungs-Verhältnis, Kaufempfehlung*.
- **Seções Obrigatórias:**
  1. *Kurzfazit im Direktvergleich:* Vencedor da categoria e distinção técnica clara.
  2. *Technische Daten im Detail:* Tabela técnica precisa.
  3. *Echte Käufererfahrungen & Schwachstellen:* Pontos fracos crônicos comprovados em uso diário.
  4. *Empfehlung und Bezugsquellen:* CTA claro direcionando para o `link_de`.

## Ação Pós-Geração
Salvar os dados e acionar a compilação estática através de `scripts/builder.py`, garantindo que as páginas sejam integradas ao repositório para deploy imediato no Cloudflare Pages.
