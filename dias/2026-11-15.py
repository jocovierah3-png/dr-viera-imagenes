# 15-nov-2026 · Modelo acv-v3, enfoque soluciones.
# 07:30 [MITO] «Hago 100 abdominales diarios para bajar la barriga.» Ramirez-Campillo R, Andrade DC, Clemente FM, Afonso J, Pérez-Castilla A, Gentil P. Human Movement 2021;23(3):1-14. doi:10.5114/hm.2022.110373 (revisión sistemática con metaanálisis; 13 estudios, 1.158 personas; ES -0,03, IC -0,10 a 0,05; 37 comparaciones: 17 a favor de la zona entrenada, 20 de la no entrenada; la mayoría entrenó un brazo o una pierna). Ramírez-Campillo R, et al. J Strength Cond Res 2013 (11 personas; entrenar una pierna 12 semanas: la grasa bajó en brazos y tronco).
# 12:30 [COMPRADOR · ¿Normal o lo reviso?] «Ceno tarde, me acuesto y me sube el ardor.» Fujiwara Y, et al. Am J Gastroenterol 2005;100(12):2633-2636. doi:10.1111/j.1572-0241.2005.00354.x (casos y controles, Japón; 147 con reflujo y 294 controles; cena menos de 3 h antes de dormir vs 4 h o más: OR 7,45, IC 3,38-16,4, ajustado por tabaco, alcohol e IMC). Eusebi LH, et al. Gut 2018;67(3):430-440. doi:10.1136/gutjnl-2016-313589 (108 poblaciones, 460.984 personas; acidez o regurgitación semanal 13,3 %, IC 12,0-14,6). Katz PO, et al. ACG Am J Gastroenterol 2022;117:27-56 (evitar comer 2-3 h antes de acostarse, elevar cabecera, signos de alarma: dificultad para tragar, pérdida de peso, sangrado).
# 19:00 [ALCANCE] «Me llevo el celular al baño… y se me pasa el tiempo.» Ramprasad C, et al. PLoS One 2025;20(9):e0329983. doi:10.1371/journal.pone.0329983 (transversal; 125 adultos con colonoscopia de tamizaje, Boston; 66 % usaba el celular en el inodoro; hemorroides 46 % más riesgo ajustado por edad, sexo, IMC, ejercicio, pujo y fibra, p=0,044; más de 5 min por visita 37,3 % vs 7,1 %, p=0,006; pujar no se asoció).
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'kit'))
from plantilla import *
import importlib.util
_s = importlib.util.spec_from_file_location('d13', str(pathlib.Path(__file__).with_name('2026-11-13.py')))
_m = importlib.util.module_from_spec(_s); _s.loader.exec_module(_m)
S, row = _m.S, _m.row

def abdominales(av):
    return f"""{S}<div class="wrap">{head(av,'MITO vs REALIDAD')}
<div class="mir">«Hago 100 abdominales diarios para bajar la barriga.»</div>
<h1 class="k">Ejercitar una zona <em>no</em> le<br>quitó la grasa a esa zona.<br>La grasa baja de todo el cuerpo.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>Human Movement</i> 2021</span><span class="chip">13 estudios · 1.158 personas</span><span class="chip r">revisión de estudios</span></div>
<div class="est"><h4>37 comparaciones: ¿dónde se perdió más grasa?</h4>
{row('En la zona','entrenada','17',17/20*100,'--g2','veces')}{row('En la zona','sin entrenar','20',100,'--navy','veces')}
<div class="cur"><b>Como lanzar una moneda.</b> Y quien entrenó solo una pierna por 12 semanas perdió grasa… en los brazos y el tronco.</div></div>
<div class="sh">Lo que sí baja la barriga:</div>
<div class="yn"><div><i>1</i>Camina rápido o trota 30 minutos casi todos los días</div><div><i>2</i>Fuerza de cuerpo entero: sentadillas y flexiones, 2 a 3 veces por semana</div><div><i>3</i>Cambia las bebidas azucaradas por agua y duerme 7 horas</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Los abdominales sí sirven: dan fuerza y cuidan la espalda.</b> <b class="y">Mándaselo a quien hace abdominales cada noche.</b></p></div>
<div class="foot"><div class="warn"><b>Revisión de estudios:</b> la mayoría entrenó un brazo o una pierna; pocos midieron la barriga. Algún estudio pequeño sí vio un efecto local.</div>
<div class="ref">Ramirez-Campillo R, et al.<br>Human Movement 2021;23(3):1-14<br>doi:10.5114/hm.2022.110373<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def acidez(av):
    return f"""{S}<div class="wrap">{head(av,'¿NORMAL O LO REVISO?')}
