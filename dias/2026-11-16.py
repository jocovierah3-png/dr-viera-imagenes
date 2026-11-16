# 16-nov-2026 · Modelo acv-v3, enfoque soluciones.
# 07:30 [MITO] «Me pasé a la gaseosa sin azúcar para bajar de peso.» OMS. Use of non-sugar sweeteners: WHO guideline. Ginebra: OMS; 2023 (recomendación condicional: no usar edulcorantes sin azúcar para controlar el peso ni reducir riesgo de enfermedades; no aplica a personas con diabetes ya diagnosticada). Base: Rios-Leyvraz M, Montez J. Health effects of the use of non-sugar sweeteners: a systematic review and meta-analysis. OMS; 2022 (283 estudios; ensayos de 6-18 meses sin efecto claro en el peso; leve baja a corto plazo; certeza baja).
# 12:30 [COMPRADOR] «Tengo 42 y me siento bien; la mamografía es a los 50.» US Preventive Services Task Force. Nicholson WK, et al. JAMA 2024;331(22):1918-1930. doi:10.1001/jama.2024.5534 (recomendación B: mamografía cada 2 años de 40 a 74). Trentham-Dietz A, et al. JAMA 2024;331(22):1947-1960. doi:10.1001/jama.2023.24766 (6 modelos CISNET; muertes por cáncer de mama evitadas por 1.000 mujeres: desde 40 = 8,2; desde 50 = 6,7; 1.376 falsas alarmas por 1.000 en toda la vida de tamizaje).
# 19:00 [ALCANCE] «Me tomo un energizante para aguantar la tarde.» Kaldenbach S, Hysing M, Strand TA, Sivertsen B. BMJ Open 2024;14(2):e072951. doi:10.1136/bmjopen-2023-072951 (transversal, SHoT 2022; 53.266 estudiantes de 18-35, Noruega; diario vs rara vez/nunca: insomnio mujeres 51 vs 33 %, hombres 37 vs 22 %; ~30 min menos de sueño; menos de 6 h RR 2,07 hombres, 1,87 mujeres).
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'kit'))
from plantilla import *
import importlib.util
_s = importlib.util.spec_from_file_location('d13', str(pathlib.Path(__file__).with_name('2026-11-13.py')))
_m = importlib.util.module_from_spec(_s); _s.loader.exec_module(_m)
S, row = _m.S, _m.row

def light(av):
    return f"""{S}<div class="wrap">{head(av,'MITO vs REALIDAD')}
<div class="mir">«Me pasé a la gaseosa sin azúcar para bajar de peso.»</div>
<h1 class="k">La OMS <em>no</em> recomienda<br>los endulzantes sin azúcar<br>para bajar de peso.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>Guía OMS</i> 2023</span><span class="chip">283 estudios revisados</span><span class="chip r">certeza baja</span></div>
<div class="est"><h4>¿Ayudaron a bajar de peso?</h4>
<div class="cmp"><div class="gg"><b class="big">Al inicio</b>en semanas, una baja pequeña de peso</div><div class="rr"><b class="big">6 a 18 meses</b>sin efecto claro en el peso</div></div>
<div class="cur"><b>Lo que sí pasa:</b> el gusto por lo dulce sigue igual de fuerte.</div></div>
<div class="sh">Lo que sí funciona:</div>
<div class="yn"><div><i>1</i>Agua con limón, hierbas o fruta picada en vez de gaseosa</div><div><i>2</i>Baja el dulce poco a poco: media cucharadita menos cada semana</div><div><i>3</i>Fruta entera de postre en lugar de algo «light»</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Mejor que la gaseosa con azúcar, sí. Pero lo que te ayuda es el agua.</b> <b class="y">Mándaselo a quien compra todo «cero azúcar».</b></p></div>
<div class="foot"><div class="warn"><b>Recomendación condicional de la OMS.</b> No aplica a personas con diabetes ya diagnosticada: sigue lo que diga tu médico.</div>
<div class="ref">OMS. Use of non-sugar sweeteners:<br>WHO guideline. Ginebra; 2023<br>Rios-Leyvraz M, Montez J. OMS 2022<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def mamografia(av):
    return f"""{S}<div class="wrap">{head(av,'DATO ÚTIL')}
