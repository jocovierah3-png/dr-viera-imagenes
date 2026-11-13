# 13-nov-2026 · Modelo acv-v3, enfoque soluciones.
# 07:30 [DATO ÚTIL · ¿Normal o lo reviso?] «Se me duermen las manos en la noche.» Atroshi I, et al. JAMA 1999;282(2):153-158. doi:10.1001/jama.282.2.153 (Suecia, muestra al azar de 3.000 adultos de 25-74 años, 83 % respondió; síntomas de hormigueo/adormecimiento/dolor en la mano 14,4 %; túnel carpiano clínicamente seguro 3,8 %, IC 3,1-4,6). NHS: Carpal tunnel syndrome (síntomas peores de noche, pulgar-índice-medio; férula de noche; ver al médico si no mejora o hay debilidad).
# 12:30 [COMPRADOR] «Me siento bien; mis arterias están limpias.» Bundgaard H, García-Lunar I, Kofoed KF, et al. N Engl J Med 2026;395:1818-1829. doi:10.1056/NEJMoa2609059 (REACT; 16.808 adultos de 18-70 años sin enfermedad del corazón conocida, Dinamarca y España; ecografía 3D de carótidas y femorales + tomografía coronaria; placa silenciosa 57,1 %, IC 56,3-58,0; ~1 de cada 13 a los 18-29 y ~9 de cada 10 a los 60-70; hombres 5-10 años antes; en mujeres sube fuerte alrededor de la menopausia; SCORE2 detectó a pocos). Estudio transversal: no prueba que tamizar a todos prevenga infartos.
# 19:00 [ALCANCE · MITO] «Dicen que en 21 días se forma un hábito… y yo lo dejo a la semana.» Lally P, et al. Eur J Soc Psychol 2010;40(6):998-1009. doi:10.1002/ejsp.674 (96 adultos, 84 días; mediana 66 días hasta hacerse automático, rango 18-254 estimado; faltar 1 día no afectó). Singh B, Murphy A, Maher C, Smith AE. Healthcare (Basel) 2024;12(23):2488. doi:10.3390/healthcare12232488 (revisión sistemática, 20 estudios, 2.601 adultos; medianas 59-66 días; variabilidad 4-335 días; hábitos de la mañana y elegidos por uno mismo, más fuertes).
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'kit'))
from plantilla import *
import importlib.util
_s = importlib.util.spec_from_file_location('d12', str(pathlib.Path(__file__).with_name('2026-11-12.py')))
_m = importlib.util.module_from_spec(_s); _s.loader.exec_module(_m)
S, row = _m.S, _m.row
S += """<style>
.ppl{grid-template-columns:repeat(20,1fr);gap:7px;margin-top:26px}
.ppl i{height:34px}
.nv{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:16px}
.nv div{border-radius:14px;padding:14px 18px;font:700 22px/1.3 Manrope}
.nv h5{font:800 17px Manrope;letter-spacing:.12em;margin-bottom:6px}
.nv .a{background:#E8F7EE}.nv .a h5{color:#15803D}
.nv .b{background:#FDE8E8}.nv .b h5{color:var(--red)}
.cal{display:flex;align-items:center;gap:14px;margin-top:12px;font:700 22px/1.25 Manrope}
.cal b{flex:none;font:800 34px Manrope;color:var(--red)}
</style>"""

def ppl(n_red, total=40):
    return '<div class="ppl">' + ''.join(f'<i class="{"r" if k < n_red else ""}"></i>' for k in range(total)) + '</div>'

def manos(av):
    return f"""{S}<div class="wrap">{head(av,'¿NORMAL O LO REVISO?')}
<div class="mir">«Se me duermen las manos en la noche.»</div>
<h1 class="k">Si el hormigueo <em>te despierta</em><br>y es en el pulgar, índice<br>y medio: revísalo.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>JAMA</i> 1999</span><span class="chip">2.466 adultos de 25 a 74 años</span><span class="chip r">NHS</span></div>
<div class="est"><h4>En un grupo de WhatsApp de 30 adultos <span>(estudio en Suecia)</span></h4>
{row('Hormigueo','o manos dormidas','4',14.4/14.4*100,'--navy','de 30')}{row('Túnel','carpiano','1',3.8/14.4*100,'--red','de 30')}</div>
<div class="nv"><div class="a"><h5>NORMAL</h5>Dormiste sobre el brazo y se quita al mover la mano en minutos.</div><div class="b"><h5>REVÍSALO</h5>Vuelve casi cada noche, dura semanas o se te caen las cosas.</div></div>
<div class="sh">Lo que ayuda desde hoy:</div>
<div class="yn"><div><i>1</i>Duerme con la muñeca recta, sin doblarla bajo la almohada</div><div><i>2</i>Pausas al teclear, coser o usar el celular mucho rato</div><div><i>3</i>Pregunta al médico por una férula para la noche</div></div>
<div class="help w"><div class="ic">!</div><p><b class="y">Si de golpe se duerme un lado de la cara o del cuerpo, o cuesta hablar: 911.</b> Mándaselo a quien se sacude las manos al despertar.</p></div>
<div class="foot"><div class="warn"><b>Datos de población de Suecia.</b> Más común en mujeres, embarazo, diabetes y trabajos con la mano. Muchos casos leves mejoran solos.</div>
<div class="ref">Atroshi I, et al.<br>JAMA 1999;282(2):153-158<br>doi:10.1001/jama.282.2.153<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def placa(av):
    return f"""{S}<div class="wrap">{head(av,'ESTUDIO NUEVO','r')}