<div class="mir">«Ceno tarde, me acuesto… y me sube el ardor al pecho.»</div>
<h1 class="k">Cenar <em>menos de 3 horas</em><br>antes de dormir se asoció<br>con 7 veces más reflujo.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>Am J Gastroenterol</i> 2005</span><span class="chip">441 adultos · Japón</span><span class="chip r">13 de cada 100 adultos cada semana</span></div>
<div class="est"><h4>Probabilidad de tener reflujo, según la hora de la cena</h4>
{row('Cenó 4 horas','o más antes de dormir','1',1/7.45*100,'--navy','vez')}{row('Cenó menos de','3 horas antes','7,5',100,'--red','veces')}</div>
<div class="nv"><div class="a"><h5>NORMAL</h5>De vez en cuando, tras una comida pesada, y se calma.</div><div class="b"><h5>REVÍSALO</h5>Casi a diario, cuesta tragar, bajas de peso sin querer o heces negras.</div></div>
<div class="sh">Lo que ayuda desde hoy:</div>
<div class="yn"><div><i>1</i>Cena 3 horas antes de acostarte, o algo liviano</div><div><i>2</i>Sube la cabecera de la cama con bloques bajo las patas</div><div><i>3</i>Anota qué comida te da ardor y evítala</div></div>
<div class="help w"><div class="ic">!</div><p><b class="y">Ardor con falta de aire, sudor frío o dolor al brazo: 911, puede ser el corazón.</b> ¿Tu papá vive con acidez? Mándaselo.</p></div>
<div class="foot"><div class="warn"><b>Casos y controles (147 con reflujo, 294 sin él):</b> asociación, no causa. Cifra semanal: <i>Gut</i> 2018, 460.984 personas. Guía ACG 2022.</div>
<div class="ref">Fujiwara Y, et al.<br>Am J Gastroenterol 2005;100(12):2633-6<br>doi:10.1111/j.1572-0241.2005.00354.x<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def celular(av):
    return f"""{S}<div class="wrap">{head(av,'ESTUDIO','r')}
<div class="mir">«Me llevo el celular al baño… y se me pasa el tiempo.»</div>
<h1 class="k">Usar el celular en el baño<br>se asoció con <em>46 % más</em><br>riesgo de hemorroides.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>PLOS ONE</i> 2025</span><span class="chip">125 adultos con colonoscopia</span><span class="chip r">2 de cada 3 lo hacían</span></div>
<div class="est"><h4>Se quedaban sentados más de 5 minutos <span>(de cada 100)</span></h4>
{row('Con','celular','37',100,'--red','de 100')}{row('Sin','celular','7',7.1/37.3*100,'--navy','de 100')}
<div class="cur"><b>Lo curioso:</b> pujar no marcó la diferencia. El tiempo sentado, sí.</div></div>
<div class="sh">La regla de los 5 minutos:</div>
<div class="yn"><div><i>1</i>Deja el celular fuera del baño</div><div><i>2</i>Si en 5 minutos no pasa nada, levántate y vuelve más tarde</div><div><i>3</i>Frutas, verduras, granos y agua para no tener que pujar</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Mucho rato en el inodoro aprieta las venas de esa zona.</b> <b class="y">Mándaselo a quien se demora 20 minutos en el baño.</b></p></div>
<div class="foot"><div class="warn"><b>Estudio transversal y pequeño:</b> asociación, no causa. Cada persona contó sus hábitos. ¿Sangrado al ir al baño? Revísalo con tu médico.</div>
<div class="ref">Ramprasad C, et al.<br>PLoS One 2025;20(9):e0329983<br>doi:10.1371/journal.pone.0329983<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

JOBS = {
    'dr-viera-0730-abdominales-barriga': abdominales,
    'dr-viera-1230-acidez-cena': acidez,
    'dr-viera-1900-celular-bano': celular,
}
if __name__ == '__main__':
    render(JOBS, pathlib.Path(__file__).resolve().parents[1] / '2026-11-15')
