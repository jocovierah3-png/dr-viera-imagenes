# 26-nov-2026 · Modelo acv-v3, enfoque soluciones.
# 07:30 [MITO] «El desodorante da cáncer de mama.» Mirick DK, Davis S, Thomas DB. J Natl Cancer Inst 2002;94(20):1578-1580. doi:10.1093/jnci/94.20.1578 (casos y controles poblacional, Seattle; 813 mujeres con cáncer de mama y 793 sin cáncer, 20-74 años; antitranspirante OR 0,9, p=0,23; desodorante OR 1,2, p=0,19; aplicar en la hora tras afeitarse: OR 0,9 y 1,2, sin aumento). NCI/ACS: sin evidencia de relación.
# 12:30 [COMPRADOR] «Mi mamá solo se cayó… y se rompió la cadera.» USPSTF. JAMA 2025;333(6):498-508. doi:10.1001/jama.2024.27154 (osteoporosis 27,1 % mujeres y 5,7 % hombres de 65+; tamizaje con densitometría en mujeres 65+ y posmenopáusicas <65 con riesgo, grado B; hombres, grado I).
# 19:00 [ALCANCE] «Soy joven, estoy bien.» Krishnan V, ..., Lloyd-Jones DM. Circ Popul Health Outcomes 2026 (AHA, 20-ago-2026; FF-CHAYA, 1.283 adultos, media 22,9 años, transversal; etapa CKM 0: 20,7 %, 1: 40,2 %, 2: 36,2 %, 3: 2,8 %; 79,2 % en etapas 1-3; más grosor de la carótida en etapas 1-3; población con más desventaja social; DOI no verificado: red bloqueada).
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'kit'))
from plantilla import *
import importlib.util
_s = importlib.util.spec_from_file_location('d22', str(pathlib.Path(__file__).with_name('2026-11-22.py')))
_m = importlib.util.module_from_spec(_s); _s.loader.exec_module(_m)
S, row = _m.S, _m.row

def desodorante(av):
    return f"""{S}<div class="wrap">{head(av,'MITO vs REALIDAD')}
<div class="mir">«Deja ese desodorante, que da cáncer de mama.»</div>
<h1 class="k">En 1.606 mujeres, usar<br>desodorante <em>no subió</em> el<br>riesgo de cáncer de mama.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>J Natl Cancer Inst</i> 2002</span><span class="chip">813 con cáncer · 793 sin</span><span class="chip r">20 a 74 años</span></div>
<div class="est"><h4>Riesgo de cáncer de mama <span>(no usar = 100)</span></h4>
{row('No usar','ni desodorante ni antitranspirante','100',83,'--g2','')}{row('Antitranspirante','a diario','90',75,'--navy','')}{row('Desodorante','a diario','120',100,'--navy','')}
<div class="cur"><b>Ni 90 ni 120 son diferencias reales: caben en el azar.</b> Tampoco al ponerlo justo después de afeitarse.</div></div>
<div class="sh">Lo que sí cuida tus mamas:</div>
<div class="yn"><div><i>1</i>Si notas una bolita o un cambio en tus mamas, consulta pronto</div><div><i>2</i>Desde los 40, pregunta por tu mamografía cada 2 años</div><div><i>3</i>Muévete a diario y toma poco alcohol o nada</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Usa el desodorante tranquila: el cuidado está en revisarte.</b> <b class="y">Mándaselo a la tía que reenvía la cadena en WhatsApp.</b></p></div>
<div class="foot"><div class="warn"><b>Estudio de casos y controles</b> en EE. UU.: asociación, no causa. El Instituto Nacional del Cáncer de EE. UU. tampoco halla relación.</div>
<div class="ref">Mirick DK, et al. J Natl Cancer Inst<br>2002;94(20):1578-1580<br>doi:10.1093/jnci/94.20.1578<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def huesos(av):
    return f"""{S}<div class="wrap">{head(av,'DATO ÚTIL')}
