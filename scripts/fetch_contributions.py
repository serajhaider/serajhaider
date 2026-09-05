import json,re
from datetime import date,timedelta
from pathlib import Path
import requests
from bs4 import BeautifulSoup
USER='serajhaider'
URL=f'https://github.com/users/{USER}/contributions'
def streaks(counts):
    days=sorted(counts)
    best=cur=0; longest=0; prev=None
    for d in days:
        if counts[d]>0:
            cur=cur+1 if prev==d-timedelta(days=1) else 1; longest=max(longest,cur)
        else: cur=0
        prev=d
    # current streak ending today or yesterday
    end=date.today();
    if counts.get(end,0)==0: end=end-timedelta(days=1)
    while counts.get(end,0)>0: best+=1; end-=timedelta(days=1)
    return best,longest

def main():
    r=requests.get(URL,headers={'User-Agent':'Mozilla/5.0'},timeout=30); r.raise_for_status()
    soup=BeautifulSoup(r.text,'html.parser'); counts={}
    for cell in soup.select('td.ContributionCalendar-day[data-date]'):
        try: counts[date.fromisoformat(cell['data-date'])]=int(cell.get('data-count','0'))
        except: pass
    if not counts:
        # fallback to aria-label text
        for el in soup.select('[data-date]'):
            try:
                d=date.fromisoformat(el['data-date']); m=re.search(r'(\d+) contribution',el.get('aria-label',''))
                if m: counts[d]=int(m.group(1))
            except: pass
    if not counts: raise RuntimeError('GitHub contribution calendar could not be parsed.')
    current,longest=streaks(counts); total=sum(counts.values()); best=max(counts.items(),key=lambda x:x[1])
    data={'username':USER,'fetched_at':date.today().isoformat(),'days':[{'date':d.isoformat(),'count':c} for d,c in sorted(counts.items())],'metrics':{'total_contributions':total,'current_streak':current,'longest_streak':longest,'best_day':{'date':best[0].isoformat(),'count':best[1]}}}
    Path('data').mkdir(exist_ok=True); Path('data/contributions.json').write_text(json.dumps(data,indent=2),encoding='utf8')
if __name__=='__main__': main()
