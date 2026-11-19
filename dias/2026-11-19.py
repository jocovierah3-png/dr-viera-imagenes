# 19-nov-2026 · Modelo acv-v3, enfoque soluciones.
# 07:30 [MITO] «Uso sal rosada porque es más sana.» Fayet-Moore F, Wibisono C, Carr P, et al. Foods 2020;9(10):1490. doi:10.3390/foods9101490 (análisis de laboratorio de 31 sales rosadas en Australia; 1 cucharadita aporta 1-5 % de lo que se necesita al día de magnesio, calcio, potasio; harían falta ~30 g/día, unas 6 cucharaditas, para que los minerales aporten algo; una muestra con plomo sobre el límite). OMS: menos de 5 g de sal al día.
# 12:30 [COMPRADOR · ¿Normal o lo reviso?] «Mi esposo ronca y a veces deja de respirar.» Young T, Evans L, Finn L, Palta M. Sleep 1997;20(9):705-706. doi:10.1093/sleep/20.9.705 (Wisconsin Sleep Cohort; 4.925 adultos trabajadores, polisomnografía en 1.090; apnea moderada o grave sin diagnóstico: 82 % hombres, 93 % mujeres). Preguntas basadas en STOP-Bang: Chung F, et al. Anesthesiology 2008;108(5):812-821.
# 19:00 [ALCANCE] «Caliento mi almuerzo en el táper.» Hussain KA, et al. Environ Sci Technol 2023 (laboratorio; envases de polipropileno y polietileno aprobados para comida; 3 min a máxima potencia: hasta 4,22 millones de microplásticos y 2.110 millones de nanoplásticos por cm²; DOI no verificado). Marfella R, et al. N Engl J Med 2024;390:900-910. doi:10.1056/NEJMoa2309822 (observacional; 257 personas operadas de placa de carótida; con plástico en la placa 30/150 = 20 % vs sin plástico 8/107 = 7,5 % infarto, derrame o muerte en ~34 meses; HR 4,53, IC 2,00-10,27).
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'kit'))
from plantilla import *
import importlib.util
_s = importlib.util.spec_from_file_location('d18', str(pathlib.Path(__file__).with_name('2026-11-18.py')))
_m = importlib.util.module_from_spec(_s); _s.loader.exec_module(_m)
S, row = _m.S, _m.row

def sal(av):
    return f"""{S}<div class="wrap">{head(av,'MITO vs REALIDAD')}
<div class="mir">«Yo uso sal rosada porque es más sana.»</div>
<h1 class="k">Sí trae minerales… pero para<br>que te sirvan tendrías que comer<br><em>6 cucharaditas al día</em>.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>Foods</i> 2020</span><span class="chip">31 sales rosadas analizadas</span><span class="chip r">laboratorio · Australia</span></div>
<div class="est"><h4>Cucharaditas de sal al día</h4>
{row('Lo máximo','que recomienda la OMS','1',1/6*100,'--grn','cdta')}{row('Para que sus','minerales sirvan','6',100,'--red','cdtas')}
<div class="cur"><b>Rosada o blanca, es casi pura sal.</b> 1 cucharadita da solo 1 a 5 % de los minerales del día.</div></div>
<div class="sh">Lo que sí cuida tu presión:</div>
<div class="yn"><div><i>1</i>Sea cual sea la sal: máximo 1 cucharadita al día, sumando todo</div><div><i>2</i>Saca el salero de la mesa y prueba antes de echar</div><div><i>3</i>Dale sabor con limón, ajo, cebolla, culantro o comino</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Los minerales vienen de frutas, verduras y granos, no del salero.</b> <b class="y">Mándaselo a quien compró sal rosada «por salud».</b></p></div>
<div class="foot"><div class="warn"><b>Análisis de laboratorio</b> de sales vendidas en Australia; una muestra tenía plomo sobre el límite. Con presión alta o problemas de riñón, pregunta a tu médico cuánta sal.</div>
<div class="ref">Fayet-Moore F, et al.<br>Foods 2020;9(10):1490<br>doi:10.3390/foods9101490<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def ronca(av):
    return f"""{S}<div class="wrap">{head(av,'¿NORMAL O LO REVISO?')}
