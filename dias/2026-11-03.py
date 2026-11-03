# 3-nov-2026 · Modelo acv-v3, enfoque soluciones.
# 07:30 [MITO] «Tomo mi multivitamínico para cuidarme.» Loftfield E, et al. JAMA Netw Open 2024;7(6):e2418729. doi:10.1001/jamanetworkopen.2024.18729 (3 cohortes de EE. UU., 390.124 adultos, 164.762 muertes, >20 años; uso diario vs no uso: HR 1,04, IC 0,99-1,08 en la 2.ª mitad; 1,04 (1,02-1,07) en la 1.ª; sin beneficio en mortalidad).
# 12:30 [COMPRADOR] «Mi papá ya tiene el corazón delicado, pero la gripe es solo gripe.» Udell JA, et al. JAMA 2013;310(16):1711-1720 (metaanálisis de 5 ensayos al azar, 6.469 pacientes; eventos del corazón 2,9 % vs 4,7 %; RR 0,64, IC 0,48-0,86; efecto concentrado en síndrome coronario reciente). DOI no verificado (PubMed bloqueado).
# 19:00 [ALCANCE] «Me duermo viendo el celular.» Hjetland GJ, et al. Front Psychiatry 2025;16:1548273. doi:10.3389/fpsyt.2025.1548273 (transversal, 45.202 estudiantes de 18-28 años, Noruega; cada hora de pantalla en la cama: 59 % más probabilidad de insomnio y 24 min menos de sueño).
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






def multi(av):
    return f"""{S}<div class="wrap">{head(av,'MITO vs REALIDAD')}
<div class="mir">«Tomo mi multivitamínico para cuidarme.»</div>
<h1 class="k">Tomarlo a diario<br><em>no mostró</em> que<br>vivas más años.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>JAMA Netw Open</i> 2024</span><span class="chip">3 estudios · 390.124 adultos de EE. UU.</span><span class="chip r">más de 20 años · 164.762 muertes</span></div>
<div class="est"><h4>Riesgo de morir, quien lo toma a diario <span>(1,00 = quien no lo toma)</span></h4>
<div class="b2"><div class="w">No lo toma<small>referencia</small></div><div class="t"><div style="width:50%;background:var(--navy)"></div></div><div class="n">1,00<small>referencia</small></div></div>
<div class="b2"><div class="w">Lo toma<small>a diario</small></div><div class="t"><div style="width:52%;background:var(--red)"></div></div><div class="n">1,04<small>1,02 a 1,07</small></div></div></div>
<div class="ojo">No hubo ventaja para vivir más. Los autores <b>no afirman que haga daño</b>: solo que <b>no se vio beneficio</b> en adultos sanos.</div>
<div class="sh">Entonces, ¿qué hago? <span>Pon tu esfuerzo donde sí rinde:</span></div>
<div class="yn"><div><i>1</i>Come fruta y verdura a diario, de colores</div><div><i>2</i>Camina 30 minutos casi todos los días</div><div><i>3</i>Duerme tus horas y no fumes</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Si tu médico te lo indicó</b> (embarazo, falta de algo en tu sangre), sigue su consejo. <b class="y">Mándaselo a quien gasta en pastillas “por si acaso”.</b></p></div>
<div class="foot"><div class="warn"><b>Estudio observacional:</b> asociación, no causa.<br>Vale para adultos sanos; no cambies tu tratamiento sin consultar.</div>
<div class="ref">Loftfield E, et al. JAMA Netw Open 2024;7(6):e2418729<br>doi:10.1001/jamanetworkopen.2024.18729<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def gripe(av):
    return f"""{S}<div class="wrap">{head(av,'COMPRADOR')}
