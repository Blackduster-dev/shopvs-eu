#!/usr/bin/env python3

# -*- coding: utf-8 -*-

"""

Builder Estático do ShopVS EU (ES + DE)

Preserva o index.html interativo da raiz e compila os artigos técnicos bilíngues.

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



MODAL_SCRIPT = """

<script>

function toggleTechDrawer(id) {

    const el = document.getElementById(id);

    if (!el) return;

    el.classList.toggle('hidden');

    document.body.classList.toggle('overflow-hidden');

}

</script>

"""



def render_article(artigo, lang="es"):

    is_de = (lang == "de")

    pa = artigo["produto_a"]

    pb = artigo["produto_b"]



    specs_a = pa.get("specs_de" if is_de else "specs_es", pa.get("specs_tecnicas", {}))

    specs_b = pb.get("specs_de" if is_de else "specs_es", pb.get("specs_tecnicas", {}))

    ficha_a = pa.get("ficha_expandida_de" if is_de else "ficha_expandida_es", pa.get("ficha_expandida", {}))

    ficha_b = pb.get("ficha_expandida_de" if is_de else "ficha_expandida_es", pb.get("ficha_expandida", {}))

    pros_a_list = pa.get("pros_de" if is_de else "pros_es", pa.get("pros", []))

    pros_b_list = pb.get("pros_de" if is_de else "pros_es", pb.get("pros", []))

    contras_a_list = pa.get("contras_de" if is_de else "contras_es", pa.get("contras_reais", []))

    contras_b_list = pb.get("contras_de" if is_de else "contras_es", pb.get("contras_reais", []))



    link_a = pa["link_de"] if is_de else pa["link_es"]

    link_b = pb["link_de"] if is_de else pb["link_es"]

    categoria = artigo.get("categoria_de" if is_de else "categoria_es", artigo.get("categoria", ""))



    specs_rows = ""

    for i, (k, v) in enumerate(specs_a.items()):

        v2 = specs_b.get(k, "-")

        bg_cls = "bg-white" if i % 2 == 0 else "bg-nordic-canvas/40"

        specs_rows += f"""

        <tr class="{bg_cls} hover:bg-slate-50/80 transition-colors">

            <td class="py-3 px-4 font-semibold text-nordic-navy w-1/3 sm:w-1/4">{k}</td>

            <td class="py-3 px-4 font-mono font-medium text-nordic-navy bg-nordic-emeraldBg/30 w-1/3 sm:w-auto">{v}</td>

            <td class="py-3 px-4 font-mono font-medium text-slate-700 w-1/3 sm:w-auto">{v2}</td>

        </tr>"""



    pros_a = "".join([f"<li class='flex items-start gap-2.5'><span class='w-5 h-5 rounded-full bg-nordic-emeraldBg text-nordic-emerald font-bold text-xs flex items-center justify-center shrink-0 mt-0.5'>✓</span><span>{p}</span></li>" for p in pros_a_list])

    pros_b = "".join([f"<li class='flex items-start gap-2.5'><span class='w-5 h-5 rounded-full bg-nordic-emeraldBg text-nordic-emerald font-bold text-xs flex items-center justify-center shrink-0 mt-0.5'>✓</span><span>{p}</span></li>" for p in pros_b_list])

    contras_a = "".join([f"<li class='flex items-start gap-2.5'><span class='w-5 h-5 rounded bg-nordic-crimsonBg text-nordic-crimson font-mono font-bold text-xs flex items-center justify-center shrink-0 mt-0.5'>✕</span><span>{c}</span></li>" for c in contras_a_list])

    contras_b = "".join([f"<li class='flex items-start gap-2.5'><span class='w-5 h-5 rounded bg-nordic-crimsonBg text-nordic-crimson font-mono font-bold text-xs flex items-center justify-center shrink-0 mt-0.5'>✕</span><span>{c}</span></li>" for c in contras_b_list])



    ficha_a_html = "".join([f"<div class='p-3 bg-white rounded border border-nordic-border'><span class='text-xs font-mono font-bold text-nordic-petrol uppercase block mb-1'>{k}</span><span class='text-xs text-slate-700 font-medium'>{v}</span></div>" for k, v in ficha_a.items()])

    ficha_b_html = "".join([f"<div class='p-3 bg-white rounded border border-nordic-border'><span class='text-xs font-mono font-bold text-slate-600 uppercase block mb-1'>{k}</span><span class='text-xs text-slate-700 font-medium'>{v}</span></div>" for k, v in ficha_b.items()])



    # Textos do template por idioma

    if is_de:

        title = f"{pa['nome']} vs. {pb['nome']} im Test: Direktvergleich 2026 | ShopVS Deutschland"

        desc = f"Technischer Direktvergleich zwischen {pa['nome']} und {pb['nome']}. Messwerte, Labor-Audit und Praxistest."

        legal_notice = '<strong>Transparenzhinweis:</strong> Als Amazon-Partner verdiene ich an qualifizierten Verkäufen. Preise werden dynamisch beim Händler geprüft.'

        cta_a = "Aktuellen Preis auf Amazon.de prüfen &rarr;"

        cta_b = "Aktuellen Preis auf Amazon.de prüfen &rarr;"

        btn_ficha = "Erweiterte technische Datenblätter öffnen"

        verdict_title = "Kurzfazit der Prüfredaktion"

        table_title = "Technische Daten im Direktvergleich"

        flaws_badge = "Bekannte Schwachstellen"

        compare_tool_text = "Im interaktiven Vergleichstool öffnen"

    else:

        title = f"{pa['nome']} vs. {pb['nome']}: Comparativa Técnica 2026 | ShopVS España"

        desc = f"Auditoría técnica entre {pa['nome']} y {pb['nome']}. Mediciones en laboratorio, comparativa a fondo y opiniones reales."

        legal_notice = '<strong>Aviso de Afiliación:</strong> En calidad de Afiliado de Amazon, obtengo ingresos por las compras adscritas que cumplen los requisitos aplicables.'

        cta_a = "Consultar precio actual y stock en Amazon.es &rarr;"

        cta_b = "Consultar precio actual y stock en Amazon.es &rarr;"

        btn_ficha = "Ver Ficha Técnica Expandida (6 Parámetros)"

        verdict_title = "Veredicto Rápido de Nuestros Ingenieros"

        table_title = "Matriz de Especificaciones Técnicas"

        flaws_badge = "Fallos Crónicos Reportados"

        compare_tool_text = "Abrir en el Comparador Interactivo"



    other_url = f"/es/{artigo['slug_es']}.html" if is_de else f"/de/{artigo['slug_de']}.html"
    th_param = "Kenngröße" if is_de else "Parámetro"
    score_label_pa = pa.get(f"score_label_{lang}", pa.get("score_label", ""))
    score_label_pb = pb.get(f"score_label_{lang}", pb.get("score_label", ""))
    cat_id = artigo.get("categoria_id") or pa.get("categoria_id", "cafeteras")



    html = f"""<!DOCTYPE html>

