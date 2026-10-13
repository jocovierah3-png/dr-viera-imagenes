import base64, pathlib, sys
from playwright.sync_api import sync_playwright
D=pathlib.Path(__file__).parent  # carpeta kit/
def b64(p): return base64.b64encode((D/p).read_bytes()).decode()
def ff(fam,w,st,f): return f"@font-face{{font-family:'{fam}';src:url(data:font/woff2;base64,{b64(f)}) format('woff2');font-weight:{w};font-style:{st}}}"
M='fontsource-manrope-5.1.0/package/files/manrope-latin-{}-normal.woff2'
N='fontsource-newsreader-5.1.0/package/files/newsreader-latin-{}-{}.woff2'
FONTS=''.join(ff('Manrope',w,'normal',M.format(w)) for w in (500,600,700,800))+''.join(ff('Newsreader',w,s,N.format(w,s)) for w in (500,600) for s in ('normal','italic'))
CSS="""
:root{--navy:#102D50;--g1:#F2F4F7;--red:#E92724;--yel:#FFD200;--g2:#667085;--grn:#22C55E;--grn2:#4ADE80}
*{margin:0;padding:0;box-sizing:border-box}
body{width:1080px;height:1350px;background:#fff;font-family:Manrope,sans-serif;color:var(--navy);overflow:hidden;position:relative}
.wrap{position:absolute;inset:0;padding:56px 64px 40px;display:flex;flex-direction:column}
.head{display:flex;align-items:center;gap:20px}
.av{width:96px;height:96px;border-radius:50%;object-fit:cover}
.nm{font:800 36px Manrope;line-height:1.1}.hd{font:600 23px Manrope;color:var(--g2);margin-top:2px}
.tag{margin-left:auto;font:800 18px Manrope;letter-spacing:.14em;border:2.5px solid var(--navy);padding:10px 18px;border-radius:999px}
.tag.r{background:var(--red);border-color:var(--red);color:#fff}
h1{font:800 66px/1.06 Manrope;letter-spacing:-.03em;margin-top:40px}
h1 em{font-style:normal;color:var(--red)}
h1 mark{background:linear-gradient(transparent 58%,var(--yel) 58%,var(--yel) 92%,transparent 92%);color:inherit;padding:0 4px}
.src{display:flex;gap:12px;margin-top:26px;flex-wrap:wrap}
.chip{font:700 21px Manrope;background:var(--g1);border-radius:8px;padding:8px 14px}
.chip i{font-family:Newsreader;font-size:24px;font-weight:600}
.chip.r{background:#FDE8E8;color:var(--red)}
.ct{font:800 26px Manrope;margin-top:44px;display:flex;justify-content:space-between;align-items:baseline}
.ct span{font:600 19px Manrope;color:var(--g2)}
.bar{display:grid;grid-template-columns:250px 1fr 150px;align-items:center;margin-top:26px;column-gap:18px}
.who{font:800 27px/1.1 Manrope}.who small{display:block;font:600 18px Manrope;color:var(--g2);margin-top:4px}
.track{position:relative;height:70px;background:var(--g1);border-radius:6px}
.fill{position:absolute;left:0;top:0;bottom:0;border-radius:6px}
.ci{position:absolute;top:50%;height:2px;background:var(--navy)}
.ci:before,.ci:after{content:"";position:absolute;top:-11px;width:2px;height:24px;background:var(--navy)}
.ci:before{left:0}.ci:after{right:0}
.ref1{position:absolute;top:-10px;bottom:-10px;width:0;border-left:3px dashed var(--g2)}
.val{font:800 66px/1 Manrope;letter-spacing:-.04em;text-align:right}
.val small{display:block;font:700 19px Manrope;color:var(--navy);letter-spacing:0;margin-top:2px}
.note{font:600 18px/1.4 Manrope;color:var(--g2);margin-top:16px}
.ojo{font:700 29px/1.32 Manrope;margin-top:30px;padding-left:22px;border-left:6px solid var(--red)}
.ojo b{color:var(--red)}
.help{margin:auto -64px 0;background:var(--navy);color:#fff;padding:24px 64px;display:flex;gap:22px;align-items:center}
.help .ic{flex:none;width:56px;height:56px;border-radius:50%;background:var(--grn);color:var(--navy);display:flex;align-items:center;justify-content:center;font:800 30px Manrope}
.help.w .ic{background:var(--yel)}
.help p{font:600 25px/1.34 Manrope}.help b{font-weight:800}.help b.g{color:var(--grn2)}.help b.y{color:var(--yel)}
.foot{margin-top:20px;display:flex;justify-content:space-between;align-items:flex-end;gap:24px}
.warn{font:600 19px/1.45 Manrope;color:var(--g2)}.warn b{color:var(--navy)}
.ref{font:500 italic 17px/1.4 Newsreader;color:var(--g2);text-align:right}
.ref b{font:700 normal 16px Manrope;color:var(--navy);letter-spacing:.12em}
.pr{display:grid;grid-template-columns:230px 1fr 170px;align-items:center;column-gap:18px;margin-top:34px}
.tl{display:grid;grid-template-columns:150px 1fr 56px;align-items:center;gap:12px;margin:6px 0}
.tl span{font:600 18px Manrope;color:var(--g2)}.tl em{font:800 22px Manrope;font-style:normal}
.t2{position:relative;height:26px}.t2.big{height:48px}.f2{position:absolute;left:0;top:0;bottom:0;border-radius:5px}
.ojo{margin-top:40px}
/* mito */
.mv{display:grid;grid-template-columns:1fr 1.25fr;gap:18px;margin-top:34px}
.box{border-radius:14px;padding:22px 24px}
.box h3{font:800 20px Manrope;letter-spacing:.14em;margin-bottom:10px}
.box p{font:700 28px/1.25 Manrope}
.box.m{background:var(--g1);color:var(--g2);display:flex;flex-direction:column;justify-content:center}.box.m p{font-size:34px}.box.m p{text-decoration:line-through;text-decoration-color:var(--red);text-decoration-thickness:3px}
.box.m h3{color:var(--red)}
.box.r{background:#fff;border:3px solid var(--navy)}.box.r h3{color:var(--grn)}
.box.r p b{color:var(--red)}
.al{margin-top:40px}
.al h4{font:800 26px Manrope}.al h4 span{font:600 20px Manrope;color:var(--g2);margin-left:8px}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:22px 22px;margin-top:24px}
.it{display:flex;gap:14px;align-items:center;font:700 28px/1.2 Manrope}
.it i{flex:none;width:34px;height:34px;border-radius:50%;background:var(--red);color:#fff;font:800 22px Manrope;font-style:normal;display:flex;align-items:center;justify-content:center}
"""
def head(av,tag,cls=''):
    return f'<div class="head"><img class="av" src="{av}"><div><div class="nm">Dr. Joel Viera</div><div class="hd">@dr.joelviera · Médico</div></div><div class="tag {cls}">{tag}</div></div>'
