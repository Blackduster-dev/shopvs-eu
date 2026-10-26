# ⚡ ShopVS EU - Comparativas Técnicas & Produkttests

Operação automatizada de afiliados para o mercado europeu (**Espanha `.es`** e **Alemanha `.de`**), baseada em esteira de agentes, dados técnicos de produtos e design editorial de alta autoridade (*Stiftung Warentest / OCU style*).

Hospedado gratuitamente no **Cloudflare Pages**: [shopvs-eu.pages.dev](https://shopvs-eu.pages.dev/)

---

## 🏛️ Arquitetura do Sistema

```plaintext
shopvs-eu/
├── .antigravity/
│   └── skills/
│       ├── 01_garimpador_duplo_eu.md          # Skill Agente 1: Garimpagem unificada com ASIN espelhado
│       ├── 02_redator_bilingue_es_de.md        # Skill Agente 2: Redação técnica anti-IA & anti-ban
│       └── 03_distribuidor_pinterest_telegram.md # Skill Agente 3: Ativos visuais e canais de tráfego
├── config_afiliados.json                       # Tags Amazon, Awin Publisher ID e domínios
├── data/
│   ├── produto_duplo.json                      # Contrato de dados estruturados
│   └── telegram_disparos.txt                   # Disparos formatados prontos para os canais
├── scripts/
│   ├── gerar_pins.py                           # Renderizador de imagens 1000x1500px (Pillow)
│   ├── builder.py                              # Compilador estático com design editorial sóbrio
│   └── pipeline_master.py                      # Orquestrador da esteira de ponta a ponta
├── es/
│   ├── index.html                              # Hub Espanha com lista de comparativas
│   └── delonghi-magnifica-s-vs-krups-essential.html # Artigo piloto completo em Castelhano
├── de/
│   ├── index.html                              # Hub Alemanha com lista de vergleiche
│   └── delonghi-magnifica-s-vs-krups-essential-test.html # Artigo piloto completo em Hochdeutsch
├── legal/
│   └── index.html                              # Impressum oficial (§ 5 TMG) & Política GDPR
├── assets/
│   └── pins/                                   # Imagens geradas em alta resolução para Pinterest
├── index.html                                  # Vitrine raiz com seletor de mercado e metodologia
├── wrangler.jsonc                              # Deploy configuration para Cloudflare Pages
└── README.md
```

---

## 🚀 Como Executar a Esteira

Para rodar todo o pipeline (verificação de skills, build das páginas HTML em ES e DE, geração dos pins do Pinterest e formatação do Telegram):

```bash
python scripts/pipeline_master.py
```

### Para atualizar com novos produtos:
1. Atualize o arquivo `data/produto_duplo.json` com o novo par de produtos concorrentes (ou deixe o Hunter Agent alimentar).
2. Execute `python scripts/pipeline_master.py`.
3. Faça commit e push para o GitHub:
   ```bash
   git add .
   git commit -m "Add new technical comparison: Modelo A vs Modelo B"
   git push origin main
   ```
4. O Cloudflare Pages detecta a alteração automaticamente e atualiza o site na Europa em menos de 20 segundos.

---

## ⚖️ Conformidade Legal e Anti-Ban (Europa)
- **Sem preços estáticos:** Em conformidade com as diretrizes da Amazon Associates, nenhum preço numérico fixo em Euro é embutido no texto (apenas botões de consulta dinâmica).
- **Impressum (§ 5 TMG):** Exigência legal obrigatória para operar e ser aprovado no mercado alemão (DACH).
- **GDPR Friendly:** Sem cookies invasivos de terceiros, preservando a privacidade do visitante e dispensando banners pesados.
