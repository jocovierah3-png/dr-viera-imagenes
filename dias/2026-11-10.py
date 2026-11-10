# 10-nov-2026 · Modelo acv-v3, enfoque soluciones.
# 07:30 [MITO] «Tomo omega 3 para cuidar mi corazón.» Abdelhamid AS, et al. Cochrane Database Syst Rev 2020;3:CD003177. doi:10.1002/14651858.CD003177.pub5 (86 ensayos al azar, 162.796 personas; muertes por cualquier causa RR 0,97 (0,93-1,01)). Cifras por búsqueda web (PubMed bloqueado).
# 12:30 [COMPRADOR] «Mis papás comen normal; a su edad ya qué.» Estruch R, et al. N Engl J Med 2018;378:e34. doi:10.1056/NEJMoa1800389 (PREDIMED: ensayo al azar, 7.447 adultos 55-80 con riesgo alto, ~4,8 años; infarto, derrame o muerte cardiovascular: aceite de oliva HR 0,69 (0,53-0,91); frutos secos HR 0,72 (0,54-0,95)).
# 19:00 [ALCANCE] «Es solo una temporada; trabajo 12 horas y aguanto.» Pega F, et al. Environ Int 2021;154:106595. doi:10.1016/j.envint.2021.106595 (OMS/OIT: 55 h o más por semana vs 35-40 h; derrame RR 1,35 (1,13-1,61); corazón RR 1,17; 745.194 muertes en 2016, estimación). Observacional. IC del corazón no verificado.
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'kit'))
from plantilla import *
import importlib.util
_s = importlib.util.spec_from_file_location('d3', str(pathlib.Path(__file__).with_name('2026-11-03.py')))
_m = importlib.util.module_from_spec(_s); _s.loader.exec_module(_m)
S = _m.S

def omega(av):
    return f"""{S}<div class="wrap">{head(av,'MITO vs REALIDAD')}
<div class="mir">«Tomo omega 3 para cuidar mi corazón.»</div>
<h1 class="k">Las cápsulas de omega 3<br><em>no</em> bajaron las muertes<br>en 86 estudios<br>con 162.796 personas.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>Cochrane</i> 2020</span><span class="chip">86 ensayos al azar</span><span class="chip r">revisión sistemática</span></div>
<div class="est"><h4>Muertes por cualquier causa: omega 3 vs sin omega 3 <span>(riesgo relativo, 1,00 = igual)</span></h4>
<div class="cmp"><div class="gg"><b class="big">0,97</b>casi igual: el rango 0,93 a 1,01 incluye 1,00</div><div class="rr"><b class="big">162.796</b>personas en total, con poca o ninguna diferencia</div></div></div>
<div class="sh">Entonces, ¿qué hago? <span>Para cuidar tu corazón:</span></div>
<div class="yn"><div><i>1</i>Come pescado, sardina o atún, 2 veces por semana</div><div><i>2</i>Camina 30 minutos y revisa tu presión, azúcar y colesterol</div><div><i>3</i>Si tu médico te las indicó, no las dejes sin consultar</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">La comida y el movimiento rinden más que la cápsula.</b> <b class="y">Mándaselo a quien compra omega 3 «para el corazón».</b></p></div>
<div class="foot"><div class="warn"><b>Habla de cápsulas, no de comer pescado.</b> No aplica si tu médico las indicó (por ejemplo, triglicéridos muy altos). No dejes tratamientos por tu cuenta.</div>
<div class="ref">Abdelhamid AS, et al. Cochrane Database Syst Rev 2020;3:CD003177<br>doi:10.1002/14651858.CD003177.pub5<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def medit(av):
    def row(lbl, sub, n, pct, col):
        return f'<div class="b2"><div class="w">{lbl}<small>{sub}</small></div><div class="t"><div style="width:{pct}%;background:var({col})"></div></div><div class="n" style="font-size:46px;white-space:nowrap">{n}<small>infartos o derrames</small></div></div>'
    return f"""{S}<div class="wrap">{head(av,'ESTUDIO')}