<html lang="{lang}" class="scroll-smooth">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>{title}</title>

    <meta name="description" content="{desc}">

    {COMMON_HEAD}

</head>

<body class="min-h-screen flex flex-col antialiased selection:bg-nordic-amber selection:text-white">

    <aside class="bg-nordic-navy text-white text-[11px] font-mono tracking-wide border-b border-nordic-navyLight/50">

        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-2 flex flex-wrap items-center justify-between gap-2">

            <span class="text-slate-300">{legal_notice}</span>

            <a href="/compare/?cat={cat_id}&a={pa['id']}&b={pb['id']}&lang={lang}" class="text-nordic-amber font-bold hover:underline">{compare_tool_text} &rarr;</a>

        </div>

    </aside>



    <header class="sticky top-0 z-40 bg-white/95 backdrop-blur-md border-b border-nordic-border">

        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">

            <div class="flex items-center gap-4">

                <a href="/?lang={lang}" class="w-8 h-8 rounded border border-nordic-border flex items-center justify-center text-nordic-navy hover:border-nordic-navy transition-colors">

                    <span class="material-symbols-outlined text-[18px]">arrow_back</span>

                </a>

                <a href="/" class="flex items-center gap-2">

                    <span class="font-display font-extrabold text-xl text-nordic-navy">ShopVS<span class="text-nordic-amber">.eu</span></span>

                    <span class="text-[10px] bg-nordic-emeraldBg text-nordic-emerald px-2 py-0.5 rounded font-mono font-bold uppercase">{lang.upper()}</span>

                </a>

            </div>

            <div class="flex items-center gap-3">

                <div class="flex items-center bg-slate-100 p-0.5 rounded border border-nordic-border text-xs font-bold font-mono">

                    <a href="/es/{artigo['slug_es']}.html" class="px-2.5 py-1 rounded {'bg-nordic-navy text-white shadow-sm' if not is_de else 'text-slate-600'}">🇪🇸 ES</a>

                    <a href="/de/{artigo['slug_de']}.html" class="px-2.5 py-1 rounded {'bg-nordic-navy text-white shadow-sm' if is_de else 'text-slate-600'}">🇩🇪 DE</a>

                </div>

                <a href="/legal/" class="text-xs font-semibold text-slate-600 hover:text-nordic-navy border border-nordic-border px-3 py-1.5 rounded hover:bg-slate-50 hidden sm:flex items-center gap-1.5">

                    <span class="material-symbols-outlined text-[16px] text-nordic-petrol">gavel</span>

                    <span>Impressum (§ 5 TMG)</span>

                </a>

            </div>

        </div>

    </header>



    <main class="flex-1 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 w-full flex flex-col gap-8">

        <section class="bg-white border border-nordic-border rounded-xl p-6 sm:p-8 shadow-technical">

            <div class="max-w-3xl mb-8">

                <span class="text-xs font-mono font-bold text-nordic-petrol uppercase">{categoria}</span>

                <h1 class="text-3xl sm:text-4xl lg:text-5xl font-display font-extrabold text-nordic-navy leading-tight mt-1 mb-3">

                    {pa['nome']} <span class="text-nordic-amber font-mono font-light">vs.</span> {pb['nome']}

                </h1>

            </div>



            <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">

                <div class="bg-white border-2 border-nordic-emerald rounded-xl p-6 sm:p-7 shadow-technical relative flex flex-col justify-between">

                    <div class="absolute -top-3.5 left-6 bg-nordic-emerald text-white text-[11px] font-mono font-bold uppercase px-3 py-1 rounded shadow-sm">

                        ★ {score_label_pa}

                    </div>

                    <div>

                        <div class="flex flex-col sm:flex-row items-center gap-5 mt-2 mb-6">

                            <div class="w-36 h-36 bg-white rounded-lg border border-nordic-border p-2 flex items-center justify-center shrink-0 shadow-sm">
                                <img src="{pa['imagem_url']}" alt="{pa['nome']}" class="w-full h-full object-contain mix-blend-multiply">
                            </div>

                            <div class="flex-1 text-center sm:text-left">

                                <span class="text-xs font-mono font-bold text-nordic-petrol uppercase">{pa['marca']}</span>

                                <h2 class="text-xl sm:text-2xl font-display font-extrabold text-nordic-navy mt-0.5">{pa['nome']}</h2>

                                <span class="text-xs text-slate-500 font-mono block mt-1">ASIN: {pa['asin']} • Score: {pa['score_lab']}/10</span>

                            </div>

                        </div>

                        <ul class="space-y-2.5 text-xs sm:text-sm text-slate-700 mb-6">{pros_a}</ul>

                    </div>

                    <div class="pt-4 border-t border-nordic-border flex flex-col gap-3">

                        <a href="{link_a}" target="_blank" rel="nofollow noopener sponsored" class="w-full bg-nordic-amber hover:bg-nordic-amberHover text-white font-display font-extrabold text-sm py-4 px-6 rounded-lg flex items-center justify-between transition-all shadow-cta">

                            <span>{cta_a}</span>

                            <span class="material-symbols-outlined text-[20px]">shopping_cart</span>

                        </a>

                        <button type="button" onclick="toggleTechDrawer('drawer-a')" class="w-full bg-nordic-canvas hover:bg-slate-200 text-nordic-navy border border-nordic-border font-mono font-bold text-xs py-2.5 px-4 rounded">

                            {btn_ficha}

                        </button>

                    </div>

                </div>



                <div class="bg-white border border-nordic-borderDark rounded-xl p-6 sm:p-7 shadow-technical relative flex flex-col justify-between">

                    <div class="absolute -top-3.5 left-6 bg-nordic-navy text-white text-[11px] font-mono font-bold uppercase px-3 py-1 rounded shadow-sm">

                        {score_label_pb}

                    </div>

                    <div>

                        <div class="flex flex-col sm:flex-row items-center gap-5 mt-2 mb-6">

                            <div class="w-36 h-36 bg-white rounded-lg border border-nordic-border p-2 flex items-center justify-center shrink-0 shadow-sm">
                                <img src="{pb['imagem_url']}" alt="{pb['nome']}" class="w-full h-full object-contain mix-blend-multiply">
                            </div>

                            <div class="flex-1 text-center sm:text-left">

                                <span class="text-xs font-mono font-bold text-slate-500 uppercase">{pb['marca']}</span>

                                <h2 class="text-xl sm:text-2xl font-display font-extrabold text-nordic-navy mt-0.5">{pb['nome']}</h2>

                                <span class="text-xs text-slate-500 font-mono block mt-1">ASIN: {pb['asin']} • Score: {pb['score_lab']}/10</span>

                            </div>

                        </div>

                        <ul class="space-y-2.5 text-xs sm:text-sm text-slate-700 mb-6">{pros_b}</ul>

                    </div>

                    <div class="pt-4 border-t border-nordic-border flex flex-col gap-3">

                        <a href="{link_b}" target="_blank" rel="nofollow noopener sponsored" class="w-full bg-nordic-navy hover:bg-slate-800 text-white font-display font-extrabold text-sm py-4 px-6 rounded-lg flex items-center justify-between transition-all shadow-md">

                            <span>{cta_b}</span>

                            <span class="material-symbols-outlined text-[20px]">shopping_cart</span>

                        </a>

                        <button type="button" onclick="toggleTechDrawer('drawer-b')" class="w-full bg-nordic-canvas hover:bg-slate-200 text-nordic-navy border border-nordic-border font-mono font-bold text-xs py-2.5 px-4 rounded">

                            {btn_ficha}

                        </button>

                    </div>

                </div>

            </div>

        </section>



        <section class="bg-nordic-navy text-white rounded-xl p-6 sm:p-8 shadow-card-active border border-nordic-navyLight">

            <div class="flex items-center gap-2 mb-3 text-nordic-amber font-mono font-bold text-xs uppercase tracking-widest">

                <span class="material-symbols-outlined text-[20px]">bolt</span>

                {verdict_title}

            </div>

            <p class="text-sm sm:text-base text-slate-200 leading-relaxed">{artigo['veredito_resumo'][lang]}</p>

        </section>



        <section class="bg-white border border-nordic-border rounded-xl overflow-hidden shadow-technical">

            <div class="p-6 border-b border-nordic-border">

                <h3 class="text-xl font-display font-extrabold text-nordic-navy">{table_title}</h3>

            </div>

            <div class="overflow-x-auto">

                <table class="w-full text-left border-collapse text-xs sm:text-sm">

                    <thead>

                        <tr class="bg-nordic-navy text-white font-mono text-[11px] uppercase tracking-wider">

                            <th class="py-3.5 px-4 font-bold">{th_param}</th>

                            <th class="py-3.5 px-4 font-bold bg-nordic-navyLight/60 border-l border-nordic-navyLight">{pa['nome']}</th>

                            <th class="py-3.5 px-4 font-bold border-l border-nordic-navyLight">{pb['nome']}</th>

                        </tr>

                    </thead>

                    <tbody class="divide-y divide-nordic-border">{specs_rows}</tbody>

                </table>

            </div>

        </section>



        <section class="grid grid-cols-1 md:grid-cols-2 gap-6">

            <div class="bg-white border border-nordic-border rounded-xl p-6 shadow-technical">

                <div class="flex items-center justify-between pb-3 border-b border-nordic-border mb-4">

                    <span class="font-display font-bold text-nordic-navy text-base">{pa['nome']}</span>

                    <span class="text-xs font-mono text-nordic-crimson font-bold bg-nordic-crimsonBg px-2 py-0.5 rounded">{flaws_badge}</span>

                </div>

                <ul class="space-y-3 text-xs sm:text-sm text-slate-700">{contras_a}</ul>

            </div>

            <div class="bg-white border border-nordic-border rounded-xl p-6 shadow-technical">

                <div class="flex items-center justify-between pb-3 border-b border-nordic-border mb-4">

                    <span class="font-display font-bold text-nordic-navy text-base">{pb['nome']}</span>

                    <span class="text-xs font-mono text-nordic-crimson font-bold bg-nordic-crimsonBg px-2 py-0.5 rounded">{flaws_badge}</span>

                </div>

                <ul class="space-y-3 text-xs sm:text-sm text-slate-700">{contras_b}</ul>

            </div>

        </section>

    </main>



    <div id="drawer-a" class="fixed inset-0 z-50 bg-black/60 flex items-center justify-center p-4 hidden">

        <div class="bg-white rounded-xl border border-nordic-border max-w-2xl w-full p-6 sm:p-8 shadow-2xl">

            <div class="flex items-center justify-between pb-4 border-b border-nordic-border mb-5">

                <h3 class="font-display font-extrabold text-lg text-nordic-navy">{pa['nome']}</h3>

                <button type="button" onclick="toggleTechDrawer('drawer-a')" class="w-8 h-8 rounded-full bg-slate-100 font-bold">✕</button>

            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 mb-6">{ficha_a_html}</div>

        </div>

    </div>



    <div id="drawer-b" class="fixed inset-0 z-50 bg-black/60 flex items-center justify-center p-4 hidden">

        <div class="bg-white rounded-xl border border-nordic-border max-w-2xl w-full p-6 sm:p-8 shadow-2xl">

            <div class="flex items-center justify-between pb-4 border-b border-nordic-border mb-5">

                <h3 class="font-display font-extrabold text-lg text-nordic-navy">{pb['nome']}</h3>

                <button type="button" onclick="toggleTechDrawer('drawer-b')" class="w-8 h-8 rounded-full bg-slate-100 font-bold">✕</button>

            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 mb-6">{ficha_b_html}</div>

        </div>

    </div>



    {MODAL_SCRIPT}



    <footer class="bg-white border-t border-nordic-border py-10 mt-12 text-xs text-slate-500">

        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col sm:flex-row items-center justify-between gap-4 font-mono">

            <div>&copy; 2026 ShopVS EU • European Benchmark Lab</div>

            <div class="flex items-center gap-5">

                <a href="/" class="hover:text-nordic-navy">Home</a>

                <a href="/compare/" class="hover:text-nordic-navy">Comparador</a>

                <a href="/legal/" class="hover:text-nordic-navy font-bold text-nordic-navy">Impressum & GDPR (§ 5 TMG)</a>

            </div>

        </div>

    </footer>

</body>

</html>"""



    slug = artigo["slug_de"] if is_de else artigo["slug_es"]

    out_path = os.path.join(BASE_DIR, lang, f"{slug}.html")

    with open(out_path, "w", encoding="utf-8") as f:

        f.write(html)

    print(f"[OK] Artigo {lang.upper()} compilado: {out_path}")



def build_all():

    duelos_file = os.path.join(BASE_DIR, "data", "duelos.json")
    if os.path.exists(duelos_file):
        with open(duelos_file, "r", encoding="utf-8") as f:
            duelos = json.load(f)
    else:
        duplo_data = load_json("data/produto_duplo.json")
        duelos = duplo_data if isinstance(duplo_data, list) else [duplo_data]

    os.makedirs(os.path.join(BASE_DIR, "es"), exist_ok=True)

    os.makedirs(os.path.join(BASE_DIR, "de"), exist_ok=True)

    for artigo in duelos:
        render_article(artigo, "es")
        render_article(artigo, "de")
    





if __name__ == "__main__":

    build_all()
