import os, re
import mk_pages as P, mk_other as O
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'mk') + os.sep
if os.path.basename(os.path.dirname(os.path.abspath(__file__))) == '_sources':
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..') + os.sep
pages = {'index.html': P.build_index(), 'duerp.html': P.build_duerp(), 'audit-qse.html': P.build_audit(),
         'prevention-rps.html': P.build_rps(), 'securite-incendie.html': P.build_incendie(), 'diagnostic-ssiap.html': P.build_ssiap(),
         'continuite-activite.html': P.build_pca(), 'iprp-externalise.html': P.build_iprp(),
         'references.html': O.build_refs(), 'a-propos.html': O.build_about(), 'faq.html': O.build_faq(),
         'contact.html': O.build_contact(), 'mentions-legales.html': O.build_mentions(), '404.html': O.build_404()}
def imgs(h):
    for n in ['photo-formation', 'firetraining-screenshot']:
        h = h.replace(f'src="assets/{n}.jpg"', f'src="assets/{n}-1200.webp" srcset="assets/{n}-800.webp 800w, assets/{n}-1200.webp 1200w" sizes="(max-width: 860px) 92vw, 580px"')
    return h
def typo(h):
    parts = re.split(r'(<script.*?</script>|<style.*?</style>)', h, flags=re.S)
    return ''.join(p if p.startswith(('<script', '<style')) else p.replace(' : ', '&nbsp;: ').replace(' ?', '&nbsp;?') for p in parts)
for n, h in pages.items():
    open(out + n, 'w').write(imgs(typo(h))); print(n, len(h))
open(out + 'blog.html', 'w').write(O.build_blog_redirect())
