# 22-nov-2026 · Modelo acv-v3, enfoque soluciones.
# 07:30 [MITO] «Antes de correr hay que estirar o te lesionas.» Pope RP, Herbert RD, Kirwan JD, Graham BJ. Med Sci Sports Exerc 2000;32(2):271-277 (ensayo al azar, 1.538 reclutas varones; todos calentaron; todas las lesiones HR 0,95, IC 95 % 0,77-1,18; tejidos blandos HR 0,83, 0,63-1,09; la baja condición física fue factor de riesgo). Herbert RD, Gabriel M. BMJ 2002;325:468. doi:10.1136/bmj.325.7362.468 (revisión sistemática; HR combinado 0,95, 0,78-1,16; dolor muscular a las 24 h, 0,9 mm en escala de 100).
# 12:30 [COMPRADOR · ¿Normal o lo reviso?] «Me levanto 2 o 3 veces cada noche a orinar.» Pesonen JS, et al. J Urol 2020;203(3):486-495. doi:10.1097/JU.0000000000000463 (11 estudios observacionales; nicturia y mortalidad RR 1,27, IC 95 % 1,16-1,40; diferencia absoluta a 5 años 1,6 % a los 60 y 4,0 % a los 75; certeza moderada como señal, muy baja como causa). Bosch JL, Weiss JP. J Urol 2010 (20-40 años, 2 o más veces: 2-18 %).
# 19:00 [ALCANCE] «No tengo tiempo para leer.» Bavishi A, Slade MD, Levy BR. Soc Sci Med 2016;164:44-48 (Health and Retirement Study, 3.635 adultos de 50+, 12 años; lectores de libros 20 % menos riesgo de morir (HR 0,80); hasta 3,5 h/semana 17 % y más de 3,5 h 23 % según prensa; ventaja de 23 meses; diarios y revistas con menos efecto; observacional; DOI no verificado).
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'kit'))
from plantilla import *
import importlib.util
_s = importlib.util.spec_from_file_location('d21', str(pathlib.Path(__file__).with_name('2026-11-21.py')))
_m = importlib.util.module_from_spec(_s); _s.loader.exec_module(_m)
S, row = _m.S, _m.row
_s2 = importlib.util.spec_from_file_location('d15', str(pathlib.Path(__file__).with_name('2026-11-15.py')))
_m2 = importlib.util.module_from_spec(_s2); _s2.loader.exec_module(_m2)
S15 = _m2.S

def estirar(av):
    return f"""{S}<div class="wrap">{head(av,'MITO vs REALIDAD')}
<div class="mir">«Antes de correr o jugar fútbol hay que estirar, si no, te lesionas.»</div>
<h1 class="k">En 1.538 personas, estirar antes<br>del ejercicio <em>casi no cambió</em><br>las lesiones.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>Med Sci Sports Exerc</i> 2000</span><span class="chip">ensayo al azar</span><span class="chip r">confirmado en <i>BMJ</i> 2002</span></div>
<div class="est"><h4>Lesiones en 12 semanas de entrenamiento <span>(sin estirar = 100)</span></h4>
{row('Sin estirar','solo calentaron','100',100,'--g2','casos')}{row('Estiraron','antes de entrenar','95',95,'--navy','casos')}
<div class="cur"><b>La diferencia fue tan chica que pudo ser azar.</b> Lo que más pesó fue llegar con poca condición física.</div></div>
<div class="sh">Lo que sí te cuida antes y después:</div>
<div class="yn"><div><i>1</i>Calienta 5 a 10 minutos moviéndote: trote suave, rodillas arriba</div><div><i>2</i>Sube el esfuerzo poco a poco, semana a semana, no de golpe</div><div><i>3</i>Estira después, si te gusta: ayuda a moverte mejor, no es obligatorio</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Mejor calentar que estirar en frío.</b> <b class="y">Mándaselo a tu grupo del fútbol del fin de semana.</b></p></div>
<div class="foot"><div class="warn"><b>Ensayo en reclutas militares</b> (hombres jóvenes). Si tu fisioterapeuta te indicó estiramientos por una lesión, sigue su plan.</div>
<div class="ref">Pope RP, et al. MSSE 2000;32(2):271-7<br>Herbert RD, Gabriel M. BMJ 2002;325:468<br>doi:10.1136/bmj.325.7362.468<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def orinar(av):
    return f"""{S15}<div class="wrap">{head(av,'¿NORMAL O LO REVISO?')}
