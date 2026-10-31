# 31-oct-2026 · Modelo acv-v3, enfoque soluciones.
# 07:30 [MITO] «Si no desayuno, engordo.» Sievert K, et al. BMJ 2019;364:l42. doi:10.1136/bmj.l42 (revisión sistemática y metaanálisis de 13 ensayos al azar; desayuno vs saltarlo: +0,44 kg y +260 kcal/día en quienes desayunaban).
# 12:30 [COMPRADOR] «Mi papá tiene diabetes. Eso ya no se quita.» Lean MEJ, et al. Lancet 2018;391:541-551. doi:10.1016/S0140-6736(17)33102-1 (DiRECT, ensayo al azar por grupos, 306 adultos con diabetes tipo 2 de hasta 6 años; remisión a 12 meses 46 % vs 4 %; 86 % con 15 kg o más de baja).
# 19:00 [ALCANCE] «Subo el volumen para no oír la calle.» Dillard LK, et al. BMJ Glob Health 2022;7(11):e010501. doi:10.1136/bmjgh-2022-010501 (metaanálisis de 35 registros, >19.000 personas de 12-34 años; audífonos 23,8 %, locales ruidosos 48,2 % (modelado); 0,67-1,35 mil millones en riesgo).
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



def desayuno(av):
    return f"""{S}<div class="wrap">{head(av,'MITO')}
<div class="mir">«Si no desayuno, engordo.»</div>
<h1 class="k">Quienes desayunaban<br>comían <em>260 calorías más</em><br>al día y pesaron <em>0,44 kg más.</em></h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>BMJ</i> 2019</span><span class="chip">13 ensayos al azar</span><span class="chip r">Países de ingresos altos</span></div>
<div class="est"><h4>Desayunar frente a saltarse el desayuno <span>(adultos)</span></h4>
<div class="cmp"><div class="rr"><b class="big">+260</b>calorías al día en quienes desayunaban.</div><div class="rr"><b class="big">+0,44 kg</b>de peso en quienes desayunaban.</div></div></div>
<div class="ojo">El desayuno no es un truco para adelgazar. <b>Lo que cuenta es todo lo que comes en el día.</b></div>
<div class="sh">Entonces, ¿qué hago? <span>Hazlo simple:</span></div>
<div class="yn"><div><i>1</i>Si tienes hambre al despertar, desayuna</div><div><i>2</i>Si no tienes hambre, no te obligues</div><div><i>3</i>Cuida qué y cuánto comes todo el día</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Ojo:</b> si tienes diabetes con medicinas, estás embarazada o es para un niño, consulta antes de cambiar horarios. <b class="y">Mándaselo a quien dice que sin desayuno no se baja de peso.</b></p></div>
<div class="foot"><div class="warn"><b>Ensayos cortos y de calidad limitada.</b> Muestran diferencias<br>pequeñas, no que saltarse el desayuno sea mejor.</div>
<div class="ref">Sievert K, et al. BMJ 2019;364:l42<br>doi:10.1136/bmj.l42<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def diabetes(av):
    return f"""{S}<div class="wrap">{head(av,'COMPRADOR')}
<div class="mir">«Mi papá tiene diabetes. Eso ya no se quita.»</div>
<h1 class="k">Casi la mitad de personas<br>con diabetes tipo 2 llegó<br>a <em>remisión en 1 año.</em></h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>The Lancet</i> 2018</span><span class="chip">306 adultos</span><span class="chip r">Ensayo al azar · diabetes de hasta 6 años</span></div>
<div class="est"><h4>De cada 100, azúcar normal sin medicinas <span>a los 12 meses</span></h4>
<div class="b2"><div class="w">Cuidado<small>habitual</small></div><div class="t"><div style="width:4%;background:var(--red)"></div></div><div class="n">4<small>de 100</small></div></div>
<div class="b2"><div class="w">Programa de<small>bajar de peso</small></div><div class="t"><div style="width:46%;background:var(--navy)"></div></div><div class="n">46<small>de 100</small></div></div>
<div class="b2"><div class="w">Bajaron<small>15 kg o más</small></div><div class="t"><div style="width:86%;background:var(--navy)"></div></div><div class="n">86<small>de 100</small></div></div></div>
<div class="ojo">«Eso ya no se quita.» <b>Remisión no es curación.</b></div>
<div class="sh">Entonces, ¿qué hago? <span>Con tu médico:</span></div>
<div class="yn"><div><i>1</i>Pregunta si este camino sirve en tu caso</div><div><i>2</i>Baja de peso con apoyo, no por tu cuenta</div><div><i>3</i>No dejes tus medicinas sin que te lo indiquen</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Funcionó con apoyo del equipo de salud.</b> <b class="y">Mándaselo a quien tiene diabetes en tu familia.</b></p></div>
<div class="foot"><div class="warn"><b>Un programa, 12 meses:</b> no es promesa ni vale para todos.<br>Sed intensa o confusión: 911.</div>
<div class="ref">Lean MEJ, et al. Lancet 2018;391:541-551<br>doi:10.1016/S0140-6736(17)33102-1<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def oidos(av):
    return f"""{S}<div class="wrap">{head(av,'ALCANCE')}
<div class="mir">«Subo el volumen para no oír la calle.»</div>
<h1 class="k"><em>1 de cada 4</em> jóvenes<br>usa los audífonos a un<br>volumen que daña el oído.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>BMJ Global Health</i> 2022</span><span class="chip">+19.000 jóvenes</span><span class="chip r">Metaanálisis · 12 a 34 años</span></div>
<div class="est"><h4>Jóvenes con escucha de riesgo <span>de cada 100</span></h4>
<div class="b2"><div class="w">Con<small>audífonos</small></div><div class="t"><div style="width:24%;background:var(--red)"></div></div><div class="n">24<small>de 100</small></div></div>
<div class="b2"><div class="w">Discotecas y<small>conciertos</small></div><div class="t"><div style="width:48%;background:var(--red)"></div></div><div class="n">48<small>de 100</small></div></div></div>
<div class="ojo">El oído no se avisa solo: <b>el daño por ruido se acumula</b> y no se recupera.</div>
<div class="sh">Entonces, ¿qué hago? <span>Desde hoy:</span></div>
<div class="yn"><div><i>1</i>Volumen a la mitad o menos del máximo</div><div><i>2</i>Descansa los oídos: pausas de unos minutos</div><div><i>3</i>En conciertos, lejos del parlante o con tapones</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Si hay zumbido</b> o los oídos quedan tapados después de escuchar, consulta. <b class="y">Mándaselo a quien duerme con los audífonos puestos.</b></p></div>
<div class="foot"><div class="warn"><b>Estimación de riesgo,</b> no pérdida confirmada. Cifra de locales<br>modelada. Si oyes menos de golpe: consulta ya.</div>
<div class="ref">Dillard LK, et al. BMJ Glob Health 2022;7(11):e010501<br>doi:10.1136/bmjgh-2022-010501<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

JOBS = {
    'dr-viera-0730-desayuno-mito': desayuno,
    'dr-viera-1230-diabetes-remision': diabetes,
    'dr-viera-1900-audifonos-volumen': oidos,
}
if __name__ == '__main__':
    render(JOBS, pathlib.Path(__file__).resolve().parents[1] / '2026-10-31')
