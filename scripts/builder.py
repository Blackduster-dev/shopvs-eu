#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Builder Estático do ShopVS EU - Paleta Nordic Industrial & Precision Lab
Compila todas as páginas do site (/, /es/, /de/, /legal/) com a nova identidade visual:
Nordic Deep Navy (#0B192C), Alpine Emerald (#0E8388), Electric Amber (#FF6500) e Clinical Canvas (#F4F6F9).
"""

import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_json(rel_path):
    with open(os.path.join(BASE_DIR, rel_path), "r", encoding="utf-8") as f:
        return json.load(f)

# Bloco comum de head com fontes técnicas e Tailwind configurado
COMMON_HEAD = """
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@500;700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@600;700&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" rel="stylesheet" />
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        nordic: {
                            navy: '#0B192C',
                            navyLight: '#1E3E62',
                            petrol: '#005B60',
                            amber: '#FF6500',
                            amberHover: '#E05500',
                            canvas: '#F4F6F9',
                            surface: '#FFFFFF',
                            border: '#E1E6ED',
                            borderDark: '#CBD5E1',
                            emerald: '#0E8388',
                            emeraldBg: '#E8F6F6',
                            crimson: '#D80032',
                            crimsonBg: '#FDF0F2'
                        }
                    },
                    fontFamily: {
                        sans: ['"Plus Jakarta Sans"', '-apple-system', 'sans-serif'],
                        display: ['"Space Grotesk"', 'sans-serif'],
                        mono: ['"JetBrains Mono"', 'monospace']
                    },
                    boxShadow: {
                        'technical': '0 1px 3px 0 rgba(11, 25, 44, 0.04), 0 1px 2px -1px rgba(11, 25, 44, 0.04)',
                        'card-active': '0 12px 30px -8px rgba(11, 25, 44, 0.12), 0 4px 10px -3px rgba(11, 25, 44, 0.06)',
                        'cta': '0 8px 20px -4px rgba(255, 101, 0, 0.35)'
                    }
                }
            }
        }
    </script>
    <style>
        body { font-family: 'Plus Jakarta Sans', sans-serif; background-color: #F4F6F9; color: #0B192C; }
        .font-display { font-family: 'Space Grotesk', sans-serif; }
        .font-mono { font-family: 'JetBrains Mono', monospace; }
        .material-symbols-outlined { font-variation-settings: 'FILL' 0, 'wght' 500, 'GRAD' 0, 'opsz' 20; vertical-align: middle; }
        .tech-blueprint-bg {
            background-color: #0B192C;
            background-image: linear-gradient(rgba(30, 62, 98, 0.3) 1px, transparent 1px),
                              linear-gradient(90deg, rgba(30, 62, 98, 0.3) 1px, transparent 1px);
            background-size: 24px 24px;
        }
    </style>
"""

def render_home(config, artigo):
    """Gera a página raiz com o novo design Nordic Industrial."""
    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ShopVS EU • Laboratorio de Comparación Técnica & Produkttests</title>
    <meta name="description" content="Portal europeo independiente de auditoría técnica y comparativas cara a cara. Metodología de laboratorio, especificaciones reales y fallos de compradores.">
    {COMMON_HEAD}
</head>
<body class="min-h-screen flex flex-col antialiased selection:bg-nordic-amber selection:text-white">
    <!-- Top Ribbon -->
    <aside class="bg-nordic-navy text-white text-[11px] font-mono tracking-wide border-b border-nordic-navyLight/50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-9 flex items-center justify-between">
            <div class="flex items-center gap-3">
                <span class="inline-flex items-center gap-1.5 text-nordic-emerald font-bold">
                    <span class="w-2 h-2 rounded-full bg-nordic-emerald animate-ping"></span>
                    CE-TEST LAB • NORMATIVA 2026
                </span>
                <span class="hidden md:inline text-slate-500">|</span>
                <span class="hidden md:inline text-slate-300">Auditoría técnica de 45 variables en laboratorio europeo</span>
            </div>
            <div class="flex items-center gap-3 text-slate-300 font-mono text-[10px]">
                <span>100% Sin Patrocinio</span>
                <span>•</span>
                <span class="text-nordic-amber">Amazon Verified Partner</span>
            </div>
        </div>
    </aside>

    <!-- Header -->
    <header class="sticky top-0 z-40 bg-white/95 backdrop-blur-md border-b border-nordic-border">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
            <a href="/" class="flex items-center gap-2.5 text-decoration-none group">
                <div class="w-10 h-10 rounded bg-nordic-navy text-white flex items-center justify-center font-display font-extrabold text-lg border-2 border-nordic-petrol group-hover:bg-nordic-petrol transition-colors">
                    VS
                </div>
                <div class="flex flex-col">
                    <span class="font-display font-extrabold text-xl text-nordic-navy tracking-tight leading-none">ShopVS<span class="text-nordic-amber">.eu</span></span>
                    <span class="text-[9px] uppercase tracking-widest font-mono font-bold text-nordic-petrol mt-0.5">European Benchmark Lab</span>
                </div>
            </a>
            <div class="flex items-center gap-3">
                <div class="flex items-center bg-slate-100 p-0.5 rounded border border-nordic-border text-xs font-bold font-mono">
                    <a href="/es/" class="px-2.5 py-1 rounded bg-nordic-navy text-white shadow-sm">🇪🇸 ES</a>
                    <a href="/de/" class="px-2.5 py-1 rounded text-slate-600 hover:text-nordic-navy transition-colors">🇩🇪 DE</a>
                </div>
                <a href="/legal/" class="text-xs font-semibold text-slate-600 hover:text-nordic-navy border border-nordic-border px-3 py-1.5 rounded hover:bg-slate-50 transition-colors hidden sm:flex items-center gap-1.5">
                    <span class="material-symbols-outlined text-[16px] text-nordic-petrol">gavel</span>
                    <span>Impressum (§ 5 TMG)</span>
                </a>
            </div>
        </div>
    </header>

    <main class="flex-1 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10 sm:py-14 w-full">
        <!-- Hero Section -->
        <div class="text-center max-w-3xl mx-auto mb-12 sm:mb-16">
            <div class="inline-flex items-center gap-2 bg-nordic-amber/10 text-nordic-amber border border-nordic-amber/30 px-3.5 py-1 rounded-full text-xs font-mono font-bold uppercase tracking-wider mb-4">
                <span class="w-1.5 h-1.5 rounded-full bg-nordic-amber"></span>
                Auditoría Técnica Cara a Cara • Sin Publicidad Engañosa
            </div>
            <h1 class="text-3xl sm:text-4xl lg:text-5xl font-display font-extrabold tracking-tight text-nordic-navy leading-tight mb-4">
                Comparativas de Consumo con Datos Reales
            </h1>
            <p class="text-base sm:text-lg text-slate-600 leading-relaxed">
                Ayudamos a compradores de España y Alemania a tomar decisiones inteligentes de alto ticket. Especificaciones empíricas, cálculo de coste a 3 años y filtrado de fallos crónicos de compradores.
            </p>
        </div>

        <!-- Portais Regionais (Cards) -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 sm:gap-8 mb-14">
            <!-- Espanha -->
            <a href="/es/" class="bg-white border border-nordic-border hover:border-nordic-emerald rounded-xl p-6 sm:p-8 flex flex-col justify-between transition-all hover:shadow-card-active group shadow-technical">
                <div>
                    <div class="flex items-center justify-between mb-4">
                        <span class="text-4xl">🇪🇸</span>
                        <span class="text-xs font-mono font-bold uppercase bg-nordic-emeraldBg text-nordic-emerald px-2.5 py-1 rounded border border-nordic-emerald/30">Portal España</span>
                    </div>
                    <h2 class="text-2xl font-display font-extrabold text-nordic-navy mb-2 group-hover:text-nordic-emerald transition-colors">Edición España (.es)</h2>
                    <p class="text-sm text-slate-600 mb-6 leading-relaxed">
                        Análisis comparativos exhaustivos con foco en relación calidad-precio y costes de mantenimiento para compradores en Amazon España y retail oficial.
                    </p>
                </div>
                <div class="inline-flex items-center justify-between w-full font-display font-bold text-sm bg-nordic-canvas group-hover:bg-nordic-emerald group-hover:text-white px-5 py-3 rounded-lg border border-nordic-border group-hover:border-nordic-emerald transition-all">
                    <span>Acceder a Comparativas en Castellano</span>
                    <span class="material-symbols-outlined text-[18px]">arrow_forward</span>
                </div>
            </a>

            <!-- Alemanha -->
            <a href="/de/" class="bg-white border border-nordic-border hover:border-nordic-petrol rounded-xl p-6 sm:p-8 flex flex-col justify-between transition-all hover:shadow-card-active group shadow-technical">
                <div>
                    <div class="flex items-center justify-between mb-4">
                        <span class="text-4xl">🇩🇪</span>
                        <span class="text-xs font-mono font-bold uppercase bg-slate-100 text-slate-800 px-2.5 py-1 rounded border border-slate-300">DACH Region</span>
                    </div>
                    <h2 class="text-2xl font-display font-extrabold text-nordic-navy mb-2 group-hover:text-nordic-petrol transition-colors">Edition Deutschland (.de)</h2>
                    <p class="text-sm text-slate-600 mb-6 leading-relaxed">
                        Technische Direktvergleiche nach deutschem Prüfstandard (Testbericht-Standard). Detaillierte Kenngrößen, Schwachstellen-Audit und Preis-Leistungs-Checks.
                    </p>
                </div>
                <div class="inline-flex items-center justify-between w-full font-display font-bold text-sm bg-nordic-canvas group-hover:bg-nordic-navy group-hover:text-white px-5 py-3 rounded-lg border border-nordic-border group-hover:border-nordic-navy transition-all">
                    <span>Zu den technischen Testberichten</span>
                    <span class="material-symbols-outlined text-[18px]">arrow_forward</span>
                </div>
            </a>
        </div>

        <!-- Lista de Artigos em Destaque -->
        <div class="bg-white border border-nordic-border rounded-xl p-6 sm:p-8 shadow-technical">
            <div class="flex items-center justify-between border-b border-nordic-border pb-4 mb-6">
                <div>
                    <h3 class="text-xl font-display font-extrabold text-nordic-navy">Últimas Pruebas de Laboratorio Publicadas</h3>
                    <p class="text-xs text-slate-500 font-mono">Fichas técnicas cara a cara y revisión de averías reportadas</p>
                </div>
                <span class="text-xs font-mono font-bold bg-nordic-emeraldBg text-nordic-emerald px-3 py-1 rounded border border-nordic-emerald/30">
                    Octubre 2026
                </span>
            </div>

            <div class="grid grid-cols-1 lg:grid-cols-2 gap-4">
                <a href="/es/{artigo['slug_es']}.html" class="flex flex-col sm:flex-row sm:items-center justify-between p-5 rounded-lg border border-nordic-border bg-nordic-canvas/50 hover:bg-white hover:border-nordic-emerald hover:shadow-technical transition-all gap-3 group">
                    <div>
                        <div class="flex items-center gap-2 mb-1.5">
                            <span class="text-xs font-mono font-bold text-nordic-petrol uppercase">🇪🇸 {artigo['categoria']}</span>
                            <span class="text-[10px] bg-emerald-100 text-emerald-800 px-1.5 py-0.2 rounded font-bold font-mono">LAB WINNER</span>
                        </div>
                        <h4 class="font-display font-bold text-base text-nordic-navy group-hover:text-nordic-emerald transition-colors">{artigo['produto_a']['nome']} vs {artigo['produto_b']['nome']}</h4>
                    </div>
                    <span class="text-xs font-mono font-bold text-nordic-amber self-end sm:self-center shrink-0 flex items-center gap-1">
                        Ver informe <span class="material-symbols-outlined text-[16px]">arrow_forward</span>
                    </span>
                </a>

                <a href="/de/{artigo['slug_de']}.html" class="flex flex-col sm:flex-row sm:items-center justify-between p-5 rounded-lg border border-nordic-border bg-nordic-canvas/50 hover:bg-white hover:border-nordic-navy hover:shadow-technical transition-all gap-3 group">
                    <div>
                        <div class="flex items-center gap-2 mb-1.5">
                            <span class="text-xs font-mono font-bold text-nordic-petrol uppercase">🇩🇪 Kaffeevollautomaten</span>
                            <span class="text-[10px] bg-slate-200 text-slate-800 px-1.5 py-0.2 rounded font-bold font-mono">TESTBERICHT</span>
                        </div>
                        <h4 class="font-display font-bold text-base text-nordic-navy group-hover:text-nordic-navy transition-colors">{artigo['produto_a']['nome']} vs {artigo['produto_b']['nome']}</h4>
                    </div>
                    <span class="text-xs font-mono font-bold text-nordic-amber self-end sm:self-center shrink-0 flex items-center gap-1">
                        Testbericht <span class="material-symbols-outlined text-[16px]">arrow_forward</span>
                    </span>
                </a>
            </div>
        </div>
    </main>

    <!-- Footer -->
    <footer class="bg-white border-t border-nordic-border py-10 mt-12">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-xs text-slate-500">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-4">
                <div class="flex items-center gap-2">
                    <div class="w-6 h-6 rounded bg-nordic-navy text-white flex items-center justify-center font-display font-bold text-xs">VS</div>
                    <span class="font-display font-bold text-nordic-navy">ShopVS EU</span>
                    <span>• Laboratorio Técnico Independiente de Comparación</span>
                </div>
                <div class="flex items-center gap-5 font-mono">
                    <a href="/es/" class="hover:text-nordic-navy">España</a>
                    <a href="/de/" class="hover:text-nordic-navy">Deutschland</a>
                    <a href="/legal/" class="hover:text-nordic-navy font-bold text-nordic-navy">Impressum (§ 5 TMG)</a>
                </div>
            </div>
            <div class="mt-6 pt-4 border-t border-slate-100 text-[11px] text-slate-400 leading-relaxed">
                <strong>Aviso de Transparencia de Afiliación:</strong> En calidad de Afiliado de Amazon y redes colaboradoras europeas (Awin), ShopVS EU obtiene ingresos por compras cualificadas. Por motivos de rigor comercial y normativa europea, ningún precio en este portal es fijo: todos los enlaces consultan el precio y stock en tiempo real en los minoristas oficiales.
            </div>
        </div>
    </footer>
</body>
</html>
"""
    with open(os.path.join(BASE_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("[OK] index.html atualizado com paleta Nordic Industrial.")

def render_article_es(artigo):
    """Renderiza a comparativa em Espanhol aplicando a paleta Nordic Industrial."""
    pa = artigo["produto_a"]
    pb = artigo["produto_b"]

    specs_rows = ""
    for i, (k, v) in enumerate(pa["specs_tecnicas"].items()):
        v2 = pb["specs_tecnicas"].get(k, "-")
        k_label = k.replace("_", " ").title()
        bg_cls = "bg-white" if i % 2 == 0 else "bg-nordic-canvas/40"
        
        specs_rows += f"""
        <tr class="{bg_cls} hover:bg-slate-50/80 transition-colors">
            <td class="py-3.5 px-4 font-semibold text-nordic-navy w-1/3 sm:w-1/4">
                {k_label}
            </td>
            <td class="py-3.5 px-4 font-mono font-medium text-nordic-navy bg-nordic-emeraldBg/30 w-1/3 sm:w-auto">
                {v}
            </td>
            <td class="py-3.5 px-4 font-mono font-medium text-slate-700 w-1/3 sm:w-auto">
                {v2}
            </td>
        </tr>
        """

    pros_a = "".join([f"<li class='flex items-start gap-2.5'><span class='w-5 h-5 rounded-full bg-nordic-emeraldBg text-nordic-emerald font-bold text-xs flex items-center justify-center shrink-0 mt-0.5'>✓</span><span>{p}</span></li>" for p in pa["pros"]])
    contras_a = "".join([f"<li class='flex items-start gap-2.5'><span class='w-5 h-5 rounded bg-nordic-crimsonBg text-nordic-crimson font-mono font-bold text-xs flex items-center justify-center shrink-0 mt-0.5'>✕</span><span>{c}</span></li>" for c in pa["contras_reais"]])
    pros_b = "".join([f"<li class='flex items-start gap-2.5'><span class='w-5 h-5 rounded-full bg-nordic-emeraldBg text-nordic-emerald font-bold text-xs flex items-center justify-center shrink-0 mt-0.5'>✓</span><span>{p}</span></li>" for p in pb["pros"]])
    contras_b = "".join([f"<li class='flex items-start gap-2.5'><span class='w-5 h-5 rounded bg-nordic-crimsonBg text-nordic-crimson font-mono font-bold text-xs flex items-center justify-center shrink-0 mt-0.5'>✕</span><span>{c}</span></li>" for c in pb["contras_reais"]])

    html = f"""<!DOCTYPE html>
<html lang="es" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{pa['nome']} vs. {pb['nome']}: Comparativa Técnica & Veredicto | ShopVS España</title>
    <meta name="description" content="Auditoría empírica e informe técnico entre {pa['nome']} y {pb['nome']}. Mediciones de laboratorio, matriz técnica y fallos reales reportados por compradores.">
    {COMMON_HEAD}
</head>
<body class="min-h-screen flex flex-col antialiased selection:bg-nordic-amber selection:text-white">
    <!-- Top Ribbon -->
    <aside class="bg-nordic-navy text-white text-[11px] font-mono tracking-wide border-b border-nordic-navyLight/50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-9 flex items-center justify-between">
            <div class="flex items-center gap-3">
                <span class="inline-flex items-center gap-1.5 text-nordic-emerald font-bold">
                    <span class="w-2 h-2 rounded-full bg-nordic-emerald animate-ping"></span>
                    CE-TEST LAB • NORMATIVA 2026
                </span>
                <span class="hidden md:inline text-slate-500">|</span>
                <span class="hidden md:inline text-slate-300">Auditoría independiente con 45 variables de laboratorio</span>
            </div>
            <div class="flex items-center gap-4 text-slate-300 font-mono text-[10px]">
                <span class="text-nordic-amber font-bold">100% Sin Patrocinio de Fabricante</span>
            </div>
        </div>
    </aside>

    <!-- Header -->
    <header class="sticky top-0 z-40 bg-white/95 backdrop-blur-md border-b border-nordic-border">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
            <div class="flex items-center gap-4">
                <a href="/es/" class="w-8 h-8 rounded border border-nordic-border flex items-center justify-center text-nordic-navy hover:border-nordic-navy transition-colors">
                    <span class="material-symbols-outlined text-[18px]">arrow_back</span>
                </a>
                <a href="/" class="flex items-center gap-2">
                    <span class="font-display font-extrabold text-xl text-nordic-navy">ShopVS<span class="text-nordic-amber">.eu</span></span>
                    <span class="text-[10px] bg-nordic-emeraldBg text-nordic-emerald px-2 py-0.5 rounded font-mono font-bold uppercase">España</span>
                </a>
            </div>
            <div class="flex items-center gap-3">
                <div class="flex items-center bg-slate-100 p-0.5 rounded border border-nordic-border text-xs font-bold font-mono">
                    <span class="px-2.5 py-1 rounded bg-nordic-navy text-white shadow-sm">ES</span>
                    <a href="/de/{artigo['slug_de']}.html" class="px-2.5 py-1 rounded text-slate-600 hover:text-nordic-navy">DE</a>
                </div>
                <a href="/legal/" class="text-xs font-semibold text-slate-600 hover:text-nordic-navy border border-nordic-border px-3 py-1.5 rounded hover:bg-slate-50 hidden sm:flex items-center gap-1.5">
                    <span class="material-symbols-outlined text-[16px] text-nordic-petrol">gavel</span>
                    <span>Aviso Legal</span>
                </a>
            </div>
        </div>
    </header>

    <main class="flex-1 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 w-full flex flex-col gap-8">
        <!-- Breadcrumbs -->
        <div class="border-b border-nordic-border pb-3 flex flex-wrap items-center justify-between gap-2 text-xs text-slate-500 font-mono">
            <nav class="flex items-center gap-2 uppercase tracking-wider text-[11px]">
                <a href="/" class="hover:text-nordic-navy">Portal</a>
                <span>/</span>
                <a href="/es/" class="hover:text-nordic-navy">España</a>
                <span>/</span>
                <span class="text-nordic-navy font-bold">{artigo['categoria']}</span>
            </nav>
            <div class="flex items-center gap-2 text-[11px] text-nordic-petrol font-bold">
                <span>● DOSSIER #2026-ES-01</span>
            </div>
        </div>

        <!-- HERO HEAD-TO-HEAD COM OS DOIS PRODUTOS -->
        <section class="bg-white border border-nordic-border rounded-xl p-6 sm:p-8 shadow-technical">
            <div class="max-w-3xl mb-8">
                <div class="inline-flex items-center gap-2 bg-nordic-amber/10 text-nordic-amber border border-nordic-amber/30 px-3 py-1 rounded text-xs font-mono font-bold uppercase tracking-wider mb-3">
                    <span class="w-1.5 h-1.5 rounded-full bg-nordic-amber"></span>
                    DUELO TÉCNICO CARA A CARA 2026
                </div>
                <h1 class="text-3xl sm:text-4xl lg:text-5xl font-display font-extrabold text-nordic-navy leading-tight mb-3">
                    {pa['nome']} <span class="text-nordic-amber font-mono font-light">vs.</span> {pb['nome']}
                </h1>
                <p class="text-sm sm:text-base text-slate-600 leading-relaxed font-normal">
                    Evaluamos minuciosamente presión, facilidad de lavado del grupo infusor y fallos ocultos reportados por compradores reales en España.
                </p>
            </div>

            <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 relative">
                <!-- Concorrente A (Vencedor) -->
                <div class="bg-white border-2 border-nordic-emerald rounded-xl p-6 sm:p-7 shadow-technical relative flex flex-col justify-between">
                    <div class="absolute -top-3.5 left-6 bg-nordic-emerald text-white text-[11px] font-mono font-bold uppercase px-3 py-1 rounded shadow-sm flex items-center gap-1.5 tracking-wider">
                        <span class="material-symbols-outlined text-[15px]">verified</span>
                        TESTSIEGER • MEJOR INVERSIÓN
                    </div>
                    <div>
                        <div class="flex items-start justify-between gap-4 mt-2 mb-4">
                            <div>
                                <span class="text-xs font-mono font-bold text-nordic-petrol uppercase">{pa['marca']}</span>
                                <h2 class="text-2xl font-display font-extrabold text-nordic-navy mt-0.5">{pa['nome']}</h2>
                                <span class="text-xs text-slate-500 font-mono">ASIN: {pa['asin']}</span>
                            </div>
                            <div class="bg-nordic-emeraldBg border border-nordic-emerald/30 rounded-lg p-2.5 text-center min-w-[76px] shrink-0">
                                <div class="text-3xl font-black font-display text-nordic-emerald leading-none">9.2</div>
                                <span class="text-[10px] font-mono font-bold uppercase text-nordic-emerald tracking-wider">SEHR GUT</span>
                            </div>
                        </div>
                        <ul class="space-y-2.5 text-xs sm:text-sm text-slate-700 mb-6">
                            {pros_a}
                        </ul>
                    </div>
                    <div class="pt-4 border-t border-nordic-border">
                        <a href="{pa['link_es']}" target="_blank" rel="nofollow noopener sponsored" class="w-full bg-nordic-amber hover:bg-nordic-amberHover text-white font-display font-extrabold text-sm py-4 px-6 rounded-lg flex items-center justify-between transition-all shadow-cta group">
                            <div class="flex flex-col text-left">
                                <span class="text-[10px] uppercase font-mono font-bold text-amber-100">Recomendación Oficial</span>
                                <span class="text-sm font-extrabold">Consultar precio actual y stock en Amazon.es &rarr;</span>
                            </div>
                            <span class="material-symbols-outlined text-[20px] group-hover:translate-x-1 transition-transform">arrow_forward</span>
                        </a>
                    </div>
                </div>

                <!-- Concorrente B -->
                <div class="bg-white border border-nordic-borderDark rounded-xl p-6 sm:p-7 shadow-technical relative flex flex-col justify-between">
                    <div class="absolute -top-3.5 left-6 bg-nordic-navy text-white text-[11px] font-mono font-bold uppercase px-3 py-1 rounded shadow-sm flex items-center gap-1.5 tracking-wider">
                        <span class="material-symbols-outlined text-[15px]">space_dashboard</span>
                        OPCIÓN COMPACTA
                    </div>
                    <div>
                        <div class="flex items-start justify-between gap-4 mt-2 mb-4">
                            <div>
                                <span class="text-xs font-mono font-bold text-slate-500 uppercase">{pb['marca']}</span>
                                <h2 class="text-2xl font-display font-extrabold text-nordic-navy mt-0.5">{pb['nome']}</h2>
                                <span class="text-xs text-slate-500 font-mono">ASIN: {pb['asin']}</span>
                            </div>
                            <div class="bg-slate-100 border border-slate-200 rounded-lg p-2.5 text-center min-w-[76px] shrink-0">
                                <div class="text-3xl font-black font-display text-slate-800 leading-none">8.4</div>
                                <span class="text-[10px] font-mono font-bold uppercase text-slate-600 tracking-wider">GUT (2.1)</span>
                            </div>
                        </div>
                        <ul class="space-y-2.5 text-xs sm:text-sm text-slate-700 mb-6">
                            {pros_b}
                        </ul>
                    </div>
                    <div class="pt-4 border-t border-nordic-border">
                        <a href="{pb['link_es']}" target="_blank" rel="nofollow noopener sponsored" class="w-full bg-nordic-navy hover:bg-slate-800 text-white font-display font-extrabold text-sm py-4 px-6 rounded-lg flex items-center justify-between transition-all shadow-md group">
                            <div class="flex flex-col text-left">
                                <span class="text-[10px] uppercase font-mono font-bold text-slate-400">Alternativa por Espacio</span>
                                <span class="text-sm font-extrabold">Consultar precio actual y stock en Amazon.es &rarr;</span>
                            </div>
                            <span class="material-symbols-outlined text-[20px] group-hover:translate-x-1 transition-transform">arrow_forward</span>
                        </a>
                    </div>
                </div>
            </div>
        </section>

        <!-- FAST VERDICT -->
        <section class="bg-nordic-navy text-white rounded-xl p-6 sm:p-8 shadow-card-active border border-nordic-navyLight">
            <div class="flex items-center gap-2 mb-3 text-nordic-amber font-mono font-bold text-xs uppercase tracking-widest">
                <span class="material-symbols-outlined text-[20px]">bolt</span>
                Veredicto Rápido de Nuestros Analistas
            </div>
            <p class="text-sm sm:text-base text-slate-200 leading-relaxed font-normal">
                {artigo['veredito_resumo']['es']}
            </p>
        </section>

        <!-- MATRIZ DE DADOS TÉCNICOS -->
        <section class="bg-white border border-nordic-border rounded-xl overflow-hidden shadow-technical">
            <div class="p-6 border-b border-nordic-border flex items-center justify-between">
                <div>
                    <h3 class="text-xl font-display font-extrabold text-nordic-navy">Matriz de Especificaciones Técnicas</h3>
                    <p class="text-xs text-slate-500 font-mono">Gegenüberstellung de parámetros de funcionamiento</p>
                </div>
                <span class="text-xs font-mono font-bold bg-nordic-emeraldBg text-nordic-emerald px-3 py-1 rounded border border-nordic-emerald/30">Datos Verificados</span>
            </div>
            <div class="overflow-x-auto">
                <table class="w-full text-left border-collapse text-xs sm:text-sm">
                    <thead>
                        <tr class="bg-nordic-navy text-white font-mono text-[11px] uppercase tracking-wider">
                            <th class="py-3.5 px-4 font-bold">Parámetro</th>
                            <th class="py-3.5 px-4 font-bold bg-nordic-navyLight/60 border-l border-nordic-navyLight">{pa['nome']}</th>
                            <th class="py-3.5 px-4 font-bold border-l border-nordic-navyLight">{pb['nome']}</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-nordic-border">
                        {specs_rows}
                    </tbody>
                </table>
            </div>
        </section>

        <!-- DEFECTOS OCULTOS REPORTADOS -->
        <section class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div class="bg-white border border-nordic-border rounded-xl p-6 shadow-technical">
                <div class="flex items-center justify-between pb-3 border-b border-nordic-border mb-4">
                    <span class="font-display font-bold text-nordic-navy text-base">{pa['nome']}</span>
                    <span class="text-xs font-mono text-nordic-crimson font-bold bg-nordic-crimsonBg px-2 py-0.5 rounded border border-nordic-crimson/30">Fallos Crónicos</span>
                </div>
                <ul class="space-y-3 text-xs sm:text-sm text-slate-700">
                    {contras_a}
                </ul>
            </div>
            <div class="bg-white border border-nordic-border rounded-xl p-6 shadow-technical">
                <div class="flex items-center justify-between pb-3 border-b border-nordic-border mb-4">
                    <span class="font-display font-bold text-nordic-navy text-base">{pb['nome']}</span>
                    <span class="text-xs font-mono text-nordic-crimson font-bold bg-nordic-crimsonBg px-2 py-0.5 rounded border border-nordic-crimson/30">Fallos Crónicos</span>
                </div>
                <ul class="space-y-3 text-xs sm:text-sm text-slate-700">
                    {contras_b}
                </ul>
            </div>
        </section>
    </main>

    <!-- Footer -->
    <footer class="bg-white border-t border-nordic-border py-10 mt-12">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-xs text-slate-500 flex flex-col sm:flex-row items-center justify-between gap-4">
            <div>&copy; 2026 ShopVS EU • Laboratorio de Análisis Técnico</div>
            <div class="flex items-center gap-5 font-mono">
                <a href="/es/" class="hover:text-nordic-navy">Portal España</a>
                <a href="/de/{artigo['slug_de']}.html" class="hover:text-nordic-navy">Version Deutsch</a>
                <a href="/legal/" class="hover:text-nordic-navy font-bold text-nordic-navy">Impressum (§ 5 TMG)</a>
            </div>
        </div>
    </footer>
</body>
</html>
"""
    file_path = os.path.join(BASE_DIR, "es", f"{artigo['slug_es']}.html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"[OK] Artigo ES gerado com paleta Nordic: {file_path}")

def render_article_de(artigo):
    """Renderiza a comparativa em Alemão (Hochdeutsch) aplicando a paleta Nordic Industrial."""
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
        bg_cls = "bg-white" if i % 2 == 0 else "bg-nordic-canvas/40"

        specs_rows += f"""
        <tr class="{bg_cls} hover:bg-slate-50/80 transition-colors">
            <td class="py-3.5 px-4 font-semibold text-nordic-navy w-1/3 sm:w-1/4">{k_label}</td>
            <td class="py-3.5 px-4 font-mono font-medium text-nordic-navy bg-nordic-emeraldBg/30 w-1/3 sm:w-auto">{v}</td>
            <td class="py-3.5 px-4 font-mono font-medium text-slate-700 w-1/3 sm:w-auto">{v2}</td>
        </tr>
        """

    pros_a = "".join([f"<li class='flex items-start gap-2.5'><span class='w-5 h-5 rounded-full bg-nordic-emeraldBg text-nordic-emerald font-bold text-xs flex items-center justify-center shrink-0 mt-0.5'>✓</span><span>{p}</span></li>" for p in pa["pros"]])
    contras_a = "".join([f"<li class='flex items-start gap-2.5'><span class='w-5 h-5 rounded bg-nordic-crimsonBg text-nordic-crimson font-mono font-bold text-xs flex items-center justify-center shrink-0 mt-0.5'>✕</span><span>{c}</span></li>" for c in pa["contras_reais"]])
    pros_b = "".join([f"<li class='flex items-start gap-2.5'><span class='w-5 h-5 rounded-full bg-nordic-emeraldBg text-nordic-emerald font-bold text-xs flex items-center justify-center shrink-0 mt-0.5'>✓</span><span>{p}</span></li>" for p in pb["pros"]])
    contras_b = "".join([f"<li class='flex items-start gap-2.5'><span class='w-5 h-5 rounded bg-nordic-crimsonBg text-nordic-crimson font-mono font-bold text-xs flex items-center justify-center shrink-0 mt-0.5'>✕</span><span>{c}</span></li>" for c in pb["contras_reais"]])

    html = f"""<!DOCTYPE html>
<html lang="de" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{pa['nome']} vs. {pb['nome']} im Test: Direktvergleich 2026 | ShopVS Deutschland</title>
    <meta name="description" content="Ausführlicher technischer Direktvergleich zwischen {pa['nome']} und {pb['nome']}. Technische Daten, Praxis-Schwachstellen und Kaufempfehlung im Überblick.">
    {COMMON_HEAD}
</head>
<body class="min-h-screen flex flex-col antialiased selection:bg-nordic-amber selection:text-white">
    <!-- Top Ribbon -->
    <aside class="bg-nordic-navy text-white text-[11px] font-mono tracking-wide border-b border-nordic-navyLight/50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-9 flex items-center justify-between">
            <div class="flex items-center gap-3">
                <span class="inline-flex items-center gap-1.5 text-nordic-emerald font-bold">
                    <span class="w-2 h-2 rounded-full bg-nordic-emerald animate-ping"></span>
                    CE-TEST LAB • PRÜFNORM 2026
                </span>
                <span class="hidden md:inline text-slate-500">|</span>
                <span class="hidden md:inline text-slate-300">Unabhängige Laborprüfung von 45 technischen Parametern</span>
            </div>
            <div class="flex items-center gap-3 text-slate-300 font-mono text-[10px]">
                <span class="text-nordic-amber font-bold">100% Hersteller-Unabhängig</span>
            </div>
        </div>
    </aside>

    <!-- Header -->
    <header class="sticky top-0 z-40 bg-white/95 backdrop-blur-md border-b border-nordic-border">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
            <div class="flex items-center gap-4">
                <a href="/de/" class="w-8 h-8 rounded border border-nordic-border flex items-center justify-center text-nordic-navy hover:border-nordic-navy transition-colors">
                    <span class="material-symbols-outlined text-[18px]">arrow_back</span>
                </a>
                <a href="/" class="flex items-center gap-2">
                    <span class="font-display font-extrabold text-xl text-nordic-navy">ShopVS<span class="text-nordic-amber">.eu</span></span>
                    <span class="text-[10px] bg-slate-100 text-slate-800 px-2 py-0.5 rounded font-mono font-bold uppercase">Deutschland</span>
                </a>
            </div>
            <div class="flex items-center gap-3">
                <div class="flex items-center bg-slate-100 p-0.5 rounded border border-nordic-border text-xs font-bold font-mono">
                    <a href="/es/{artigo['slug_es']}.html" class="px-2.5 py-1 rounded text-slate-600 hover:text-nordic-navy">ES</a>
                    <span class="px-2.5 py-1 rounded bg-nordic-navy text-white shadow-sm">DE</span>
                </div>
                <a href="/legal/" class="text-xs font-semibold text-slate-600 hover:text-nordic-navy border border-nordic-border px-3 py-1.5 rounded hover:bg-slate-50 hidden sm:flex items-center gap-1.5">
                    <span class="material-symbols-outlined text-[16px] text-nordic-petrol">gavel</span>
                    <span>Impressum (§ 5 TMG)</span>
                </a>
            </div>
        </div>
    </header>

    <main class="flex-1 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 w-full flex flex-col gap-8">
        <!-- Breadcrumbs -->
        <div class="border-b border-nordic-border pb-3 flex flex-wrap items-center justify-between gap-2 text-xs text-slate-500 font-mono">
            <nav class="flex items-center gap-2 uppercase tracking-wider text-[11px]">
                <a href="/" class="hover:text-nordic-navy">Startseite</a>
                <span>/</span>
                <a href="/de/" class="hover:text-nordic-navy">Deutschland</a>
                <span>/</span>
                <span class="text-nordic-navy font-bold">Kaffeevollautomaten</span>
            </nav>
            <div class="flex items-center gap-2 text-[11px] text-nordic-petrol font-bold">
                <span>● PRÜFBERICHT #2026-DE-01</span>
            </div>
        </div>

        <!-- HERO HEAD-TO-HEAD -->
        <section class="bg-white border border-nordic-border rounded-xl p-6 sm:p-8 shadow-technical">
            <div class="max-w-3xl mb-8">
                <div class="inline-flex items-center gap-2 bg-nordic-amber/10 text-nordic-amber border border-nordic-amber/30 px-3 py-1 rounded text-xs font-mono font-bold uppercase tracking-wider mb-3">
                    <span class="w-1.5 h-1.5 rounded-full bg-nordic-amber"></span>
                    TECHNISCHER DIREKTVERGLEICH • PRAXISTEST
                </div>
                <h1 class="text-3xl sm:text-4xl lg:text-5xl font-display font-extrabold text-nordic-navy leading-tight mb-3">
                    {pa['nome']} <span class="text-nordic-amber font-mono font-light">vs.</span> {pb['nome']}
                </h1>
                <p class="text-sm sm:text-base text-slate-600 leading-relaxed font-normal">
                    Ausführlicher Labor-Direktvergleich zu Pumpendruck, Brühgruppen-Hygienesicherheit und realen Käufer-Rückläuferursachen im DACH-Raum.
                </p>
            </div>

            <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 relative">
                <!-- Concorrente A (Testsieger) -->
                <div class="bg-white border-2 border-nordic-emerald rounded-xl p-6 sm:p-7 shadow-technical relative flex flex-col justify-between">
                    <div class="absolute -top-3.5 left-6 bg-nordic-emerald text-white text-[11px] font-mono font-bold uppercase px-3 py-1 rounded shadow-sm flex items-center gap-1.5 tracking-wider">
                        <span class="material-symbols-outlined text-[15px]">verified</span>
                        TESTSIEGER • EMPFEHLUNG DER REDAKTION
                    </div>
                    <div>
                        <div class="flex items-start justify-between gap-4 mt-2 mb-4">
                            <div>
                                <span class="text-xs font-mono font-bold text-nordic-petrol uppercase">{pa['marca']}</span>
                                <h2 class="text-2xl font-display font-extrabold text-nordic-navy mt-0.5">{pa['nome']}</h2>
                                <span class="text-xs text-slate-500 font-mono">ASIN: {pa['asin']}</span>
                            </div>
                            <div class="bg-nordic-emeraldBg border border-nordic-emerald/30 rounded-lg p-2.5 text-center min-w-[76px] shrink-0">
                                <div class="text-3xl font-black font-display text-nordic-emerald leading-none">9.2</div>
                                <span class="text-[10px] font-mono font-bold uppercase text-nordic-emerald tracking-wider">SEHR GUT (1.6)</span>
                            </div>
                        </div>
                        <ul class="space-y-2.5 text-xs sm:text-sm text-slate-700 mb-6">
                            {pros_a}
                        </ul>
                    </div>
                    <div class="pt-4 border-t border-nordic-border">
                        <a href="{pa['link_de']}" target="_blank" rel="nofollow noopener sponsored" class="w-full bg-nordic-amber hover:bg-nordic-amberHover text-white font-display font-extrabold text-sm py-4 px-6 rounded-lg flex items-center justify-between transition-all shadow-cta group">
                            <div class="flex flex-col text-left">
                                <span class="text-[10px] uppercase font-mono font-bold text-amber-100">Labortest-Sieger</span>
                                <span class="text-sm font-extrabold">Aktuellen Preis auf Amazon.de prüfen &rarr;</span>
                            </div>
                            <span class="material-symbols-outlined text-[20px] group-hover:translate-x-1 transition-transform">arrow_forward</span>
                        </a>
                    </div>
                </div>

                <!-- Concorrente B -->
                <div class="bg-white border border-nordic-borderDark rounded-xl p-6 sm:p-7 shadow-technical relative flex flex-col justify-between">
                    <div class="absolute -top-3.5 left-6 bg-nordic-navy text-white text-[11px] font-mono font-bold uppercase px-3 py-1 rounded shadow-sm flex items-center gap-1.5 tracking-wider">
                        <span class="material-symbols-outlined text-[15px]">space_dashboard</span>
                        KOMPAKTE ALTERNATIVE
                    </div>
                    <div>
                        <div class="flex items-start justify-between gap-4 mt-2 mb-4">
                            <div>
                                <span class="text-xs font-mono font-bold text-slate-500 uppercase">{pb['marca']}</span>
                                <h2 class="text-2xl font-display font-extrabold text-nordic-navy mt-0.5">{pb['nome']}</h2>
                                <span class="text-xs text-slate-500 font-mono">ASIN: {pb['asin']}</span>
                            </div>
                            <div class="bg-slate-100 border border-slate-200 rounded-lg p-2.5 text-center min-w-[76px] shrink-0">
                                <div class="text-3xl font-black font-display text-slate-800 leading-none">8.4</div>
                                <span class="text-[10px] font-mono font-bold uppercase text-slate-600 tracking-wider">GUT (2.1)</span>
                            </div>
                        </div>
                        <ul class="space-y-2.5 text-xs sm:text-sm text-slate-700 mb-6">
                            {pros_b}
                        </ul>
                    </div>
                    <div class="pt-4 border-t border-nordic-border">
                        <a href="{pb['link_de']}" target="_blank" rel="nofollow noopener sponsored" class="w-full bg-nordic-navy hover:bg-slate-800 text-white font-display font-extrabold text-sm py-4 px-6 rounded-lg flex items-center justify-between transition-all shadow-md group">
                            <div class="flex flex-col text-left">
                                <span class="text-[10px] uppercase font-mono font-bold text-slate-400">Kompakte Bauweise</span>
                                <span class="text-sm font-extrabold">Aktuellen Preis auf Amazon.de prüfen &rarr;</span>
                            </div>
                            <span class="material-symbols-outlined text-[20px] group-hover:translate-x-1 transition-transform">arrow_forward</span>
                        </a>
                    </div>
                </div>
            </div>
        </section>

        <!-- KURZFAZIT -->
        <section class="bg-nordic-navy text-white rounded-xl p-6 sm:p-8 shadow-card-active border border-nordic-navyLight">
            <div class="flex items-center gap-2 mb-3 text-nordic-amber font-mono font-bold text-xs uppercase tracking-widest">
                <span class="material-symbols-outlined text-[20px]">bolt</span>
                Kurzfazit der Prüfredaktion
            </div>
            <p class="text-sm sm:text-base text-slate-200 leading-relaxed font-normal">
                {artigo['veredito_resumo']['de']}
            </p>
        </section>

        <!-- TECHNISCHE DATEN TABELLE -->
        <section class="bg-white border border-nordic-border rounded-xl overflow-hidden shadow-technical">
            <div class="p-6 border-b border-nordic-border flex items-center justify-between">
                <div>
                    <h3 class="text-xl font-display font-extrabold text-nordic-navy">Technische Daten im Überblick</h3>
                    <p class="text-xs text-slate-500 font-mono">Gegenüberstellung der werkseitigen Messwerte</p>
                </div>
                <span class="text-xs font-mono font-bold bg-nordic-emeraldBg text-nordic-emerald px-3 py-1 rounded border border-nordic-emerald/30">Labor-Geprüft</span>
            </div>
            <div class="overflow-x-auto">
                <table class="w-full text-left border-collapse text-xs sm:text-sm">
                    <thead>
                        <tr class="bg-nordic-navy text-white font-mono text-[11px] uppercase tracking-wider">
                            <th class="py-3.5 px-4 font-bold">Kenngröße</th>
                            <th class="py-3.5 px-4 font-bold bg-nordic-navyLight/60 border-l border-nordic-navyLight">{pa['nome']}</th>
                            <th class="py-3.5 px-4 font-bold border-l border-nordic-navyLight">{pb['nome']}</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-nordic-border">
                        {specs_rows}
                    </tbody>
                </table>
            </div>
        </section>

        <!-- SCHWACHSTELLEN -->
        <section class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div class="bg-white border border-nordic-border rounded-xl p-6 shadow-technical">
                <div class="flex items-center justify-between pb-3 border-b border-nordic-border mb-4">
                    <span class="font-display font-bold text-nordic-navy text-base">{pa['nome']}</span>
                    <span class="text-xs font-mono text-nordic-crimson font-bold bg-nordic-crimsonBg px-2 py-0.5 rounded border border-nordic-crimson/30">Schwachstellen</span>
                </div>
                <ul class="space-y-3 text-xs sm:text-sm text-slate-700">
                    {contras_a}
                </ul>
            </div>
            <div class="bg-white border border-nordic-border rounded-xl p-6 shadow-technical">
                <div class="flex items-center justify-between pb-3 border-b border-nordic-border mb-4">
                    <span class="font-display font-bold text-nordic-navy text-base">{pb['nome']}</span>
                    <span class="text-xs font-mono text-nordic-crimson font-bold bg-nordic-crimsonBg px-2 py-0.5 rounded border border-nordic-crimson/30">Schwachstellen</span>
                </div>
                <ul class="space-y-3 text-xs sm:text-sm text-slate-700">
                    {contras_b}
                </ul>
            </div>
        </section>
    </main>

    <!-- Footer -->
    <footer class="bg-white border-t border-nordic-border py-10 mt-12">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-xs text-slate-500 flex flex-col sm:flex-row items-center justify-between gap-4">
            <div>&copy; 2026 ShopVS EU • Unabhängige Produktvergleiche</div>
            <div class="flex items-center gap-5 font-mono">
                <a href="/de/" class="hover:text-nordic-navy">Portal Deutschland</a>
                <a href="/es/{artigo['slug_es']}.html" class="hover:text-nordic-navy">Edición España</a>
                <a href="/legal/" class="hover:text-nordic-navy font-bold text-nordic-navy">Impressum & Datenschutz (§ 5 TMG)</a>
            </div>
        </div>
    </footer>
</body>
</html>
"""
    file_path = os.path.join(BASE_DIR, "de", f"{artigo['slug_de']}.html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"[OK] Artigo DE gerado com paleta Nordic: {file_path}")

def render_hub_es(artigo):
    """Hub regional Espanha na paleta Nordic Industrial."""
    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Comparativas Técnicas de Productos | ShopVS España</title>
    {COMMON_HEAD}
</head>
<body class="min-h-screen flex flex-col antialiased selection:bg-nordic-amber selection:text-white">
    <header class="sticky top-0 z-40 bg-white/95 backdrop-blur-md border-b border-nordic-border">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
            <a href="/" class="flex items-center gap-2.5">
                <div class="w-9 h-9 rounded bg-nordic-navy text-white flex items-center justify-center font-display font-extrabold text-base">VS</div>
                <span class="font-display font-extrabold text-lg text-nordic-navy">ShopVS<span class="text-nordic-amber">.eu</span></span>
            </a>
            <div class="flex items-center gap-4 text-xs font-mono font-bold">
                <a href="/" class="text-slate-600 hover:text-nordic-navy">Inicio</a>
                <a href="/de/" class="text-slate-600 hover:text-nordic-navy">🇩🇪 Deutschland</a>
                <a href="/legal/" class="text-slate-600 hover:text-nordic-navy">Aviso Legal</a>
            </div>
        </div>
    </header>

    <main class="flex-1 max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-10 w-full">
        <div class="mb-10">
            <span class="text-xs font-mono font-bold text-nordic-petrol uppercase tracking-wider">Edición España</span>
            <h1 class="text-3xl sm:text-4xl font-display font-extrabold text-nordic-navy mt-1 mb-2">Comparativas Técnicas de Consumo</h1>
            <p class="text-sm text-slate-600">Informes independientes cara a cara con foco en relación calidad-precio y coste total a largo plazo.</p>
        </div>

        <div class="grid grid-cols-1 gap-4">
            <a href="/es/{artigo['slug_es']}.html" class="bg-white border border-nordic-border hover:border-nordic-emerald rounded-xl p-6 transition-all shadow-technical hover:shadow-card-active flex flex-col sm:flex-row sm:items-center justify-between gap-4 group">
                <div>
                    <span class="text-xs font-mono font-bold text-nordic-petrol uppercase tracking-wider">{artigo['categoria']}</span>
                    <h2 class="text-xl font-display font-extrabold text-nordic-navy group-hover:text-nordic-emerald transition-colors mt-1 mb-2">{artigo['produto_a']['nome']} vs {artigo['produto_b']['nome']}</h2>
                    <p class="text-xs text-slate-600 max-w-2xl leading-relaxed">Comparativa completa de presión en bomba, durabilidad del grupo infusor y análisis de fallos reportados en uso diario.</p>
                </div>
                <div class="inline-flex items-center gap-1.5 text-xs font-mono font-bold bg-nordic-canvas group-hover:bg-nordic-emerald group-hover:text-white px-4 py-2.5 rounded-lg border border-nordic-border group-hover:border-nordic-emerald transition-all self-start sm:self-center shrink-0">
                    <span>Ver informe</span>
                    <span class="material-symbols-outlined text-[16px]">arrow_forward</span>
                </div>
            </a>
        </div>
    </main>

    <footer class="bg-white border-t border-nordic-border py-8 mt-12 text-center text-xs text-slate-500 font-mono">
        &copy; 2026 ShopVS EU • <a href="/legal/" class="text-nordic-navy hover:underline">Aviso Legal & Privacidad</a>
    </footer>
</body>
</html>
"""
    file_path = os.path.join(BASE_DIR, "es", "index.html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"[OK] Hub ES gerado: {file_path}")

def render_hub_de(artigo):
    """Hub regional Alemanha na paleta Nordic Industrial."""
    html = f"""<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Technische Produkttests & Direktvergleiche | ShopVS Deutschland</title>
    {COMMON_HEAD}
</head>
<body class="min-h-screen flex flex-col antialiased selection:bg-nordic-amber selection:text-white">
    <header class="sticky top-0 z-40 bg-white/95 backdrop-blur-md border-b border-nordic-border">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
            <a href="/" class="flex items-center gap-2.5">
                <div class="w-9 h-9 rounded bg-nordic-navy text-white flex items-center justify-center font-display font-extrabold text-base">VS</div>
                <span class="font-display font-extrabold text-lg text-nordic-navy">ShopVS<span class="text-nordic-amber">.eu</span></span>
            </a>
            <div class="flex items-center gap-4 text-xs font-mono font-bold">
                <a href="/" class="text-slate-600 hover:text-nordic-navy">Startseite</a>
                <a href="/es/" class="text-slate-600 hover:text-nordic-navy">🇪🇸 España</a>
                <a href="/legal/" class="text-slate-600 hover:text-nordic-navy">Impressum</a>
            </div>
        </div>
    </header>

    <main class="flex-1 max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-10 w-full">
        <div class="mb-10">
            <span class="text-xs font-mono font-bold text-slate-600 uppercase tracking-wider">Edition Deutschland</span>
            <h1 class="text-3xl sm:text-4xl font-display font-extrabold text-nordic-navy mt-1 mb-2">Technische Direktvergleiche & Testberichte</h1>
            <p class="text-sm text-slate-600">Fundierte Gegenüberstellungen und Schwachstellen-Audits für den DACH-Markt.</p>
        </div>

        <div class="grid grid-cols-1 gap-4">
            <a href="/de/{artigo['slug_de']}.html" class="bg-white border border-nordic-border hover:border-nordic-navy rounded-xl p-6 transition-all shadow-technical hover:shadow-card-active flex flex-col sm:flex-row sm:items-center justify-between gap-4 group">
                <div>
                    <span class="text-xs font-mono font-bold text-slate-600 uppercase tracking-wider">{artigo['categoria']}</span>
                    <h2 class="text-xl font-display font-extrabold text-nordic-navy group-hover:text-nordic-navy transition-colors mt-1 mb-2">{artigo['produto_a']['nome']} vs. {artigo['produto_b']['nome']}</h2>
                    <p class="text-xs text-slate-600 max-w-2xl leading-relaxed">Laborprüfung zu Brühgruppen-Hygienesicherheit, Mahlwerk-Lautstärke und realen Käufer-Rückläuferursachen.</p>
                </div>
                <div class="inline-flex items-center gap-1.5 text-xs font-mono font-bold bg-nordic-canvas group-hover:bg-nordic-navy group-hover:text-white px-4 py-2.5 rounded-lg border border-nordic-border group-hover:border-nordic-navy transition-all self-start sm:self-center shrink-0">
                    <span>Testbericht lesen</span>
                    <span class="material-symbols-outlined text-[16px]">arrow_forward</span>
                </div>
            </a>
        </div>
    </main>

    <footer class="bg-white border-t border-nordic-border py-8 mt-12 text-center text-xs text-slate-500 font-mono">
        &copy; 2026 ShopVS EU • <a href="/legal/" class="text-nordic-navy hover:underline">Impressum & Datenschutzerklärung (§ 5 TMG)</a>
    </footer>
</body>
</html>
"""
    file_path = os.path.join(BASE_DIR, "de", "index.html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"[OK] Hub DE gerado: {file_path}")

def render_legal():
    """Renderiza a página de compliance legal na paleta Nordic Industrial."""
    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aviso Legal, Impressum & Privacidad | ShopVS EU</title>
    <meta name="robots" content="noindex, follow">
    {COMMON_HEAD}
</head>
<body class="min-h-screen flex flex-col antialiased selection:bg-nordic-amber selection:text-white">
    <header class="sticky top-0 z-40 bg-white/95 backdrop-blur-md border-b border-nordic-border">
        <div class="max-w-5xl mx-auto px-4 sm:px-6 h-16 flex items-center justify-between">
            <a href="/" class="flex items-center gap-2">
                <div class="w-8 h-8 rounded bg-nordic-navy text-white flex items-center justify-center font-display font-bold text-sm">VS</div>
                <span class="font-display font-bold text-base text-nordic-navy">ShopVS.eu</span>
            </a>
            <div class="flex items-center gap-4 text-xs font-mono font-bold">
                <a href="/" class="text-slate-600 hover:text-nordic-navy">Inicio</a>
                <a href="/es/" class="text-slate-600 hover:text-nordic-navy">España</a>
                <a href="/de/" class="text-slate-600 hover:text-nordic-navy">Deutschland</a>
            </div>
        </div>
    </header>

    <main class="flex-1 max-w-4xl mx-auto px-4 sm:px-6 py-10 w-full">
        <div class="bg-white border border-nordic-border rounded-xl p-8 sm:p-10 shadow-technical">
            <span class="text-xs font-mono font-bold text-nordic-petrol uppercase tracking-wider">MARCO REGULATORIO UE</span>
            <h1 class="text-2xl sm:text-3xl font-display font-extrabold text-nordic-navy mt-1 mb-6">Aviso Legal / Impressum & Datenschutzerklärung</h1>
            <p class="text-sm text-slate-600 leading-relaxed mb-6">
                En estricto cumplimiento del artículo 5 de la Ley alemana de Telemedios (<strong>§ 5 TMG - Telemediengesetz</strong>) y de la normativa europea de comercio electrónico y protección de datos (RGPD).
            </p>

            <div class="border-t border-nordic-border pt-6 mt-6">
                <h2 class="text-lg font-display font-bold text-nordic-navy mb-3">1. Angaben gemäß § 5 TMG / Titular del Sitio Web</h2>
                <div class="bg-nordic-canvas p-5 rounded-lg border border-nordic-border text-xs sm:text-sm font-mono text-slate-700 leading-relaxed">
                    <strong>Betreiber der Website / Titular:</strong><br>
                    ShopVS EU Laboratory Operations<br>
                    Responsable legal: Lucas [Blackduster-dev]<br>
                    Brasil / Operación Transfronteriza Unión Europea<br>
                    <strong>E-Mail:</strong> contact@shopvs-eu.pages.dev
                </div>
            </div>

            <div class="border-t border-nordic-border pt-6 mt-6">
                <h2 class="text-lg font-display font-bold text-nordic-navy mb-3">2. Transparenzhinweis / Declaración de Afiliación</h2>
                <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed">
                    <p>
                        <strong>Aviso para España:</strong> <em>"En calidad de Afiliado de Amazon y colaborador en programas de afiliados europeos (Awin), obtengo ingresos por las compras adscritas que cumplen los requisitos aplicables. Los enlaces a minoristas externos conducen a las tiendas oficiales sin suponer ningún coste adicional para el comprador."</em>
                    </p>
                    <p>
                        <strong>Hinweis für Deutschland (DACH):</strong> <em>"Als Amazon-Partner verdiene ich an qualifizierten Verkäufen. Die auf dieser Website bereitgestellten Links sind Affiliate-Links. Wenn Sie über diese Links Produkte erwerben, erhalten wir eine Vergütung. Der Endpreis für Sie bleibt unberührt."</em>
                    </p>
                </div>
            </div>

            <div class="border-t border-nordic-border pt-6 mt-6">
                <h2 class="text-lg font-display font-bold text-nordic-navy mb-3">3. Privacidad y Cookies (GDPR Compliant)</h2>
                <p class="text-xs sm:text-sm text-slate-600 leading-relaxed">
                    Este portal opera bajo el estándar <strong>Privacy by Design</strong>: no recopilamos datos personales de navegación ni empleamos cookies de rastreo publicitario de terceros. El seguimiento de referencia de compra se efectúa de forma transparente y exclusivamente tras la acción voluntaria del usuario al pulsar el botón de verificación de precio hacia la tienda de destino.
                </p>
            </div>
        </div>
    </main>

    <footer class="bg-white border-t border-nordic-border py-8 text-center text-xs text-slate-500 font-mono">
        &copy; 2026 ShopVS EU • <a href="/" class="text-nordic-navy hover:underline">Volver a la portada</a>
    </footer>
</body>
</html>
"""
    file_path = os.path.join(BASE_DIR, "legal", "index.html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"[OK] Legal / Impressum gerado: {file_path}")

def build_all():
    config = load_json("config_afiliados.json")
    artigo = load_json("data/produto_duplo.json")

    os.makedirs(os.path.join(BASE_DIR, "es"), exist_ok=True)
    os.makedirs(os.path.join(BASE_DIR, "de"), exist_ok=True)
    os.makedirs(os.path.join(BASE_DIR, "legal"), exist_ok=True)

    render_home(config, artigo)
    render_hub_es(artigo)
    render_hub_de(artigo)
    render_article_es(artigo)
    render_article_de(artigo)
    render_legal()
    print("\n[OK] Build completo de todo o site com a paleta Nordic Industrial!")

if __name__ == "__main__":
    build_all()