<div class="mir">«Mi mamá solo se resbaló… y se rompió la cadera.»</div>
<h1 class="k">Después de los 65, <em>1 de cada 4</em><br>mujeres tiene huesos frágiles<br>y no le duele nada.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>JAMA</i> 2025</span><span class="chip">Grupo de Prevención de EE. UU.</span><span class="chip r">osteoporosis</span></div>
<div class="est"><h4>De cada 100 personas de 65 años o más <span>(con osteoporosis)</span></h4>
{row('Mujeres','65 años o más','27',27,'--red','de 100')}{row('Hombres','65 años o más','6',6,'--navy','de 100')}
<div class="cur"><b>La primera señal suele ser la fractura.</b> Si tu mamá y 3 tías pasan de 65, a una le puede estar pasando.</div></div>
<div class="sh">Lo que la protege, desde hoy:</div>
<div class="yn"><div><i>1</i>Desde los 65, pide su densitometría: rápida y sin dolor</div><div><i>2</i>Antes de los 65, si ya tuvo una fractura o es muy delgada, pregunta</div><div><i>3</i>Fuerza y equilibrio en casa: pararse de la silla sin manos, 10 veces</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Saberlo a tiempo permite proteger sus huesos.</b> <b class="y">Mándaselo a tus hermanos: ¿quién lleva a mamá?</b></p></div>
<div class="foot"><div class="warn"><b>Datos de EE. UU.</b>; en Ecuador puede variar. Si se encorvó o perdió estatura, coméntalo en su control.</div>
<div class="ref">US Preventive Services Task Force.<br>JAMA 2025;333(6):498-508<br>doi:10.1001/jama.2024.27154<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def jovenes(av):
    return f"""{S}<div class="wrap">{head(av,'ESTUDIO','r')}
<div class="mir">«Tengo 23 años. Eso del corazón es para viejos.»</div>
<h1 class="k"><em>8 de cada 10</em> jóvenes de 23<br>ya tenían señales de riesgo<br>en corazón, riñón y azúcar.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>Circulation</i> 2026</span><span class="chip">1.283 jóvenes · EE. UU.</span><span class="chip r">edad media 23 años</span></div>
<div class="est"><h4>De cada 100 jóvenes de 23 años <span>(etapas del riesgo)</span></h4>
{row('Sin señales','todo en orden','21',42,'--grn','de 100')}{row('Grasa de más','sobrepeso o barriga','40',80,'--red','de 100')}{row('Presión, azúcar','o grasas en sangre altas','36',72,'--red','de 100')}
<div class="cur"><b>En tu promoción de 30, serían 24.</b> Y 3 de cada 100 ya tenían daño temprano.</div></div>
<div class="sh">Lo que te pone de vuelta en verde:</div>
<div class="yn"><div><i>1</i>Mide tu cintura: menos de la mitad de tu estatura</div><div><i>2</i>Pide presión, azúcar y colesterol, aunque te sientas bien</div><div><i>3</i>Camina 30 minutos al día y duerme 7 horas</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">A los 23 casi todo esto tiene vuelta atrás.</b> <b class="y">Mándaselo a tu pana que dice «estoy joven».</b></p></div>
<div class="foot"><div class="warn"><b>Estudio transversal:</b> asociación, no causa. Muchos participantes con menos recursos; en otros grupos puede variar.</div>
<div class="ref">Krishnan V, Lloyd-Jones DM, et al.<br>Circ Popul Health Outcomes 2026<br>American Heart Association, ago-2026<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

JOBS = {
    'dr-viera-0730-desodorante-mito': desodorante,
    'dr-viera-1230-huesos-mama': huesos,
    'dr-viera-1900-jovenes-riesgo': jovenes,
}
if __name__ == '__main__':
    render(JOBS, pathlib.Path(__file__).resolve().parents[1] / '2026-11-26')
