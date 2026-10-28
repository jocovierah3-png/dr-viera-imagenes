# 28-oct-2026 · imagen extra (16:00) · modelo soluciones.
# [ALCANCE] «No tengo tiempo para hacer ejercicio.» Stamatakis E, et al. Nat Med 2022;28:2521-2529. doi:10.1038/s41591-022-02100-x (UK Biobank, 25.241 adultos que no hacían ejercicio, 6,9 años; 3 ráfagas/día de 1-2 min: 38-40 % menos riesgo de morir por cualquier causa o cáncer, 48-49 % cardiovascular).
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'kit'))
from plantilla import *

S = """<style>
.mir{font:700 31px/1.3 Manrope;color:var(--g2);margin-top:24px}
h1.k{font:800 62px/1.05 Manrope;letter-spacing:-.03em;margin-top:10px}
.est{margin-top:22px;background:var(--g1);border-radius:16px;padding:22px 26px}
.est h4{font:800 25px/1.25 Manrope}.est h4 span{color:var(--g2);font-weight:600}
.ojo{margin-top:22px;font-size:27px}
.sh{font:800 25px Manrope;margin-top:22px}.sh span{color:var(--g2);font-weight:600}
.yn{margin-top:12px;display:flex;flex-direction:column;gap:10px}
.yn div{display:flex;gap:14px;align-items:center;font:700 25px/1.2 Manrope}
.yn i{flex:none;width:40px;height:40px;border-radius:10px;background:var(--navy);color:#fff;font:800 20px Manrope;font-style:normal;display:flex;align-items:center;justify-content:center}
.ppl{display:grid;grid-template-columns:repeat(14,1fr);gap:8px;margin-top:30px}
.ppl i{display:block;height:38px;border-radius:20px 20px 6px 6px;background:#C9CFD8;position:relative}
.ppl i:before{content:"";position:absolute;left:50%;top:-17px;width:17px;height:17px;margin-left:-8.5px;border-radius:50%;background:inherit}
.ppl i.r{background:var(--red)}
.mf{display:flex;gap:14px;margin-top:14px}
.mf div{flex:1;background:#fff;border-radius:10px;padding:10px 14px;font:700 21px/1.25 Manrope}.mf b{font:800 34px Manrope;color:var(--red);margin-right:6px}
.b2{display:grid;grid-template-columns:200px 1fr 130px;align-items:center;gap:14px;margin-top:8px}
.b2 .w{font:800 25px/1.15 Manrope}.b2 .w small{display:block;font:600 17px Manrope;color:var(--g2)}
.b2 .t{height:46px;background:#fff;border-radius:6px;position:relative}.b2 .t div{position:absolute;left:0;top:0;bottom:0;border-radius:6px}
.b2 .n{font:800 50px/1 Manrope;letter-spacing:-.04em;text-align:right}.b2 .n small{display:block;font:700 15px Manrope;letter-spacing:0;color:var(--g2)}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:14px 22px;margin-top:14px}
.grid2 div{display:flex;gap:12px;align-items:center;font:700 25px/1.2 Manrope}
.grid2 i{flex:none;width:38px;height:38px;border-radius:10px;background:var(--red);color:#fff;font:800 22px Manrope;font-style:normal;display:flex;align-items:center;justify-content:center}
.help p{font-size:25px}
.cmp{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:14px}
.cmp div{background:#fff;border-radius:12px;padding:16px 18px;font:700 24px/1.25 Manrope}
.cmp b.big{display:block;font:800 40px/1.05 Manrope;margin-bottom:6px}
.cmp .rr b.big{color:var(--red)}.cmp .gg b.big{color:var(--navy)}
</style>"""




def rafagas(av):
    return f"""{S}<div class="wrap">{head(av,'ESTUDIO NUEVO','r')}
<div class="mir">«No tengo tiempo para hacer ejercicio.»</div>
<h1 class="k">3 ráfagas de <em>1 a 2 minutos</em><br>al día se asociaron con<br>vivir más, sin gimnasio.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>Nature Medicine</i> 2022</span><span class="chip">25.241 adultos</span><span class="chip r">Ninguno hacía ejercicio</span></div>
<div class="est"><h4>Quienes hacían 3 ráfagas al día <span>(7 años de seguimiento)</span></h4>
<div class="mf"><div><b>38 a 40 %</b>menos riesgo de morir<br>por cualquier causa</div><div><b>48 a 49 %</b>menos riesgo de morir<br>por el corazón</div></div></div>
<div class="sh">Una ráfaga es <span>moverte tan rápido que te cuesta hablar:</span></div>
<div class="yn"><div><i>1</i>Sube escaleras rápido en vez del ascensor</div><div><i>2</i>Camina muy rápido hasta el bus o la tienda</div><div><i>3</i>Corre un rato con tus hijos o tu perro</div></div>
<div class="ojo">No hace falta cambiarte de ropa ni pagar un gimnasio: <b>son 3 a 6 minutos al día.</b></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Hoy:</b> sube un piso de escaleras lo más rápido que puedas. <b class="y">Mándaselo a quien dice «no tengo tiempo».</b></p></div>
<div class="foot"><div class="warn"><b>Estudio observacional:</b> se asoció, no prueba causa.<br>Si tienes problemas del corazón, consulta<br>a tu médico antes de esforzarte.</div>
<div class="ref">Stamatakis E, et al. Nat Med 2022;28:2521-2529<br>doi:10.1038/s41591-022-02100-x<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

JOBS = {'dr-viera-1600-rafagas-sin-tiempo': rafagas}
if __name__ == '__main__':
    render(JOBS, pathlib.Path(__file__).resolve().parents[1] / '2026-10-28')
