import json
from pathlib import Path
from datetime import date,timedelta

def main():
 d=json.loads(Path('data/contributions.json').read_text()); vals={x['date']:x['count'] for x in d['days']}; end=max((date.fromisoformat(x) for x in vals),default=date.today()); start=end-timedelta(days=364); start-=timedelta(days=(start.weekday()+1)%7)
 cells=[]; cur=start; x=0
 while cur<=end:
  y=(cur-start).days%7; xx=(cur-start).days//7; c=vals.get(cur.isoformat(),0); level=0 if c==0 else 1 if c<3 else 2 if c<6 else 3 if c<10 else 4; cells.append(f'<rect x="{xx*15}" y="{y*15}" width="11" height="11" rx="2" class="l{level}"><title>{cur}: {c} contributions</title></rect>'); cur+=timedelta(days=1)
 width=((end-start).days//7+1)*15+10
 svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="135" viewBox="0 0 {width} 135"><rect width="100%" height="100%" rx="14" fill="#0d0d0d" stroke="#3b3320"/><g transform="translate(8,10)">{''.join(cells)}</g><style>.l0{{fill:#242424}}.l1{{fill:#6f5a18}}.l2{{fill:#9d7d1e}}.l3{{fill:#c39b2b}}.l4{{fill:#D4AF37}}</style></svg>'''
 Path('contrib-heatmap.svg').write_text(svg,encoding='utf8')
if __name__=='__main__': main()
