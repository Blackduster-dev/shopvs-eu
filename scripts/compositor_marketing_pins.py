#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Motor de Design de Marketing para Pinterest (Zero IA Generativa)
Compõe Pins comerciais de alta conversão (1000x1500px) utilizando exclusivamente
as fotos oficiais de estúdio dos produtos + tipografia limpa de e-commerce.
"""

import os
import io
import urllib.request
from PIL import Image, ImageDraw, ImageFont, ImageOps

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def carregar_fonte(tamanho, negrito=False):
    caminhos = [
        "C:\\Windows\\Fonts\\segoeuib.ttf" if negrito else "C:\\Windows\\Fonts\\segoeui.ttf",
        "C:\\Windows\\Fonts\\arialbd.ttf" if negrito else "C:\\Windows\\Fonts\\arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if negrito else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    ]
    for p in caminhos:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, tamanho)
            except Exception:
                pass
    return ImageFont.load_default()

def obter_foto_oficial_produto(produto):
    """
    Carrega a foto oficial do produto (de URL oficial da Amazon HD ou do disco local)
    e redimensiona com filtro LANCZOS mantendo 100% da proporção original sem esticar.
    """
    # 1. Tenta baixar da URL oficial de alta resolução da Amazon se disponível
    url_remota = produto.get("imagem_oficial_hd_url", "")
    if url_remota.startswith("http"):
        try:
            req = urllib.request.Request(url_remota, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=8) as resp:
                img_bytes = resp.read()
                return Image.open(io.BytesIO(img_bytes)).convert("RGBA")
        except Exception:
            pass

    # 2. Usa a imagem oficial salva localmente no projeto
    caminho_local = os.path.join(BASE_DIR, produto.get("imagem_url", "").lstrip("/"))
    if os.path.exists(caminho_local):
        return Image.open(caminho_local).convert("RGBA")

    # Fallback neutro caso não encontre
    return Image.new("RGBA", (600, 600), (255, 255, 255, 255))

def criar_pin_marketing_oficial(pais, produto, textos_idioma, caminho_saida, variante=0):
    """
    Monta um Pin comercial de 1000x1500px com vitrine branca central para a foto oficial do produto.
    """
    W, H = 1000, 1500
    temas = [
        {"bg": (11, 25, 44), "vitrine_border": (14, 131, 136), "cta": (255, 101, 0), "tag_bg": (14, 131, 136)},
        {"bg": (17, 24, 39), "vitrine_border": (245, 158, 11), "cta": (16, 185, 129), "tag_bg": (245, 158, 11)},
        {"bg": (24, 24, 27), "vitrine_border": (56, 189, 248), "cta": (234, 88, 12), "tag_bg": (2, 132, 199)}
    ]
    tema = temas[variante % len(temas)]

    pin = Image.new("RGB", (W, H), color=tema["bg"])
    draw = ImageDraw.Draw(pin)

    # 1. Topo: Pílula de Categoria / Selo de Verificação
    draw.rounded_rectangle([60, 45, 940, 105], radius=12, fill=tema["tag_bg"])
    draw.text((90, 58), textos_idioma["kicker"], fill=(255, 255, 255), font=carregar_fonte(26, negrito=True))

    # 2. Headline do Produto + Estrelas de Avaliação
    marca_modelo = f"{produto['marca']} • {produto['nome']}"
    draw.text((60, 125), marca_modelo[:36], fill=(255, 255, 255), font=carregar_fonte(40, negrito=True))
    draw.text((60, 180), f"★★★★★  {produto.get('score_lab', '9.2')}/10  |  {textos_idioma['subtitulo']}", fill=(251, 191, 36), font=carregar_fonte(26, negrito=True))

    # 3. Vitrine Central Branca para a Foto Oficial do Produto (240px até 860px)
    box_x1, box_y1, box_x2, box_y2 = 60, 235, 940, 855
    draw.rounded_rectangle([box_x1, box_y1, box_x2, box_y2], radius=24, fill=(255, 255, 255), outline=tema["vitrine_border"], width=4)

    # Inserir Foto Oficial Real centralizada na vitrine sem distorcer
    foto_prod = obter_foto_oficial_produto(produto)
    foto_ajustada = ImageOps.contain(foto_prod, (540, 540), method=Image.Resampling.LANCZOS)
    
    # Se a imagem local tiver fundo escuro (#0B192C), cria moldura elegante central
    fx = box_x1 + ((box_x2 - box_x1) - foto_ajustada.width) // 2
    fy = box_y1 + ((box_y2 - box_y1) - foto_ajustada.height) // 2
    pin.paste(foto_ajustada.convert("RGB"), (fx, fy))

    # Selo Flutuante de Nota no canto superior direito da Vitrine
    draw.rounded_rectangle([720, 260, 915, 340], radius=14, fill=(11, 25, 44))
    draw.text((742, 278), f"TOP {produto.get('score_lab', '9.2')}", fill=(255, 255, 255), font=carregar_fonte(32, negrito=True))

    # 4. Três Bullets de Especificações / Benefícios Reais (885px até 1245px)
    specs_lista = list(produto.get("specs", {}).items())[:3]
    y_spec = 885
    for chave, valor in specs_lista:
        draw.rounded_rectangle([60, y_spec, 940, y_spec + 102], radius=14, fill=(30, 41, 59), outline=(51, 65, 85), width=2)
        draw.ellipse([82, y_spec + 24, 136, y_spec + 78], fill=(16, 185, 129))
        draw.text((98, y_spec + 26), "✓", fill=(255, 255, 255), font=carregar_fonte(34, negrito=True))
        
        texto_spec = f"{chave.replace('_', ' ').title()}: {valor}"
        draw.text((158, y_spec + 32), texto_spec[:46], fill=(248, 250, 252), font=carregar_fonte(28, negrito=True))
        y_spec += 118

    # 5. Botão CTA Comercial (1265px até 1400px)
    draw.rounded_rectangle([60, 1265, 940, 1400], radius=18, fill=tema["cta"])
    draw.text((110, 1312), textos_idioma["cta"], fill=(255, 255, 255), font=carregar_fonte(32, negrito=True))

    # 6. Rodapé de Compliance
    draw.text((210, 1430), f"ShopVS.eu • Amazon.{pais.lower()} • {textos_idioma['disclosure']}", fill=(148, 163, 184), font=carregar_fonte(21))

    os.makedirs(os.path.dirname(caminho_saida), exist_ok=True)
    pin.save(caminho_saida, quality=95)
    return True
