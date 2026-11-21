# 21-nov-2026 · Modelo acv-v3, enfoque soluciones.
# 07:30 [MITO] «Un jugo natural cada mañana es lo más sano.» Muraki I, Imamura F, Manson JE, Hu FB, Willett WC, van Dam RM, Sun Q. BMJ 2013;347:f5001. doi:10.1136/bmj.f5001 (3 cohortes prospectivas de EE. UU.: NHS 66.105, NHS II 85.104, HPFS 36.173 = 187.382; 12.198 casos de diabetes tipo 2; por cada 3 porciones/semana: fruta entera HR 0,98 (0,96-0,99); arándanos 0,74 (0,66-0,83), uvas/pasas 0,88 (0,83-0,93), manzanas/peras 0,93 (0,90-0,96); jugo de fruta HR 1,08 (1,05-1,11)). OMS 2015: los azúcares de los jugos de fruta cuentan como azúcares libres.
# 12:30 [COMPRADOR] «¿Puedes sentarte en el suelo y levantarte sin manos?» Brito LBB, Ricardo DR, Araújo DSMS, Ramos PS, Myers J, Araújo CGS. Eur J Prev Cardiol 2014;21(7):892-898. doi:10.1177/2047487312471759 (2.002 adultos de 51-80 años, Brasil; mediana 6,3 años; 159 muertes; puntaje 0-10; HR ajustados 5,44 (0-3), 3,44 (3,5-5,5), 1,84 (6-7,5) vs 8-10; cada punto más, 21 % menos mortalidad; observacional).
# 19:00 [ALCANCE] «Siempre tomo el ascensor.» Song Z, Wan L, Wang W, Li Y, Nie Y, Zhou T, Qi L, et al. Atherosclerosis 2023;386:117300. doi:10.1016/j.atherosclerosis.2023.117300 (UK Biobank, 458.860 adultos, mediana 12,5 años; vs no subir escaleras: 6-10 veces/día HR 0,84 (0,82-0,87), 11-15 HR 0,78 (0,75-0,81); infarto, derrame y enfermedad de arterias; observacional, autorreporte; dejar de subir HR 1,32).
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'kit'))
from plantilla import *
import importlib.util
_s = importlib.util.spec_from_file_location('d20', str(pathlib.Path(__file__).with_name('2026-11-20.py')))
_m = importlib.util.module_from_spec(_s); _s.loader.exec_module(_m)
S, row = _m.S, _m.row

def jugo(av):
    return f"""{S}<div class="wrap">{head(av,'MITO vs REALIDAD')}
<div class="mir">«Yo cada mañana me tomo mi jugo natural: es lo más sano.»</div>
<h1 class="k">La fruta entera se asoció<br>con menos diabetes.<br><em>El jugo, con más.</em></h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>BMJ</i> 2013</span><span class="chip">187.382 adultos · hasta 24 años</span><span class="chip r">observacional</span></div>
<div class="est"><h4>Por cada 3 porciones a la semana <span>(riesgo de diabetes; sin comerlas = 100)</span></h4>
{row('Fruta entera','manzana, uvas…','98',98/108*100,'--grn','de 100')}{row('Jugo','de fruta','108',100,'--red','de 100')}
<div class="cur"><b>Al licuar y colar, se va la fibra y queda el azúcar.</b> Un vaso junta el azúcar de varias frutas y no llena.</div></div>
<div class="sh">Lo que sí puedes hacer mañana:</div>
<div class="yn"><div><i>1</i>Cambia el vaso de jugo por la fruta entera, con cáscara si se puede</div><div><i>2</i>Si lo tomas, que sea un vaso chico, sin azúcar, y no a diario</div><div><i>3</i>Para la sed, agua; para el desayuno, fruta para masticar</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Come la fruta, no la tomes.</b> <b class="y">Mándaselo a quien te prepara el jugo cada mañana.</b></p></div>
<div class="foot"><div class="warn"><b>Estudio observacional</b> en EE. UU.: se asoció, no prueba causa. La OMS cuenta el azúcar del jugo como azúcar libre, igual que el añadido.</div>
<div class="ref">Muraki I, et al.<br>BMJ 2013;347:f5001<br>doi:10.1136/bmj.f5001<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def suelo(av):
    return f"""{S}<div class="wrap">{head(av,'DATO ÚTIL')}
