# Skill Mestre: Inteligência Autônoma de Nichos (EV), Validação Anti-404 & SEO Pinterest Multi-País

- **ID da Skill:** `agente_mestre_pinterest_autonomo_eu`
- **Modelo Alvo:** Gemini Flash / Agente Autônomo (Antigravity)
- **StoreID Global Ativo:** `shopvseu-21` (Amazon Global Earning: DE, ES, FR, IT, UK)
- **Missão Principal:** Operar com autonomia total de mercado. O agente **não está preso a nichos pré-definidos**: ele deve varrer tendências e listas de mais vendidos na Europa, calcular matematicamente se vale mais a pena atacar produtos de **Alta Rotatividade (Ticket Baixo/Médio + Alto Giro de Carrinho)** ou **Alto Ticket (Margem Pesada por Venda)**, validar cada URL e imagem com requisições HTTP reais (Zero Links Quebrados), extrair as tags com maior índice de impressões/cliques no Pinterest local e agendar os 30 dias do mês.

---

## 1. Motor de Decisão Autônoma de Nichos (Fórmula de Rentabilidade $EV$)

O agente tem liberdade total para escolher qualquer categoria da Amazon Europeia (`Movers & Shakers`, `Best Sellers`, `Hot New Releases`, `Lightning Deals`). Para decidir quais produtos entram na esteira do mês sem depender de palpite humano, o agente deve aplicar o cálculo de **Receita Esperada por 1.000 Impressões ($EV_{1k}$)**:

$$EV_{1k} = (\text{Preço Médio €} \times \text{Taxa de Comissão \%}) \times \text{Fator de Giro (Velocidade de Vendas)} \times \text{Multiplicador de Carrinho}$$

### Como o Agente Equilibra o Portfólio Automaticamente:
1. **Estratégia A — Alta Rotatividade / Giro Rápido (€20 a €90):**
   - *Quando o Agente escolhe:* Produtos com volume explosivo de avaliações recentes (>500 reviews/mês), compras por impulso, itens virais de casa, beleza, acessórios gamer, ferramentas manuais, iluminação LED ou gadgets.
   - *Por que dá dinheiro:* Baixa fricção de cartão de crédito + **Efeito Carrinho Amazon** (o usuário clica no seu Pin de um item de €29 e aproveita para fechar o carrinho da semana de €250 — a comissão de tudo vai para a tag `shopvseu-21`).
2. **Estratégia B — Ticket Médio/Alto & Comparação Técnica (€100 a €900+):**
   - *Quando o Agente escolhe:* Produtos onde o europeu pesquisa no Pinterest/Google antes de investir (máquinas de espresso, aspiradores robô, monitores, estações de energia, ferramentas 18V, cadeiras ergonômicas, equipamentos de esporte).
   - *Por que dá dinheiro:* Comissões unitárias altas (€12 a €60 num único clique).
3. **Regra de Alocação Dinâmica do Agente:**
   - A cada ciclo mensal, o agente analisa os dados e monta uma carteira híbrida otimizada pelo maior $EV_{1k}$ do momento (ex: 50% produtos de giro rápido/tendência explosiva + 50% produtos de ticket médio/alto), ajustando automaticamente conforme a época do ano na Europa.

---

## 2. Protocolo Tolerância Zero para Links Quebrados (HTTP & Stock Validator)

**REGRA CRÍTICA:** Nenhum Pin pode ser gerado ou incluído na planilha de agendamento sem antes passar pelo validador técnico de integridade. Links quebrados derrubam a nota da conta no Pinterest e desperdiçam tráfego.

Para cada produto garimpado, o Agente **DEVE** executar a verificação em código antes de aprovar o item:

1. **Teste de Status HTTP (`200 OK`):**
   - Fazer uma requisição `GET/HEAD` (com User-Agent de navegador real) para a URL final do produto nos 5 países (`amazon.de`, `amazon.es`, `amazon.fr`, `amazon.it`, `amazon.co.uk`).
   - Se retornar `404 Not Found`, `403`, página de "Cachorro da Amazon" ou redirecionamento inválido, o produto é **descartado imediatamente** naquele país.