<div class="mir">«Me levanto 2 o 3 veces cada noche a orinar. Ya es costumbre.»</div>
<h1 class="k">Orinar <em>2 o más veces</em> cada<br>noche se asoció con<br>27 % más riesgo de morir.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>J Urol</i> 2020</span><span class="chip">11 estudios</span><span class="chip r">es una señal, no la causa</span></div>
<div class="est"><h4>Riesgo de morir en el seguimiento <span>(0 a 1 vez = 100)</span></h4>
{row('0 a 1 vez','por noche','100',100/127*100,'--navy','casos')}{row('2 o más','veces por noche','127',100,'--red','casos')}</div>
<div class="nv"><div class="a"><h5>NORMAL</h5>1 vez por noche, o tras café, alcohol o mucho líquido.</div><div class="b"><h5>REVÍSALO</h5>2 o más veces casi a diario, mucha sed, chorro débil o ronquidos.</div></div>
<div class="sh">Lo que puedes hacer desde esta noche:</div>
<div class="yn"><div><i>1</i>Toma tu agua de día y baja líquidos 2 horas antes de dormir</div><div><i>2</i>Anota 3 noches cuántas veces te levantas y llévalo al médico</div><div><i>3</i>Pide que te midan el azúcar; en hombres, revisar la próstata</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Casi siempre tiene causa y arreglo.</b> <b class="y">¿Tu papá se levanta varias veces de noche? Mándaselo.</b></p></div>
<div class="foot"><div class="warn"><b>Estudios observacionales:</b> no es que orinar dañe; suele avisar de otro problema (azúcar, próstata, corazón, apnea). Los mayores tienen más.</div>
<div class="ref">Pesonen JS, et al.<br>J Urol 2020;203(3):486-495<br>doi:10.1097/JU.0000000000000463<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def leer(av):
    return f"""{S}<div class="wrap">{head(av,'ESTUDIO','r')}
<div class="mir">«¿Leer un libro? No tengo tiempo… pero 2 horas de reels, sí.»</div>
<h1 class="k">Quienes leían libros vivieron<br><em>casi 2 años más</em><br>que quienes no leían.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>Soc Sci Med</i> 2016</span><span class="chip">3.635 adultos · 12 años</span><span class="chip r">observacional</span></div>
<div class="est"><h4>Riesgo de morir en 12 años <span>(no leer libros = 100)</span></h4>
{row('No leían','libros','100',100,'--g2','de 100')}{row('Hasta 30 min','al día','83',83,'--navy','de 100')}{row('Más de 30 min','al día','77',77,'--grn','de 100')}
<div class="cur"><b>Con diarios y revistas la ventaja fue menor.</b> Los autores creen que el libro mantiene la mente más activa.</div></div>
<div class="sh">Empieza con 1 capítulo, no con 1 libro:</div>
<div class="yn"><div><i>1</i>Cambia los primeros 15 minutos de celular en la cama por 1 capítulo</div><div><i>2</i>Ten el libro donde está el celular: velador, mochila, bus</div><div><i>3</i>Elige algo que te guste, no lo que «deberías» leer</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Un capítulo al día es suficiente para empezar.</b> <b class="y">Mándaselo a tu amigo que dice «no tengo tiempo para leer».</b></p></div>
<div class="foot"><div class="warn"><b>Estudio observacional</b> en EE. UU. con adultos de 50 años o más: se asoció, no prueba causa; quienes leen pueden tener otros hábitos sanos.</div>
<div class="ref">Bavishi A, Slade MD, Levy BR.<br>Soc Sci Med 2016;164:44-48<br>Health and Retirement Study<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

JOBS = {
    'dr-viera-0730-estirar-antes': estirar,
    'dr-viera-1230-orinar-de-noche': orinar,
    'dr-viera-1900-leer-libros': leer,
}
if __name__ == '__main__':
    render(JOBS, pathlib.Path(__file__).resolve().parents[1] / '2026-11-22')