<div class="mir">«Tengo 42 y me siento bien. La mamografía es a los 50, ¿no?»</div>
<h1 class="k">Ahora se recomienda<br><em>desde los 40</em>, cada 2 años.<br>Sentirte bien no basta.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>JAMA</i> 2024</span><span class="chip">USPSTF · 6 modelos</span><span class="chip r">mujeres de 40 a 74</span></div>
<div class="est"><h4>Imagina 1.000 mujeres: <span>¿cuántas evitan morir de cáncer de mama?</span></h4>
{row('Empezando','a los 50','6,7',6.7/8.2*100,'--navy','de 1.000')}{row('Empezando','a los 40','8,2',100,'--grn','de 1.000')}</div>
<div class="qq"><div><b>SÍ/NO</b>¿Tienes 40 o más?</div><div><b>SÍ/NO</b>¿Nunca te la has hecho?</div><div><b>SÍ/NO</b>¿Mamá o hermana con cáncer de mama?</div><div><b>SÍ/NO</b>¿Notaste un bulto o cambio?</div></div>
<div class="sh">Si dijiste sí a alguna:</div>
<div class="yn"><div><i>1</i>Pide la orden de mamografía en tu próxima consulta</div><div><i>2</i>Con familiar con cáncer de mama o un bulto, no esperes: consulta ya</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Si te llaman para otra prueba, casi siempre no es cáncer.</b> <b class="y">Mándaselo a tu mamá, tu hermana o tu amiga de 40.</b></p></div>
<div class="foot"><div class="warn"><b>Estimación con modelos</b> (EE. UU.). Hay falsas alarmas. Tu médico ajusta la edad según tu riesgo.</div>
<div class="ref">US Preventive Services Task Force<br>JAMA 2024;331(22):1918-1930<br>doi:10.1001/jama.2024.5534<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def energizante(av):
    return f"""{S}<div class="wrap">{head(av,'ESTUDIO','r')}
<div class="mir">«Me tomo un energizante para aguantar la tarde.»</div>
<h1 class="k">Quienes los tomaban<br>a diario dormían <em>media hora</em><br><em>menos</em> cada noche.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>BMJ Open</i> 2024</span><span class="chip">53.266 estudiantes de 18 a 35</span><span class="chip r">Noruega</span></div>
<div class="est"><h4>Mujeres con insomnio <span>(en un aula de 30)</span></h4>
{row('Rara vez','o nunca','10',33/51*100,'--navy','de 30')}{row('Todos','los días','15',100,'--red','de 30')}
<div class="cur"><b>En hombres, igual:</b> 22 vs 37 de cada 100. Y el doble dormía menos de 6 horas.</div></div>
<div class="sh">Para tener energía sin la lata:</div>
<div class="yn"><div><i>1</i>Camina 10 minutos al aire libre cuando te baje la energía</div><div><i>2</i>Nada de energizantes ni café después de las 2 de la tarde</div><div><i>3</i>Acuéstate a la misma hora: el cansancio de la tarde baja</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Cansado → energizante → mal sueño → más cansado. Rompe el círculo.</b> <b class="y">Mándaselo a quien vive con una lata en la mano.</b></p></div>
<div class="foot"><div class="warn"><b>Encuesta en un solo momento:</b> asociación, no causa. Quien duerme mal también puede tomar más energizantes.</div>
<div class="ref">Kaldenbach S, et al.<br>BMJ Open 2024;14(2):e072951<br>doi:10.1136/bmjopen-2023-072951<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

JOBS = {
    'dr-viera-0730-endulzantes-peso': light,
    'dr-viera-1230-mamografia-40': mamografia,
    'dr-viera-1900-energizantes-sueno': energizante,
}
if __name__ == '__main__':
    render(JOBS, pathlib.Path(__file__).resolve().parents[1] / '2026-11-16')