<div class="mir">«Mis papás comen normal; a su edad ya qué.»</div>
<h1 class="k">Comida mediterránea:<br>cerca de <em>30 % menos</em><br>infartos y derrames.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>N Engl J Med</i> 2018</span><span class="chip">7.447 adultos de 55 a 80 años</span><span class="chip r">ensayo al azar · 4,8 años</span></div>
<div class="est"><h4>Por cada 100 con dieta baja en grasa <span>(riesgo relativo)</span></h4>
{row('Baja en grasa','comparación','100',100,'--red')}{row('Aceite de oliva','y mediterránea','69',69,'--grn')}{row('Frutos secos','y mediterránea','72',72,'--grn')}</div>
<div class="sh">Entonces, ¿qué hago? <span>Para ellos y para ti:</span></div>
<div class="yn"><div><i>1</i>Legumbres, pescado, fruta y verdura cada día</div><div><i>2</i>Un puñado de frutos secos y aceite de oliva a diario</div><div><i>3</i>Menos embutidos, gaseosas y fritos</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">¿Qué come hoy tu papá o tu mamá?</b> <b class="y">Mándaselo y cambien una comida esta semana.</b></p></div>
<div class="foot"><div class="warn"><b>Adultos de 55 a 80 años con riesgo alto, en España.</b> Con alergia a frutos secos, evítalos.</div>
<div class="ref">Estruch R, et al. N Engl J Med 2018;378:e34<br>doi:10.1056/NEJMoa1800389<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def horas(av):
    def row(lbl, sub, n, pct, col):
        return f'<div class="b2"><div class="w">{lbl}<small>{sub}</small></div><div class="t"><div style="width:{pct}%;background:var({col})"></div></div><div class="n" style="font-size:46px;white-space:nowrap">{n}<small>por cada 100</small></div></div>'
    return f"""{S}<div class="wrap">{head(av,'ESTUDIO')}
<div class="mir">«Es solo una temporada: trabajo 12 horas y aguanto.»</div>
<h1 class="k">Trabajar 55 horas o más<br>por semana: <em>35 % más</em><br>riesgo de derrame cerebral.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>Environ Int</i> 2021</span><span class="chip">OMS y OIT · 745.194 muertes (2016)</span><span class="chip r">estudios observacionales</span></div>
<div class="est"><h4>Frente a trabajar 35 a 40 horas <span>(riesgo relativo)</span></h4>
{row('35 a 40 horas','horario normal','100',74,'--grn')}{row('55 horas o más','derrame cerebral','135',100,'--red')}{row('55 horas o más','enfermedad del corazón','117',87,'--red')}</div>
<div class="sh">Entonces, ¿qué hago? <span>Desde esta semana:</span></div>
<div class="yn"><div><i>1</i>Levántate 5 minutos cada 2 horas</div><div><i>2</i>Elige un día sin trabajo y apaga el celular de trabajo al salir</div><div><i>3</i>Mídete la presión y el azúcar, aunque seas joven</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Pausar también es parte del trabajo.</b> <b class="y">Mándaselo a quien siempre dice «yo aguanto».</b></p></div>
<div class="foot"><div class="warn"><b>Estudios observacionales:</b> asociación, no causa. Quien trabaja tanto puede dormir y moverse menos.</div>
<div class="ref">Pega F, et al. Environ Int 2021;154:106595<br>doi:10.1016/j.envint.2021.106595<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

JOBS = {
    'dr-viera-0730-omega-3-corazon': omega,
    'dr-viera-1230-dieta-mediterranea-papas': medit,
    'dr-viera-1900-trabajar-55-horas': horas,
}
if __name__ == '__main__':
    render(JOBS, pathlib.Path(__file__).resolve().parents[1] / '2026-11-10')
