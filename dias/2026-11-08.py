# 8-nov-2026 · Modelo acv-v3, enfoque soluciones.
# 07:30 [MITO] «Tomo una aspirina al día para cuidar mi corazón.» McNeil JJ, et al. N Engl J Med 2018;379(16):1509-1518. doi:10.1056/NEJMoa1805819 (ASPREE: ensayo al azar, 19.114 adultos sanos 70+, mediana 4,7 años; enfermedad cardiovascular 10,7 vs 11,3 por 1.000 persona-año, HR 0,95 (0,83-1,08); hemorragia grave 8,6 vs 6,2, HR 1,38 (1,18-1,62)).
# 12:30 [COMPRADOR] «Mi presión es 135, para mi edad es normal.» SPRINT Research Group. N Engl J Med 2015;373:2103-2116. doi:10.1056/NEJMoa1511939 (ensayo al azar, 9.361 adultos 50+ con riesgo alto, sin diabetes ni derrame; meta <120 vs <140: 1,65 vs 2,19 por 100 persona-año, HR 0,75 (0,64-0,89); muerte HR 0,73 (0,60-0,90); más hipotensión, síncope, daño renal agudo).
# 19:00 [ALCANCE] «Duermo con la tele o la luz del pasillo encendida.» Windred DP, et al. Lancet Reg Health Eur 2024;42:100943. doi:10.1016/j.lanepe.2024.100943 (UK Biobank, 84.790 adultos, sensor de muñeca 1 semana, ~9 años; luz nocturna percentiles 50-70 / 70-90 / 90-100 vs 0-50: HR 1,29 / 1,39 / 1,53). Observacional.
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'kit'))
from plantilla import *
import importlib.util
_s = importlib.util.spec_from_file_location('d3', str(pathlib.Path(__file__).with_name('2026-11-03.py')))
_m = importlib.util.module_from_spec(_s); _s.loader.exec_module(_m)
S = _m.S

def aspirina(av):
    return f"""{S}<div class="wrap">{head(av,'MITO vs REALIDAD')}
<div class="mir">«Tomo una aspirina al día para cuidar mi corazón.»</div>
<h1 class="k">En adultos sanos,<br>la aspirina diaria <em>no<br>bajó</em> los problemas<br>del corazón y <em>sí</em> dio<br>más sangrados.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>N Engl J Med</i> 2018</span><span class="chip">19.114 personas de 70+ años</span><span class="chip r">ensayo al azar · 4,7 años</span></div>
<div class="est"><h4>Aspirina vs pastilla sin efecto <span>(por cada 1.000 personas al año)</span></h4>
<div class="cmp"><div class="gg"><b class="big">10,7 vs 11,3</b>problemas del corazón: sin diferencia clara</div><div class="rr"><b class="big">8,6 vs 6,2</b>sangrados graves: 38 % más con aspirina</div></div></div>
<div class="sh">Entonces, ¿qué hago? <span>Antes de tomarla "por si acaso":</span></div>
<div class="yn"><div><i>1</i>Pregunta a tu médico si a ti te toca, según tu riesgo</div><div><i>2</i>Ni empieces ni dejes la aspirina por tu cuenta</div><div><i>3</i>Cuida lo que sí ayuda: presión, azúcar, colesterol y caminar</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Pregunta, no adivines.</b> <b class="y">Mándaselo a quien toma una aspirina diaria «por si acaso».</b></p></div>
<div class="foot"><div class="warn"><b>Ensayo en adultos mayores sin infarto ni derrame previo:</b> no aplica si ya tuviste uno o si tu médico te la indicó. No la dejes sin consultar.</div>
<div class="ref">McNeil JJ, et al. N Engl J Med 2018;379:1509-1518<br>doi:10.1056/NEJMoa1805819<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def presion(av):
    def row(lbl, sub, n, pct, col):
        return f'<div class="b2"><div class="w">{lbl}<small>{sub}</small></div><div class="t"><div style="width:{pct}%;background:var({col})"></div></div><div class="n" style="font-size:46px;white-space:nowrap">{n}<small>por 1.000 al año</small></div></div>'
    return f"""{S}<div class="wrap">{head(av,'ESTUDIO')}
