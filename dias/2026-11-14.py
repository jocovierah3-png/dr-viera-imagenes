# 14-nov-2026 · Modelo acv-v3, enfoque soluciones.
# 07:30 [MITO] «No corro porque me voy a gastar las rodillas.» Alentorn-Geli E, et al. J Orthop Sports Phys Ther 2017;47(6):373-390. doi:10.2519/jospt.2017.7137 (revisión sistemática y metaanálisis; 17 estudios, 114.829 personas; artritis de cadera o rodilla 3,5 % en corredores recreativos, 10,2 % en sedentarios y 13,3 % en corredores de competencia; recreativos vs controles OR 0,86, IC 0,69-1,07; observacional, sin ajuste por lesiones previas ni peso).
# 12:30 [COMPRADOR] «Mi papá sube el volumen de la tele… y dice que oye bien.» Jiang F, et al. Lancet Public Health 2023;8(5):e329-e338. doi:10.1016/S2468-2667(23)00048-8 (UK Biobank, 437.704 adultos; pérdida auditiva sin audífono HR 1,42, IC 1,29-1,56; con audífono HR 1,04, IC 0,98-1,10; 88 % de quienes oían mal no usaban audífono; observacional).
# 19:00 [ALCANCE] «En TikTok dicen que la ducha fría te hace inmune.» Buijze GA, et al. PLoS One 2016;11(9):e0161749. doi:10.1371/journal.pone.0161749 (ensayo al azar sin cegamiento, 3.018 adultos de 18-65, Países Bajos; final frío de 30, 60 o 90 s por 30 días; faltas al trabajo por enfermedad IRR 0,71, 29 % menos; días enfermo sin diferencia; duración sin diferencia).
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'kit'))
from plantilla import *
import importlib.util
_s = importlib.util.spec_from_file_location('d13', str(pathlib.Path(__file__).with_name('2026-11-13.py')))
_m = importlib.util.module_from_spec(_s); _s.loader.exec_module(_m)
S, row = _m.S, _m.row

def rodillas(av):
    return f"""{S}<div class="wrap">{head(av,'MITO vs REALIDAD')}
<div class="mir">«No corro porque me voy a gastar las rodillas.»</div>
<h1 class="k">Correr por gusto <em>no</em> se<br>asoció con más artritis<br>de rodilla o cadera.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>J Orthop Sports Phys Ther</i> 2017</span><span class="chip">17 estudios · 114.829 personas</span></div>
<div class="est"><h4>Artritis de rodilla o cadera <span>(de cada 100 personas)</span></h4>
{row('Corren','por gusto','3,5',3.5/13.3*100,'--navy','de 100')}{row('No hacen','ejercicio','10',10.2/13.3*100,'--g2','de 100')}{row('Atletas','de competencia','13',100,'--red','de 100')}</div>
<div class="sh">Cómo empezar sin lastimarte:</div>
<div class="yn"><div><i>1</i>Alterna 1 minuto trotando y 2 caminando</div><div><i>2</i>Sube el tiempo poco a poco, semana a semana</div><div><i>3</i>10 sentadillas a una silla, 3 veces por semana</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">El cartílago necesita movimiento para mantenerse sano.</b> <b class="y">Mándaselo a quien dice que correr «gasta» las rodillas.</b></p></div>
<div class="foot"><div class="warn"><b>Estudios observacionales:</b> asociación, no causa. No midieron lesiones previas ni peso. ¿Rodilla hinchada, que se traba o duele al apoyar? Revísala.</div>
<div class="ref">Alentorn-Geli E, et al.<br>J Orthop Sports Phys Ther 2017;47(6):373-390<br>doi:10.2519/jospt.2017.7137<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def oido(av):
    return f"""{S}<div class="wrap">{head(av,'DATO ÚTIL')}
