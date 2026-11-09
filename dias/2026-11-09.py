# 9-nov-2026 · Modelo acv-v3, enfoque soluciones.
# 07:30 [MITO] «Tomo vitamina D para que no se me rompan los huesos.» LeBoff MS, et al. N Engl J Med 2022;387(4):299-309. doi:10.1056/NEJMoa2202106 (VITAL: ensayo al azar, 25.871 adultos sanos, mediana 5,3 años; fracturas totales HR 0,98 (0,89-1,08); cadera HR 1,01 (0,70-1,47)). DOI por búsqueda web (PubMed bloqueado).
# 12:30 [COMPRADOR] «Me cepillo los dientes; el hilo dental no lo uso.» Philip N, et al. J Am Dent Assoc 2025;156(1):17-27. doi:10.1016/j.adaj.2024.09.017 (NHANES 2009-2016, ~18.801 adultos; hilo diario vs no usarlo, muerte por enfermedad del corazón HR 0,64 (0,49-0,84)). Observacional. Cifras por búsqueda web (PubMed bloqueado).
# 19:00 [ALCANCE] «Me tomo un café a las 4 de la tarde y duermo igual.» Gardiner C, et al. Sleep Med Rev 2023;69:101764. doi:10.1016/j.smrv.2023.101764 (revisión sistemática y metaanálisis, 24 estudios; cafeína: 45 min menos de sueño, 9 min más para dormirse, 12 min más despierto; café al menos 8,8 h antes de acostarse). Cifras por búsqueda web.
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'kit'))
from plantilla import *
import importlib.util
_s = importlib.util.spec_from_file_location('d3', str(pathlib.Path(__file__).with_name('2026-11-03.py')))
_m = importlib.util.module_from_spec(_s); _s.loader.exec_module(_m)
S = _m.S

def vitd(av):
    return f"""{S}<div class="wrap">{head(av,'MITO vs REALIDAD')}
<div class="mir">«Tomo vitamina D para que no se me rompan los huesos.»</div>
<h1 class="k">En adultos sanos,<br>la vitamina D <em>no<br>bajó</em> las fracturas<br>frente a una pastilla<br>sin efecto.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>N Engl J Med</i> 2022</span><span class="chip">25.871 adultos sanos</span><span class="chip r">ensayo al azar · 5,3 años</span></div>
<div class="est"><h4>Fracturas: vitamina D vs pastilla sin efecto <span>(riesgo relativo, 1,00 = igual)</span></h4>
<div class="cmp"><div class="gg"><b class="big">0,98</b>todas las fracturas: sin diferencia</div><div class="rr"><b class="big">1,01</b>fractura de cadera: sin diferencia</div></div></div>
<div class="sh">Entonces, ¿qué hago? <span>Para cuidar tus huesos:</span></div>
<div class="yn"><div><i>1</i>Camina y haz ejercicio de fuerza: los huesos se fortalecen con uso</div><div><i>2</i>Come lácteos, huevo, pescado y verdes; toma sol con prudencia</div><div><i>3</i>Si tienes osteoporosis o te falta vitamina D, que tu médico decida</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Primero movimiento y comida, luego pastillas.</b> <b class="y">Mándaselo a quien compra vitaminas «por si acaso».</b></p></div>
<div class="foot"><div class="warn"><b>Adultos sin déficit conocido:</b> no aplica a quien tiene osteoporosis, déficit comprobado o tratamiento indicado. No dejes nada sin consultar.</div>
<div class="ref">LeBoff MS, et al. N Engl J Med 2022;387:299-309<br>doi:10.1056/NEJMoa2202106<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def hilo(av):
    def row(lbl, sub, n, pct, col):
        return f'<div class="b2"><div class="w">{lbl}<small>{sub}</small></div><div class="t"><div style="width:{pct}%;background:var({col})"></div></div><div class="n" style="font-size:46px;white-space:nowrap">{n}<small>muertes del corazón</small></div></div>'
    return f"""{S}<div class="wrap">{head(av,'ESTUDIO')}
