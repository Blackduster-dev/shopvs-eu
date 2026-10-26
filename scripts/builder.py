#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Builder Estático do ShopVS EU - Design System Stitch & Frontend Lead
Gera páginas estáticas totalmente responsivas (Mobile 375px -> Desktop 1440px)
Incorpora tokens de design do Google Stitch (DESIGN.md) e boas práticas de UI editorial.
"""

import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_json(rel_path):
    with open(os.path.join(BASE_DIR, rel_path), "r", encoding="utf-8") as f:
        return json.load(f)

# Configuração e CSS/Tokens comuns em Tailwind
COMMON_HEAD = """
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" rel="stylesheet" />
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        'lab-bg': '#f8f9ff',
                        'lab-surface': '#ffffff',
                        'lab-border': '#e2e8f0',
                        'lab-border-dark': '#cbd5e1',
                        'lab-primary': '#0037b0',
                        'lab-primary-container': '#1d4ed8',
                        'lab-text': '#0b1c30',
                        'lab-muted': '#565e74',
                        'lab-tertiary': '#004f38',
                        'lab-tertiary-fixed': '#97f5cc',
                        'lab-amber': '#d97706',
                        'lab-error': '#ba1a1a',
                        'lab-error-bg': '#ffdad6'
                    },
                    fontFamily: {
                        sans: ['Inter', '-apple-system', 'BlinkMacSystemFont', 'sans-serif'],
                    }
                }
            }
        }
    </script>
    <style>
        body { font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif; background-color: #f8f9ff; color: #0b1c30; }
        .material-symbols-outlined { font-variation-settings: 'FILL' 0, 'wght' 500, 'GRAD' 0, 'opsz' 20; vertical-align: middle; }
    </style>
"""

def render_home(config, artigo):
    """Página inicial responsiva com seletor de região e destaques de laboratório."""
    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ShopVS EU • Laboratorio de Comparación Técnica & Produkttests</title>
    <meta name="description" content="Portal europeo independiente de auditoría técnica y comparativas cara a cara. Metodología de laboratorio, especificaciones reales y fallos de compradores.">
    {COMMON_HEAD}
</head>
<body class="min-h-screen flex flex-col bg-lab-bg text-lab-text antialiased">
    <!-- Header -->
    <header class="sticky top-0 z-50 bg-white/95 backdrop-blur border-b border-lab-border">
        <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
            <a href="/" class="flex items-center gap-2.5 text-decoration-none group">
                <span class="w-9 h-9 rounded bg-lab-primary text-white flex items-center justify-center font-bold text-lg shadow-sm">VS</span>
                <div class="flex flex-col">
                    <span class="font-bold text-base tracking-tight text-lab-text leading-tight group-hover:text-lab-primary transition-colors">ShopVS EU</span>
                    <span class="text-[10px] text-lab-muted uppercase tracking-wider font-semibold">Test Laboratory & Benchmark</span>
                </div>
            </a>
            <div class="flex items-center gap-3">
                <div class="flex items-center bg-slate-100 rounded-md p-1 border border-lab-border text-xs font-semibold">
                    <a href="/es/" class="px-2.5 py-1 rounded bg-white text-lab-primary shadow-xs">🇪🇸 ES</a>
                    <a href="/de/" class="px-2.5 py-1 rounded text-lab-muted hover:text-lab-text transition-colors">🇩🇪 DE</a>
                </div>
                <a href="/legal/" class="text-xs font-medium text-lab-muted hover:text-lab-text hidden sm:inline-flex items-center gap-1">
                    <span class="material-symbols-outlined text-[16px]">gavel</span> Impressum (§ 5 TMG)
                </a>
            </div>
        </div>
    </header>

    <main class="flex-1 max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-8 sm:py-12 w-full">
        <!-- Hero Section -->
        <div class="text-center max-w-3xl mx-auto mb-10 sm:mb-14">
            <div class="inline-flex items-center gap-2 bg-blue-50 text-blue-800 border border-blue-200 px-3 py-1 rounded-full text-xs font-bold uppercase tracking-wider mb-4">
                <span class="material-symbols-outlined text-[15px] text-blue-700">verified</span>
                Auditoría Técnica Independiente • Normativa UE
            </div>
            <h1 class="text-3xl sm:text-4xl lg:text-5xl font-extrabold tracking-tight text-lab-text leading-tight mb-4">
                Comparativas de Productos Sin Sesgo Comercial
            </h1>
            <p class="text-base sm:text-lg text-lab-muted leading-relaxed">
                Evaluamos cara a cara los modelos más vendidos en los mercados de España y Alemania. Fichas técnicas auditadas, mediciones de laboratorio y fallos crónicos reales.
            </p>
        </div>

        <!-- Portales Regionales (Cards) -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-12">
            <!-- España -->
            <a href="/es/" class="bg-white border border-lab-border hover:border-lab-primary rounded-lg p-6 sm:p-8 flex flex-col justify-between transition-all hover:shadow-md group">
                <div>
                    <div class="flex items-center justify-between mb-4">
                        <span class="text-3xl">🇪🇸</span>
                        <span class="text-[11px] font-bold uppercase bg-slate-100 text-slate-700 px-2 py-0.5 rounded">Mercado España</span>
                    </div>
                    <h2 class="text-xl font-bold text-lab-text mb-2 group-hover:text-lab-primary transition-colors">Edición España (.es)</h2>
                    <p class="text-sm text-lab-muted mb-6 leading-relaxed">
                        Análisis comparativos exhaustivos con foco en relación calidad-precio para compradores en Amazon España y cadenas oficiales.
                    </p>
                </div>
                <div class="inline-flex items-center justify-between w-full font-semibold text-sm bg-slate-50 group-hover:bg-lab-primary group-hover:text-white px-4 py-2.5 rounded border border-lab-border group-hover:border-lab-primary transition-all">
                    <span>Acceder al Portal España</span>
                    <span class="material-symbols-outlined text-[18px]">arrow_forward</span>
                </div>
            </a>

            <!-- Alemanha -->
            <a href="/de/" class="bg-white border border-lab-border hover:border-lab-primary rounded-lg p-6 sm:p-8 flex flex-col justify-between transition-all hover:shadow-md group">
                <div>
                    <div class="flex items-center justify-between mb-4">
                        <span class="text-3xl">🇩🇪</span>
                        <span class="text-[11px] font-bold uppercase bg-slate-100 text-slate-700 px-2 py-0.5 rounded">DACH Region</span>
                    </div>
                    <h2 class="text-xl font-bold text-lab-text mb-2 group-hover:text-lab-primary transition-colors">Edition Deutschland (.de)</h2>
                    <p class="text-sm text-lab-muted mb-6 leading-relaxed">
                        Technische Direktvergleiche nach strengen Prüfrichtlinien (Testbericht-Standard). Detaillierte Kenngrößen und Schwachstellen-Audit.
                    </p>
                </div>
                <div class="inline-flex items-center justify-between w-full font-semibold text-sm bg-slate-50 group-hover:bg-lab-primary group-hover:text-white px-4 py-2.5 rounded border border-lab-border group-hover:border-lab-primary transition-all">
                    <span>Zu den Direktvergleichen</span>
                    <span class="material-symbols-outlined text-[18px]">arrow_forward</span>
                </div>
            </a>
        </div>

        <!-- Últimos Testes de Laboratório -->
        <div class="bg-white border border-lab-border rounded-lg p-6 sm:p-8 shadow-xs">
            <div class="flex items-center justify-between border-b border-lab-border pb-4 mb-6">
                <div>
                    <h3 class="text-lg font-bold text-lab-text">Últimos Informes Técnicos Publicados</h3>
                    <p class="text-xs text-lab-muted">Fichas técnicas comparativas y auditoría de averías frecuentes</p>
                </div>
                <span class="text-xs font-semibold bg-emerald-50 text-emerald-700 px-2.5 py-1 rounded border border-emerald-200">
                    Octubre 2026
                </span>
            </div>

            <div class="grid grid-cols-1 lg:grid-cols-2 gap-4">
                <a href="/es/{artigo['slug_es']}.html" class="flex flex-col sm:flex-row sm:items-center justify-between p-4 rounded-md border border-lab-border bg-slate-50/60 hover:bg-blue-50/50 hover:border-blue-300 transition-all gap-3 group">
                    <div>
                        <div class="flex items-center gap-2 mb-1">
                            <span class="text-xs font-bold text-lab-primary uppercase">🇪🇸 {artigo['categoria']}</span>
                            <span class="text-[10px] bg-slate-200 px-1.5 py-0.2 rounded font-semibold text-slate-700">Lab Test</span>
                        </div>
                        <h4 class="font-bold text-sm text-lab-text group-hover:text-lab-primary">{artigo['produto_a']['nome']} vs {artigo['produto_b']['nome']}</h4>
                    </div>
                    <span class="text-xs font-semibold text-lab-primary self-end sm:self-center shrink-0 flex items-center gap-1">
                        Leer análisis <span class="material-symbols-outlined text-[15px]">arrow_forward</span>
                    </span>
                </a>

                <a href="/de/{artigo['slug_de']}.html" class="flex flex-col sm:flex-row sm:items-center justify-between p-4 rounded-md border border-lab-border bg-slate-50/60 hover:bg-blue-50/50 hover:border-blue-300 transition-all gap-3 group">
                    <div>
                        <div class="flex items-center gap-2 mb-1">
                            <span class="text-xs font-bold text-lab-primary uppercase">🇩🇪 Kaffeevollautomaten</span>
                            <span class="text-[10px] bg-slate-200 px-1.5 py-0.2 rounded font-semibold text-slate-700">Testbericht</span>
                        </div>
                        <h4 class="font-bold text-sm text-lab-text group-hover:text-lab-primary">{artigo['produto_a']['nome']} vs {artigo['produto_b']['nome']}</h4>
                    </div>
                    <span class="text-xs font-semibold text-lab-primary self-end sm:self-center shrink-0 flex items-center gap-1">
                        Testbericht lesen <span class="material-symbols-outlined text-[15px]">arrow_forward</span>
                    </span>
                </a>
            </div>
        </div>
    </main>

    <!-- Footer -->
    <footer class="bg-white border-t border-lab-border mt-16 py-8">
        <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex flex-col md:flex-row items-center justify-between gap-4 text-xs text-lab-muted">
                <div>
                    <strong>ShopVS EU</strong> • Laboratorio Técnico Independiente de Comparación de Productos
                </div>
                <div class="flex items-center gap-4">
                    <a href="/es/" class="hover:text-lab-text">España</a>
                    <a href="/de/" class="hover:text-lab-text">Deutschland</a>
                    <a href="/legal/" class="hover:text-lab-text font-semibold">Impressum & Aviso Legal (§ 5 TMG)</a>
                </div>
            </div>
            <div class="mt-6 pt-4 border-t border-slate-100 text-[11px] text-slate-400 leading-relaxed">
                <strong>Aviso de Transparencia:</strong> En calidad de Afiliado de Amazon y colaborador de programas de afiliados (Awin), ShopVS EU obtiene ingresos por compras que cumplen con los requisitos aplicables. Por motivos de cumplimiento legal y exactitud comercial, ningún precio es fijo; todos los enlaces conducen a la consulta en tiempo real en los minoristas oficiales.
            </div>
        </div>
    </footer>
</body>
</html>
"""
    with open(os.path.join(BASE_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("[OK] index.html atualizado com design Stitch responsivo.")

def render_article_es(artigo):
    """Renderiza a página de comparativa completa em Espanhol adaptada de DESIGN.md."""
    pa = artigo["produto_a"]
    pb = artigo["produto_b"]

    specs_rows = ""
    for i, (k, v) in enumerate(pa["specs_tecnicas"].items()):
        v2 = pb["specs_tecnicas"].get(k, "-")
        k_label = k.replace("_", " ").title()
        bg_cls = "bg-white" if i % 2 == 0 else "bg-slate-50/80"
        
        specs_rows += f"""
        <tr class="{bg_cls} border-b border-lab-border text-xs sm:text-sm">
            <td class="py-3 px-3 sm:px-4 font-semibold text-lab-muted w-1/3 sm:w-1/4">{k_label}</td>
            <td class="py-3 px-3 sm:px-4 text-lab-text font-medium w-1/3 sm:w-auto">{v}</td>
            <td class="py-3 px-3 sm:px-4 text-lab-text font-medium w-1/3 sm:w-auto">{v2}</td>
        </tr>
        """

    pros_a = "".join([f"<li class='flex items-start gap-1.5'><span class='text-emerald-600 font-bold'>✓</span><span>{p}</span></li>" for p in pa["pros"]])
    contras_a = "".join([f"<li class='flex items-start gap-1.5'><span class='text-rose-600 font-bold'>✕</span><span>{c}</span></li>" for c in pa["contras_reais"]])
    pros_b = "".join([f"<li class='flex items-start gap-1.5'><span class='text-emerald-600 font-bold'>✓</span><span>{p}</span></li>" for p in pb["pros"]])
    contras_b = "".join([f"<li class='flex items-start gap-1.5'><span class='text-rose-600 font-bold'>✕</span><span>{c}</span></li>" for c in pb["contras_reais"]])

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{pa['nome']} vs {pb['nome']}: Comparativa y Veredicto Técnico | ShopVS España</title>
    <meta name="description" content="Análisis técnico cara a cara entre {pa['nome']} y {pb['nome']}. Medición de prestaciones, matriz de datos y quejas reales reportadas.">
    {COMMON_HEAD}
</head>
<body class="min-h-screen flex flex-col bg-lab-bg text-lab-text antialiased">
    <!-- Header -->
    <header class="sticky top-0 z-50 bg-white/95 backdrop-blur border-b border-lab-border">
        <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
            <div class="flex items-center gap-3">
                <a href="/es/" class="w-8 h-8 rounded border border-lab-border flex items-center justify-center text-lab-text hover:text-lab-primary hover:border-lab-primary transition-colors">
                    <span class="material-symbols-outlined text-[18px]">arrow_back</span>
                </a>
                <a href="/" class="flex items-center gap-2 text-decoration-none">
                    <span class="font-extrabold text-base tracking-tight text-lab-text">ShopVS EU</span>
                    <span class="text-[10px] bg-blue-50 text-blue-700 px-1.5 py-0.5 rounded font-bold uppercase">España</span>
                </a>
            </div>
            <div class="flex items-center gap-2">
                <div class="flex items-center bg-slate-100 rounded p-0.5 border border-lab-border text-xs font-semibold">
                    <span class="px-2 py-0.5 rounded bg-white text-lab-primary shadow-xs">ES</span>
                    <a href="/de/{artigo['slug_de']}.html" class="px-2 py-0.5 rounded text-lab-muted hover:text-lab-text">DE</a>
                </div>
                <a href="/legal/" class="text-xs font-medium text-lab-muted hover:text-lab-text hidden sm:inline-flex items-center gap-1">
                    <span class="material-symbols-outlined text-[16px]">gavel</span> Aviso Legal
                </a>
            </div>
        </div>
    </header>

    <main class="flex-1 max-w-5xl mx-auto px-4 sm:px-6 py-6 sm:py-10 w-full flex flex-col gap-8">
        <!-- Breadcrumbs & Badge Metodologia -->
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-lab-border pb-4">
            <nav class="flex items-center gap-1.5 text-xs text-lab-muted font-medium uppercase tracking-wider">
                <a href="/" class="hover:text-lab-primary">Inicio</a>
                <span>/</span>
                <a href="/es/" class="hover:text-lab-primary">España</a>
                <span>/</span>
                <span class="text-lab-text font-bold">{artigo['categoria']}</span>
            </nav>
            <div class="inline-flex items-center gap-2 bg-emerald-50 text-emerald-800 border border-emerald-200 px-3 py-1 rounded text-xs font-bold self-start sm:self-auto">
                <span class="material-symbols-outlined text-[16px] text-emerald-600">verified</span>
                Auditoría Técnica Independiente • 45 Variables
            </div>
        </div>

        <!-- Hero Head-to-Head (Desktop Grid / Mobile Stack) -->
        <section class="bg-white border border-lab-border rounded-lg p-5 sm:p-8 shadow-xs">
            <div class="flex items-center justify-between pb-4 border-b border-lab-border mb-6">
                <span class="text-xs font-bold uppercase tracking-wider text-lab-muted">Benchmarking Head-to-Head 2026</span>
                <span class="text-xs font-bold bg-slate-100 text-slate-700 px-2 py-0.5 rounded">Ficha Verificada</span>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-6 relative">
                <!-- Machine 1: De'Longhi -->
                <div class="bg-slate-50/70 border border-lab-border rounded-lg p-5 flex flex-col justify-between">
                    <div>
                        <div class="flex items-center justify-between mb-3">
                            <span class="text-[11px] font-bold uppercase text-lab-primary tracking-wider">{pa['marca']}</span>
                            <span class="bg-emerald-100 text-emerald-800 text-[10px] font-bold px-2 py-0.5 rounded">TESTSIEGER (1.6)</span>
                        </div>
                        <h2 class="text-xl sm:text-2xl font-bold text-lab-text mb-1">{pa['nome']}</h2>
                        <span class="text-xs text-lab-muted font-mono mb-4 block">ASIN: {pa['asin']}</span>
                    </div>
                    <div class="pt-4 border-t border-lab-border/60">
                        <span class="text-xs text-lab-muted font-semibold block mb-1">Destacado de Laboratorio:</span>
                        <p class="text-xs text-lab-text leading-relaxed">Grupo infusor extraíble de limpieza en grifo y molinillo de acero cónico de 13 posiciones.</p>
                    </div>
                </div>

                <!-- Machine 2: Krups -->
                <div class="bg-slate-50/70 border border-lab-border rounded-lg p-5 flex flex-col justify-between">
                    <div>
                        <div class="flex items-center justify-between mb-3">
                            <span class="text-[11px] font-bold uppercase text-slate-600 tracking-wider">{pb['marca']}</span>
                            <span class="bg-slate-200 text-slate-700 text-[10px] font-bold px-2 py-0.5 rounded">BUEN RESULTADO (2.2)</span>
                        </div>
                        <h2 class="text-xl sm:text-2xl font-bold text-lab-text mb-1">{pb['nome']}</h2>
                        <span class="text-xs text-lab-muted font-mono mb-4 block">ASIN: {pb['asin']}</span>
                    </div>
                    <div class="pt-4 border-t border-lab-border/60">
                        <span class="text-xs text-lab-muted font-semibold block mb-1">Destacado de Laboratorio:</span>
                        <p class="text-xs text-lab-text leading-relaxed">Chasis ultra-compacto ideal para cocinas pequeñas y bloque térmico Thermoblock ultra-rápido.</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- Veredicto Rápido (Kurzfazit) -->
        <section class="bg-blue-50/70 border border-blue-200 rounded-lg p-5 sm:p-6">
            <div class="flex items-center gap-2 mb-3">
                <span class="material-symbols-outlined text-blue-700 text-[20px]">bolt</span>
                <h3 class="font-bold text-sm sm:text-base text-blue-900 uppercase tracking-wide">Veredicto Rápido de Nuestros Analistas</h3>
            </div>
            <p class="text-sm sm:text-base text-blue-950 leading-relaxed font-medium">
                {artigo['veredito_resumo']['es']}
            </p>
        </section>

        <!-- Matriz Comparativa de Laboratório -->
        <section class="bg-white border border-lab-border rounded-lg overflow-hidden shadow-xs">
            <div class="p-4 sm:p-5 border-b border-lab-border flex items-center justify-between">
                <div>
                    <h3 class="font-bold text-base sm:text-lg text-lab-text">Matriz Comparativa de Laboratorio</h3>
                    <p class="text-xs text-lab-muted">Gegenüberstellung de parámetros técnicos verificados</p>
                </div>
                <span class="text-xs font-bold text-lab-primary bg-blue-50 px-2.5 py-1 rounded">Especificaciones</span>
            </div>
            <div class="overflow-x-auto">
                <table class="w-full text-left border-collapse">
                    <thead>
                        <tr class="bg-slate-900 text-white text-xs uppercase tracking-wider">
                            <th class="py-3 px-3 sm:px-4 font-bold">Parámetro</th>
                            <th class="py-3 px-3 sm:px-4 font-bold">{pa['nome']}</th>
                            <th class="py-3 px-3 sm:px-4 font-bold">{pb['nome']}</th>
                        </tr>
                    </thead>
                    <tbody>
                        {specs_rows}
                    </tbody>
                </table>
            </div>
        </section>

        <!-- Auditoria de Falhas Reais e Fortalezas -->
        <section class="flex flex-col gap-4">
            <div>
                <h3 class="font-bold text-lg text-lab-text">Auditoría de Fiabilidad y Fallos Crónicos Reportados</h3>
                <p class="text-xs text-lab-muted">Síntesis de quejas reales de usuarios verificados y pruebas continuas de uso</p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <!-- Coluna Produto A -->
                <div class="bg-white border border-lab-border rounded-lg p-5 sm:p-6 flex flex-col justify-between shadow-xs">
                    <div>
                        <h4 class="font-bold text-base text-lab-text mb-3 flex items-center justify-between">
                            <span>{pa['nome']}</span>
                            <span class="text-xs font-mono text-slate-500">{pa['asin']}</span>
                        </h4>
                        
                        <div class="mb-4">
                            <span class="text-xs font-bold text-emerald-800 uppercase tracking-wider block mb-2 flex items-center gap-1">
                                <span class="material-symbols-outlined text-[16px] text-emerald-600">thumb_up</span>
                                Fortalezas de Ingeniería
                            </span>
                            <ul class="text-xs sm:text-sm text-slate-700 space-y-1.5">
                                {pros_a}
                            </ul>
                        </div>

                        <div class="bg-rose-50 border border-rose-200 rounded p-3 mb-5">
                            <span class="text-xs font-bold text-rose-800 uppercase tracking-wider block mb-1.5 flex items-center gap-1">
                                <span class="material-symbols-outlined text-[16px] text-rose-600">warning</span>
                                Quejas Crónicas Reportadas
                            </span>
                            <ul class="text-xs text-rose-900 space-y-1">
                                {contras_a}
                            </ul>
                        </div>
                    </div>

                    <div>
                        <a href="{pa['link_es']}" target="_blank" rel="nofollow noopener sponsored" class="w-full bg-lab-amber hover:bg-amber-700 text-white font-bold text-xs sm:text-sm py-3 px-4 rounded flex items-center justify-between transition-colors shadow-xs">
                            <span>Consultar precio actual y stock en Amazon.es</span>
                            <span class="material-symbols-outlined text-[18px]">arrow_forward</span>
                        </a>
                        <span class="text-[10px] text-slate-500 text-center block mt-1.5">Vendido y enviado por Amazon España</span>
                    </div>
                </div>

                <!-- Coluna Produto B -->
                <div class="bg-white border border-lab-border rounded-lg p-5 sm:p-6 flex flex-col justify-between shadow-xs">
                    <div>
                        <h4 class="font-bold text-base text-lab-text mb-3 flex items-center justify-between">
                            <span>{pb['nome']}</span>
                            <span class="text-xs font-mono text-slate-500">{pb['asin']}</span>
                        </h4>
                        
                        <div class="mb-4">
                            <span class="text-xs font-bold text-emerald-800 uppercase tracking-wider block mb-2 flex items-center gap-1">
                                <span class="material-symbols-outlined text-[16px] text-emerald-600">thumb_up</span>
                                Fortalezas de Ingeniería
                            </span>
                            <ul class="text-xs sm:text-sm text-slate-700 space-y-1.5">
                                {pros_b}
                            </ul>
                        </div>

                        <div class="bg-rose-50 border border-rose-200 rounded p-3 mb-5">
                            <span class="text-xs font-bold text-rose-800 uppercase tracking-wider block mb-1.5 flex items-center gap-1">
                                <span class="material-symbols-outlined text-[16px] text-rose-600">warning</span>
                                Quejas Crónicas Reportadas
                            </span>
                            <ul class="text-xs text-rose-900 space-y-1">
                                {contras_b}
                            </ul>
                        </div>
                    </div>

                    <div>
                        <a href="{pb['link_es']}" target="_blank" rel="nofollow noopener sponsored" class="w-full bg-lab-primary hover:bg-blue-800 text-white font-bold text-xs sm:text-sm py-3 px-4 rounded flex items-center justify-between transition-colors shadow-xs">
                            <span>Consultar precio actual y stock en Amazon.es</span>
                            <span class="material-symbols-outlined text-[18px]">arrow_forward</span>
                        </a>
                        <span class="text-[10px] text-slate-500 text-center block mt-1.5">Vendido y enviado por Amazon España</span>
                    </div>
                </div>
            </div>
        </section>

        <!-- Banner de Transparência -->
        <section class="bg-slate-100/80 border border-lab-border rounded-lg p-4 text-xs text-lab-muted flex items-start gap-3">
            <span class="material-symbols-outlined text-slate-600 text-[20px] shrink-0 mt-0.5">info</span>
            <div>
                <strong class="text-lab-text block mb-0.5">Garantía de Transparencia Editorial</strong>
                Nuestros veredictos se fundamentan en parámetros empíricos. No publicamos precios numéricos fijos en cumplimiento de las directrices de la UE y de la Amazon Associates Operating Agreement, garantizando que el usuario siempre vea la tarifa oficial actualizada en tiempo real.
            </div>
        </section>
    </main>

    <!-- Footer -->
    <footer class="bg-white border-t border-lab-border mt-12 py-8">
        <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 text-xs text-lab-muted flex flex-col sm:flex-row items-center justify-between gap-4">
            <div>&copy; 2026 ShopVS EU • Laboratorio de Análisis Técnico</div>
            <div class="flex items-center gap-4">
                <a href="/es/" class="hover:text-lab-text">Portal España</a>
                <a href="/de/{artigo['slug_de']}.html" class="hover:text-lab-text">Version Deutsch</a>
                <a href="/legal/" class="hover:text-lab-text font-semibold">Impressum (§ 5 TMG)</a>
            </div>
        </div>
    </footer>
</body>
</html>
"""
    file_path = os.path.join(BASE_DIR, "es", f"{artigo['slug_es']}.html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"[OK] Artigo ES gerado com design Stitch responsivo: {file_path}")

def render_article_de(artigo):
    """Renderiza a página de comparativa completa em Alemão (Hochdeutsch) com design Stitch."""
    pa = artigo["produto_a"]
    pb = artigo["produto_b"]

    specs_rows = ""
    for i, (k, v) in enumerate(pa["specs_tecnicas"].items()):
        v2 = pb["specs_tecnicas"].get(k, "-")
        k_label = k.replace("_", " ").title()
        if k == "potencia": k_label = "Leistung"
        elif k == "pressao": k_label = "Pumpendruck"
        elif k == "reservatorio_agua": k_label = "Wassertank"
        elif k == "capacidade_graos": k_label = "Bohnenbehälter"
        elif k == "moedor": k_label = "Mahlwerk"
        elif k == "limpeza_infusor": k_label = "Brühgruppe"
        bg_cls = "bg-white" if i % 2 == 0 else "bg-slate-50/80"

        specs_rows += f"""
        <tr class="{bg_cls} border-b border-lab-border text-xs sm:text-sm">
            <td class="py-3 px-3 sm:px-4 font-semibold text-lab-muted w-1/3 sm:w-1/4">{k_label}</td>
            <td class="py-3 px-3 sm:px-4 text-lab-text font-medium w-1/3 sm:w-auto">{v}</td>
            <td class="py-3 px-3 sm:px-4 text-lab-text font-medium w-1/3 sm:w-auto">{v2}</td>
        </tr>
        """

    pros_a = "".join([f"<li class='flex items-start gap-1.5'><span class='text-emerald-600 font-bold'>✓</span><span>{p}</span></li>" for p in pa["pros"]])
    contras_a = "".join([f"<li class='flex items-start gap-1.5'><span class='text-rose-600 font-bold'>✕</span><span>{c}</span></li>" for c in pa["contras_reais"]])
    pros_b = "".join([f"<li class='flex items-start gap-1.5'><span class='text-emerald-600 font-bold'>✓</span><span>{p}</span></li>" for p in pb["pros"]])
    contras_b = "".join([f"<li class='flex items-start gap-1.5'><span class='text-rose-600 font-bold'>✕</span><span>{c}</span></li>" for c in pb["contras_reais"]])

    html = f"""<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{pa['nome']} vs. {pb['nome']} im Test: Direktvergleich 2026 | ShopVS Deutschland</title>
    <meta name="description" content="Ausführlicher technischer Direktvergleich zwischen {pa['nome']} und {pb['nome']}. Technische Daten, Praxis-Schwachstellen und Kaufempfehlung im Überblick.">
    {COMMON_HEAD}
</head>
<body class="min-h-screen flex flex-col bg-lab-bg text-lab-text antialiased">
    <!-- Header -->
    <header class="sticky top-0 z-50 bg-white/95 backdrop-blur border-b border-lab-border">
        <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
            <div class="flex items-center gap-3">
                <a href="/de/" class="w-8 h-8 rounded border border-lab-border flex items-center justify-center text-lab-text hover:text-lab-primary hover:border-lab-primary transition-colors">
                    <span class="material-symbols-outlined text-[18px]">arrow_back</span>
                </a>
                <a href="/" class="flex items-center gap-2 text-decoration-none">
                    <span class="font-extrabold text-base tracking-tight text-lab-text">ShopVS EU</span>
                    <span class="text-[10px] bg-slate-100 text-slate-800 px-1.5 py-0.5 rounded font-bold uppercase">Deutschland</span>
                </a>
            </div>
            <div class="flex items-center gap-2">
                <div class="flex items-center bg-slate-100 rounded p-0.5 border border-lab-border text-xs font-semibold">
                    <a href="/es/{artigo['slug_es']}.html" class="px-2 py-0.5 rounded text-lab-muted hover:text-lab-text">ES</a>
                    <span class="px-2 py-0.5 rounded bg-white text-lab-primary shadow-xs">DE</span>
                </div>
                <a href="/legal/" class="text-xs font-medium text-lab-muted hover:text-lab-text hidden sm:inline-flex items-center gap-1">
                    <span class="material-symbols-outlined text-[16px]">gavel</span> Impressum (§ 5 TMG)
                </a>
            </div>
        </div>
    </header>

    <main class="flex-1 max-w-5xl mx-auto px-4 sm:px-6 py-6 sm:py-10 w-full flex flex-col gap-8">
        <!-- Breadcrumbs & Badge Metodologia -->
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-lab-border pb-4">
            <nav class="flex items-center gap-1.5 text-xs text-lab-muted font-medium uppercase tracking-wider">
                <a href="/" class="hover:text-lab-primary">Startseite</a>
                <span>/</span>
                <a href="/de/" class="hover:text-lab-primary">Deutschland</a>
                <span>/</span>
                <span class="text-lab-text font-bold">Kaffeevollautomaten</span>
            </nav>
            <div class="inline-flex items-center gap-2 bg-slate-100 text-slate-800 border border-slate-300 px-3 py-1 rounded text-xs font-bold self-start sm:self-auto">
                <span class="material-symbols-outlined text-[16px] text-slate-700">verified</span>
                Unabhängiger Labortest • Prüfstandard 2026
            </div>
        </div>

        <!-- Hero Head-to-Head (Desktop Grid / Mobile Stack) -->
        <section class="bg-white border border-lab-border rounded-lg p-5 sm:p-8 shadow-xs">
            <div class="flex items-center justify-between pb-4 border-b border-lab-border mb-6">
                <span class="text-xs font-bold uppercase tracking-wider text-lab-muted">Technischer Direktvergleich • Praxistest</span>
                <span class="text-xs font-bold bg-slate-100 text-slate-700 px-2 py-0.5 rounded">Geprüftes Datenblatt</span>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-6 relative">
                <!-- Machine 1: De'Longhi -->
                <div class="bg-slate-50/70 border border-lab-border rounded-lg p-5 flex flex-col justify-between">
                    <div>
                        <div class="flex items-center justify-between mb-3">
                            <span class="text-[11px] font-bold uppercase text-lab-primary tracking-wider">{pa['marca']}</span>
                            <span class="bg-emerald-100 text-emerald-800 text-[10px] font-bold px-2 py-0.5 rounded">TESTSIEGER (1.6)</span>
                        </div>
                        <h2 class="text-xl sm:text-2xl font-bold text-lab-text mb-1">{pa['nome']}</h2>
                        <span class="text-xs text-lab-muted font-mono mb-4 block">ASIN: {pa['asin']}</span>
                    </div>
                    <div class="pt-4 border-t border-lab-border/60">
                        <span class="text-xs text-lab-muted font-semibold block mb-1">Labor-Bewertung:</span>
                        <p class="text-xs text-lab-text leading-relaxed">Herausnehmbare Brühgruppe zur leichten Reinigung unter fließendem Wasser und 13-stufiges Edelstahl-Kegelmahlwerk.</p>
                    </div>
                </div>

                <!-- Machine 2: Krups -->
                <div class="bg-slate-50/70 border border-lab-border rounded-lg p-5 flex flex-col justify-between">
                    <div>
                        <div class="flex items-center justify-between mb-3">
                            <span class="text-[11px] font-bold uppercase text-slate-600 tracking-wider">{pb['marca']}</span>
                            <span class="bg-slate-200 text-slate-700 text-[10px] font-bold px-2 py-0.5 rounded">GUT (2.2)</span>
                        </div>
                        <h2 class="text-xl sm:text-2xl font-bold text-lab-text mb-1">{pb['nome']}</h2>
                        <span class="text-xs text-lab-muted font-mono mb-4 block">ASIN: {pb['asin']}</span>
                    </div>
                    <div class="pt-4 border-t border-lab-border/60">
                        <span class="text-xs text-lab-muted font-semibold block mb-1">Labor-Bewertung:</span>
                        <p class="text-xs text-lab-text leading-relaxed">Kompakte Gehäusemaße für kleine Küchenzeilen und schneller Thermoblock-Heizzyklus.</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- Kurzfazit -->
        <section class="bg-slate-100 border border-slate-300 rounded-lg p-5 sm:p-6">
            <div class="flex items-center gap-2 mb-3">
                <span class="material-symbols-outlined text-slate-800 text-[20px]">bolt</span>
                <h3 class="font-bold text-sm sm:text-base text-slate-900 uppercase tracking-wide">Kurzfazit der Testredaktion</h3>
            </div>
            <p class="text-sm sm:text-base text-slate-950 leading-relaxed font-medium">
                {artigo['veredito_resumo']['de']}
            </p>
        </section>

        <!-- Matriz Comparativa Técnica -->
        <section class="bg-white border border-lab-border rounded-lg overflow-hidden shadow-xs">
            <div class="p-4 sm:p-5 border-b border-lab-border flex items-center justify-between">
                <div>
                    <h3 class="font-bold text-base sm:text-lg text-lab-text">Technische Daten im Überblick</h3>
                    <p class="text-xs text-lab-muted">Gegenüberstellung der werkseitigen Messwerte</p>
                </div>
                <span class="text-xs font-bold text-slate-700 bg-slate-100 px-2.5 py-1 rounded">Messmatrix</span>
            </div>
            <div class="overflow-x-auto">
                <table class="w-full text-left border-collapse">
                    <thead>
                        <tr class="bg-slate-900 text-white text-xs uppercase tracking-wider">
                            <th class="py-3 px-3 sm:px-4 font-bold">Kenngröße</th>
                            <th class="py-3 px-3 sm:px-4 font-bold">{pa['nome']}</th>
                            <th class="py-3 px-3 sm:px-4 font-bold">{pb['nome']}</th>
                        </tr>
                    </thead>
                    <tbody>
                        {specs_rows}
                    </tbody>
                </table>
            </div>
        </section>

        <!-- Schwachstellen & Praxistest -->
        <section class="flex flex-col gap-4">
            <div>
                <h3 class="font-bold text-lg text-lab-text">Praxiserfahrungen & Bekannte Schwachstellen</h3>
                <p class="text-xs text-lab-muted">Auswertung verifizierter Kundenrückmeldungen und Langzeittests im DACH-Raum</p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <!-- Coluna Produto A -->
                <div class="bg-white border border-lab-border rounded-lg p-5 sm:p-6 flex flex-col justify-between shadow-xs">
                    <div>
                        <h4 class="font-bold text-base text-lab-text mb-3 flex items-center justify-between">
                            <span>{pa['nome']}</span>
                            <span class="text-xs font-mono text-slate-500">{pa['asin']}</span>
                        </h4>
                        
                        <div class="mb-4">
                            <span class="text-xs font-bold text-emerald-800 uppercase tracking-wider block mb-2 flex items-center gap-1">
                                <span class="material-symbols-outlined text-[16px] text-emerald-600">thumb_up</span>
                                Technische Stärken
                            </span>
                            <ul class="text-xs sm:text-sm text-slate-700 space-y-1.5">
                                {pros_a}
                            </ul>
                        </div>

                        <div class="bg-rose-50 border border-rose-200 rounded p-3 mb-5">
                            <span class="text-xs font-bold text-rose-800 uppercase tracking-wider block mb-1.5 flex items-center gap-1">
                                <span class="material-symbols-outlined text-[16px] text-rose-600">warning</span>
                                Dokumentierte Schwachstellen
                            </span>
                            <ul class="text-xs text-rose-900 space-y-1">
                                {contras_a}
                            </ul>
                        </div>
                    </div>

                    <div>
                        <a href="{pa['link_de']}" target="_blank" rel="nofollow noopener sponsored" class="w-full bg-lab-amber hover:bg-amber-700 text-white font-bold text-xs sm:text-sm py-3 px-4 rounded flex items-center justify-between transition-colors shadow-xs">
                            <span>Aktuellen Preis & Verfügbarkeit auf Amazon.de prüfen</span>
                            <span class="material-symbols-outlined text-[18px]">arrow_forward</span>
                        </a>
                        <span class="text-[10px] text-slate-500 text-center block mt-1.5">Verkauf und Versand durch Amazon Deutschland</span>
                    </div>
                </div>

                <!-- Coluna Produto B -->
                <div class="bg-white border border-lab-border rounded-lg p-5 sm:p-6 flex flex-col justify-between shadow-xs">
                    <div>
                        <h4 class="font-bold text-base text-lab-text mb-3 flex items-center justify-between">
                            <span>{pb['nome']}</span>
                            <span class="text-xs font-mono text-slate-500">{pb['asin']}</span>
                        </h4>
                        
                        <div class="mb-4">
                            <span class="text-xs font-bold text-emerald-800 uppercase tracking-wider block mb-2 flex items-center gap-1">
                                <span class="material-symbols-outlined text-[16px] text-emerald-600">thumb_up</span>
                                Technische Stärken
                            </span>
                            <ul class="text-xs sm:text-sm text-slate-700 space-y-1.5">
                                {pros_b}
                            </ul>
                        </div>

                        <div class="bg-rose-50 border border-rose-200 rounded p-3 mb-5">
                            <span class="text-xs font-bold text-rose-800 uppercase tracking-wider block mb-1.5 flex items-center gap-1">
                                <span class="material-symbols-outlined text-[16px] text-rose-600">warning</span>
                                Dokumentierte Schwachstellen
                            </span>
                            <ul class="text-xs text-rose-900 space-y-1">
                                {contras_b}
                            </ul>
                        </div>
                    </div>

                    <div>
                        <a href="{pb['link_de']}" target="_blank" rel="nofollow noopener sponsored" class="w-full bg-slate-800 hover:bg-slate-900 text-white font-bold text-xs sm:text-sm py-3 px-4 rounded flex items-center justify-between transition-colors shadow-xs">
                            <span>Aktuellen Preis & Verfügbarkeit auf Amazon.de prüfen</span>
                            <span class="material-symbols-outlined text-[18px]">arrow_forward</span>
                        </a>
                        <span class="text-[10px] text-slate-500 text-center block mt-1.5">Verkauf und Versand durch Amazon Deutschland</span>
                    </div>
                </div>
            </div>
        </section>

        <!-- Compliance Hinweis -->
        <section class="bg-slate-100/80 border border-lab-border rounded-lg p-4 text-xs text-lab-muted flex items-start gap-3">
            <span class="material-symbols-outlined text-slate-600 text-[20px] shrink-0 mt-0.5">info</span>
            <div>
                <strong class="text-lab-text block mb-0.5">Transparenzhinweis gemäß § 5 TMG</strong>
                Als Amazon-Partner verdiene ich an qualifizierten Verkäufen. Zur Gewährleistung exakter Angaben zu Lieferzeiten und Händlerangeboten werden keine statischen Europreise abgedruckt. Die Preiskontrolle erfolgt direkt über den jeweiligen Partner-Link.
            </div>
        </section>
    </main>

    <!-- Footer -->
    <footer class="bg-white border-t border-lab-border mt-12 py-8">
        <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 text-xs text-lab-muted flex flex-col sm:flex-row items-center justify-between gap-4">
            <div>&copy; 2026 ShopVS EU • Unabhängige Produktvergleiche</div>
            <div class="flex items-center gap-4">
                <a href="/de/" class="hover:text-lab-text">Portal Deutschland</a>
                <a href="/es/{artigo['slug_es']}.html" class="hover:text-lab-text">Edición España</a>
                <a href="/legal/" class="hover:text-lab-text font-semibold">Impressum & Datenschutz (§ 5 TMG)</a>
            </div>
        </div>
    </footer>
</body>
</html>
"""
    file_path = os.path.join(BASE_DIR, "de", f"{artigo['slug_de']}.html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"[OK] Artigo DE gerado com design Stitch responsivo: {file_path}")

def render_hub_es(artigo):
    """Hub regional Espanha responsivo."""
    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Comparativas Técnicas de Productos | ShopVS España</title>
    {COMMON_HEAD}
</head>
<body class="min-h-screen flex flex-col bg-lab-bg text-lab-text antialiased">
    <header class="sticky top-0 z-50 bg-white/95 backdrop-blur border-b border-lab-border">
        <div class="max-w-6xl mx-auto px-4 sm:px-6 h-16 flex items-center justify-between">
            <a href="/" class="flex items-center gap-2">
                <span class="w-8 h-8 rounded bg-lab-primary text-white flex items-center justify-center font-bold">VS</span>
                <span class="font-bold text-base text-lab-text">ShopVS EU</span>
            </a>
            <div class="flex items-center gap-4 text-xs font-semibold">
                <a href="/" class="text-lab-muted hover:text-lab-text">Inicio</a>
                <a href="/de/" class="text-lab-muted hover:text-lab-text">🇩🇪 Deutschland</a>
                <a href="/legal/" class="text-lab-muted hover:text-lab-text">Aviso Legal</a>
            </div>
        </div>
    </header>

    <main class="flex-1 max-w-5xl mx-auto px-4 sm:px-6 py-8 w-full">
        <div class="mb-8">
            <span class="text-xs font-bold text-lab-primary uppercase tracking-wider">Edición España</span>
            <h1 class="text-2xl sm:text-3xl font-extrabold text-lab-text mt-1 mb-2">Comparativas Técnicas de Consumo</h1>
            <p class="text-sm text-lab-muted">Informes objetivos de laboratorio para decisiones de compra de alto valor.</p>
        </div>

        <div class="grid grid-cols-1 gap-4">
            <a href="/es/{artigo['slug_es']}.html" class="bg-white border border-lab-border hover:border-lab-primary rounded-lg p-5 sm:p-6 transition-all shadow-xs flex flex-col sm:flex-row sm:items-center justify-between gap-4 group">
                <div>
                    <span class="text-xs font-bold text-lab-primary uppercase tracking-wider">{artigo['categoria']}</span>
                    <h2 class="text-lg font-bold text-lab-text group-hover:text-lab-primary transition-colors mt-1 mb-2">{artigo['produto_a']['nome']} vs {artigo['produto_b']['nome']}</h2>
                    <p class="text-xs text-lab-muted max-w-xl">Comparativa de presión real en bares, facilidad de limpieza del grupo de infusión y análisis de fallos reportados en uso diario.</p>
                </div>
                <div class="inline-flex items-center gap-1.5 text-xs font-bold bg-slate-50 group-hover:bg-lab-primary group-hover:text-white px-3.5 py-2 rounded border border-lab-border group-hover:border-lab-primary transition-all self-start sm:self-center shrink-0">
                    <span>Ver informe</span>
                    <span class="material-symbols-outlined text-[16px]">arrow_forward</span>
                </div>
            </a>
        </div>
    </main>

    <footer class="bg-white border-t border-lab-border py-6 mt-12">
        <div class="max-w-6xl mx-auto px-4 text-center text-xs text-lab-muted">
            &copy; 2026 ShopVS EU • <a href="/legal/" class="text-lab-primary hover:underline">Aviso Legal & Privacidad</a>
        </div>
    </footer>
</body>
</html>
"""
    file_path = os.path.join(BASE_DIR, "es", "index.html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"[OK] Hub ES gerado: {file_path}")

def render_hub_de(artigo):
    """Hub regional Alemanha responsivo."""
    html = f"""<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Technische Produkttests & Direktvergleiche | ShopVS Deutschland</title>
    {COMMON_HEAD}
</head>
<body class="min-h-screen flex flex-col bg-lab-bg text-lab-text antialiased">
    <header class="sticky top-0 z-50 bg-white/95 backdrop-blur border-b border-lab-border">
        <div class="max-w-6xl mx-auto px-4 sm:px-6 h-16 flex items-center justify-between">
            <a href="/" class="flex items-center gap-2">
                <span class="w-8 h-8 rounded bg-lab-primary text-white flex items-center justify-center font-bold">VS</span>
                <span class="font-bold text-base text-lab-text">ShopVS EU</span>
            </a>
            <div class="flex items-center gap-4 text-xs font-semibold">
                <a href="/" class="text-lab-muted hover:text-lab-text">Startseite</a>
                <a href="/es/" class="text-lab-muted hover:text-lab-text">🇪🇸 España</a>
                <a href="/legal/" class="text-lab-muted hover:text-lab-text">Impressum</a>
            </div>
        </div>
    </header>

    <main class="flex-1 max-w-5xl mx-auto px-4 sm:px-6 py-8 w-full">
        <div class="mb-8">
            <span class="text-xs font-bold text-slate-800 uppercase tracking-wider">Edition Deutschland</span>
            <h1 class="text-2xl sm:text-3xl font-extrabold text-lab-text mt-1 mb-2">Technische Direktvergleiche & Testberichte</h1>
            <p class="text-sm text-lab-muted">Labor-Gegenüberstellungen und Schwachstellen-Audits für fundierte Kaufentscheidungen.</p>
        </div>

        <div class="grid grid-cols-1 gap-4">
            <a href="/de/{artigo['slug_de']}.html" class="bg-white border border-lab-border hover:border-lab-primary rounded-lg p-5 sm:p-6 transition-all shadow-xs flex flex-col sm:flex-row sm:items-center justify-between gap-4 group">
                <div>
                    <span class="text-xs font-bold text-slate-700 uppercase tracking-wider">{artigo['categoria']}</span>
                    <h2 class="text-lg font-bold text-lab-text group-hover:text-lab-primary transition-colors mt-1 mb-2">{artigo['produto_a']['nome']} vs. {artigo['produto_b']['nome']}</h2>
                    <p class="text-xs text-lab-muted max-w-xl">Prüfung von Brühgruppen-Wartung, Mahlwerk-Lautstärke und echten Kunden-Rückläuferursachen.</p>
                </div>
                <div class="inline-flex items-center gap-1.5 text-xs font-bold bg-slate-50 group-hover:bg-lab-primary group-hover:text-white px-3.5 py-2 rounded border border-lab-border group-hover:border-lab-primary transition-all self-start sm:self-center shrink-0">
                    <span>Testbericht lesen</span>
                    <span class="material-symbols-outlined text-[16px]">arrow_forward</span>
                </div>
            </a>
        </div>
    </main>

    <footer class="bg-white border-t border-lab-border py-6 mt-12">
        <div class="max-w-6xl mx-auto px-4 text-center text-xs text-lab-muted">
            &copy; 2026 ShopVS EU • <a href="/legal/" class="text-slate-800 hover:underline">Impressum & Datenschutzerklärung (§ 5 TMG)</a>
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
    print("\n[OK] Build completo com design Stitch responsivo!")

if __name__ == "__main__":
    build_all()