<div class="mir">«Me siento bien; mis arterias están limpias.»</div>
<h1 class="k"><em>57 de cada 100</em> adultos<br>que se sentían sanos ya<br>tenían placa en sus arterias.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>N Engl J Med</i> 2026</span><span class="chip">16.808 adultos de 18 a 70</span><span class="chip r">ecografía y tomografía</span></div>
<div class="est"><h4>En un bus con 40 adultos «sanos», <span>23 ya tienen placa sin saberlo</span></h4>
{ppl(23)}
<div class="mf"><div><b>1 de 13</b>de 18 a 29 años</div><div><b>9 de 10</b>de 60 a 70 años</div></div></div>
<div class="ojo" style="font-size:25px">Los hombres van <b>5 a 10 años antes</b>. En las mujeres sube rápido <b>con la menopausia</b>.</div>
<div class="sh">Lo que sí está en tus manos: <span>aunque te sientas bien</span></div>
<div class="yn"><div><i>1</i>Mídete presión, colesterol y azúcar este año</div><div><i>2</i>Si fumas, este es el mejor momento para dejarlo</div><div><i>3</i>Camina rápido 30 minutos, 5 días a la semana</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">La placa crece lento: hay años para frenarla.</b> <b class="y">¿Tus papás se sienten «sanitos»? Mándaselo y llévalos a medirse.</b></p></div>
<div class="foot"><div class="warn"><b>Foto de un solo momento</b> en Dinamarca y España. No significa que todos necesiten una ecografía: el control básico es el primer paso.</div>
<div class="ref">Bundgaard H, et al. (REACT)<br>N Engl J Med 2026;395:1818-1829<br>doi:10.1056/NEJMoa2609059<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def habitos(av):
    return f"""{S}<div class="wrap">{head(av,'MITO vs REALIDAD')}
<div class="mir">«En 21 días se forma un hábito… y yo lo dejo a la semana.»</div>
<h1 class="k">No es tu fuerza de voluntad:<br>un hábito tarda <em>unos 66 días</em><br>en salir solo.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>Healthcare</i> 2024</span><span class="chip">20 estudios · 2.601 adultos</span><span class="chip r">+ <i>Eur J Soc Psychol</i> 2010</span></div>
<div class="est"><h4>Días hasta que el hábito se vuelve automático</h4>
{row('El mito','lo que todos repiten','21',21/66*100,'--g2','días')}{row('La realidad','mediana de los estudios','66',100,'--red','días')}
<div class="cal"><b>18 ene</b>Si empiezas hoy, cerca de esa fecha ya te sale sin pensarlo.</div></div>
<div class="sh">Cómo lograr que se quede:</div>
<div class="yn"><div><i>1</i>Pégalo a algo que ya haces: «después del café, camino 10 min»</div><div><i>2</i>Misma hora cada día; en la mañana se pega mejor</div><div><i>3</i>¿Fallaste un día? No pasa nada: retoma mañana</div><div><i>4</i>Elige tú el hábito: los elegidos por uno duran más</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Faltar un día no borra lo avanzado.</b> <b class="y">Mándaselo a tu amigo que ya empezó el gym 5 veces este año.</b></p></div>
<div class="foot"><div class="warn"><b>Varía mucho entre personas:</b> de 4 a 335 días. Solo 4 estudios midieron el tiempo; son promedios, no una regla fija.</div>
<div class="ref">Singh B, et al. Healthcare 2024;12(23):2488<br>doi:10.3390/healthcare12232488<br>Lally P, et al. doi:10.1002/ejsp.674<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

JOBS = {
    'dr-viera-0730-manos-dormidas': manos,
    'dr-viera-1230-placa-silenciosa': placa,
    'dr-viera-1900-habito-66-dias': habitos,
}
if __name__ == '__main__':
    render(JOBS, pathlib.Path(__file__).resolve().parents[1] / '2026-11-13')
