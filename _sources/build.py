import p_index, p_univers, p_other, p_formations, p_hub, p_local, p_pro
import os
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..') + os.sep
pages = {'index.html': p_index.build(), 'firetraining-ms.html': p_univers.build_ft(), 'conseil.html': p_univers.build_co(),
         'contact.html': p_other.build_contact(), 'mentions-legales.html': p_other.build_mentions(),
         'formations.html': p_hub.build_catalogue(), 'formation-incendie.html': p_formations.build_incendie(),
         'formation-sst.html': p_formations.build_sst(), 'formations-reglementaires.html': p_formations.build_reg(),
         'faq.html': p_hub.build_faq(), 'firetraining-pro.html': p_pro.build(), '404.html': p_other.build_404()}
for k in p_local.DEPTS: pages[p_local.DEPTS[k]['slug']] = p_local.build_dept(k)
import re
def imgs(h):
    for n in ['photo-formation', 'firetraining-screenshot']:
        h = h.replace(f'src="assets/{n}.jpg"', f'src="assets/{n}-1200.webp" srcset="assets/{n}-800.webp 800w, assets/{n}-1200.webp 1200w" sizes="(max-width: 860px) 92vw, 580px"')
    return h
def heads(h):
    return h.replace('<h4 class="', '<h3 class="h4 ').replace('<h4>', '<h3 class="h4">').replace('</h4>', '</h3>')
def typo(h):
    parts = re.split(r'(<script.*?</script>|<style.*?</style>)', h, flags=re.S)
    return ''.join(p if p.startswith(('<script','<style')) else p.replace(' : ', '&nbsp;: ').replace(' ?', '&nbsp;?') for p in parts)
for n, h in pages.items():
    h = heads(imgs(typo(h)))
    open(out + n, 'w').write(h); print(n, len(h))

open(out + 'references.html', 'w').write(p_hub.build_references_redirect())
