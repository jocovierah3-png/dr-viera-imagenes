# 27-nov-2026 · Modelo acv-v3, enfoque soluciones.
# 07:30 [MITO] «El celular al lado de la cama da cáncer en la cabeza.» Karipidis K, et al. Environ Int 2024;191:108983. doi:10.1016/j.envint.2024.108983 (revisión sistemática y metaanálisis de estudios observacionales encargada por la OMS; uso regular vs no uso: glioma mRR 1,01, IC 95 % 0,89-1,13; meningioma 0,92; sin asociación con 10+ años de uso; certeza moderada; hay críticas publicadas).
# 12:30 [COMPRADOR] «Si no me duele nada, ¿para qué me hago exámenes?» Shaukat A, et al. N Engl J Med 2013;369(12):1106-1114. doi:10.1056/NEJMoa1300720 (ensayo al azar de Minnesota, 46.551 adultos de 50-80 años, 30 años; mortalidad por cáncer colorrectal RR 0,68 (0,56-0,82) anual y 0,78 (0,65-0,93) bienal; mortalidad total sin cambio). Inicio a los 45: USPSTF, JAMA 2021;325(19):1965-1977.
# 19:00 [ALCANCE] «Almuerzo sin cola no es almuerzo.» Lara-Castor L, et al. Nat Med 2025;31(2):552-564. doi:10.1038/s41591-024-03345-4 (Global Dietary Database, 184 países, 2020; 2,2 M casos nuevos de diabetes tipo 2 = 9,8 % atribuibles a bebidas azucaradas; América Latina y el Caribe 24,4 %; estimación por modelos que supone causalidad; hay corrección publicada s41591-025-03524-x).
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'kit'))
from plantilla import *
import importlib.util
_s = importlib.util.spec_from_file_location('d26', str(pathlib.Path(__file__).with_name('2026-11-26.py')))
_m = importlib.util.module_from_spec(_s); _s.loader.exec_module(_m)
S, row = _m.S, _m.row

def celular(av):
    return f"""{S}<div class="wrap">{head(av,'MITO vs REALIDAD')}
<div class="mir">«No duermas con el celular al lado, que da cáncer en la cabeza.»</div>
<h1 class="k">La revisión pedida por la OMS:<br>usar celular <em>no subió</em> el riesgo<br>de cáncer en el cerebro.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>Environ Int</i> 2024</span><span class="chip">encargada por la OMS</span><span class="chip r">también con 10+ años de uso</span></div>
<div class="est"><h4>Riesgo de tumor cerebral (glioma) <span>(no usar = 100)</span></h4>
{row('No usan','celular','100',99,'--g2','')}{row('Usan celular','de forma regular','101',100,'--navy','')}
<div class="cur"><b>101 contra 100 es lo mismo: cabe en el azar.</b> Tampoco subió en quienes lo usaban hace 10 años o más.</div></div>
<div class="sh">Lo que sí cuida tu cabeza:</div>
<div class="yn"><div><i>1</i>Aleja el celular al dormir, pero por tu sueño, no por cáncer</div><div><i>2</i>Nunca lo mires al manejar: ese es el peligro real del celular</div><div><i>3</i>Casco siempre en moto y bici, aunque sea «una vueltita»</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Duerme tranquilo: el riesgo real está en la calle.</b> <b class="y">Mándaselo a tu mamá, la que te dice «aleja ese celular».</b></p></div>
<div class="foot"><div class="warn"><b>Revisión de estudios observacionales</b>, certeza moderada. Hay críticas publicadas; la OMS completará su evaluación final.</div>
<div class="ref">Karipidis K, et al. Environ Int<br>2024;191:108983<br>doi:10.1016/j.envint.2024.108983<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def colon(av):
    return f"""{S}<div class="wrap">{head(av,'DATO ÚTIL')}
<div class="mir">«Si no me duele nada, ¿para qué me hago exámenes?»</div>
<h1 class="k">Una prueba de heces <em>cada año</em><br>bajó 32 % las muertes por<br>cáncer de colon.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>N Engl J Med</i> 2013</span><span class="chip">46.551 personas · al azar</span><span class="chip r">30 años de seguimiento</span></div>
<div class="est"><h4>Muertes por cáncer de colon en 30 años <span>(sin prueba = 100)</span></h4>
{row('Sin prueba','no se revisaban','100',100,'--g2','')}{row('Cada 2 años','prueba de heces','78',78,'--navy','')}{row('Cada año','prueba de heces','68',68,'--grn','')}
<div class="cur"><b>Encuentra sangre escondida antes de que duela.</b> Si sale positiva, la colonoscopía saca los pólipos a tiempo.</div></div>
<div class="sh">Lo que puedes hacer este mes:</div>
<div class="yn"><div><i>1</i>Desde los 45, pide la prueba de sangre oculta en heces: es en casa</div><div><i>2</i>Si sale positiva, completa la colonoscopía: ese paso es el que salva</div><div><i>3</i>Sangre en las heces o cambios al ir al baño, a cualquier edad: consulta</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Una muestra pequeña, sin dolor, que puede salvar una vida.</b> <b class="y">¿Tus papás pasan de 45? Mándaselo y acompáñalos.</b></p></div>
<div class="foot"><div class="warn"><b>Ensayo al azar</b> en EE. UU. con adultos de 50 a 80 años. Empezar a los 45: Grupo de Prevención de EE. UU., 2021.</div>
<div class="ref">Shaukat A, et al. N Engl J Med<br>2013;369(12):1106-1114<br>doi:10.1056/NEJMoa1300720<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def gaseosa(av):
    return f"""{S}<div class="wrap">{head(av,'ESTUDIO','r')}
<div class="mir">«Almuerzo sin cola no es almuerzo.»</div>
<h1 class="k">En América Latina, <em>1 de cada 4</em><br>casos nuevos de diabetes se<br>atribuye a bebidas azucaradas.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>Nature Medicine</i> 2025</span><span class="chip">184 países</span><span class="chip r">la región más afectada</span></div>
<div class="est"><h4>De cada 100 casos nuevos de diabetes <span>(por bebidas con azúcar)</span></h4>
{row('En el mundo','promedio','10',41,'--navy','de 100')}{row('América Latina','y el Caribe','24',100,'--red','de 100')}
<div class="cur"><b>Si en tu barrio salen 4 casos nuevos de diabetes,</b> en 1 habrían pesado las gaseosas y jugos con azúcar.</div></div>
<div class="sh">Cambios fáciles desde hoy:</div>
<div class="yn"><div><i>1</i>Pon una jarra de agua fría con limón o hierbita en el almuerzo</div><div><i>2</i>Si no la dejas, pásala de todos los días a solo el fin de semana</div><div><i>3</i>Jugos de caja, energizantes y té embotellado también cuentan</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Cada cola que cambias por agua cuenta.</b> <b class="y">Etiqueta al amigo que no almuerza sin su cola.</b></p></div>
<div class="foot"><div class="warn"><b>Estimación con modelos</b> (datos de 2020): supone que la relación es causal; no mide caso por caso.</div>
<div class="ref">Lara-Castor L, et al. Nat Med<br>2025;31(2):552-564<br>doi:10.1038/s41591-024-03345-4<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

JOBS = {
    'dr-viera-0730-celular-cancer-mito': celular,
    'dr-viera-1230-prueba-heces-colon': colon,
    'dr-viera-1900-gaseosa-diabetes': gaseosa,
}
if __name__ == '__main__':
    render(JOBS, pathlib.Path(__file__).resolve().parents[1] / '2026-11-27')
