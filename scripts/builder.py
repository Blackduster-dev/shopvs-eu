#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Builder Estático do ShopVS EU
Compila os dados de produtos em páginas com identidade editorial europeia (Anti-IA).
Gera /index.html, /es/index.html, /de/index.html e páginas específicas de comparativas.
"""

import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_json(rel_path):
    with open(os.path.join(BASE_DIR, rel_path), "r", encoding="utf-8") as f:
        return json.load(f)

def render_home(config, artigos):
    """Gera a página inicial raiz com design sóbrio institucional europeu."""
    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ShopVS EU • Laboratorio de Comparación Técnica & Produkttests</title>
    <meta name="description" content="Laboratorio europeo independiente de comparativas técnicas cara a cara. Análisis objetivo de especificaciones, fallos reportados y relación calidad-precio.">
    <style>
        :root {{
            --bg: #f8fafc;
            --surface: #ffffff;
            --border: #e2e8f0;
            --primary: #0f172a;
            --secondary: #334155;
            --accent: #2563eb;
            --badge-bg: #eff6ff;
            --badge-text: #1d4ed8;
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, sans-serif; background: var(--bg); color: var(--secondary); line-height: 1.6; }}
        header {{ background: var(--surface); border-bottom: 1px solid var(--border); padding: 18px 0; }}
        .container {{ max-width: 1100px; margin: 0 auto; padding: 0 24px; }}
        .nav {{ display: flex; justify-content: space-between; align-items: center; }}
        .brand {{ font-size: 20px; font-weight: 800; color: var(--primary); text-decoration: none; display: flex; align-items: center; gap: 8px; }}
        .nav-links a {{ color: var(--secondary); text-decoration: none; margin-left: 20px; font-weight: 500; font-size: 14px; }}
        .nav-links a:hover {{ color: var(--accent); }}
        
        .hero {{ padding: 56px 0 40px; text-align: center; }}
        .badge-method {{ display: inline-flex; align-items: center; gap: 8px; background: var(--badge-bg); color: var(--badge-text); padding: 6px 14px; border-radius: 999px; font-size: 13px; font-weight: 600; margin-bottom: 20px; border: 1px solid #dbeafe; }}
        .hero h1 {{ font-size: 38px; color: var(--primary); font-weight: 800; line-height: 1.2; margin-bottom: 16px; letter-spacing: -0.02em; }}
        .hero p {{ font-size: 18px; color: #64748b; max-width: 720px; margin: 0 auto 32px; }}

        .region-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 24px; margin-bottom: 56px; }}
        .region-card {{ background: var(--surface); border: 1px solid var(--border); border-radius: 10px; padding: 32px; text-decoration: none; color: inherit; transition: all 0.2s ease; display: flex; flex-direction: column; justify-content: space-between; box-shadow: 0 1px 3px rgba(0,0,0,0.04); }}
        .region-card:hover {{ border-color: var(--accent); transform: translateY(-2px); box-shadow: 0 8px 20px rgba(0,0,0,0.06); }}
        .region-flag {{ font-size: 32px; margin-bottom: 12px; }}
        .region-card h2 {{ font-size: 22px; color: var(--primary); margin-bottom: 8px; }}
        .region-card p {{ font-size: 14px; color: #64748b; margin-bottom: 24px; }}
        .region-btn {{ background: #f1f5f9; color: var(--primary); font-weight: 600; padding: 10px 18px; border-radius: 6px; text-align: center; font-size: 14px; }}
        .region-card:hover .region-btn {{ background: var(--accent); color: #fff; }}

        .featured-section {{ background: var(--surface); border: 1px solid var(--border); border-radius: 10px; padding: 36px; margin-bottom: 48px; }}
        .section-header {{ display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 24px; border-bottom: 1px solid var(--border); padding-bottom: 12px; }}
        .section-title {{ font-size: 20px; color: var(--primary); font-weight: 700; }}
        .article-list {{ display: flex; flex-direction: column; gap: 16px; }}
        .article-item {{ display: flex; justify-content: space-between; align-items: center; padding: 16px; border-radius: 8px; background: #f8fafc; border: 1px solid var(--border); text-decoration: none; color: inherit; transition: 0.15s; }}
        .article-item:hover {{ background: #eff6ff; border-color: #93c5fd; }}
        .article-tag {{ font-size: 12px; font-weight: 700; text-transform: uppercase; color: #2563eb; margin-bottom: 4px; }}
        .article-name {{ font-size: 16px; font-weight: 700; color: var(--primary); }}
        .article-date {{ font-size: 13px; color: #94a3b8; }}

        footer {{ background: #0f172a; color: #94a3b8; padding: 40px 0; font-size: 13px; margin-top: 60px; }}
        .footer-grid {{ display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 20px; }}
        .footer-links a {{ color: #cbd5e1; text-decoration: none; margin-left: 16px; }}
        .footer-links a:hover {{ color: #ffffff; }}
        .disclaimer {{ margin-top: 24px; padding-top: 20px; border-top: 1px solid #334155; font-size: 12px; line-height: 1.6; color: #64748b; }}
    </style>
</head>
<body>
    <header>
        <div class="container nav">
            <a href="/" class="brand">⚖️ ShopVS EU</a>
            <div class="nav-links">
                <a href="/es/">🇪🇸 Edición España</a>
                <a href="/de/">🇩🇪 Edition Deutschland</a>
                <a href="/legal/">Aviso Legal / Impressum</a>
            </div>
        </div>
    </header>

    <main class="container">
        <section class="hero">
            <div class="badge-method">
                <span>🔬 METODOLOGÍA EDITORIAL INDEPENDIENTE</span>
                <span>•</span>
                <span>SIN PRECIOS ALTERADOS</span>
            </div>
            <h1>Comparativas Técnicas de Alta Precisión</h1>
            <p>Comparamos productos líderes del mercado europeo con datos técnicos verificados y análisis exhaustivo de fallos ocultos reportados por compradores.</p>
        </section>

        <section class="region-grid">
            <a href="/es/" class="region-card">
                <div>
                    <div class="region-flag">🇪🇸</div>
                    <h2>Portal España (ES)</h2>
                    <p>Análisis técnico directo de productos populares en Amazon España y grandes almacenes locales. Selección estricta de relación calidad-precio.</p>
                </div>
                <div class="region-btn">Ver Comparativas en Español &rarr;</div>
            </a>
            <a href="/de/" class="region-card">
                <div>
                    <div class="region-flag">🇩🇪</div>
                    <h2>Portal Deutschland (DACH)</h2>
                    <p>Technische Direktvergleiche nach deutschem Prüfstandard. Detaillierte Spezifikationen, Schwachstellen-Analyse und Preis-Leistungs-Checks.</p>
                </div>
                <div class="region-btn">Zu den Direktvergleichen &rarr;</div>
            </a>
        </section>

        <section class="featured-section">
            <div class="section-header">
                <h2 class="section-title">Últimos Informes Técnicos Publicados</h2>
                <span style="font-size: 13px; color: #64748b;">Actualizado Octubre 2026</span>
            </div>
            <div class="article-list">
                <a href="/es/{artigos['slug_es']}.html" class="article-item">
                    <div>
                        <div class="article-tag">🇪🇸 Hogar & Cocina • Comparativa Directa</div>
                        <div class="article-name">{artigos['produto_a']['nome']} vs {artigos['produto_b']['nome']}</div>
                    </div>
                    <div class="article-date">Leer análisis &rarr;</div>
                </a>
                <a href="/de/{artigos['slug_de']}.html" class="article-item">
                    <div>
                        <div class="article-tag">🇩🇪 Kaffeevollautomaten • Testbericht</div>
                        <div class="article-name">{artigos['produto_a']['nome']} vs {artigos['produto_b']['nome']} im Praxistest</div>
                    </div>
                    <div class="article-date">Testbericht lesen &rarr;</div>
                </a>
            </div>
        </section>
    </main>

    <footer>
        <div class="container">
            <div class="footer-grid">
                <div>
                    <strong>ShopVS EU</strong> • Laboratorio Europeo de Análisis Técnico de Productos
                </div>
                <div class="footer-links">
                    <a href="/es/">España</a>
                    <a href="/de/">Deutschland</a>
                    <a href="/legal/">Aviso Legal & Impressum (§ 5 TMG)</a>
                </div>
            </div>
            <div class="disclaimer">
                <p><strong>Aviso de Transparencia de Afiliación:</strong> En calidad de Afiliado de Amazon y plataformas asociadas (Awin), obtenemos ingresos por las compras adscritas que cumplen los requisitos aplicables. Los precios y disponibilidad mostrados en las tiendas enlazadas pueden variar tras nuestra revisión.</p>
                <p style="margin-top: 6px;"><strong>Transparenzhinweis (DE):</strong> Als Amazon-Partner und Affiliate-Partner verdienen wir an qualifizierten Verkäufen.</p>
            </div>
        </div>
    </footer>
</body>
</html>
"""
    with open(os.path.join(BASE_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("[OK] index.html raiz atualizado com design editorial anti-IA.")

def render_article_es(artigo):
    """Gera página de artigo em Castelhano com tabela técnica e sem preço fixo."""
    pa = artigo["produto_a"]
    pb = artigo["produto_b"]

    specs_rows = ""
    for k, v in pa["specs_tecnicas"].items():
        v2 = pb["specs_tecnicas"].get(k, "-")
        k_label = k.replace("_", " ").title()
        specs_rows += f"""
        <tr>
            <td class="spec-label"><strong>{k_label}</strong></td>
            <td class="spec-val-a">{v}</td>
            <td class="spec-val-b">{v2}</td>
        </tr>
        """

    pros_a_html = "".join([f"<li>✓ {p}</li>" for p in pa["pros"]])
    contras_a_html = "".join([f"<li class='con'>✕ {c}</li>" for c in pa["contras_reais"]])
    pros_b_html = "".join([f"<li>✓ {p}</li>" for p in pb["pros"]])
    contras_b_html = "".join([f"<li class='con'>✕ {c}</li>" for c in pb["contras_reais"]])

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{pa['nome']} vs {pb['nome']}: Comparativa y Veredicto Técnico | ShopVS España</title>
    <meta name="description" content="Comparativa técnica exhaustiva entre {pa['nome']} y {pb['nome']}. Análisis de opiniones reales, tabla de especificaciones y fallos ocultos antes de comprar.">
    <style>
        :root {{
            --bg: #f8fafc;
            --surface: #ffffff;
            --border: #e2e8f0;
            --primary: #0f172a;
            --text: #1e293b;
            --muted: #64748b;
            --accent: #2563eb;
            --cta: #d97706;
            --cta-hover: #b45309;
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, sans-serif; background: var(--bg); color: var(--text); line-height: 1.6; }}
        header {{ background: var(--surface); border-bottom: 1px solid var(--border); padding: 16px 0; }}
        .container {{ max-width: 920px; margin: 0 auto; padding: 0 20px; }}
        .nav {{ display: flex; justify-content: space-between; align-items: center; }}
        .brand {{ font-size: 18px; font-weight: 800; color: var(--primary); text-decoration: none; }}
        .breadcrumb {{ font-size: 13px; color: var(--muted); margin: 24px 0 12px; }}
        .breadcrumb a {{ color: var(--muted); text-decoration: none; }}
        .badge-lab {{ display: inline-block; background: #e0f2fe; color: #0369a1; padding: 4px 10px; border-radius: 4px; font-size: 12px; font-weight: 700; margin-bottom: 12px; }}
        h1 {{ font-size: 30px; color: var(--primary); font-weight: 800; line-height: 1.25; margin-bottom: 16px; letter-spacing: -0.02em; }}
        .meta-bar {{ display: flex; gap: 20px; font-size: 13px; color: var(--muted); padding-bottom: 20px; border-bottom: 1px solid var(--border); margin-bottom: 28px; }}

        .card {{ background: var(--surface); border: 1px solid var(--border); border-radius: 8px; padding: 28px; margin-bottom: 28px; box-shadow: 0 1px 3px rgba(0,0,0,0.03); }}
        .card h2 {{ font-size: 20px; color: var(--primary); margin-bottom: 16px; display: flex; align-items: center; gap: 8px; }}
        
        .verdict-box {{ background: #eff6ff; border-left: 4px solid var(--accent); padding: 20px; border-radius: 4px; margin-bottom: 28px; font-size: 15px; color: #1e3a8a; }}
        
        /* Tabela Comparativa */
        .table-wrap {{ overflow-x: auto; margin: 20px 0; }}
        table {{ width: 100%; border-collapse: collapse; text-align: left; font-size: 14px; }}
        th {{ background: #f1f5f9; padding: 14px; border: 1px solid var(--border); color: var(--primary); font-weight: 700; }}
        td {{ padding: 12px 14px; border: 1px solid var(--border); }}
        tr:nth-child(even) {{ background: #f8fafc; }}
        .spec-label {{ font-weight: 600; color: #475569; width: 30%; }}
        .spec-val-a, .spec-val-b {{ width: 35%; }}

        /* Prós e Contras */
        .dual-columns {{ display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 16px; }}
        @media (max-width: 640px) {{ .dual-columns {{ grid-template-columns: 1fr; }} }}
        .column-box {{ background: #f8fafc; border: 1px solid var(--border); border-radius: 6px; padding: 20px; }}
        .column-box h3 {{ font-size: 16px; color: var(--primary); margin-bottom: 12px; }}
        ul {{ list-style: none; }}
        li {{ font-size: 14px; margin-bottom: 8px; color: #334155; }}
        li.con {{ color: #991b1b; }}

        /* CTA Dinâmico (Sem Preço Fixo) */
        .cta-btn {{ display: inline-flex; align-items: center; justify-content: center; width: 100%; background: var(--cta); color: #ffffff; text-decoration: none; padding: 14px 20px; border-radius: 6px; font-weight: 700; font-size: 15px; margin-top: 16px; transition: background 0.15s; text-align: center; }}
        .cta-btn:hover {{ background: var(--cta-hover); }}
        .cta-btn.secondary {{ background: #2563eb; }}
        .cta-btn.secondary:hover {{ background: #1d4ed8; }}
        .sub-cta {{ font-size: 12px; color: var(--muted); text-align: center; margin-top: 8px; }}

        footer {{ background: #0f172a; color: #94a3b8; padding: 36px 0; font-size: 13px; margin-top: 60px; }}
        .disclaimer-box {{ font-size: 12px; color: #64748b; margin-top: 16px; border-top: 1px solid #334155; padding-top: 16px; }}
    </style>
</head>
<body>
    <header>
        <div class="container nav">
            <a href="/" class="brand">⚖️ ShopVS EU</a>
            <div style="font-size: 14px;">
                <a href="/es/" style="color:var(--accent); text-decoration:none; font-weight:600;">🇪🇸 Comparativas España</a>
                <span style="color:var(--muted); margin: 0 8px;">|</span>
                <a href="/legal/" style="color:var(--muted); text-decoration:none;">Aviso Legal</a>
            </div>
        </div>
    </header>

    <main class="container">
        <div class="breadcrumb">
            <a href="/">Inicio</a> &rsaquo; <a href="/es/">España</a> &rsaquo; {artigo['categoria']}
        </div>

        <span class="badge-lab">INFORME TÉCNICO DE COMPARACIÓN</span>
        <h1>{pa['nome']} vs {pb['nome']}: ¿Cuál Merece la Pena en 2026?</h1>
        
        <div class="meta-bar">
            <span>📅 Fecha de revisión: {artigo['data_publicacao']}</span>
            <span>⏱️ Tiempo de lectura: 4 minutos</span>
            <span>🔬 Metodología: Pruebas de laboratorio y opiniones verificadas</span>
        </div>

        <div class="verdict-box">
            <strong>💡 Veredicto Rápido de Nuestros Analistas:</strong><br>
            {artigo['veredito_resumo']['es']}
        </div>

        <div class="card">
            <h2>📊 Tabla Comparativa de Especificaciones Técnicas</h2>
            <p style="font-size:14px; color:var(--muted); margin-bottom:12px;">Comparación directa de especificaciones oficiales y mediciones de funcionamiento.</p>
            <div class="table-wrap">
                <table>
                    <thead>
                        <tr>
                            <th>Característica</th>
                            <th>{pa['nome']}</th>
                            <th>{pb['nome']}</th>
                        </tr>
                    </thead>
                    <tbody>
                        {specs_rows}
                    </tbody>
                </table>
            </div>
        </div>

        <div class="card">
            <h2>🔍 Análisis de Rendimiento y Fallos Reportados</h2>
            <p style="font-size:14px; color:var(--muted); margin-bottom:16px;">Sintetizamos las pruebas prácticas y las quejas reales reportadas por compradores en los últimos 90 días:</p>
            
            <div class="dual-columns">
                <div class="column-box">
                    <h3>1. {pa['nome']}</h3>
                    <ul style="margin-bottom:16px;">
                        {pros_a_html}
                        {contras_a_html}
                    </ul>
                    <a href="{pa['link_es']}" target="_blank" rel="nofollow noopener sponsored" class="cta-btn">
                        Ver precio y disponibilidad en Amazon.es &rarr;
                    </a>
                    <div class="sub-cta">Envío garantizado por Amazon Prime España</div>
                </div>

                <div class="column-box">
                    <h3>2. {pb['nome']}</h3>
                    <ul style="margin-bottom:16px;">
                        {pros_b_html}
                        {contras_b_html}
                    </ul>
                    <a href="{pb['link_es']}" target="_blank" rel="nofollow noopener sponsored" class="cta-btn secondary">
                        Ver precio y disponibilidad en Amazon.es &rarr;
                    </a>
                    <div class="sub-cta">Envío garantizado por Amazon Prime España</div>
                </div>
            </div>
        </div>

        <div class="card">
            <h2>🎯 Conclusión Final: ¿Cuál deberías comprar?</h2>
            <p style="font-size:15px; margin-bottom:12px;">
                Si priorizas la <strong>higiene y durabilidad a largo plazo</strong>, la <strong>{pa['nome']}</strong> justifica con creces su elección gracias al grupo de infusión extraíble que puedes lavar bajo el grifo sin gastar en pastillas de limpieza químicas todos los meses.
            </p>
            <p style="font-size:15px;">
                Por el contrario, si tu <strong>espacio en cocina es muy reducido</strong> y buscas una cafetera que caliente el café de inmediato sin complicaciones, la <strong>{pb['nome']}</strong> cumplirá tus expectativas con una relación tamaño-precio difícil de batir.
            </p>
        </div>
    </main>

    <footer>
        <div class="container">
            <p>&copy; 2026 ShopVS EU • Comparativas Técnicas Independientes • <a href="/legal/" style="color:#cbd5e1;">Aviso Legal / Impressum</a></p>
            <div class="disclaimer-box">
                <strong>Aviso Legal de Afiliación (España):</strong> En calidad de Afiliado de Amazon, obtengo ingresos por las compras adscritas que cumplen los requisitos aplicables. Los precios son establecidos por el comercio y se actualizan dinámicamente en el enlace de compra oficial.
            </div>
        </div>
    </footer>
</body>
</html>
"""
    file_path = os.path.join(BASE_DIR, "es", f"{artigo['slug_es']}.html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"[OK] Artigo ES gerado: {file_path}")

def render_article_de(artigo):
    """Gera página de artigo em Hochdeutsch no estilo Stiftung Warentest / Testbericht."""
    pa = artigo["produto_a"]
    pb = artigo["produto_b"]

    specs_rows = ""
    for k, v in pa["specs_tecnicas"].items():
        v2 = pb["specs_tecnicas"].get(k, "-")
        k_label = k.replace("_", " ").title()
        if k == "potencia": k_label = "Leistung"
        elif k == "pressao": k_label = "Pumpendruck"
        elif k == "reservatorio_agua": k_label = "Wassertank-Volumen"
        elif k == "capacidade_graos": k_label = "Bohnenbehälter"
        elif k == "moedor": k_label = "Mahlwerk"
        elif k == "limpeza_infusor": k_label = "Brühgruppen-Reinigung"
        specs_rows += f"""
        <tr>
            <td class="spec-label"><strong>{k_label}</strong></td>
            <td class="spec-val-a">{v}</td>
            <td class="spec-val-b">{v2}</td>
        </tr>
        """

    pros_a_html = "".join([f"<li>✓ {p}</li>" for p in pa["pros"]])
    contras_a_html = "".join([f"<li class='con'>✕ {c}</li>" for c in pa["contras_reais"]])
    pros_b_html = "".join([f"<li>✓ {p}</li>" for p in pb["pros"]])
    contras_b_html = "".join([f"<li class='con'>✕ {c}</li>" for c in pb["contras_reais"]])

    html = f"""<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{pa['nome']} vs. {pb['nome']} im Test: Direktvergleich 2026 | ShopVS Deutschland</title>
    <meta name="description" content="Ausführlicher technischer Direktvergleich zwischen {pa['nome']} und {pb['nome']}. Technische Daten, Praxis-Schwachstellen und Kaufempfehlung im Überblick.">
    <style>
        :root {{
            --bg: #f8fafc;
            --surface: #ffffff;
            --border: #e2e8f0;
            --primary: #0f172a;
            --text: #1e293b;
            --muted: #64748b;
            --accent: #1e3a8a;
            --cta: #d97706;
            --cta-hover: #b45309;
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, sans-serif; background: var(--bg); color: var(--text); line-height: 1.6; }}
        header {{ background: var(--surface); border-bottom: 1px solid var(--border); padding: 16px 0; }}
        .container {{ max-width: 920px; margin: 0 auto; padding: 0 20px; }}
        .nav {{ display: flex; justify-content: space-between; align-items: center; }}
        .brand {{ font-size: 18px; font-weight: 800; color: var(--primary); text-decoration: none; }}
        .breadcrumb {{ font-size: 13px; color: var(--muted); margin: 24px 0 12px; }}
        .breadcrumb a {{ color: var(--muted); text-decoration: none; }}
        .badge-lab {{ display: inline-block; background: #e2e8f0; color: #1e293b; padding: 4px 10px; border-radius: 4px; font-size: 12px; font-weight: 700; margin-bottom: 12px; }}
        h1 {{ font-size: 30px; color: var(--primary); font-weight: 800; line-height: 1.25; margin-bottom: 16px; letter-spacing: -0.02em; }}
        .meta-bar {{ display: flex; gap: 20px; font-size: 13px; color: var(--muted); padding-bottom: 20px; border-bottom: 1px solid var(--border); margin-bottom: 28px; }}

        .card {{ background: var(--surface); border: 1px solid var(--border); border-radius: 8px; padding: 28px; margin-bottom: 28px; box-shadow: 0 1px 3px rgba(0,0,0,0.03); }}
        .card h2 {{ font-size: 20px; color: var(--primary); margin-bottom: 16px; display: flex; align-items: center; gap: 8px; }}
        
        .verdict-box {{ background: #f1f5f9; border-left: 4px solid var(--primary); padding: 20px; border-radius: 4px; margin-bottom: 28px; font-size: 15px; color: var(--text); }}
        
        /* Tabelle */
        .table-wrap {{ overflow-x: auto; margin: 20px 0; }}
        table {{ width: 100%; border-collapse: collapse; text-align: left; font-size: 14px; }}
        th {{ background: #f1f5f9; padding: 14px; border: 1px solid var(--border); color: var(--primary); font-weight: 700; }}
        td {{ padding: 12px 14px; border: 1px solid var(--border); }}
        tr:nth-child(even) {{ background: #f8fafc; }}
        .spec-label {{ font-weight: 600; color: #475569; width: 30%; }}
        .spec-val-a, .spec-val-b {{ width: 35%; }}

        /* Vor- & Nachteile */
        .dual-columns {{ display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 16px; }}
        @media (max-width: 640px) {{ .dual-columns {{ grid-template-columns: 1fr; }} }}
        .column-box {{ background: #f8fafc; border: 1px solid var(--border); border-radius: 6px; padding: 20px; }}
        .column-box h3 {{ font-size: 16px; color: var(--primary); margin-bottom: 12px; }}
        ul {{ list-style: none; }}
        li {{ font-size: 14px; margin-bottom: 8px; color: #334155; }}
        li.con {{ color: #991b1b; }}

        /* CTA Dynamisch */
        .cta-btn {{ display: inline-flex; align-items: center; justify-content: center; width: 100%; background: var(--cta); color: #ffffff; text-decoration: none; padding: 14px 20px; border-radius: 6px; font-weight: 700; font-size: 15px; margin-top: 16px; transition: background 0.15s; text-align: center; }}
        .cta-btn:hover {{ background: var(--cta-hover); }}
        .cta-btn.secondary {{ background: #1e3a8a; }}
        .cta-btn.secondary:hover {{ background: #172554; }}
        .sub-cta {{ font-size: 12px; color: var(--muted); text-align: center; margin-top: 8px; }}

        footer {{ background: #0f172a; color: #94a3b8; padding: 36px 0; font-size: 13px; margin-top: 60px; }}
        .disclaimer-box {{ font-size: 12px; color: #64748b; margin-top: 16px; border-top: 1px solid #334155; padding-top: 16px; }}
    </style>
</head>
<body>
    <header>
        <div class="container nav">
            <a href="/" class="brand">⚖️ ShopVS EU</a>
            <div style="font-size: 14px;">
                <a href="/de/" style="color:var(--accent); text-decoration:none; font-weight:600;">🇩🇪 Produkttests Deutschland</a>
                <span style="color:var(--muted); margin: 0 8px;">|</span>
                <a href="/legal/" style="color:var(--muted); text-decoration:none;">Impressum gemäß § 5 TMG</a>
            </div>
        </div>
    </header>

    <main class="container">
        <div class="breadcrumb">
            <a href="/">Startseite</a> &rsaquo; <a href="/de/">Deutschland</a> &rsaquo; {artigo['categoria']}
        </div>

        <span class="badge-lab">TECHNISCHER DIREKTVERGLEICH • PRAXISTEST</span>
        <h1>{pa['nome']} vs. {pb['nome']}: Welcher Kaffeevollautomat lohnt sich?</h1>
        
        <div class="meta-bar">
            <span>📅 Stand: {artigo['data_publicacao']}</span>
            <span>⏱️ Lesezeit: 4 Minuten</span>
            <span>🔬 Prüfbasis: Labor-Spezifikationen & verifizierte Käuferdaten</span>
        </div>

        <div class="verdict-box">
            <strong>📋 Kurzfazit der Redaktion:</strong><br>
            {artigo['veredito_resumo']['de']}
        </div>

        <div class="card">
            <h2>📊 Technische Daten im Überblick</h2>
            <p style="font-size:14px; color:var(--muted); margin-bottom:12px;">Gegenüberstellung der Herstellerangaben und messtechnischen Kenngrößen.</p>
            <div class="table-wrap">
                <table>
                    <thead>
                        <tr>
                            <th>Kenngröße</th>
                            <th>{pa['nome']}</th>
                            <th>{pb['nome']}</th>
                        </tr>
                    </thead>
                    <tbody>
                        {specs_rows}
                    </tbody>
                </table>
            </div>
        </div>

        <div class="card">
            <h2>🔍 Praxiseindrücke & Bekannte Schwachstellen</h2>
            <p style="font-size:14px; color:var(--muted); margin-bottom:16px;">Zusammenfassung realer Käufermeinungen und Langzeit-Erfahrungen aus dem DACH-Raum:</p>
            
            <div class="dual-columns">
                <div class="column-box">
                    <h3>1. {pa['nome']}</h3>
                    <ul style="margin-bottom:16px;">
                        {pros_a_html}
                        {contras_a_html}
                    </ul>
                    <a href="{pa['link_de']}" target="_blank" rel="nofollow noopener sponsored" class="cta-btn">
                        Aktuellen Preis auf Amazon.de prüfen &rarr;
                    </a>
                    <div class="sub-cta">Verkauf und Versand durch Amazon Deutschland</div>
                </div>

                <div class="column-box">
                    <h3>2. {pb['nome']}</h3>
                    <ul style="margin-bottom:16px;">
                        {pros_b_html}
                        {contras_b_html}
                    </ul>
                    <a href="{pb['link_de']}" target="_blank" rel="nofollow noopener sponsored" class="cta-btn secondary">
                        Aktuellen Preis auf Amazon.de prüfen &rarr;
                    </a>
                    <div class="sub-cta">Verkauf und Versand durch Amazon Deutschland</div>
                </div>
            </div>
        </div>

        <div class="card">
            <h2>🎯 Kaufempfehlung im Detail</h2>
            <p style="font-size:15px; margin-bottom:12px;">
                Wer Wert auf <strong>Hygienesicherheit und Langlebigkeit</strong> legt, trifft mit der <strong>{pa['nome']}</strong> die nachhaltigere Wahl. Die Brühgruppe kann komplett entnommen und unter fließendem Wasser gereinigt werden, was teure Entkalkungstabletten-Zyklen minimiert.
            </p>
            <p style="font-size:15px;">
                Die <strong>{pb['nome']}</strong> empfiehlt sich hingegen vorrangig für <strong>sehr kompakte Einbauverhältnisse</strong> oder Einsteiger, die eine unkomplizierte Bedienung zu einem meist günstigeren Anschaffungspreis suchen.
            </p>
        </div>
    </main>

    <footer>
        <div class="container">
            <p>&copy; 2026 ShopVS EU • Unabhängige Produktvergleiche • <a href="/legal/" style="color:#cbd5e1;">Impressum & Datenschutz (§ 5 TMG)</a></p>
            <div class="disclaimer-box">
                <strong>Transparenzhinweis (DE / AT):</strong> Als Amazon-Partner verdiene ich an qualifizierten Verkäufen. Die Preise werden vom Händler bestimmt und über den offiziellen Kauf-Link tagesaktuell abgerufen.
            </div>
        </div>
    </footer>
</body>
</html>
"""
    file_path = os.path.join(BASE_DIR, "de", f"{artigo['slug_de']}.html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"[OK] Artigo DE gerado: {file_path}")

def render_hub_es(artigos):
    """Gera hub /es/index.html."""
    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Comparativas Técnicas de Productos | ShopVS España</title>
    <style>
        body {{ font-family: -apple-system, system-ui, sans-serif; background: #f8fafc; color: #1e293b; margin: 0; padding: 0; }}
        header {{ background: #ffffff; border-bottom: 1px solid #e2e8f0; padding: 20px 0; }}
        .container {{ max-width: 900px; margin: 0 auto; padding: 0 20px; }}
        .brand {{ font-size: 18px; font-weight: 800; color: #0f172a; text-decoration: none; }}
        h1 {{ font-size: 28px; color: #0f172a; margin: 32px 0 12px; }}
        .card {{ background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 24px; margin-bottom: 16px; display: flex; justify-content: space-between; align-items: center; text-decoration: none; color: inherit; transition: 0.15s; }}
        .card:hover {{ border-color: #2563eb; transform: translateY(-2px); }}
        .btn {{ background: #2563eb; color: #fff; padding: 8px 16px; border-radius: 6px; font-size: 13px; font-weight: 600; }}
        footer {{ background: #0f172a; color: #94a3b8; padding: 32px 0; font-size: 13px; margin-top: 60px; text-align: center; }}
    </style>
</head>
<body>
    <header>
        <div class="container" style="display:flex; justify-content:space-between; align-items:center;">
            <a href="/" class="brand">⚖️ ShopVS EU</a>
            <div>
                <a href="/" style="text-decoration:none; color:#64748b; font-size:14px; margin-right:12px;">Inicio</a>
                <a href="/legal/" style="text-decoration:none; color:#64748b; font-size:14px;">Aviso Legal</a>
            </div>
        </div>
    </header>
    <main class="container">
        <h1>🇪🇸 Comparativas Técnicas en España</h1>
        <p style="color:#64748b; margin-bottom:28px;">Informes independientes cara a cara. Análisis objetivo de especificaciones y fallos de compradores.</p>
        
        <a href="/es/{artigos['slug_es']}.html" class="card">
            <div>
                <span style="font-size:12px; font-weight:700; color:#2563eb; text-transform:uppercase;">{artigos['categoria']}</span>
                <h3 style="font-size:18px; margin-top:4px; color:#0f172a;">{artigos['produto_a']['nome']} vs {artigos['produto_b']['nome']}</h3>
                <p style="font-size:13px; color:#64748b; margin-top:6px;">Comparativa completa de molinillo, presión en bares y limpieza del grupo de infusión.</p>
            </div>
            <span class="btn">Leer Análisis &rarr;</span>
        </a>
    </main>
    <footer>
        <div class="container">
            <p>&copy; 2026 ShopVS EU • <a href="/legal/" style="color:#cbd5e1;">Aviso Legal y Privacidad</a></p>
        </div>
    </footer>
</body>
</html>
"""
    file_path = os.path.join(BASE_DIR, "es", "index.html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"[OK] Hub ES gerado: {file_path}")

def render_hub_de(artigos):
    """Gera hub /de/index.html."""
    html = f"""<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Technische Produkttests & Direktvergleiche | ShopVS Deutschland</title>
    <style>
        body {{ font-family: -apple-system, system-ui, sans-serif; background: #f8fafc; color: #1e293b; margin: 0; padding: 0; }}
        header {{ background: #ffffff; border-bottom: 1px solid #e2e8f0; padding: 20px 0; }}
        .container {{ max-width: 900px; margin: 0 auto; padding: 0 20px; }}
        .brand {{ font-size: 18px; font-weight: 800; color: #0f172a; text-decoration: none; }}
        h1 {{ font-size: 28px; color: #0f172a; margin: 32px 0 12px; }}
        .card {{ background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 24px; margin-bottom: 16px; display: flex; justify-content: space-between; align-items: center; text-decoration: none; color: inherit; transition: 0.15s; }}
        .card:hover {{ border-color: #1e3a8a; transform: translateY(-2px); }}
        .btn {{ background: #1e3a8a; color: #fff; padding: 8px 16px; border-radius: 6px; font-size: 13px; font-weight: 600; }}
        footer {{ background: #0f172a; color: #94a3b8; padding: 32px 0; font-size: 13px; margin-top: 60px; text-align: center; }}
    </style>
</head>
<body>
    <header>
        <div class="container" style="display:flex; justify-content:space-between; align-items:center;">
            <a href="/" class="brand">⚖️ ShopVS EU</a>
            <div>
                <a href="/" style="text-decoration:none; color:#64748b; font-size:14px; margin-right:12px;">Startseite</a>
                <a href="/legal/" style="text-decoration:none; color:#64748b; font-size:14px;">Impressum (§ 5 TMG)</a>
            </div>
        </div>
    </header>
    <main class="container">
        <h1>🇩🇪 Technische Direktvergleiche & Testberichte</h1>
        <p style="color:#64748b; margin-bottom:28px;">Prüfung von Spezifikationen, echter Käuferkritik und Preis-Leistungs-Verhältnis für den DACH-Markt.</p>
        
        <a href="/de/{artigos['slug_de']}.html" class="card">
            <div>
                <span style="font-size:12px; font-weight:700; color:#1e3a8a; text-transform:uppercase;">{artigos['categoria']}</span>
                <h3 style="font-size:18px; margin-top:4px; color:#0f172a;">{artigos['produto_a']['nome']} vs. {artigos['produto_b']['nome']}</h3>
                <p style="font-size:13px; color:#64748b; margin-top:6px;">Detaillierter Test zu Mahlwerk, Pumpendruck und Reinigung der Brühgruppe.</p>
            </div>
            <span class="btn">Testbericht lesen &rarr;</span>
        </a>
    </main>
    <footer>
        <div class="container">
            <p>&copy; 2026 ShopVS EU • <a href="/legal/" style="color:#cbd5e1;">Impressum & Datenschutzerklärung</a></p>
        </div>
    </footer>
</body>
</html>
"""
    file_path = os.path.join(BASE_DIR, "de", "index.html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"[OK] Hub DE gerado: {file_path}")

def build_all():
    config = load_json("config_afiliados.json")
    artigo = load_json("data/produto_duplo.json")

    os.makedirs(os.path.join(BASE_DIR, "es"), exist_ok=True)
    os.makedirs(os.path.join(BASE_DIR, "de"), exist_ok=True)

    render_home(config, artigo)
    render_hub_es(artigo)
    render_hub_de(artigo)
    render_article_es(artigo)
    render_article_de(artigo)
    print("\n[OK] Build estatico completado com sucesso!")

if __name__ == "__main__":
    build_all()