<div class="mir">«Mi papá ya tiene el corazón delicado, pero la gripe es solo gripe.»</div>
<h1 class="k">Vacunarse contra la gripe:<br><em>3 de cada 100</em> vs <em>5 de cada 100</em><br>con problemas del corazón.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>JAMA</i> 2013</span><span class="chip">5 ensayos al azar · 6.469 pacientes</span><span class="chip r">riesgo 36 % menor</span></div>
<div class="est"><h4>De cada 100 personas, en el seguimiento <span>(infarto y otros problemas del corazón)</span></h4>
<div class="b2"><div class="w">Sin vacuna<small>gripe</small></div><div class="t"><div style="width:94%;background:var(--red)"></div></div><div class="n">4,7<small>de cada 100</small></div></div>
<div class="b2"><div class="w">Con vacuna<small>gripe</small></div><div class="t"><div style="width:58%;background:var(--grn)"></div></div><div class="n">2,9<small>de cada 100</small></div></div></div>
<div class="ojo">El beneficio se vio sobre todo en quienes <b>tuvieron un infarto o dolor de pecho grave hace poco.</b> Son ensayos pequeños: falta confirmarlo.</div>
<div class="sh">Entonces, ¿qué hago? <span>Por tus papás:</span></div>
<div class="yn"><div><i>1</i>Pregunta en el centro de salud si les toca la vacuna</div><div><i>2</i>Llévalos tú: ponte la tuya el mismo día</div><div><i>3</i>Con fiebre y falta de aire, consulta pronto</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">La gripe no es “solo gripe”</b> si el corazón ya está delicado. <b class="y">¿Ya se vacunaron tus papás? Mándaselo a tus hermanos.</b></p></div>
<div class="foot"><div class="warn"><b>Metaanálisis de ensayos pequeños:</b> evidencia moderada.<br>Consulta con su médico si tienen alergias o dudas.</div>
<div class="ref">Udell JA, et al. JAMA 2013;310(16):1711-1720<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def pantalla(av):
    return f"""{S}<div class="wrap">{head(av,'ESTUDIO NUEVO')}
<div class="mir">«Me duermo viendo el celular.»</div>
<h1 class="k">Cada hora de pantalla<br>en la cama: <em>59 % más</em><br>de insomnio.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>Front. Psychiatry</i> 2025</span><span class="chip">45.202 estudiantes de 18 a 28 años</span><span class="chip r">Noruega</span></div>
<div class="est"><h4>Por cada hora extra de pantalla ya acostado <span>(comparado con no usarla)</span></h4>
<div class="b2"><div class="w">Insomnio<small>probabilidad</small></div><div class="t"><div style="width:80%;background:var(--red)"></div></div><div class="n" style="white-space:nowrap;font-size:46px">59 %<small>más</small></div></div>
<div class="b2"><div class="w">Sueño<small>por noche</small></div><div class="t"><div style="width:30%;background:var(--red)"></div></div><div class="n">24<small>minutos menos</small></div></div></div>
<div class="ojo">Daba igual si era redes sociales u otra cosa: <b>lo que contó fue usar la pantalla en la cama.</b></div>
<div class="sh">Entonces, ¿qué hago? <span>Esta noche, prueba:</span></div>
<div class="yn"><div><i>1</i>Deja el cargador lejos de la cama</div><div><i>2</i>Pon la alarma en un reloj, no en el celular</div><div><i>3</i>Última pantalla afuera del cuarto; lee algo en papel</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Empieza con una noche</b> y mira cómo amaneces. <b class="y">Mándaselo a tu amigo que “no puede dormir”.</b></p></div>
<div class="foot"><div class="warn"><b>Estudio transversal:</b> asociación, no causa; no prueba qué fue primero.<br>Si el insomnio dura meses, consulta a tu médico.</div>
<div class="ref">Hjetland GJ, et al. Front Psychiatry 2025;16:1548273<br>doi:10.3389/fpsyt.2025.1548273<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

JOBS = {
    'dr-viera-0730-multivitaminicos': multi,
    'dr-viera-1230-gripe-corazon': gripe,
    'dr-viera-1900-pantalla-cama': pantalla,
}
if __name__ == '__main__':
    render(JOBS, pathlib.Path(__file__).resolve().parents[1] / '2026-11-03')
