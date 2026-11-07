# 7-nov-2026 · Modelo acv-v3, enfoque soluciones.
# 07:30 [MITO] «Uso lentes con filtro de luz azul para que no me cansen los ojos.» Singh S, et al. Cochrane Database Syst Rev 2023;(8):CD013244.pub2 (17 estudios, 619 personas; sin mejoría clara del cansancio de ojos con pantalla; sueño: resultados mixtos; riesgo de sesgo alto).
# 12:30 [COMPRADOR] «Mi peso es normal, así que estoy bien.» Browning LM, Hsieh SD, Ashwell M. Nutr Res Rev 2010;23(2):247-269. doi:10.1017/S0954422410000144 (78 estudios; cintura/estatura mejor o igual que cintura e IMC para predecir diabetes y enfermedad del corazón; valor límite promedio 0,50 en hombres y mujeres; AUROC 0,704 vs 0,693 vs 0,671). Observacional/transversal.
# 19:00 [ALCANCE] «Vivo estresado y no tengo tiempo para meditar.» Balban MY, et al. Cell Rep Med 2023;4(1):100895 (ensayo al azar a distancia, ~108 adultos, 28 días, 5 min al día; suspiro cíclico mejoró más el ánimo y bajó más la frecuencia respiratoria que meditación). Réplica independiente sin publicar dudó del efecto en ánimo. DOI no verificado: PubMed bloqueado.
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'kit'))
from plantilla import *
import importlib.util
_s = importlib.util.spec_from_file_location('d3', str(pathlib.Path(__file__).with_name('2026-11-03.py')))
_m = importlib.util.module_from_spec(_s); _s.loader.exec_module(_m)
S = _m.S

def luz(av):
    return f"""{S}<div class="wrap">{head(av,'MITO vs REALIDAD')}
<div class="mir">«Uso lentes con filtro de luz azul para que no me cansen los ojos.»</div>
<h1 class="k">Los lentes de luz azul<br><em>no mostraron</em> menos<br>cansancio de ojos.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>Cochrane</i> 2023</span><span class="chip">17 estudios · 619 personas</span><span class="chip r">pruebas pequeñas y cortas</span></div>
<div class="est"><h4>Al comparar con lentes comunes <span>(uso de computadora)</span></h4>
<div class="cmp"><div class="gg"><b class="big">Sin mejoría clara</b>en el cansancio de los ojos</div><div class="rr"><b class="big">Sueño: sin claridad</b>los resultados fueron mixtos</div></div></div>
<div class="ojo">No es que dañen: <b>el cansancio viene de mirar fijo y de cerca</b>, no solo del color de la luz.</div>
<div class="sh">Entonces, ¿qué hago? <span>Cuida tus ojos gratis:</span></div>
<div class="yn"><div><i>1</i>Cada 20 minutos mira algo lejano por 20 segundos</div><div><i>2</i>Parpadea más y aleja la pantalla a un brazo</div><div><i>3</i>Si te arden o ves borroso seguido, revisa tu vista</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Ahorra el gasto</b> y haz la pausa de 20 segundos. <b class="y">Mándaselo a quien pasa el día frente al computador.</b></p></div>
<div class="foot"><div class="warn"><b>Ensayos pequeños, calidad limitada:</b> no prueban que sean inútiles en todo caso.<br>Si tienes dolor de ojos o visión que cambia, consulta.</div>
<div class="ref">Singh S, et al. Cochrane Database Syst Rev 2023;(8):CD013244<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def cintura(av):
    def row(alt, cint, pct):
        return f'<div class="b2"><div class="w">Mides {alt} cm<small>de estatura</small></div><div class="t"><div style="width:{pct}%;background:var(--grn)"></div></div><div class="n" style="font-size:42px;white-space:nowrap">{cint}<small>cm de cintura</small></div></div>'
    return f"""{S}<div class="wrap">{head(av,'DATO ÚTIL')}
<div class="mir">«Mi peso es normal, así que estoy bien.»</div>
<h1 class="k">Tu cintura debe medir<br><em>menos de la mitad</em><br>de tu estatura.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>Nutr Res Rev</i> 2010</span><span class="chip">78 estudios</span><span class="chip r">mismo límite: 0,5 en hombres y mujeres</span></div>
<div class="est"><h4>Tu límite en centímetros <span>(la mitad de tu estatura)</span></h4>
{row(160,'80',50)}{row(170,'85',50)}{row(180,'90',50)}</div>
<div class="ojo">Predijo mejor <b>diabetes y corazón</b> que el peso solo.</div>
<div class="sh">Entonces, ¿qué hago? <span>Hoy, 2 minutos:</span></div>
<div class="yn"><div><i>1</i>Cinta a la altura del ombligo, sin apretar, al soltar el aire</div><div><i>2</i>Divide tu cintura entre tu estatura: menos de 0,5 es buena señal</div><div><i>3</i>Si pasa de 0,5, pide que te midan presión y azúcar</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">¿Cuánto mide la cintura de tus papás?</b> <b class="y">Mándaselo a tu hermano y midan a la familia.</b></p></div>
<div class="foot"><div class="warn"><b>Revisión de estudios observacionales:</b> es una pista de riesgo, no un diagnóstico.<br>Para adultos; no aplica a niños ni a embarazadas.</div>
<div class="ref">Browning LM, et al. Nutr Res Rev 2010;23:247-269<br>doi:10.1017/S0954422410000144<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def suspiro(av):
    return f"""{S}<div class="wrap">{head(av,'ESTUDIO')}
<div class="mir">«Vivo estresado y no tengo tiempo para meditar.»</div>
<h1 class="k">5 minutos de respiración<br>al día mejoraron<br>el <em>ánimo</em> en 1 mes.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>Cell Rep Med</i> 2023</span><span class="chip">unos 100 adultos · 28 días</span><span class="chip r">ensayo al azar</span></div>
<div class="est"><h4>Respiración con suspiro vs meditación <span>(5 min al día)</span></h4>
<div class="cmp"><div class="gg"><b class="big">Más ánimo</b>que con meditación</div><div class="gg"><b class="big">Menos respiraciones</b>por minuto en reposo</div></div></div>
<div class="ojo">Se llama <b>suspiro cíclico</b>: una exhalación larga y lenta. Cualquiera puede hacerlo sentado.</div>
<div class="sh">Entonces, ¿qué hago? <span>Pruébalo hoy:</span></div>
<div class="yn"><div><i>1</i>Inhala por la nariz y suma una segunda inhalación corta</div><div><i>2</i>Suelta el aire largo y lento por la boca</div><div><i>3</i>Repite 5 minutos, a la misma hora cada día</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Cinco minutos, sin app ni dinero.</b> <b class="y">Mándaselo al amigo que siempre anda estresado.</b></p></div>
<div class="foot"><div class="warn"><b>Ensayo pequeño y a distancia:</b> el efecto fue modesto y falta confirmarlo.<br>No reemplaza ayuda profesional si la ansiedad es fuerte.</div>
<div class="ref">Balban MY, et al. Cell Rep Med 2023;4(1):100895<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

JOBS = {
    'dr-viera-0730-lentes-luz-azul': luz,
    'dr-viera-1230-cintura-mitad-estatura': cintura,
    'dr-viera-1900-suspiro-ciclico': suspiro,
}
if __name__ == '__main__':
    render(JOBS, pathlib.Path(__file__).resolve().parents[1] / '2026-11-07')
