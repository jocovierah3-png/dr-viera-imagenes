# 4-nov-2026 · Modelo acv-v3, enfoque soluciones.
# 07:30 [MITO] «Mi vecino adelgazó ayunando.» Garegnani LI, et al. Cochrane Database Syst Rev 2026;(2):CD015610. doi:10.1002/14651858.CD015610.pub2 (22 ensayos al azar, 1.995 adultos; vs consejo dietético normal, diferencia en peso menor a 1 %, certeza baja)
# 12:30 [COMPRADOR] «Llevo meses durmiendo mal.» Trauer JM, et al. Ann Intern Med 2015;163(3):191-204. doi:10.7326/M14-2841 (20 estudios, 1.162 adultos; dormirse 19 min antes, 26 min menos despierto)
# 19:00 [ALCANCE] «Hoy como lo que sea: snacks, gaseosa, comida lista.» Lane MM, et al. BMJ 2024;384:e077310. doi:10.1136/bmj-2023-077310 (revisión paraguas, 45 análisis, 9.888.373 personas; 32 con asociación; trastornos mentales comunes OR 1,53)
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'kit'))
from plantilla import *
import importlib.util
_s = importlib.util.spec_from_file_location('d3', str(pathlib.Path(__file__).with_name('2026-11-03.py')))
_m = importlib.util.module_from_spec(_s); _s.loader.exec_module(_m)
S = _m.S

def ayuno(av):
    return f"""{S}<div class="wrap">{head(av,'MITO vs REALIDAD')}
<div class="mir">«Mi vecino adelgazó ayunando; yo también tengo que ayunar.»</div>
<h1 class="k">Ayunar no adelgaza<br><em>más</em> que comer normal<br>con menos calorías.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>Cochrane</i> 2026</span><span class="chip">22 ensayos al azar · 1.995 adultos</span><span class="chip r">certeza baja</span></div>
<div class="est"><h4>Ayuno intermitente vs. plan de comida normal <span>(adultos con sobrepeso)</span></h4>
<div class="cmp"><div class="rr"><b class="big">Menos de 1 kg</b>de diferencia si pesas 100 kg</div><div class="gg"><b class="big">Igual</b>calidad de vida en ambos grupos</div></div></div>
<div class="ojo">No hay prueba de que ayunar haga daño. Solo que <b>no mostró ganar</b> a comer normal con menos calorías.</div>
<div class="sh">Entonces, ¿qué hago? <span>Escoge lo que sí puedas mantener:</span></div>
<div class="yn"><div><i>1</i>Ayunar o comer 3 veces: elige lo que cumples meses</div><div><i>2</i>Llena la mitad del plato con verduras</div><div><i>3</i>Camina 30 minutos casi todos los días</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Con diabetes, embarazo o medicinas,</b> consulta antes de ayunar. <b class="y">Mándaselo a quien cuenta las horas sin comer.</b></p></div>
<div class="foot"><div class="warn"><b>Revisión de ensayos:</b> evidencia de certeza baja; pocos estudios largos.<br>Vale para adultos con sobrepeso u obesidad.</div>
<div class="ref">Garegnani LI, et al. Cochrane Database Syst Rev 2026;(2):CD015610<br>doi:10.1002/14651858.CD015610.pub2<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def insomnio(av):
    return f"""{S}<div class="wrap">{head(av,'COMPRADOR')}
<div class="mir">«Llevo meses durmiendo mal, pero no sé qué hacer.»</div>
<h1 class="k">Insomnio de meses:<br>te duermes <em>19 minutos</em><br>antes, sin pastillas.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>Ann Intern Med</i> 2015</span><span class="chip">20 estudios · 1.162 adultos</span><span class="chip r">terapia para dormir</span></div>
<div class="est"><h4>Con terapia cognitivo-conductual <span>(comparado con no recibirla)</span></h4>
<div class="b2"><div class="w">Tardas en dormirte<small>cada noche</small></div><div class="t"><div style="width:66%;background:var(--grn)"></div></div><div class="n">19<small>minutos menos</small></div></div>
<div class="b2"><div class="w">Despierto de noche<small>cada noche</small></div><div class="t"><div style="width:90%;background:var(--grn)"></div></div><div class="n">26<small>minutos menos</small></div></div></div>
<div class="ojo">El total de horas dormidas cambió poco: <b>lo que mejora es dormirte antes y despertar menos.</b></div>
<div class="sh">Entonces, ¿qué hago? <span>Empieza esta semana:</span></div>
<div class="yn"><div><i>1</i>Levántate a la misma hora todos los días</div><div><i>2</i>Cama solo para dormir; sin sueño, sal un rato</div><div><i>3</i>Pregunta a tu médico por la terapia para el insomnio</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Si llevas 3 meses o más</b> durmiendo mal, consúltalo. <b class="y">¿Quién en tu casa da vueltas en la cama? Mándaselo.</b></p></div>
<div class="foot"><div class="warn"><b>Metaanálisis:</b> adultos con insomnio crónico, edad media 56 años.<br>No incluye insomnio ligado a otras enfermedades.</div>
<div class="ref">Trauer JM, et al. Ann Intern Med 2015;163(3):191-204<br>doi:10.7326/M14-2841<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def ultra(av):
    pp = ''.join('<i class="r"></i>' if k < 32 else '<i></i>' for k in range(45))
    return f"""{S}<div class="wrap">{head(av,'ESTUDIO NUEVO')}
<div class="mir">«Hoy como lo que sea: snacks, gaseosa, comida lista.»</div>
<h1 class="k">De <em>45</em> resultados<br>revisados, <em>32</em> se ligaron<br>a los ultraprocesados.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>BMJ</i> 2024</span><span class="chip">9,9 millones de personas</span><span class="chip r">revisión paraguas</span></div>
<div class="est"><h4>Cada cuadro es un resultado de salud <span>(rojo: se ligó a más riesgo)</span></h4>
<style>.u i{{height:24px!important;border-radius:6px!important}}.u i:before{{display:none!important}}</style><div class="ppl u" style="grid-template-columns:repeat(15,1fr);gap:8px;margin-top:16px">{pp}</div>
<div class="mf"><div><b>53 %</b>más: ansiedad o depresión</div><div><b style="font-size:28px">Convincente</b>muerte por el corazón</div></div></div>
<div class="ojo">Es asociación: <b>quien come más ultraprocesados también vive distinto.</b></div>
<div class="sh">Entonces, ¿qué hago? <span>Cambia uno, no todo:</span></div>
<div class="yn"><div><i>1</i>Cambia 1 por día: gaseosa por agua, snack por fruta</div><div><i>2</i>Si la etiqueta es larguísima, déjalo para ocasiones</div><div><i>3</i>Cocina el domingo para 3 días</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">No tienes que ser perfecto:</b> menos veces ya es avance. <b class="y">Mándaselo a tu amigo que vive de snacks.</b></p></div>
<div class="foot"><div class="warn"><b>Observacional:</b> asociación, no causa; certeza varía por resultado.<br>Ej.: galletas, gaseosas, embutidos, snacks, sopas instantáneas.</div>
<div class="ref">Lane MM, et al. BMJ 2024;384:e077310<br>doi:10.1136/bmj-2023-077310<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

JOBS = {
    'dr-viera-0730-ayuno-intermitente': ayuno,
    'dr-viera-1230-insomnio-terapia': insomnio,
    'dr-viera-1900-ultraprocesados': ultra,
}
if __name__ == '__main__':
    render(JOBS, pathlib.Path(__file__).resolve().parents[1] / '2026-11-04')