def bar(who,sub,v,scale,color,label,ci=None,ref=None,unit='%'):
    p=lambda x:x/scale*100
    c=f'<div class="ci" style="left:{p(ci[0]):.1f}%;width:{p(ci[1])-p(ci[0]):.1f}%"></div>' if ci else ''
    r=f'<div class="ref1" style="left:{p(ref):.1f}%"></div>' if ref else ''
    return f'<div class="bar"><div class="who">{who}<small>{sub}</small></div><div class="track"><div class="fill" style="width:{p(v):.1f}%;background:{color}"></div>{c}{r}</div><div class="val" style="color:{color}">{label}</div></div>'

def pair(who,hr,lo,hi,lab):
    p=lambda x:x/1.1*100
    return f'''<div class="pr"><div class="who">{who}</div><div><div class="tl"><span>Referencia</span><div class="t2"><div class="f2" style="width:{p(1):.1f}%;background:#C9CFD8"></div></div><em>1</em></div>
<div class="tl"><span>+48 min REM</span><div class="t2 big"><div class="f2" style="width:{p(hr):.1f}%;background:#102D50"></div><div class="ci" style="left:{p(lo):.1f}%;width:{p(hi)-p(lo):.1f}%"></div></div><em>{str(hr).replace('.',',')}</em></div></div><div class="val" style="color:#E92724">{lab}<small>menos riesgo</small></div></div>'''

def page(body,fonts): return f"<html><head><meta charset='utf-8'><style>{fonts}{CSS}</style></head><body>{body}</body></html>"
AV=f"data:image/png;base64,{b64('avatar.png')}"

def render(jobs,outdir):
    """jobs: dict nombre_archivo -> funcion(av) que devuelve el HTML del <div class="wrap">."""
    outdir=pathlib.Path(outdir); outdir.mkdir(parents=True,exist_ok=True)
    chk="(()=>{const w=document.querySelector('.wrap');const f=document.querySelector('.foot').getBoundingClientRect();return {scroll:w.scrollHeight,foot:Math.round(f.bottom)}})()"
    with sync_playwright() as p:
        b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1350})
        for name,fn in jobs.items():
            pg.set_content(page(fn(AV),FONTS)); pg.wait_for_timeout(500)
            m=pg.evaluate(chk); ok=m['scroll']<=1350 and m['foot']<=1330
            print(name,m,'OK' if ok else 'DESBORDA: acortar textos')
            pg.screenshot(path=str(outdir/f'{name}.png'))
        b.close()