<div class="mir">«Mi esposo ronca como tractor… y a ratos deja de respirar.»</div>
<h1 class="k">De cada 10 hombres con apnea<br>del sueño moderada o grave,<br><em>8 no sabían que la tenían</em>.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>Sleep</i> 1997</span><span class="chip">4.925 adultos que trabajaban</span><span class="chip r">estudio de sueño</span></div>
<div class="est"><h4>Con apnea moderada o grave, <span>¿cuántos no tenían diagnóstico?</span></h4>
{row('Hombres','','82',82/93*100,'--navy','de 100')}{row('Mujeres','','93',100,'--red','de 100')}</div>
<div class="sh">Roncar solo, suele ser normal. <span>Revísalo si hay SÍ:</span></div>
<div class="qq"><div><b>SÍ/NO</b>¿Ronca tan fuerte que se oye con la puerta cerrada?</div><div><b>SÍ/NO</b>¿Alguien lo vio dejar de respirar dormido?</div><div><b>SÍ/NO</b>¿Amanece cansado o se duerme sentado de día?</div><div><b>SÍ/NO</b>¿Tiene presión alta?</div></div>
<div class="yn"><div><i>1</i>Con 2 o más SÍ: pide al médico un estudio del sueño</div><div><i>2</i>Si le da sueño manejando, que se detenga y descanse</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">La apnea tiene tratamiento y se vuelve a dormir bien.</b> <b class="y">Mándaselo a quien duerme junto a alguien que ronca.</b></p></div>
<div class="foot"><div class="warn"><b>Estudio de población en EE. UU.</b> Preguntas basadas en el cuestionario STOP-Bang: orientan, no diagnostican.</div>
<div class="ref">Young T, et al.<br>Sleep 1997;20(9):705-706<br>doi:10.1093/sleep/20.9.705<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def taper(av):
    return f"""{S}<div class="wrap">{head(av,'ESTUDIO','r')}
<div class="mir">«Caliento mi almuerzo en el táper, en el microondas.»</div>
<h1 class="k">3 minutos de microondas:<br>el táper soltó <em>millones</em> de<br>partículas de plástico.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>Environ Sci Technol</i> 2023</span><span class="chip">envases aprobados para comida</span><span class="chip r">laboratorio</span></div>
<div class="cmp"><div class="rr"><b class="big">4 millones</b>microplásticos por cm² de envase</div><div class="rr"><b class="big">2.000 millones</b>partículas aún más pequeñas</div></div>
<div class="est"><h4>¿Y en personas? <span>infarto, derrame o muerte (<i>NEJM</i> 2024)</span></h4>
{row('Placa','sin plástico','7,5',7.5/20*100,'--navy','de 100')}{row('Placa','con plástico','20',100,'--red','de 100')}</div>
<div class="sh">Fácil de cambiar desde hoy:</div>
<div class="yn"><div><i>1</i>Pasa la comida a un plato de vidrio o loza para calentarla</div><div><i>2</i>No metas tarrinas ni botellas plásticas al microondas</div><div><i>3</i>Para llevar el almuerzo: envase de vidrio o acero</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">El táper para llevar; el plato para calentar.</b> <b class="y">Mándaselo a tu compañero de almuerzo.</b></p></div>
<div class="foot"><div class="warn"><b>Medición de laboratorio</b>: aún no se sabe cuánto daño hace en personas. <i>NEJM</i>: adultos mayores con placa en la carótida; se asoció, no prueba causa.</div>
<div class="ref">Hussain KA, et al. Environ Sci Technol 2023<br>Marfella R, et al. N Engl J Med 2024;390:900-910<br>doi:10.1056/NEJMoa2309822<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

JOBS = {
    'dr-viera-0730-sal-rosada': sal,
    'dr-viera-1230-ronquido-apnea': ronca,
    'dr-viera-1900-taper-microondas': taper,
}
if __name__ == '__main__':
    render(JOBS, pathlib.Path(__file__).resolve().parents[1] / '2026-11-19')
