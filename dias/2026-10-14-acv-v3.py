# 14-oct-2026 · Derrames cerebrales en menores de 55 · v3 "llegar a la gente"
# Público: alcance 20–35 (y quien cuida a su pareja/amigos). Barrera: "soy joven, a mí no me pasa".
# Orden: espejo → golpe → prueba a escala humana (estadio) → romper la excusa ("es cansancio") → señales → alivio.
# Estadio: 35.000 personas × 33,9 y 62,2 por 100.000 al año = 12 y 22 (Fisher ER, et al. Neurology 2026).
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'kit'))
from plantilla import *

S = """<style>
.mir{font:700 31px/1.3 Manrope;color:var(--g2);margin-top:30px}
h1.k{font:800 64px/1.05 Manrope;letter-spacing:-.03em;margin-top:10px}
.est{margin-top:30px;background:var(--g1);border-radius:16px;padding:22px 26px}
.est h4{font:800 25px/1.25 Manrope}.est h4 span{color:var(--g2);font-weight:600}
.row{display:grid;grid-template-columns:96px 1fr 120px;align-items:center;gap:14px;margin-top:14px}
.row .y{font:800 25px Manrope}.row .y small{display:block;font:600 16px Manrope;color:var(--g2)}
.dots{display:flex;gap:6px;flex-wrap:nowrap}
.dots i{width:23px;height:23px;border-radius:50%;background:var(--navy);display:block}
.dots.r i{background:var(--red)}
.row .n{font:800 52px/1 Manrope;text-align:right;letter-spacing:-.04em}.row .n small{display:block;font:700 15px Manrope;letter-spacing:0;color:var(--g2)}
.row.r .n{color:var(--red)}
.ojo{margin-top:26px;font-size:28px}
.sh{font:800 25px Manrope;margin-top:26px}.sh span{color:var(--g2);font-weight:600}
.sig{display:grid;grid-template-columns:1fr 1fr;gap:14px 22px;margin-top:14px}
.sig div{display:flex;gap:14px;align-items:center;font:700 26px/1.15 Manrope}
.sig i{flex:none;width:44px;height:44px;border-radius:10px;background:var(--red);color:#fff;font:800 24px Manrope;font-style:normal;display:flex;align-items:center;justify-content:center}
.help p{font-size:25px}
</style>"""

def dots(n, cls=''):
    return f'<div class="dots {cls}">' + '<i></i>' * n + '</div>'

def acv(av):
    return f"""{S}<div class="wrap">{head(av,'ESTUDIO NUEVO','r')}
<div class="mir">«Soy joven. Eso les pasa a los viejos.»</div>
<h1 class="k">Los derrames cerebrales<br>en menores de 55<br><em>casi se duplicaron.</em></h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>Neurology</i> 2026</span><span class="chip">27 años de datos</span><span class="chip r">Adultos de 20 a 54 años</span></div>
<div class="est"><h4>Imagina un estadio lleno: <span>35.000 personas de tu edad</span></h4>
<div class="row"><div class="y">1993<small>antes</small></div>{dots(12)}<div class="n">12<small>derrames al año</small></div></div>
<div class="row r"><div class="y">2020<small>ahora</small></div>{dots(22,'r')}<div class="n">22<small>derrames al año</small></div></div></div>
<div class="ojo">El error más común: <b>«seguro es cansancio, ya se me pasa».</b> Cada minuto cuenta.</div>
<div class="sh">Si ves esto, <span>aunque la persona sea joven:</span></div>
<div class="sig"><div><i>C</i>Cara caída de un lado</div><div><i>B</i>Brazo sin fuerza</div><div><i>H</i>Habla rara o enredada</div><div><i>T</i>Tiempo: llama al 911 YA</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Lo que sí está en tus manos:</b> mídete la presión. <b class="y">La presión alta casi nunca da síntomas.</b></p></div>
<div class="foot"><div class="warn"><b>Estudio observacional:</b> muestra que aumentó,<br>no prueba por qué. Estadio: cálculo con 34 y 62<br>casos por cada 100.000 al año. Emergencias: <b>911</b></div>
<div class="ref">Fisher ER, et al. Neurology 2026<br>doi:10.1212/WNL.0000000000218622<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

JOBS = {'dr-viera-1900-derrames-jovenes-v3': acv}
if __name__ == '__main__':
    render(JOBS, pathlib.Path(__file__).resolve().parents[1] / '2026-10-14')
