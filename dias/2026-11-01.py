# 1-nov-2026 · Modelo acv-v3, enfoque soluciones.
# 07:30 [MITO] «Un huevo al día me sube el colesterol y me da infarto.» Drouin-Chartier JP, et al. BMJ 2020;368:m513. doi:10.1136/bmj.m513 (3 cohortes de EE. UU., hasta 32 años, 14.806 casos de enfermedad cardiovascular; ≥1 huevo/día vs <1/mes HR 0,93, IC 0,82-1,05).
# 12:30 [COMPRADOR] «Trabajo sentado todo el día, no tengo opción.» Ekelund U, et al. Lancet 2016;388:1302-1310. doi:10.1016/S0140-6736(16)30370-1 (metaanálisis armonizado de cohortes, 1.005.791 personas; sentado +8 h y poco activo HR 1,59 (1,52-1,66) vs <4 h y muy activo; 60-75 min/día de actividad moderada: sin riesgo extra).
# 19:00 [ALCANCE] «El gym es para verse bien; yo ya camino.» Momma H, et al. Br J Sports Med 2022;56(13):755-763. doi:10.1136/bjsports-2021-105061 (revisión y metaanálisis de cohortes, 16 estudios; mortalidad total RR 0,85, IC 0,79-0,93; máximo beneficio ~10-20 % con 30-60 min/semana).
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





def huevo(av):
    return f"""{S}<div class="wrap">{head(av,'MITO')}
<div class="mir">«Un huevo al día me sube el colesterol y me da infarto.»</div>
<h1 class="k">Comer <em>1 huevo o más al día</em><br>no se asoció con más<br>enfermedad del corazón.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>BMJ</i> 2020</span><span class="chip">3 cohortes · hasta 32 años</span><span class="chip r">14.806 casos de enfermedad del corazón</span></div>
<div class="est"><h4>Riesgo de enfermedad del corazón <span>(1,00 = casi no comían huevo)</span></h4>
<div class="b2"><div class="w">Menos de 1<small>huevo al mes</small></div><div class="t"><div style="width:50%;background:var(--navy)"></div></div><div class="n">1,00<small>referencia</small></div></div>
<div class="b2"><div class="w">1 o más<small>huevos al día</small></div><div class="t"><div style="width:46.5%;background:var(--navy)"></div></div><div class="n">0,93<small>0,82 a 1,05</small></div></div></div>
<div class="ojo">La diferencia <b>no fue clara</b>: el huevo solo no explica el infarto. <b>Importa más todo el plato.</b></div>
<div class="sh">Entonces, ¿qué hago? <span>Hazlo simple:</span></div>
<div class="yn"><div><i>1</i>Un huevo al día cabe en una dieta sana</div><div><i>2</i>Cocínalo hervido, al vapor o con poco aceite</div><div><i>3</i>Mejor con verduras que con embutidos</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Ojo:</b> con diabetes o colesterol muy alto, pregunta a tu médico cuántos te convienen. <b class="y">Mándaselo a quien se quita el huevo por miedo al colesterol.</b></p></div>
<div class="foot"><div class="warn"><b>Estudio observacional:</b> asociación, no causa. Hasta 1 huevo<br>al día; con diabetes los datos son menos claros.</div>
<div class="ref">Drouin-Chartier JP, et al. BMJ 2020;368:m513<br>doi:10.1136/bmj.m513<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def sentado(av):
    return f"""{S}<div class="wrap">{head(av,'COMPRADOR')}
