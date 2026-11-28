# 28-nov-2026 · Modelo acv-v3, enfoque soluciones.
# 07:30 [MITO] «Deja de tronarte los dedos, que te va a dar artritis.» deWeber K, Olszewski M, Ortolano R. J Am Board Fam Med 2011;24(2):169-174. doi:10.3122/jabfm.2011.02.100156 (casos y controles retrospectivo, 215 adultos de 50-89 años con radiografía de mano; artritis en cualquier articulación de la mano 18,1 % en quienes se truenan los dedos vs 21,5 % en quienes no, p=0,548; sin relación con duración ni exposición acumulada; autorreporte).
# 12:30 [COMPRADOR] «No llamen a nadie, no quiero arruinar la cena.» Mohammad MA, et al. BMJ 2018;363:k4811. doi:10.1136/bmj.k4811 (SWEDEHEART, 283.014 infartos, Suecia 1998-2013; control = 2 semanas antes y después; Nochebuena IRR 1,37 (1,29-1,46); Navidad/Año Nuevo 1,15 (1,12-1,19); más en mayores de 75 y con diabetes o enfermedad del corazón; pico ~22:00 según prensa; observacional).
# 19:00 [ALCANCE] «No tengo tiempo para el gimnasio.» Garcia L, et al. Br J Sports Med 2023;57(15):979-989. doi:10.1136/bjsports-2022-105669 (metaanálisis dosis-respuesta de cohortes; 196 artículos, 94 cohortes, >30 M personas; 75 min/semana de actividad moderada fuera del trabajo: 23 % menos muerte temprana, 17 % menos enfermedad cardiovascular, 7 % menos cáncer; ~1 de 10 muertes tempranas evitables; cifras de 75 min por comunicado de Cambridge: red bloqueada para el texto completo).
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'kit'))
from plantilla import *
import importlib.util
_s = importlib.util.spec_from_file_location('d26', str(pathlib.Path(__file__).with_name('2026-11-26.py')))
_m = importlib.util.module_from_spec(_s); _s.loader.exec_module(_m)
S, row = _m.S, _m.row

def nudillos(av):
    return f"""{S}<div class="wrap">{head(av,'MITO vs REALIDAD')}
<div class="mir">«Deja de tronarte los dedos, que te va a dar artritis.»</div>
<h1 class="k">Tronarse los dedos <em>no subió</em><br>la artritis de las manos en<br>215 adultos de 50 a 89 años.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>J Am Board Fam Med</i> 2011</span><span class="chip">215 personas</span><span class="chip r">aunque lo hicieran por décadas</span></div>
<div class="est"><h4>De cada 100, con artritis en las manos <span>(radiografía)</span></h4>
{row('No se truenan','los dedos','22',100,'--g2','de 100')}{row('Se truenan','los dedos','18',84,'--navy','de 100')}
<div class="cur"><b>18 contra 22 es lo mismo: cabe en el azar.</b> El «crac» es una burbuja de gas dentro de la articulación.</div></div>
<div class="sh">Lo que sí cuida tus manos:</div>
<div class="yn"><div><i>1</i>Si al tronar hay dolor, hinchazón o pierdes fuerza, consúltalo</div><div><i>2</i>Rigidez de más de 30 minutos al despertar: eso sí se revisa</div><div><i>3</i>En las pausas, abre y cierra el puño 10 veces</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Si no duele, el sonido no te daña.</b> <b class="y">Etiqueta a quien siempre te dice «deja de tronarte los dedos».</b></p></div>
<div class="foot"><div class="warn"><b>Estudio pequeño de casos y controles</b> en EE. UU.: asociación, no causa. Se basó en lo que cada persona recordó.</div>
<div class="ref">deWeber K, et al. J Am Board Fam Med<br>2011;24(2):169-174<br>doi:10.3122/jabfm.2011.02.100156<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def nochebuena(av):
    return f"""{S}<div class="wrap">{head(av,'ESTUDIO','r')}
<div class="mir">«No llamen a nadie, no quiero arruinar la cena.»</div>
<h1 class="k">En Nochebuena, los infartos<br>subieron <em>37 %</em> frente a las<br>semanas de antes y después.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>BMJ</i> 2018</span><span class="chip">283.014 infartos · Suecia</span><span class="chip r">más en mayores de 75</span></div>
<div class="est"><h4>Infartos por día <span>(días normales = 100)</span></h4>
{row('Días normales','2 semanas antes y después','100',73,'--g2','')}{row('Navidad y','Año Nuevo','115',84,'--navy','')}{row('Nochebuena','24 de diciembre','137',100,'--red','')}
<div class="cur"><b>Si un día normal llegan 100 infartos, en Nochebuena llegan 137.</b> Más en mayores de 75 y con diabetes o problemas del corazón.</div></div>
<div class="sh">Lo que protege a los tuyos en las fiestas:</div>
<div class="yn"><div><i>1</i>Que nadie deje sus pastillas por estar de viaje o de fiesta</div><div><i>2</i>Dolor o presión en el pecho, falta de aire o sudor frío: 911 ya</div><div><i>3</i>Cena con menos sal y alcohol, y una caminata juntos después</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Llamar a tiempo no arruina la cena: salva la fiesta.</b> <b class="y">Mándaselo a tus hermanos: ¿quién cuida a papá esta Navidad?</b></p></div>
<div class="foot"><div class="warn"><b>Estudio observacional</b> en Suecia, 16 años: asociación, no causa. El pico fue cerca de las 10 de la noche.</div>
<div class="ref">Mohammad MA, et al. BMJ<br>2018;363:k4811<br>doi:10.1136/bmj.k4811<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def once(av):
    return f"""{S}<div class="wrap">{head(av,'ESTUDIO','r')}
<div class="mir">«No tengo tiempo para el gimnasio.»</div>
<h1 class="k">Solo <em>11 minutos</em> al día de<br>caminar rápido se asoció a<br>23 % menos muertes tempranas.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>Br J Sports Med</i> 2023</span><span class="chip">más de 30 millones de personas</span><span class="chip r">196 estudios</span></div>
<div class="est"><h4>Riesgo de morir antes de tiempo <span>(no moverse = 100)</span></h4>
{row('No se mueven','casi nada','100',100,'--g2','')}{row('11 minutos','al día','77',77,'--grn','')}
<div class="cur"><b>Si todos lo hicieran, se evitaría 1 de cada 10 muertes tempranas.</b> Y hubo 17 % menos enfermedades del corazón.</div></div>
<div class="sh">11 minutos que caben en tu día:</div>
<div class="yn"><div><i>1</i>Bájate una parada antes y camina rápido el resto</div><div><i>2</i>Escaleras en vez de ascensor, cada vez que puedas</div><div><i>3</i>Contesta las llamadas caminando, no sentado</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">«Rápido» es poder hablar, pero no cantar.</b> <b class="y">Etiqueta al amigo que siempre dice «no tengo tiempo».</b></p></div>
<div class="foot"><div class="warn"><b>Metaanálisis de estudios observacionales</b>: asociación, no causa. 11 minutos al día = 75 a la semana, fuera del trabajo.</div>
<div class="ref">Garcia L, et al. Br J Sports Med<br>2023;57(15):979-989<br>doi:10.1136/bjsports-2022-105669<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

JOBS = {
    'dr-viera-0730-tronarse-dedos-mito': nudillos,
    'dr-viera-1230-infarto-nochebuena': nochebuena,
    'dr-viera-1900-once-minutos': once,
}
if __name__ == '__main__':
    render(JOBS, pathlib.Path(__file__).resolve().parents[1] / '2026-11-28')