<div class="mir">«Mi papá sube el volumen de la tele… y dice que oye bien.»</div>
<h1 class="k">Oír mal sin audífono:<br><em>42 % más</em> riesgo de demencia.<br>Con audífono, sin riesgo extra.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>Lancet Public Health</i> 2023</span><span class="chip">437.704 adultos</span><span class="chip r">Reino Unido</span></div>
<div class="est"><h4>Por cada 100 casos de demencia en quien oye bien:</h4>
{row('Oye bien','','100',100/142*100,'--g2','casos')}{row('Oye mal','sin audífono','142',100,'--red','casos')}{row('Oye mal','con audífono','104',104/142*100,'--navy','casos')}</div>
<div class="sh">¿Le pasa a alguien en tu casa? <span>Un SÍ basta para revisarlo</span></div>
<div class="qq"><div><b>SÍ/NO</b>¿Sube mucho la tele?</div><div><b>SÍ/NO</b>¿Pide que le repitan?</div><div><b>SÍ/NO</b>¿Se pierde si hay ruido?</div><div><b>SÍ/NO</b>¿Responde otra cosa?</div></div>
<div class="yn" style="margin-top:14px"><div><i>✓</i>Pide una prueba de audición; si le indican audífono, que lo use a diario</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Solo 12 de cada 100 que oían mal usaban audífono.</b> <b class="y">¿Tus papás oyen bien la tele? Mándaselo a tus hermanos.</b></p></div>
<div class="foot"><div class="warn"><b>Estudio observacional:</b> asociación, no causa. Voluntarios del Reino Unido; quien usa audífono puede tener otras ventajas.</div>
<div class="ref">Jiang F, et al.<br>Lancet Public Health 2023;8(5):e329-e338<br>doi:10.1016/S2468-2667(23)00048-8<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def ducha(av):
    return f"""{S}<div class="wrap">{head(av,'TENDENCIA vs CIENCIA')}
<div class="mir">«En TikTok dicen que la ducha fría te hace inmune.»</div>
<h1 class="k">No evitó enfermarse…<br>pero faltaron al trabajo<br><em>29 % menos</em> días.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>PLOS ONE</i> 2016</span><span class="chip">3.018 adultos de 18 a 65</span><span class="chip r">ensayo al azar · 30 días</span></div>
<div class="est"><h4>Faltas al trabajo por enfermedad <span>(si con ducha normal eran 100 días)</span></h4>
{row('Ducha','normal','100',100,'--g2','días')}{row('Final frío','30 a 90 segundos','71',71,'--navy','días')}
<div class="cur"><b>Lo curioso:</b> se enfermaron los mismos días. Y 30 segundos funcionaron igual que 90.</div></div>
<div class="sh">Cómo probarlo sin sufrir:</div>
<div class="yn"><div><i>1</i>Báñate normal y termina con 30 segundos de agua fría</div><div><i>2</i>Respira lento y profundo mientras cae el agua</div><div><i>3</i>Hazlo 30 días seguidos, como en el estudio</div></div>
<div class="help w"><div class="ic">!</div><p><b class="y">¿Problemas del corazón o presión alta? Pregunta antes: el frío de golpe acelera el corazón.</b> Mándaselo a quien te reta a la ducha fría.</p></div>
<div class="foot"><div class="warn"><b>Ensayo sin cegamiento:</b> cada persona contó sus faltas. Adultos sin enfermedades graves, Países Bajos. No es una vacuna ni reemplaza dormir bien.</div>
<div class="ref">Buijze GA, et al.<br>PLoS One 2016;11(9):e0161749<br>doi:10.1371/journal.pone.0161749<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

JOBS = {
    'dr-viera-0730-correr-rodillas': rodillas,
    'dr-viera-1230-oido-audifono': oido,
    'dr-viera-1900-ducha-fria': ducha,
}
if __name__ == '__main__':
    render(JOBS, pathlib.Path(__file__).resolve().parents[1] / '2026-11-14')