<div class="mir">«Trabajo sentado todo el día, no tengo opción.»</div>
<h1 class="k">Sentado <em>más de 8 horas</em><br>y sin moverte: <em>1,59 veces</em><br>más riesgo de morir.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>The Lancet</i> 2016</span><span class="chip">1.005.791 personas</span><span class="chip r">Metaanálisis de cohortes</span></div>
<div class="est"><h4>Riesgo de morir <span>(1,00 = poco sentado y muy activo)</span></h4>
<div class="b2"><div class="w">Poco sentado,<small>muy activo</small></div><div class="t"><div style="width:50%;background:var(--navy)"></div></div><div class="n">1,00<small>referencia</small></div></div>
<div class="b2"><div class="w">+8 h sentado,<small>casi sin moverse</small></div><div class="t"><div style="width:79.5%;background:var(--red)"></div></div><div class="n">1,59<small>1,52 a 1,66</small></div></div>
<div class="b2"><div class="w">+8 h sentado,<small>muy activo</small></div><div class="t"><div style="width:50%;background:var(--grn)"></div></div><div class="n" style="font-size:30px;line-height:1.1">Sin<small style="font-size:15px">riesgo extra</small></div></div></div>
<div class="ojo"><b>El problema es no moverte.</b> Con 60 a 75 min diarios de movimiento, sin riesgo extra.</div>
<div class="sh">Entonces, ¿qué hago? <span>Aunque trabajes sentado:</span></div>
<div class="yn"><div><i>1</i>Camina en llamadas, almuerzo y al llegar o salir</div><div><i>2</i>Escaleras en vez de ascensor, siempre que puedas</div><div><i>3</i>Muévete también después del trabajo</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Empieza con lo que puedas</b> y ve subiendo. <b class="y">¿Cuántas horas pasa sentado tu papá o tu pareja? Mándaselo.</b></p></div>
<div class="foot"><div class="warn"><b>Estudio observacional:</b> asociación, no causa. Si te falta el aire<br>o sientes dolor en el pecho al moverte: consulta.</div>
<div class="ref">Ekelund U, et al. Lancet 2016;388:1302-1310<br>doi:10.1016/S0140-6736(16)30370-1<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def pesas(av):
    return f"""{S}<div class="wrap">{head(av,'ALCANCE')}
<div class="mir">«El gym es para verse bien. Yo ya camino.»</div>
<h1 class="k">Quienes hacen <em>fuerza</em> tuvieron<br><em>15 % menos</em> riesgo<br>de morir.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>Br J Sports Med</i> 2022</span><span class="chip">16 estudios</span><span class="chip r">Metaanálisis de cohortes</span></div>
<div class="est"><h4>Riesgo de morir por cualquier causa <span>(1,00 = sin fuerza)</span></h4>
<div class="b2"><div class="w">Sin ejercicio<small>de fuerza</small></div><div class="t"><div style="width:50%;background:var(--navy)"></div></div><div class="n">1,00<small>referencia</small></div></div>
<div class="b2"><div class="w">Con ejercicio<small>de fuerza</small></div><div class="t"><div style="width:42.5%;background:var(--navy)"></div></div><div class="n">0,85<small>0,79 a 0,93</small></div></div></div>
<div class="ojo">El mayor beneficio apareció con <b>30 a 60 minutos por semana</b>, no con horas en el gym. Más no fue mejor.</div>
<div class="sh">Entonces, ¿qué hago? <span>En casa, sin gym:</span></div>
<div class="yn"><div><i>1</i>2 o 3 días a la semana, 15 a 20 minutos</div><div><i>2</i>Sentadillas, flexiones en la pared, subir escaleras</div><div><i>3</i>Una botella llena de agua como pesa</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Sigue caminando:</b> fuerza y caminata se suman. <b class="y">Mándaselo a quien dice que las pesas son solo para verse bien.</b></p></div>
<div class="foot"><div class="warn"><b>Estudio observacional:</b> asociación, no causa.<br>Con lesión o enfermedad del corazón, consulta antes.</div>
<div class="ref">Momma H, et al. Br J Sports Med 2022;56:755-763<br>doi:10.1136/bjsports-2021-105061<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

JOBS = {
    'dr-viera-0730-huevo-mito': huevo,
    'dr-viera-1230-sentado-trabajo': sentado,
    'dr-viera-1900-fuerza-muscular': pesas,
}
if __name__ == '__main__':
    render(JOBS, pathlib.Path(__file__).resolve().parents[1] / '2026-11-01')
