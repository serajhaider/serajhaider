from pathlib import Path
import html
rows=[('OS','Windows / Linux'),('Host','Kathmandu, Nepal'),('Role','Computer Science Student'),('Stack','Python • React • Node • Flutter'),('AI/ML','Data Science • ML • XGBoost'),('Portfolio','serajhaidar.com.np'),('GitHub','github.com/serajhaider')]
def main():
    items=[]
    for i,(k,v) in enumerate(rows):
        y=78+i*38; items.append(f'<g style="animation-delay:{i*.12:.2f}s"><text x="32" y="{y}" class="key">{html.escape(k)}</text><text x="160" y="{y}" class="val">{html.escape(v)}</text></g>')
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="420" viewBox="0 0 900 420"><rect width="100%" height="100%" rx="22" fill="#0d0d0d" stroke="#1e3a5f"/><circle cx="28" cy="24" r="6" fill="#2563eb"/><circle cx="48" cy="24" r="6" fill="#3b82f6"/><circle cx="68" cy="24" r="6" fill="#60a5fa"/><text x="100" y="29" fill="#93c5fd" font-family="monospace" font-size="14">The Cipher Stack</text><g font-family="monospace" font-size="18"><style>.key{{fill:#60a5fa}}.val{{fill:#dbeafe}}</style>{''.join(items)}</g><style>@keyframes fade{{from{{opacity:0;transform:translateY(5px)}}to{{opacity:1;transform:translateY(0)}}}}g g{{opacity:0;animation:fade .5s ease forwards}}</style></svg>'''
    Path('info-card.svg').write_text(svg,encoding='utf8')
if __name__=='__main__': main()