<div class="mir">«Mi presión está en 135 y, para mi edad, es normal.»</div>
<h1 class="k">Presión en 120 y no<br>en 140: <em>25 % menos</em><br>infartos y derrames.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>N Engl J Med</i> 2015</span><span class="chip">9.361 adultos de 50+ años</span><span class="chip r">ensayo al azar · 3,3 años</span></div>
<div class="est"><h4>Problemas graves del corazón <span>(meta de 140 vs meta de 120)</span></h4>
{row('Meta 140','presión de arriba','22',100,'--red')}{row('Meta 120','presión de arriba','16,5',75,'--grn')}</div>
<div class="ojo">Además, hubo <b>27 % menos muertes</b> en el grupo de la meta 120.</div>
<div class="sh">Entonces, ¿qué hago? <span>Esta semana:</span></div>
<div class="yn"><div><i>1</i>Mide tu presión en casa 2 veces al día por 7 días</div><div><i>2</i>Llévale esas cifras a tu médico y pregunta: «¿cuál es MI meta?»</div><div><i>3</i>Menos sal, caminar a diario y seguir el tratamiento indicado</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">¿Cuánto tiene de presión tu mamá o tu papá?</b> <b class="y">Mándaselo a tu familia y que se midan esta semana.</b></p></div>
<div class="foot"><div class="warn"><b>Personas de 50+ con riesgo alto, sin diabetes ni derrame previo.</b> La meta 120 tuvo más mareos, desmayos y daño del riñón. Tu médico define tu meta.</div>
<div class="ref">SPRINT Research Group. N Engl J Med 2015;373:2103-2116<br>doi:10.1056/NEJMoa1511939<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def luz(av):
    def row(lbl, sub, n, pct, col):
        return f'<div class="b2"><div class="w">{lbl}<small>{sub}</small></div><div class="t"><div style="width:{pct}%;background:var({col})"></div></div><div class="n" style="font-size:42px;white-space:nowrap">{n}<small>riesgo de diabetes</small></div></div>'
    return f"""{S}<div class="wrap">{head(av,'ESTUDIO NUEVO')}
<div class="mir">«Duermo con la tele o la luz del pasillo encendida.»</div>
<h1 class="k">Las noches con más luz<br>se asociaron a<br><em>53 % más</em> diabetes.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>Lancet Reg Health Eur</i> 2024</span><span class="chip">84.790 adultos · 9 años</span><span class="chip r">estudio observacional</span></div>
<div class="est"><h4>Según cuánta luz recibías de noche <span>(sensor en la muñeca)</span></h4>
{row('Noche oscura','la mitad más oscura','base',65,'--grn')}{row('Algo de luz','50 a 70 % de la gente','+29 %',84,'--red')}{row('Más luz','70 a 90 % de la gente','+39 %',91,'--red')}{row('Mucha luz','el 10 % más iluminado','+53 %',100,'--red')}</div>
<div class="sh">Entonces, ¿qué hago? <span>Gratis y desde esta noche:</span></div>
<div class="yn"><div><i>1</i>Duerme lo más oscuro posible: cortina gruesa o antifaz</div><div><i>2</i>Apaga tele y celular; si necesitas luz, que sea tenue</div><div><i>3</i>Si te levantas de noche, usa luz baja</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Apagar la luz no cuesta nada.</b> <b class="y">Mándaselo a quien duerme con la tele prendida.</b></p></div>
<div class="foot"><div class="warn"><b>Estudio observacional:</b> asociación, no causa. Falta probar si oscurecer el cuarto baja el riesgo.</div>
<div class="ref">Windred DP, et al. Lancet Reg Health Eur 2024;42:100943<br>doi:10.1016/j.lanepe.2024.100943<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

JOBS = {
    'dr-viera-0730-aspirina-diaria': aspirina,
    'dr-viera-1230-presion-meta-120': presion,
    'dr-viera-1900-luz-de-noche-diabetes': luz,
}
if __name__ == '__main__':
    render(JOBS, pathlib.Path(__file__).resolve().parents[1] / '2026-11-08')