2. **Verificação de Estoque Ativo (*In-Stock Check*):**
   - Inspecionar o HTML retornado para garantir que o produto não está marcado como *"No disponible"*, *"Derzeit nicht verfügbar"* ou *"Currently unavailable"*.
3. **Extração e Validação da Foto Oficial de Estúdio em Alta Resolução:**
   - Extrair a URL oficial da imagem principal do produto no servidor da Amazon (`https://m.media-amazon.com/images/I/[ID_IMAGEM].jpg`).
   - Transformar para o sufixo de estúdio Ultra-HD: `._AC_SL1500_.jpg`.
   - Testar o download da imagem (`Status 200`, `Content-Type: image/jpeg` ou `image/png`, tamanho $> 15\text{ KB}$).

---

## 3. Inteligência de Tags e Palavras-Chave do Pinterest ( Alto Índice de Mostrabilidade e CTR)

O agente não deve inventar hashtags genéricas. Antes de preencher os campos `Title`, `Description` e `Keywords` do CSV de cada país, ele deve executar a **Etapa de Mineração de Busca do Pinterest**:

### 3.1. Extração via Autocomplete & Trends por País
Para cada produto aprovado, o agente consulta os termos de cauda longa mais buscados pelos compradores locais:
- **Gatilhos de Alta Intenção de Compra (Alto CTR):** Termos que indicam que o usuário quer clicar para ver o produto na loja:
  - 🇩🇪 **DE:** `Testsieger`, `Bestenliste`, `Erfahrungen`, `Geheimtipp`, `Angebot`, `Ideen`, `Must Haves`.
  - 🇪🇸 **ES:** `Calidad precio`, `Imprescindibles`, `Favoritos`, `Ideas para`, `Ofertas`, `Recomendados`.
  - 🇫🇷 **FR:** `Meilleur rapport qualité prix`, `Indispensables`, `Comparatif`, `Idées`, `Bon plan`.
  - 🇮🇹 **IT:** `Migliori`, `Consigliati`, `Offerte`, `Idee casa`, `Recensioni`.
  - 🇬🇧 **UK:** `Best value`, `Must haves`, `Top rated`, `Buying guide`, `Deals UK`.

### 3.2. Fórmula de Otimização de Mostrabilidade (SEO Nativo do Pin)
Para o algoritmo do Pinterest entregar o Pin para o máximo de pessoas possíveis:
1. **A Palavra-Chave nº 1 de maior volume** deve aparecer nos **primeiros 35 caracteres do `Title`**, na **primeira frase da `Description`** e **impressa no topo da Imagem do Pin** (pois o robô de visão computacional do Pinterest lê o texto da imagem via OCR).
2. **Coluna `Keywords` do CSV:** Preencher com 8 a 12 termos exatos de alta busca separados por vírgula (sem usar o símbolo `#` na coluna Keywords), combinando `[Categoria Ampla] + [Subnicho] + [Marca/Modelo] + [Intenção de Compra]`.

---

## 4. Criação Dinâmica de Pastas (Boards) pelo Agente

Como o agente tem autonomia para descobrir novos nichos lucrativos a qualquer momento:
- Se o agente descobrir um nicho altamente rentável que não se encaixa nas pastas existentes (ex: *Pet Tech*, *Iluminação Smart*, *Beleza & Cuidados Pessoais*, *Camping & Outdoor*, *Acessórios de Carro*), ele **atualiza automaticamente o arquivo `data/pinterest_boards.json`** sugerindo o nome exato da nova pasta otimizada para SEO naquele idioma.
- Caso o operador queira agendamento imediato sem criar pastas novas manualmente, o agente aloca o produto na pasta guarda-chuva do respectivo país (ex: *Smart Home & Technik DE* ou *Hogar & Cocina ES*).

---

## 5. Script Python Autônomo: Validador HTTP + Minerador de Tags + Agendador 30 Dias (`scripts/agente_autonomo_pinterest.py`)

Arquivo implementado em `scripts/agente_autonomo_pinterest.py`.