<div class="mir">«¿Pararme del suelo sin usar las manos? Uy, ya no puedo.»</div>
<h1 class="k">No poder pararse del suelo<br>sin apoyos se asoció con<br><em>hasta 5 veces más riesgo</em>.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>Eur J Prev Cardiol</i> 2014</span><span class="chip">2.002 adultos de 51 a 80</span><span class="chip r">6 años de seguimiento</span></div>
<div class="est"><h4>Riesgo de morir según el puntaje <span>(10 menos 1 por cada apoyo)</span></h4>
{row('8 a 10','puntos','1',1/5.44*100,'--grn','vez')}{row('6 a 7,5','puntos','1,8',1.84/5.44*100,'--navy','veces')}{row('0 a 3','puntos','5,4',100,'--red','veces')}
<div class="cur"><b>No es una sentencia:</b> mide fuerza y equilibrio, y eso se entrena.</div></div>
<div class="sh">Tú y tus papás pueden mejorarlo:</div>
<div class="yn"><div><i>1</i>Párate de una silla sin manos, 10 veces, cada día</div><div><i>2</i>Equilíbrate en un pie mientras te cepillas los dientes</div><div><i>3</i>Practica bajar y subir del suelo con apoyo, sobre una alfombra</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Cada punto que ganas cuenta.</b> <b class="y">Hazlo hoy con tus papás, con alguien al lado para cuidarlos.</b></p></div>
<div class="foot"><div class="warn"><b>Estudio observacional</b> en Brasil: se asoció, no prueba causa. Si te duelen rodillas o cadera, o te has caído, consulta antes.</div>
<div class="ref">Brito LBB, et al.<br>Eur J Prev Cardiol 2014;21(7):892-898<br>doi:10.1177/2047487312471759<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def escaleras(av):
    return f"""{S}<div class="wrap">{head(av,'ESTUDIO','r')}
<div class="mir">«Para un piso, ¿para qué subo a pie? Tomo el ascensor.»</div>
<h1 class="k">Subir escaleras unas 6 a 10<br>veces al día se asoció con<br><em>16 % menos</em> infartos y derrames.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>Atherosclerosis</i> 2023</span><span class="chip">458.860 adultos · 12 años</span><span class="chip r">observacional</span></div>
<div class="est"><h4>De cada 100 casos de infarto o derrame <span>(sin subir escaleras = 100)</span></h4>
{row('No subo','escaleras','100',100,'--g2','casos')}{row('6 a 10','veces al día','84',84,'--navy','casos')}{row('11 a 15','veces al día','78',78,'--grn','casos')}
<div class="cur"><b>Ojo:</b> quienes subían y luego lo dejaron tuvieron más riesgo que quienes nunca subieron. Lo que cuenta es mantenerlo.</div></div>
<div class="sh">Súmalo sin gastar un minuto extra:</div>
<div class="yn"><div><i>1</i>Regla de 3 pisos: si son 3 o menos, por la escalera</div><div><i>2</i>En edificios altos, bájate 2 pisos antes del tuyo</div><div><i>3</i>En casa, sube por cada cosa en vez de juntarlas</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Cada tramo cuenta; no necesitas gimnasio.</b> <b class="y">Mándaselo a tu compañero de oficina que siempre espera el ascensor.</b></p></div>
<div class="foot"><div class="warn"><b>Estudio observacional</b> en Reino Unido (adultos de 40 a 69 años): se asoció, no prueba causa; las escaleras se contaron por lo que dijo cada persona.</div>
<div class="ref">Song Z, et al.<br>Atherosclerosis 2023;386:117300<br>doi:10.1016/j.atherosclerosis.2023.117300<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

JOBS = {
    'dr-viera-0730-jugo-vs-fruta': jugo,
    'dr-viera-1230-pararse-del-suelo': suelo,
    'dr-viera-1900-escaleras': escaleras,
}
if __name__ == '__main__':
    render(JOBS, pathlib.Path(__file__).resolve().parents[1] / '2026-11-21')
