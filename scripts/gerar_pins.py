#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador de Pins Verticais (1000x1500px) para Pinterest Europa (ES e DE)
Utiliza Pillow para desenhar composições com visual limpo, institucional e de alta legibilidade.
"""

import os
from PIL import Image, ImageDraw, ImageFont

def get_font(size, bold=False):
    """Carrega fontes do sistema Windows com fallback gracioso."""
    candidates = []
    if bold:
        candidates = [
            "C:\\Windows\\Fonts\\segoeuib.ttf",
            "C:\\Windows\\Fonts\\arialbd.ttf",
            "C:\\Windows\\Fonts\\calibrib.ttf",
        ]
    else:
        candidates = [
            "C:\\Windows\\Fonts\\segoeui.ttf",
            "C:\\Windows\\Fonts\\arial.ttf",
            "C:\\Windows\\Fonts\\calibri.ttf",
        ]
    
    for path in candidates:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                pass
    return ImageFont.load_default()

def criar_card_pinterest(idioma, produto_a, produto_b, destaques, caminho_saida):
    """
    Desenha um Pin vertical de alta resolução (1000 x 1500 px)
    com identidade editorial técnica europeia.
    """
    largura, altura = 1000, 1500
    # Fundo elegante azul marinho profundo profissional
    img = Image.new("RGB", (largura, altura), color=(15, 23, 42))
    draw = ImageDraw.Draw(img)

    # Fontes
    font_badge = get_font(26, bold=True)
    font_title = get_font(44, bold=True)
    font_vs = get_font(32, bold=True)
    font_spec_title = get_font(26, bold=True)
    font_spec_text = get_font(30, bold=False)
    font_btn = get_font(34, bold=True)
    font_footer = get_font(22, bold=False)

    if idioma.upper() == "ES":
        badge_text = "LABORATORIO DE COMPARATIVAS TÉCNICAS • EUROPA"
        titulo_topo = "COMPARATIVA TÉCNICA 2026"
        sub_vs = "Frente a Frente: Análisis de Prestaciones Reales"
        spec_box_title = "DIFERENCIAS CRUCIALES SEGÚN NUESTRO TEST"
        btn_text = "VER VEREDICTO Y PRECIOS ACTUALES"
        legal_text = "ShopVS EU • Enlaces de compra verificados"
    else:
        badge_text = "EUROPÄISCHES TESTLABOR • DIREKTVERGLEICH"
        titulo_topo = "DIREKTVERGLEICH 2026"
        sub_vs = "Praxistest & Technische Daten im Detail"
        spec_box_title = "ENTSCHEIDENDE UNTERSCHIEDE IM PRAXISTEST"
        btn_text = "JETZT TESTBERICHT & PREISE PRÜFEN"
        legal_text = "ShopVS EU • Geprüfte Händler-Verlinkungen"

    # 1. Badge superior
    draw.rectangle([60, 60, 940, 115], fill=(30, 41, 59), outline=(51, 65, 85), width=2)
    draw.text((80, 75), badge_text, fill=(56, 189, 248), font=font_badge)

    # 2. Caixa de Título e Confronto
    draw.rectangle([60, 140, 940, 480], fill=(24, 32, 47), outline=(56, 189, 248), width=3)
    draw.text((90, 170), titulo_topo, fill=(148, 163, 184), font=font_vs)
    
    # Produto A
    draw.text((90, 225), f"• {produto_a[:38]}", fill=(255, 255, 255), font=font_title)
    draw.text((120, 295), "VS.", fill=(245, 158, 11), font=font_title)
    # Produto B
    draw.text((90, 360), f"• {produto_b[:38]}", fill=(255, 255, 255), font=font_title)
    draw.text((90, 435), sub_vs, fill=(148, 163, 184), font=get_font(22))

    # 3. Título da Seção Técnica
    draw.text((70, 520), spec_box_title, fill=(226, 232, 240), font=font_spec_title)

    # 4. Três Caixas de Destaques Técnicos
    y_start = 570
    box_height = 160
    gap = 35

    for i, item in enumerate(destaques[:3]):
        y = y_start + i * (box_height + gap)
        # Caixa de fundo
        draw.rectangle([60, y, 940, y + box_height], fill=(30, 41, 59), outline=(71, 85, 105), width=2)
        
        # Ícone de verificação em destaque
        draw.ellipse([85, y + 40, 155, y + 110], fill=(16, 185, 129))
        draw.text((105, y + 45), "✓", fill=(255, 255, 255), font=get_font(42, bold=True))

        # Texto do destaque
        draw.text((180, y + 55), item, fill=(241, 245, 249), font=font_spec_text)

    # 5. Botão de Chamada para Ação (CTA)
    cta_y = 1220
    draw.rectangle([60, cta_y, 940, cta_y + 130], fill=(245, 158, 11))
    draw.text((120, cta_y + 45), btn_text, fill=(15, 23, 42), font=font_btn)

    # 6. Rodapé Institucional
    draw.text((320, 1420), legal_text, fill=(148, 163, 184), font=font_footer)

    # Salvar
    os.makedirs(os.path.dirname(caminho_saida), exist_ok=True)
    img.save(caminho_saida, quality=95)
    print(f"[OK] Pin vertical gerado: {caminho_saida}")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_dir = os.path.join(base_dir, "assets", "pins")

    # Amostra de teste Espanha
    criar_card_pinterest(
        idioma="ES",
        produto_a="De'Longhi Magnifica S",
        produto_b="Krups Essential EA8108",
        destaques=[
            "Presión real: 15 Bares estables",
            "Molinillo de acero cónico (13 niveles)",
            "Grupo infusor extraíble y lavable en grifo"
        ],
        caminho_saida=os.path.join(output_dir, "delonghi-vs-krups-es.png")
    )

    # Amostra de teste Alemanha
    criar_card_pinterest(
        idioma="DE",
        produto_a="De'Longhi Magnifica S",
        produto_b="Krups Essential EA8108",
        destaques=[
            "Pumpendruck: 15 Bar Thermoblock",
            "Präzises 13-stufiges Kegelmahlwerk",
            "Vollständig herausnehmbare Brühgruppe"
        ],
        caminho_saida=os.path.join(output_dir, "delonghi-vs-krups-de.png")
    )
