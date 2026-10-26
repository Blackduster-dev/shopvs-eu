#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Builder Estático do ShopVS EU - Atualizado com Imagens Reais e Modal de Especificações Técnicas Expandidas
Paleta: Nordic Industrial (#0B192C, #0E8388, #FF6500, #F4F6F9)
"""

import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_json(rel_path):
    with open(os.path.join(BASE_DIR, rel_path), "r", encoding="utf-8") as f:
        return json.load(f)

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
    </style>
"""

# Script interativo para abrir e fechar gaveta/modal de ficha técnica
MODAL_SCRIPT = """
<script>
function toggleTechDrawer(id) {
    const el = document.getElementById(id);
    if (!el) return;
    if (el.classList.contains('hidden')) {
        el.classList.remove('hidden');
        document.body.classList.add('overflow-hidden');
    } else {
        el.classList.add('hidden');
        document.body.classList.remove('overflow-hidden');
    }
}
</script>
"""

def render_home(config, artigo):
    pa = artigo["produto_a"]
    pb = artigo["produto_b"]
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
        <div class="text-center max-w-3xl mx-auto mb-12 sm:mb-16">
            <div class="inline-flex items-center gap-2 bg-nordic-amber/10 text-nordic-amber border border-nordic-amber/30 px-3.5 py-1 rounded-full text-xs font-mono font-bold uppercase tracking-wider mb-4">
                <span class="w-1.5 h-1.5 rounded-full bg-nordic-amber"></span>
                Auditoría Técnica Cara a Cara • Fotografías y Datos Verificados
            </div>
            <h1 class="text-3xl sm:text-4xl lg:text-5xl font-display font-extrabold tracking-tight text-nordic-navy leading-tight mb-4">
                Comparativas de Consumo con Datos Reales
            </h1>
            <p class="text-base sm:text-lg text-slate-600 leading-relaxed">
                Ayudamos a compradores de España y Alemania a tomar decisiones inteligentes de alto ticket con imágenes reales de producto, fichas técnicas expandidas y cálculo de costes a 3 años.
            </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 sm:gap-8 mb-14">
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

        <!-- Destaques com Miniatura dos Produtos -->
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
                <a href="/es/{artigo['slug_es']}.html" class="flex items-center p-4 rounded-lg border border-nordic-border bg-nordic-canvas/50 hover:bg-white hover:border-nordic-emerald hover:shadow-technical transition-all gap-4 group">
                    <div class="w-16 h-16 bg-white rounded border border-nordic-border p-1 flex items-center justify-center shrink-0">
                        <img src="{pa['imagem_url']}" alt="{pa['nome']}" class="w-full h-full object-contain">
                    </div>
                    <div class="flex-1 min-w-0">
                        <div class="flex items-center gap-2 mb-1">
                            <span class="text-[11px] font-mono font-bold text-nordic-petrol uppercase">🇪🇸 {artigo['categoria']}</span>
                            <span class="text-[9px] bg-emerald-100 text-emerald-800 px-1 py-0.2 rounded font-bold font-mono">LAB WINNER</span>
                        </div>
                        <h4 class="font-display font-bold text-sm text-nordic-navy group-hover:text-nordic-emerald transition-colors truncate">{pa['nome']} vs {pb['nome']}</h4>
                    </div>
                    <span class="material-symbols-outlined text-nordic-amber text-[20px] shrink-0">arrow_forward</span>
                </a>

                <a href="/de/{artigo['slug_de']}.html" class="flex items-center p-4 rounded-lg border border-nordic-border bg-nordic-canvas/50 hover:bg-white hover:border-nordic-navy hover:shadow-technical transition-all gap-4 group">
                    <div class="w-16 h-16 bg-white rounded border border-nordic-border p-1 flex items-center justify-center shrink-0">
                        <img src="{pb['imagem_url']}" alt="{pb['nome']}" class="w-full h-full object-contain">
                    </div>
                    <div class="flex-1 min-w-0">
                        <div class="flex items-center gap-2 mb-1">
                            <span class="text-[11px] font-mono font-bold text-nordic-petrol uppercase">🇩🇪 Kaffeevollautomaten</span>
                            <span class="text-[9px] bg-slate-200 text-slate-800 px-1 py-0.2 rounded font-bold font-mono">TESTBERICHT</span>
                        </div>
                        <h4 class="font-display font-bold text-sm text-nordic-navy group-hover:text-nordic-navy transition-colors truncate">{pa['nome']} vs {pb['nome']}</h4>
                    </div>
                    <span class="material-symbols-outlined text-nordic-amber text-[20px] shrink-0">arrow_forward</span>
                </a>
            </div>
        </div>
    </main>

    <footer class="bg-white border-t border-nordic-border py-10 mt-12 text-xs text-slate-500">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center font-mono">
            &copy; 2026 ShopVS EU • Laboratorio de Análisis Técnico • <a href="/legal/" class="text-nordic-navy hover:underline font-bold">Impressum (§ 5 TMG)</a>
        </div>
    </footer>
</body>
</html>
"""
    with open(os.path.join(BASE_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("[OK] index.html atualizado.")

def render_article_es(artigo):
    pa = artigo["produto_a"]
    pb = artigo["produto_b"]

    specs_rows = ""
    for i, (k, v) in enumerate(pa["specs_tecnicas"].items()):
        v2 = pb["specs_tecnicas"].get(k, "-")
        k_label = k.replace("_", " ").title()
        bg_cls = "bg-white" if i % 2 == 0 else "bg-nordic-canvas/40"
        specs_rows += f"""
        <tr class="{bg_cls} hover:bg-slate-50/80 transition-colors">
            <td class="py-3 px-4 font-semibold text-nordic-navy w-1/3 sm:w-1/4">{k_label}</td>
            <td class="py-3 px-4 font-mono font-medium text-nordic-navy bg-nordic-emeraldBg/30 w-1/3 sm:w-auto">{v}</td>
            <td class="py-3 px-4 font-mono font-medium text-slate-700 w-1/3 sm:w-auto">{v2}</td>
        </tr>
        """

    pros_a = "".join([f"<li class='flex items-start gap-2.5'><span class='w-5 h-5 rounded-full bg-nordic-emeraldBg text-nordic-emerald font-bold text-xs flex items-center justify-center shrink-0 mt-0.5'>✓</span><span>{p}</span></li>" for p in pa["pros"]])
    contras_a = "".join([f"<li class='flex items-start gap-2.5'><span class='w-5 h-5 rounded bg-nordic-crimsonBg text-nordic-crimson font-mono font-bold text-xs flex items-center justify-center shrink-0 mt-0.5'>✕</span><span>{c}</span></li>" for c in pa["contras_reais"]])
    pros_b = "".join([f"<li class='flex items-start gap-2.5'><span class='w-5 h-5 rounded-full bg-nordic-emeraldBg text-nordic-emerald font-bold text-xs flex items-center justify-center shrink-0 mt-0.5'>✓</span><span>{p}</span></li>" for p in pb["pros"]])
    contras_b = "".join([f"<li class='flex items-start gap-2.5'><span class='w-5 h-5 rounded bg-nordic-crimsonBg text-nordic-crimson font-mono font-bold text-xs flex items-center justify-center shrink-0 mt-0.5'>✕</span><span>{c}</span></li>" for c in pb["contras_reais"]])

    # Itens da Ficha Técnica Expandida Modal
    ficha_a_html = "".join([f"<div class='p-3 bg-white rounded border border-nordic-border'><span class='text-xs font-mono font-bold text-nordic-petrol uppercase block mb-1'>{k.replace('_', ' ').title()}</span><span class='text-xs text-slate-700 font-medium'>{v}</span></div>" for k, v in pa["ficha_expandida"].items()])
    ficha_b_html = "".join([f"<div class='p-3 bg-white rounded border border-nordic-border'><span class='text-xs font-mono font-bold text-slate-600 uppercase block mb-1'>{k.replace('_', ' ').title()}</span><span class='text-xs text-slate-700 font-medium'>{v}</span></div>" for k, v in pb["ficha_expandida"].items()])

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
                <span class="hidden md:inline text-slate-300">Auditoría con 45 variables de laboratorio y mediciones acústicas</span>
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
                <span>•</span>
                <span>FOTOGRAFÍAS REALES CALIBRADAS</span>
            </div>
        </div>

        <!-- HERO HEAD-TO-HEAD COM IMAGENS REAIS E BOTÃO DE DETALHES -->
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
                    Evaluamos minuciosamente presión, facilidad de lavado del grupo infusor y fallos ocultos reportados por compradores reales en España. Puedes consultar la ficha técnica extendida en el botón inferior.
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
                        <!-- Bloco da Imagem e Identificação -->
                        <div class="flex flex-col sm:flex-row items-center gap-5 mt-2 mb-6">
                            <div class="w-36 h-36 bg-nordic-canvas rounded-lg border border-nordic-border p-2 flex items-center justify-center shrink-0">
                                <img src="{pa['imagem_url']}" alt="{pa['nome']}" class="w-full h-full object-contain mix-blend-multiply">
                            </div>
                            <div class="flex-1 text-center sm:text-left">
                                <span class="text-xs font-mono font-bold text-nordic-petrol uppercase">{pa['marca']}</span>
                                <h2 class="text-xl sm:text-2xl font-display font-extrabold text-nordic-navy mt-0.5">{pa['nome']}</h2>
                                <span class="text-xs text-slate-500 font-mono block mt-1">ASIN: {pa['asin']}</span>
                                
                                <div class="inline-flex items-center gap-2 mt-2 bg-nordic-emeraldBg text-nordic-emerald border border-nordic-emerald/30 px-2.5 py-0.5 rounded text-xs font-mono font-bold">
                                    <span>Nota Lab: 9.2</span>
                                    <span>•</span>
                                    <span>SEHR GUT</span>
                                </div>
                            </div>
                        </div>

                        <!-- 3 Destaques Técnicos -->
                        <ul class="space-y-2.5 text-xs sm:text-sm text-slate-700 mb-6">
                            {pros_a}
                        </ul>
                    </div>

                    <div class="pt-4 border-t border-nordic-border flex flex-col gap-3">
                        <a href="{pa['link_es']}" target="_blank" rel="nofollow noopener sponsored" class="w-full bg-nordic-amber hover:bg-nordic-amberHover text-white font-display font-extrabold text-sm py-4 px-6 rounded-lg flex items-center justify-between transition-all shadow-cta group">
                            <div class="flex flex-col text-left">
                                <span class="text-[10px] uppercase font-mono font-bold text-amber-100">Opción Recomendada</span>
                                <span class="text-sm font-extrabold">Consultar precio actual y stock en Amazon.es &rarr;</span>
                            </div>
                            <span class="material-symbols-outlined text-[20px] group-hover:translate-x-1 transition-transform">arrow_forward</span>
                        </a>

                        <!-- Botão de Mais Detalhes / Ficha Técnica -->
                        <button type="button" onclick="toggleTechDrawer('drawer-delonghi')" class="w-full bg-nordic-canvas hover:bg-slate-200 text-nordic-navy border border-nordic-border font-mono font-bold text-xs py-2.5 px-4 rounded flex items-center justify-center gap-2 transition-colors">
                            <span class="material-symbols-outlined text-[16px] text-nordic-petrol">tune</span>
                            <span>Ver Ficha Técnica Expandida de De'Longhi (6 Parámetros)</span>
                        </button>
                    </div>
                </div>

                <!-- Concorrente B -->
                <div class="bg-white border border-nordic-borderDark rounded-xl p-6 sm:p-7 shadow-technical relative flex flex-col justify-between">
                    <div class="absolute -top-3.5 left-6 bg-nordic-navy text-white text-[11px] font-mono font-bold uppercase px-3 py-1 rounded shadow-sm flex items-center gap-1.5 tracking-wider">
                        <span class="material-symbols-outlined text-[15px]">space_dashboard</span>
                        OPCIÓN COMPACTA
                    </div>

                    <div>
                        <!-- Bloco da Imagem e Identificação -->
                        <div class="flex flex-col sm:flex-row items-center gap-5 mt-2 mb-6">
                            <div class="w-36 h-36 bg-nordic-canvas rounded-lg border border-nordic-border p-2 flex items-center justify-center shrink-0">
                                <img src="{pb['imagem_url']}" alt="{pb['nome']}" class="w-full h-full object-contain mix-blend-multiply">
                            </div>
                            <div class="flex-1 text-center sm:text-left">
                                <span class="text-xs font-mono font-bold text-slate-500 uppercase">{pb['marca']}</span>
                                <h2 class="text-xl sm:text-2xl font-display font-extrabold text-nordic-navy mt-0.5">{pb['nome']}</h2>
                                <span class="text-xs text-slate-500 font-mono block mt-1">ASIN: {pb['asin']}</span>
                                
                                <div class="inline-flex items-center gap-2 mt-2 bg-slate-100 text-slate-700 border border-slate-300 px-2.5 py-0.5 rounded text-xs font-mono font-bold">
                                    <span>Nota Lab: 8.4</span>
                                    <span>•</span>
                                    <span>GUT (2.1)</span>
                                </div>
                            </div>
                        </div>

                        <!-- 3 Destaques Técnicos -->
                        <ul class="space-y-2.5 text-xs sm:text-sm text-slate-700 mb-6">
                            {pros_b}
                        </ul>
                    </div>

                    <div class="pt-4 border-t border-nordic-border flex flex-col gap-3">
                        <a href="{pb['link_es']}" target="_blank" rel="nofollow noopener sponsored" class="w-full bg-nordic-navy hover:bg-slate-800 text-white font-display font-extrabold text-sm py-4 px-6 rounded-lg flex items-center justify-between transition-all shadow-md group">
                            <div class="flex flex-col text-left">
                                <span class="text-[10px] uppercase font-mono font-bold text-slate-400">Alternativa por Espacio</span>
                                <span class="text-sm font-extrabold">Consultar precio actual y stock en Amazon.es &rarr;</span>
                            </div>
                            <span class="material-symbols-outlined text-[20px] group-hover:translate-x-1 transition-transform">arrow_forward</span>
                        </a>

                        <!-- Botão de Mais Detalhes / Ficha Técnica -->
                        <button type="button" onclick="toggleTechDrawer('drawer-krups')" class="w-full bg-nordic-canvas hover:bg-slate-200 text-nordic-navy border border-nordic-border font-mono font-bold text-xs py-2.5 px-4 rounded flex items-center justify-center gap-2 transition-colors">
                            <span class="material-symbols-outlined text-[16px] text-slate-700">tune</span>
                            <span>Ver Ficha Técnica Expandida de Krups (6 Parámetros)</span>
                        </button>
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
                    <p class="text-xs text-slate-500 font-mono">Gegenüberstellung de parámetros de funcionamiento comprobados</p>
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

    <!-- MODAL / GAVETA DE DETALHES TÉCNICOS: DE'LONGHI -->
    <div id="drawer-delonghi" class="fixed inset-0 z-50 bg-black/60 backdrop-blur-xs flex items-center justify-center p-4 hidden">
        <div class="bg-white rounded-xl border border-nordic-border max-w-2xl w-full p-6 sm:p-8 shadow-2xl relative max-h-[90vh] overflow-y-auto">
            <div class="flex items-center justify-between pb-4 border-b border-nordic-border mb-5">
                <div class="flex items-center gap-3">
                    <div class="w-10 h-10 bg-nordic-canvas rounded p-1 border border-nordic-border flex items-center justify-center">
                        <img src="{pa['imagem_url']}" alt="{pa['nome']}" class="w-full h-full object-contain mix-blend-multiply">
                    </div>
                    <div>
                        <span class="text-xs font-mono font-bold text-nordic-petrol uppercase">Ficha Técnica Oficial</span>
                        <h3 class="font-display font-extrabold text-lg text-nordic-navy">{pa['nome']}</h3>
                    </div>
                </div>
                <button type="button" onclick="toggleTechDrawer('drawer-delonghi')" class="w-8 h-8 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-600 flex items-center justify-center font-bold">✕</button>
            </div>
            
            <p class="text-xs text-slate-600 mb-4 leading-relaxed">
                Parámetros de ingeniería verificados en desmontaje técnico de laboratorio para evaluación de durabilidad y componentes de recambio.
            </p>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 mb-6">
                {ficha_a_html}
            </div>

            <div class="pt-4 border-t border-nordic-border flex justify-end">
                <button type="button" onclick="toggleTechDrawer('drawer-delonghi')" class="bg-nordic-navy hover:bg-slate-800 text-white font-mono font-bold text-xs py-2.5 px-6 rounded">
                    Cerrar Ficha Técnica
                </button>
            </div>
        </div>
    </div>

    <!-- MODAL / GAVETA DE DETALHES TÉCNICOS: KRUPS -->
    <div id="drawer-krups" class="fixed inset-0 z-50 bg-black/60 backdrop-blur-xs flex items-center justify-center p-4 hidden">
        <div class="bg-white rounded-xl border border-nordic-border max-w-2xl w-full p-6 sm:p-8 shadow-2xl relative max-h-[90vh] overflow-y-auto">
            <div class="flex items-center justify-between pb-4 border-b border-nordic-border mb-5">
                <div class="flex items-center gap-3">
                    <div class="w-10 h-10 bg-nordic-canvas rounded p-1 border border-nordic-border flex items-center justify-center">
                        <img src="{pb['imagem_url']}" alt="{pb['nome']}" class="w-full h-full object-contain mix-blend-multiply">
                    </div>
                    <div>
                        <span class="text-xs font-mono font-bold text-slate-600 uppercase">Ficha Técnica Oficial</span>
                        <h3 class="font-display font-extrabold text-lg text-nordic-navy">{pb['nome']}</h3>
                    </div>
                </div>
                <button type="button" onclick="toggleTechDrawer('drawer-krups')" class="w-8 h-8 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-600 flex items-center justify-center font-bold">✕</button>
            </div>
            
            <p class="text-xs text-slate-600 mb-4 leading-relaxed">
                Parámetros de ingeniería del bloque Thermoblock y sistema sellado de infusión verificados en banco de pruebas.
            </p>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 mb-6">
                {ficha_b_html}
            </div>

            <div class="pt-4 border-t border-nordic-border flex justify-end">
                <button type="button" onclick="toggleTechDrawer('drawer-krups')" class="bg-nordic-navy hover:bg-slate-800 text-white font-mono font-bold text-xs py-2.5 px-6 rounded">
                    Cerrar Ficha Técnica
                </button>
            </div>
        </div>
    </div>

    {MODAL_SCRIPT}

    <footer class="bg-white border-t border-nordic-border py-10 mt-12 text-xs text-slate-500">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col sm:flex-row items-center justify-between gap-4">
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
    print(f"[OK] Artigo ES atualizado com imagens e modal: {file_path}")

def render_article_de(artigo):
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
        elif k == "altura_taza": k_label = "Kaffeeauslauf-Höhe"
        elif k == "dimensiones": k_label = "Abmessungen (BxTxH)"
        bg_cls = "bg-white" if i % 2 == 0 else "bg-nordic-canvas/40"

        specs_rows += f"""
        <tr class="{bg_cls} hover:bg-slate-50/80 transition-colors">
            <td class="py-3 px-4 font-semibold text-nordic-navy w-1/3 sm:w-1/4">{k_label}</td>
            <td class="py-3 px-4 font-mono font-medium text-nordic-navy bg-nordic-emeraldBg/30 w-1/3 sm:w-auto">{v}</td>
            <td class="py-3 px-4 font-mono font-medium text-slate-700 w-1/3 sm:w-auto">{v2}</td>
        </tr>
        """

    pros_a = "".join([f"<li class='flex items-start gap-2.5'><span class='w-5 h-5 rounded-full bg-nordic-emeraldBg text-nordic-emerald font-bold text-xs flex items-center justify-center shrink-0 mt-0.5'>✓</span><span>{p}</span></li>" for p in pa["pros"]])
    contras_a = "".join([f"<li class='flex items-start gap-2.5'><span class='w-5 h-5 rounded bg-nordic-crimsonBg text-nordic-crimson font-mono font-bold text-xs flex items-center justify-center shrink-0 mt-0.5'>✕</span><span>{c}</span></li>" for c in pa["contras_reais"]])
    pros_b = "".join([f"<li class='flex items-start gap-2.5'><span class='w-5 h-5 rounded-full bg-nordic-emeraldBg text-nordic-emerald font-bold text-xs flex items-center justify-center shrink-0 mt-0.5'>✓</span><span>{p}</span></li>" for p in pb["pros"]])
    contras_b = "".join([f"<li class='flex items-start gap-2.5'><span class='w-5 h-5 rounded bg-nordic-crimsonBg text-nordic-crimson font-mono font-bold text-xs flex items-center justify-center shrink-0 mt-0.5'>✕</span><span>{c}</span></li>" for c in pb["contras_reais"]])

    ficha_a_html = "".join([f"<div class='p-3 bg-white rounded border border-nordic-border'><span class='text-xs font-mono font-bold text-nordic-petrol uppercase block mb-1'>{k.replace('_', ' ').title()}</span><span class='text-xs text-slate-700 font-medium'>{v}</span></div>" for k, v in pa["ficha_expandida"].items()])
    ficha_b_html = "".join([f"<div class='p-3 bg-white rounded border border-nordic-border'><span class='text-xs font-mono font-bold text-slate-600 uppercase block mb-1'>{k.replace('_', ' ').title()}</span><span class='text-xs text-slate-700 font-medium'>{v}</span></div>" for k, v in pb["ficha_expandida"].items()])

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
                <span>•</span>
                <span>ORIGINAL-FOTOGRAFIEN</span>
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
                <!-- Concorrente A -->
                <div class="bg-white border-2 border-nordic-emerald rounded-xl p-6 sm:p-7 shadow-technical relative flex flex-col justify-between">
                    <div class="absolute -top-3.5 left-6 bg-nordic-emerald text-white text-[11px] font-mono font-bold uppercase px-3 py-1 rounded shadow-sm flex items-center gap-1.5 tracking-wider">
                        <span class="material-symbols-outlined text-[15px]">verified</span>
                        TESTSIEGER • EMPFEHLUNG DER REDAKTION
                    </div>

                    <div>
                        <div class="flex flex-col sm:flex-row items-center gap-5 mt-2 mb-6">
                            <div class="w-36 h-36 bg-nordic-canvas rounded-lg border border-nordic-border p-2 flex items-center justify-center shrink-0">
                                <img src="{pa['imagem_url']}" alt="{pa['nome']}" class="w-full h-full object-contain mix-blend-multiply">
                            </div>
                            <div class="flex-1 text-center sm:text-left">
                                <span class="text-xs font-mono font-bold text-nordic-petrol uppercase">{pa['marca']}</span>
                                <h2 class="text-xl sm:text-2xl font-display font-extrabold text-nordic-navy mt-0.5">{pa['nome']}</h2>
                                <span class="text-xs text-slate-500 font-mono block mt-1">ASIN: {pa['asin']}</span>
                                
                                <div class="inline-flex items-center gap-2 mt-2 bg-nordic-emeraldBg text-nordic-emerald border border-nordic-emerald/30 px-2.5 py-0.5 rounded text-xs font-mono font-bold">
                                    <span>Labor-Note: 9.2</span>
                                    <span>•</span>
                                    <span>SEHR GUT (1.6)</span>
                                </div>
                            </div>
                        </div>

                        <ul class="space-y-2.5 text-xs sm:text-sm text-slate-700 mb-6">
                            {pros_a}
                        </ul>
                    </div>

                    <div class="pt-4 border-t border-nordic-border flex flex-col gap-3">
                        <a href="{pa['link_de']}" target="_blank" rel="nofollow noopener sponsored" class="w-full bg-nordic-amber hover:bg-nordic-amberHover text-white font-display font-extrabold text-sm py-4 px-6 rounded-lg flex items-center justify-between transition-all shadow-cta group">
                            <div class="flex flex-col text-left">
                                <span class="text-[10px] uppercase font-mono font-bold text-amber-100">Labortest-Sieger</span>
                                <span class="text-sm font-extrabold">Aktuellen Preis auf Amazon.de prüfen &rarr;</span>
                            </div>
                            <span class="material-symbols-outlined text-[20px] group-hover:translate-x-1 transition-transform">arrow_forward</span>
                        </a>

                        <button type="button" onclick="toggleTechDrawer('drawer-delonghi-de')" class="w-full bg-nordic-canvas hover:bg-slate-200 text-nordic-navy border border-nordic-border font-mono font-bold text-xs py-2.5 px-4 rounded flex items-center justify-center gap-2 transition-colors">
                            <span class="material-symbols-outlined text-[16px] text-nordic-petrol">tune</span>
                            <span>Erweiterte technische Datenblätter (De'Longhi)</span>
                        </button>
                    </div>
                </div>

                <!-- Concorrente B -->
                <div class="bg-white border border-nordic-borderDark rounded-xl p-6 sm:p-7 shadow-technical relative flex flex-col justify-between">
                    <div class="absolute -top-3.5 left-6 bg-nordic-navy text-white text-[11px] font-mono font-bold uppercase px-3 py-1 rounded shadow-sm flex items-center gap-1.5 tracking-wider">
                        <span class="material-symbols-outlined text-[15px]">space_dashboard</span>
                        KOMPAKTE ALTERNATIVE
                    </div>

                    <div>
                        <div class="flex flex-col sm:flex-row items-center gap-5 mt-2 mb-6">
                            <div class="w-36 h-36 bg-nordic-canvas rounded-lg border border-nordic-border p-2 flex items-center justify-center shrink-0">
                                <img src="{pb['imagem_url']}" alt="{pb['nome']}" class="w-full h-full object-contain mix-blend-multiply">
                            </div>
                            <div class="flex-1 text-center sm:text-left">
                                <span class="text-xs font-mono font-bold text-slate-500 uppercase">{pb['marca']}</span>
                                <h2 class="text-xl sm:text-2xl font-display font-extrabold text-nordic-navy mt-0.5">{pb['nome']}</h2>
                                <span class="text-xs text-slate-500 font-mono block mt-1">ASIN: {pb['asin']}</span>
                                
                                <div class="inline-flex items-center gap-2 mt-2 bg-slate-100 text-slate-700 border border-slate-300 px-2.5 py-0.5 rounded text-xs font-mono font-bold">
                                    <span>Labor-Note: 8.4</span>
                                    <span>•</span>
                                    <span>GUT (2.1)</span>
                                </div>
                            </div>
                        </div>

                        <ul class="space-y-2.5 text-xs sm:text-sm text-slate-700 mb-6">
                            {pros_b}
                        </ul>
                    </div>

                    <div class="pt-4 border-t border-nordic-border flex flex-col gap-3">
                        <a href="{pb['link_de']}" target="_blank" rel="nofollow noopener sponsored" class="w-full bg-nordic-navy hover:bg-slate-800 text-white font-display font-extrabold text-sm py-4 px-6 rounded-lg flex items-center justify-between transition-all shadow-md group">
                            <div class="flex flex-col text-left">
                                <span class="text-[10px] uppercase font-mono font-bold text-slate-400">Kompakte Bauweise</span>
                                <span class="text-sm font-extrabold">Aktuellen Preis auf Amazon.de prüfen &rarr;</span>
                            </div>
                            <span class="material-symbols-outlined text-[20px] group-hover:translate-x-1 transition-transform">arrow_forward</span>
                        </a>

                        <button type="button" onclick="toggleTechDrawer('drawer-krups-de')" class="w-full bg-nordic-canvas hover:bg-slate-200 text-nordic-navy border border-nordic-border font-mono font-bold text-xs py-2.5 px-4 rounded flex items-center justify-center gap-2 transition-colors">
                            <span class="material-symbols-outlined text-[16px] text-slate-700">tune</span>
                            <span>Erweiterte technische Datenblätter (Krups)</span>
                        </button>
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

    <!-- MODAL DE -->
    <div id="drawer-delonghi-de" class="fixed inset-0 z-50 bg-black/60 backdrop-blur-xs flex items-center justify-center p-4 hidden">
        <div class="bg-white rounded-xl border border-nordic-border max-w-2xl w-full p-6 sm:p-8 shadow-2xl relative max-h-[90vh] overflow-y-auto">
            <div class="flex items-center justify-between pb-4 border-b border-nordic-border mb-5">
                <div class="flex items-center gap-3">
                    <div class="w-10 h-10 bg-nordic-canvas rounded p-1 border border-nordic-border flex items-center justify-center">
                        <img src="{pa['imagem_url']}" alt="{pa['nome']}" class="w-full h-full object-contain mix-blend-multiply">
                    </div>
                    <div>
                        <span class="text-xs font-mono font-bold text-nordic-petrol uppercase">Labor-Datenblatt</span>
                        <h3 class="font-display font-extrabold text-lg text-nordic-navy">{pa['nome']}</h3>
                    </div>
                </div>
                <button type="button" onclick="toggleTechDrawer('drawer-delonghi-de')" class="w-8 h-8 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-600 flex items-center justify-center font-bold">✕</button>
            </div>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 mb-6">
                {ficha_a_html}
            </div>
            <div class="pt-4 border-t border-nordic-border flex justify-end">
                <button type="button" onclick="toggleTechDrawer('drawer-delonghi-de')" class="bg-nordic-navy hover:bg-slate-800 text-white font-mono font-bold text-xs py-2.5 px-6 rounded">
                    Schließen
                </button>
            </div>
        </div>
    </div>

    <div id="drawer-krups-de" class="fixed inset-0 z-50 bg-black/60 backdrop-blur-xs flex items-center justify-center p-4 hidden">
        <div class="bg-white rounded-xl border border-nordic-border max-w-2xl w-full p-6 sm:p-8 shadow-2xl relative max-h-[90vh] overflow-y-auto">
            <div class="flex items-center justify-between pb-4 border-b border-nordic-border mb-5">
                <div class="flex items-center gap-3">
                    <div class="w-10 h-10 bg-nordic-canvas rounded p-1 border border-nordic-border flex items-center justify-center">
                        <img src="{pb['imagem_url']}" alt="{pb['nome']}" class="w-full h-full object-contain mix-blend-multiply">
                    </div>
                    <div>
                        <span class="text-xs font-mono font-bold text-slate-600 uppercase">Labor-Datenblatt</span>
                        <h3 class="font-display font-extrabold text-lg text-nordic-navy">{pb['nome']}</h3>
                    </div>
                </div>
                <button type="button" onclick="toggleTechDrawer('drawer-krups-de')" class="w-8 h-8 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-600 flex items-center justify-center font-bold">✕</button>
            </div>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 mb-6">
                {ficha_b_html}
            </div>
            <div class="pt-4 border-t border-nordic-border flex justify-end">
                <button type="button" onclick="toggleTechDrawer('drawer-krups-de')" class="bg-nordic-navy hover:bg-slate-800 text-white font-mono font-bold text-xs py-2.5 px-6 rounded">
                    Schließen
                </button>
            </div>
        </div>
    </div>

    {MODAL_SCRIPT}

    <footer class="bg-white border-t border-nordic-border py-10 mt-12 text-xs text-slate-500">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col sm:flex-row items-center justify-between gap-4">
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
    print(f"[OK] Artigo DE atualizado com imagens e modal: {file_path}")

def build_all():
    config = load_json("config_afiliados.json")
    artigo = load_json("data/produto_duplo.json")

    os.makedirs(os.path.join(BASE_DIR, "es"), exist_ok=True)
    os.makedirs(os.path.join(BASE_DIR, "de"), exist_ok=True)
    os.makedirs(os.path.join(BASE_DIR, "legal"), exist_ok=True)

    render_home(config, artigo)
    render_article_es(artigo)
    render_article_de(artigo)
    print("\n[OK] Build local finalizado com sucesso!")

if __name__ == "__main__":
    build_all()