<div class="mir">«Me cepillo los dientes, pero el hilo dental no lo uso.»</div>
<h1 class="k">Quienes usaban hilo<br>dental cada día tuvieron<br><em>36 % menos</em> muertes<br>por el corazón.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>J Am Dent Assoc</i> 2025</span><span class="chip">cerca de 18.800 adultos</span><span class="chip r">estudio observacional · EE. UU.</span></div>
<div class="est"><h4>Por cada 100 de quienes no usaban hilo <span>(riesgo relativo)</span></h4>
{row('Sin hilo dental','base','100',100,'--red')}{row('Hilo todos los días','usuarios diarios','64',64,'--grn')}</div>
<div class="sh">Entonces, ¿qué hago? <span>Toma 2 minutos:</span></div>
<div class="yn"><div><i>1</i>Usa hilo dental una vez al día, antes de dormir</div><div><i>2</i>Cepíllate 2 veces al día y pide cita con el dentista este año</div><div><i>3</i>Si las encías sangran siempre, no lo ignores: consulta</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">¿Hace cuánto no va al dentista tu papá o tu mamá?</b> <b class="y">Mándaselo y pídeles cita esta semana.</b></p></div>
<div class="foot"><div class="warn"><b>Estudio observacional:</b> asociación, no causa. Quien usa hilo quizá cuide más su salud en general.</div>
<div class="ref">Philip N, et al. J Am Dent Assoc 2025;156(1):17-27<br>doi:10.1016/j.adaj.2024.09.017<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def cafe(av):
    def row(lbl, sub, n, pct, col):
        return f'<div class="b2"><div class="w">{lbl}<small>{sub}</small></div><div class="t"><div style="width:{pct}%;background:var({col})"></div></div><div class="n" style="font-size:46px;white-space:nowrap">{n}<small>con cafeína</small></div></div>'
    return f"""{S}<div class="wrap">{head(av,'ESTUDIO')}
<div class="mir">«Me tomo un café a las 4 de la tarde y duermo igual.»</div>
<h1 class="k">El café de la tarde<br>te quita <em>45 minutos</em><br>de sueño, aunque<br>«duermas igual».</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>Sleep Med Rev</i> 2023</span><span class="chip">24 estudios reunidos</span><span class="chip r">revisión sistemática</span></div>
<div class="est"><h4>Cambios en la noche con cafeína <span>(promedio de los estudios)</span></h4>
{row('Sueño total','minutos menos','45 min',100,'--red')}{row('Despierto','minutos más','12 min',27,'--red')}{row('Al dormirte','minutos más','9 min',20,'--red')}</div>
<div class="sh">Entonces, ¿qué hago? <span>Gratis y desde hoy:</span></div>
<div class="yn"><div><i>1</i>Tu último café, al menos 9 horas antes de acostarte</div><div><i>2</i>Si duermes a las 22:00, corta a las 13:00</div><div><i>3</i>Después: agua o infusión sin cafeína</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Cambiar la hora del café cuesta cero.</b> <b class="y">Mándaselo a quien dice «yo con café duermo normal».</b></p></div>
<div class="foot"><div class="warn"><b>Estudios cortos, varios en laboratorio:</b> el efecto varía según la persona y la cantidad.</div>
<div class="ref">Gardiner C, et al. Sleep Med Rev 2023;69:101764<br>doi:10.1016/j.smrv.2023.101764<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

JOBS = {
    'dr-viera-0730-vitamina-d-fracturas': vitd,
    'dr-viera-1230-hilo-dental-corazon': hilo,
    'dr-viera-1900-cafe-tarde-sueno': cafe,
}
if __name__ == '__main__':
    render(JOBS, pathlib.Path(__file__).resolve().parents[1] / '2026-11-09')
