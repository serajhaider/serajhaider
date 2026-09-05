from pathlib import Path
from PIL import Image
import html
RAMP=' .`:-=+*cs#%@'; BLUE='#60A5FA'

def main():
    src=Path('source-prepped.png')
    if not src.exists(): raise SystemExit('Run prep_photo.py first, or place source-prepped.png in the root.')
    im=Image.open(src).convert('L'); maxw=72; scale=min(1,maxw/im.width); w=max(1,int(im.width*scale)); h=max(1,int(im.height*scale*0.48)); im=im.resize((w,h))
    pix=im.load(); lines=[]
    for y in range(h):
        lines.append(''.join(RAMP[pix[x,y]*(len(RAMP)-1)//255] for x in range(w)))
    rows=[]
    for i,line in enumerate(lines): rows.append(f'<text x="30" y="{48+i*12}" class="ascii" style="animation-delay:{i*0.025:.3f}s">{html.escape(line)}</text>')
    H=max(220,80+len(lines)*12)
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="760" height="{H}" viewBox="0 0 760 {H}"><rect width="100%" height="100%" rx="22" fill="#0d0d0d" stroke="#1e3a5f"/><circle cx="28" cy="24" r="6" fill="#2563eb"/><circle cx="48" cy="24" r="6" fill="#3b82f6"/><circle cx="68" cy="24" r="6" fill="#60a5fa"/><text x="100" y="29" fill="#93c5fd" font-family="monospace" font-size="14">The Cipher Stack / portrait</text><g fill="{BLUE}" font-family="monospace" font-size="11">{''.join(rows)}</g><style>@keyframes fin{{from{{opacity:0;transform:translateX(-8px)}}to{{opacity:1;transform:translateX(0)}}}}.ascii{{opacity:0;animation:fin .55s ease forwards}}@media(prefers-reduced-motion:reduce){{.ascii{{animation:none;opacity:1}}}}</style></svg>'''
    Path('hxni-ascii.svg').write_text(svg,encoding='utf8')
if __name__=='__main__': main()
