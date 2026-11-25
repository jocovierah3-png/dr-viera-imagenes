# 25-nov-2026 · Modelo acv-v3, enfoque soluciones.
# 07:30 [MITO] «Dejé el pan porque el gluten inflama.» Lebwohl B, et al. BMJ 2017;357:j1892. doi:10.1136/bmj.j1892 (cohortes NHS + HPFS, 64.714 mujeres + 45.303 hombres sin celiaquía, 1986-2010, 26 años; quintil más alto vs más bajo de gluten: enfermedad coronaria HR 0,95; IC 95 % 0,88-1,02; observacional).
# 12:30 [COMPRADOR] «Mi papá tiene diabetes, pero los pies no le duelen.» Armstrong DG, Boulton AJM, Bus SA. N Engl J Med 2017;376:2367-2375. doi:10.1056/NEJMra1615439 (revisión: úlcera de pie en la vida 19-34 % de personas con diabetes; recurrencia ~40 % al año de sanar).
# 19:00 [ALCANCE] «Vivo cansada; debe ser el trabajo.» Stevens GA, et al. Lancet Glob Health 2022;10(5):e627-e639. doi:10.1016/S2214-109X(22)00084-5 (197 países, 2000-2019; anemia en mujeres no embarazadas de 15-49: 31 % → 30 %; embarazadas 36 % en 2019).
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'kit'))
from plantilla import *
import importlib.util
_s = importlib.util.spec_from_file_location('d22', str(pathlib.Path(__file__).with_name('2026-11-22.py')))
_m = importlib.util.module_from_spec(_s); _s.loader.exec_module(_m)
S, row = _m.S, _m.row

def gluten(av):
    return f"""{S}<div class="wrap">{head(av,'MITO vs REALIDAD')}
<div class="mir">«Dejé el pan porque el gluten inflama. Ahora como más sano.»</div>
<h1 class="k">Si no eres celíaco,<br>dejar el gluten <em>no cuidó<br>más tu corazón.</em></h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>BMJ</i> 2017</span><span class="chip">110.017 adultos · 26 años</span><span class="chip r">estudio observacional</span></div>
<div class="est"><h4>Riesgo de enfermedad del corazón <span>(los que menos gluten comían = 100)</span></h4>
{row('Menos gluten','1 de cada 5 que menos comía','100',100,'--g2','')}{row('Más gluten','1 de cada 5 que más comía','95',95,'--navy','')}
<div class="cur"><b>Prácticamente igual.</b> Y quien deja el gluten suele dejar también los cereales integrales, que sí cuidan el corazón.</div></div>
<div class="sh">Lo que sí te sirve:</div>
<div class="yn"><div><i>1</i>Si el pan te cae mal, no lo dejes por tu cuenta: pide antes la prueba de celiaquía</div><div><i>2</i>Cambia pan blanco por integral, avena o quinua</div><div><i>3</i>«Sin gluten» no quiere decir sin azúcar ni «light»: lee la etiqueta</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">El problema no es el gluten: es el pan blanco y el dulce.</b> <b class="y">Mándaselo a quien dejó el pan «porque inflama».</b></p></div>
<div class="foot"><div class="warn"><b>Estudio observacional</b> en EE. UU.: asociación, no causa. Con celiaquía, el gluten sí se evita.</div>
<div class="ref">Lebwohl B, et al. BMJ<br>2017;357:j1892<br>doi:10.1136/bmj.j1892<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def pies(av):
    return f"""{S}<div class="wrap">{head(av,'DATO ÚTIL')}
<div class="mir">«Mi papá tiene diabetes, pero los pies no le duelen.»</div>
<h1 class="k">Con diabetes, <em>hasta 1 de<br>cada 3</em> tendrá una herida<br>en el pie. Muchas no duelen.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>N Engl J Med</i> 2017</span><span class="chip">revisión de estudios</span><span class="chip r">personas con diabetes</span></div>
<div class="est"><h4>De cada 100 personas con diabetes <span>(pie diabético)</span></h4>
{row('En su vida','tendrán una herida','19 a 34',34,'--red','de 100')}{row('Le vuelve','al año de haber sanado','40',40,'--red','de 100')}
<div class="cur"><b>¿Por qué no duele?</b> El azúcar alta daña los nervios: una piedrita en el zapato o una ampolla pasan sin sentirse.</div></div>
<div class="sh">Lo que lo protege, desde hoy:</div>
<div class="yn"><div><i>1</i>Mírale los pies cada noche: planta y entre los dedos</div><div><i>2</i>Nada de andar descalzo; revisa el zapato por dentro antes de ponérselo</div><div><i>3</i>Pide que el médico le revise los pies en cada control</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">1 minuto cada noche cuida sus pies.</b> <b class="y">Mándaselo a quien cuida a su papá o mamá con diabetes.</b></p></div>
<div class="foot"><div class="warn"><b>Herida que no sana,</b> se pone roja, caliente o huele mal: al médico ese mismo día.</div>
<div class="ref">Armstrong DG, et al. N Engl J Med<br>2017;376:2367-2375<br>doi:10.1056/NEJMra1615439<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def anemia(av):
    return f"""{S}<div class="wrap">{head(av,'ESTUDIO','r')}
<div class="mir">«Vivo cansada. Debe ser el trabajo… o el estrés.»</div>
<h1 class="k"><em>3 de cada 10</em> mujeres<br>de 15 a 49 años tienen<br>anemia en el mundo.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>Lancet Glob Health</i> 2022</span><span class="chip">197 países · 2000-2019</span><span class="chip r">estimación mundial</span></div>
<div class="est"><h4>Mujeres de 15 a 49 años con anemia <span>(de cada 100)</span></h4>
{row('Año 2000','sin embarazo','31',31,'--red','de 100')}{row('Año 2019','sin embarazo','30',30,'--red','de 100')}
<div class="cur"><b>En 20 años casi no bajó.</b> En un grupo de WhatsApp de 30 amigas, serían 9.</div></div>
<div class="sh">¿Te pasa? Responde Sí o No:</div>
<div class="yn"><div><i>?</i>Te falta el aire al subir escaleras, más que antes</div><div><i>?</i>Tu regla es abundante o dura más de 7 días</div><div><i>?</i>Estás pálida, se te quiebran las uñas o tienes las manos frías</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">2 o más Sí: pide un examen de sangre (hemograma); no tomes hierro por tu cuenta.</b> <b class="y">Mándaselo a la amiga que siempre dice «estoy cansada».</b></p></div>
<div class="foot"><div class="warn"><b>Estimación mundial;</b> en Ecuador puede variar. El cansancio tiene muchas causas: el examen lo aclara.</div>
<div class="ref">Stevens GA, et al. Lancet Glob Health<br>2022;10(5):e627-e639<br>doi:10.1016/S2214-109X(22)00084-5<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

JOBS = {
    'dr-viera-0730-gluten-mito': gluten,
    'dr-viera-1230-pie-diabetico': pies,
    'dr-viera-1900-anemia-cansancio': anemia,
}
if __name__ == '__main__':
    render(JOBS, pathlib.Path(__file__).resolve().parents[1] / '2026-11-25')
