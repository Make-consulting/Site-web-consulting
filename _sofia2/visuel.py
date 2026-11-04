#!/usr/bin/env python3
"""Génère le visuel LinkedIn MAKE Consulting (1080x1350, JPG) avec le vrai logo.

Usage :
  python3 _sofia2/visuel.py --titre "Il n'est jamais rien arrivé." \
      --sous-titre "La phrase la plus dangereuse d'un atelier" \
      --theme "Culture sécurité" --sortie medias/linkedin/2026-11-05-exemple.jpg

Aucune dépendance à un quota d'IA : rendu HTML -> image avec Playwright,
polices et logo du site (assets/).
"""
import argparse
import base64
import html
import pathlib

from playwright.sync_api import sync_playwright

RACINE = pathlib.Path(__file__).resolve().parent.parent
ASSETS = RACINE / "assets"


def b64(chemin: pathlib.Path) -> str:
    return base64.b64encode(chemin.read_bytes()).decode()


def page_html(titre: str, sous_titre: str, theme: str, variante: str) -> str:
    fraunces = b64(ASSETS / "fonts" / "fraunces.woff2")
    fraunces_it = b64(ASSETS / "fonts" / "fraunces-italic.woff2")
    manrope = b64(ASSETS / "fonts" / "manrope.woff2")
    logo = b64(ASSETS / "logo.png")
    titre, sous_titre = titre.replace("'", "’"), sous_titre.replace("'", "’")
    sombre = variante == "sombre"
    fond = "#1A2548" if sombre else "#FBFBFD"
    encre = "#FBFBFD" if sombre else "#1A2548"
    encre2 = "#C9CFE3" if sombre else "#2B3A6B"
    carte_logo = "background:#FBFBFD;border-radius:18px;padding:14px 16px;" if sombre else ""
    n = len(titre)
    taille = 112 if n <= 28 else 96 if n <= 42 else 82 if n <= 58 else 70
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:Fraunces;src:url(data:font/woff2;base64,{fraunces}) format('woff2');font-weight:100 900}}
@font-face{{font-family:Fraunces;font-style:italic;src:url(data:font/woff2;base64,{fraunces_it}) format('woff2');font-weight:100 900}}
@font-face{{font-family:Manrope;src:url(data:font/woff2;base64,{manrope}) format('woff2');font-weight:200 800}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;background:{fond};font-family:Manrope,sans-serif;color:{encre};position:relative;overflow:hidden}}
.bande{{position:absolute;left:0;top:0;width:22px;height:100%;background:#8B1A1A}}
.motif{{position:absolute;right:-180px;top:-180px;width:620px;height:620px;border-radius:50%;border:2px solid {"rgba(176,138,46,.35)" if sombre else "rgba(26,37,72,.08)"}}}
.motif2{{position:absolute;right:-60px;top:-60px;width:380px;height:380px;border-radius:50%;border:2px solid {"rgba(176,138,46,.25)" if sombre else "rgba(139,26,26,.10)"}}}
.contenu{{position:absolute;left:110px;right:110px;top:110px;bottom:300px;display:flex;flex-direction:column;justify-content:center}}
.theme{{font-size:26px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:#B08A2E;display:flex;align-items:center;gap:18px}}
.theme:before{{content:"";width:56px;height:3px;background:#B08A2E}}
h1{{font-family:Fraunces,serif;font-weight:600;font-size:{taille}px;line-height:1.08;letter-spacing:-.01em;margin-top:56px}}
.filet{{width:120px;height:6px;background:#8B1A1A;margin:64px 0 48px;border-radius:3px}}
p{{font-size:44px;line-height:1.3;font-weight:500;color:{encre2}}}
.pied{{position:absolute;left:110px;right:90px;bottom:90px;display:flex;align-items:flex-end;justify-content:space-between}}
.signature{{font-size:28px;font-weight:700;letter-spacing:.04em}}
.signature span{{display:block;font-size:22px;font-weight:500;color:{encre2};margin-top:6px;letter-spacing:0}}
.logo{{{carte_logo}display:flex}}
.logo img{{height:150px;width:auto;display:block}}
</style></head><body>
<div class="bande"></div><div class="motif"></div><div class="motif2"></div>
<div class="contenu">
  <div class="theme">{html.escape(theme)}</div>
  <h1>{html.escape(titre)}</h1>
  <div class="filet"></div>
  <p>{html.escape(sous_titre)}</p>
</div>
<div class="pied">
  <div class="signature">MAKE Consulting<span>Conseil QSE · Prévention · IPRP</span></div>
  <div class="logo"><img src="data:image/png;base64,{logo}" alt=""></div>
</div>
</body></html>"""


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--titre", required=True)
    ap.add_argument("--sous-titre", required=True)
    ap.add_argument("--theme", default="Prévention des risques")
    ap.add_argument("--variante", choices=["clair", "sombre"], default="clair")
    ap.add_argument("--sortie", required=True)
    a = ap.parse_args()
    sortie = pathlib.Path(a.sortie)
    sortie.parent.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        nav = p.chromium.launch()
        page = nav.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)
        page.set_content(page_html(a.titre, a.sous_titre, a.theme, a.variante))
        page.evaluate("document.fonts.ready")
        page.screenshot(path=str(sortie), type="jpeg", quality=90, full_page=False)
        nav.close()
    print(sortie)


if __name__ == "__main__":
    main()
