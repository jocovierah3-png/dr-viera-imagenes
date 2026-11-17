# 17-nov-2026 · Modelo acv-v3, enfoque soluciones.
# 07:30 [MITO] «¿La pastilla de la presión es mejor de noche?» Mackenzie IS, Rogers A, Poulter NR, et al. (TIME). Lancet 2022;400(10361):1417-1425. doi:10.1016/S0140-6736(22)01786-X (ensayo al azar, Reino Unido; 21.104 adultos con presión alta; mediana 5,2 años; muerte vascular, infarto o derrame no fatal: noche 0,69 vs mañana 0,72 por 100 persona-año; HR 0,95, IC 0,83-1,10; sin problemas de seguridad; 91 % personas blancas).
# 12:30 [COMPRADOR] «No le duele el pecho; debe ser cansancio.» Canto JG, et al. JAMA 2012;307(8):813-822. doi:10.1001/jama.2012.199 (registro NRMI, EE. UU., 1994-2006; 1.143.513 personas con infarto; sin dolor de pecho al llegar: mujeres 42,0 % vs hombres 30,7 %; muerte en el hospital mujeres 14,6 % vs hombres 10,3 %; la diferencia por sexo fue mayor en jóvenes; observacional).
# 19:00 [ALCANCE] «5 minutitos más.» Robbins R, et al. Sci Rep 2025. doi:10.1038/s41598-025-99563-y (21.222 usuarios de una app de sueño, ~3 M noches; 55,6 % de las sesiones terminó con posponer; promedio 10,8 min; descriptivo). Sundelin T, Landry S, Axelsson J. J Sleep Res 2023. doi:10.1111/jsr.14054 (encuesta 1.732; laboratorio 31 personas que posponen habitualmente: 30 min de posponer ≈ 6 min menos de sueño; sin peor ánimo, sueño ni cortisol; pequeño).
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'kit'))
from plantilla import *
import importlib.util
_s = importlib.util.spec_from_file_location('d13', str(pathlib.Path(__file__).with_name('2026-11-13.py')))
_m = importlib.util.module_from_spec(_s); _s.loader.exec_module(_m)
S, row = _m.S, _m.row
_s2 = importlib.util.spec_from_file_location('d14', str(pathlib.Path(__file__).with_name('2026-11-14.py')))
_m2 = importlib.util.module_from_spec(_s2); _s2.loader.exec_module(_m2)
S2 = _m2.S if hasattr(_m2, 'S') else S

def presion(av):
    return f"""{S}<div class="wrap">{head(av,'MITO vs REALIDAD')}
<div class="mir">«¿La pastilla de la presión es mejor tomarla en la noche?»</div>
<h1 class="k">Mañana o noche:<br>protegió <em>igual</em>. Lo que importa<br>es no olvidarla.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>Lancet</i> 2022</span><span class="chip">21.104 adultos con presión alta</span><span class="chip r">5 años · al azar</span></div>
<div class="est"><h4>Imagina 1.000 personas con presión alta: <span>infartos, derrames o muertes en un año</span></h4>
{row('Pastilla','en la mañana','7,2',100,'--navy','de 1.000')}{row('Pastilla','en la noche','6,9',6.9/7.2*100,'--navy','de 1.000')}
<div class="cur"><b>Prácticamente igual.</b> Ni más ni menos seguro tomarla de noche.</div></div>
<div class="sh">La hora que funciona es la que no olvidas:</div>
<div class="yn"><div><i>1</i>Pégala a algo diario: el café o el cepillado de dientes</div><div><i>2</i>Pastillero de la semana o alarma en el celular</div><div><i>3</i>No la cambies ni la dejes por tu cuenta: pregunta a tu médico</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">La pastilla que protege es la que se toma todos los días.</b> <b class="y">Mándaselo a quien discute la hora de su pastilla.</b></p></div>
<div class="foot"><div class="warn"><b>Ensayo al azar en Reino Unido</b>, casi todos personas blancas. Si tu médico te indicó una hora por un motivo, sigue su indicación.</div>
<div class="ref">Mackenzie IS, et al. (TIME)<br>Lancet 2022;400:1417-1425<br>doi:10.1016/S0140-6736(22)01786-X<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def infarto(av):
    return f"""{S}<div class="wrap">{head(av,'DATO ÚTIL')}
<div class="mir">«No le duele el pecho; debe ser cansancio o gastritis.»</div>
<h1 class="k"><em>4 de cada 10 mujeres</em><br>con infarto llegaron al hospital<br>sin dolor de pecho.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>JAMA</i> 2012</span><span class="chip">1.143.513 personas con infarto</span><span class="chip r">EE. UU.</span></div>
<div class="est"><h4>De cada 100 personas con infarto, <span>¿cuántas no tuvieron dolor de pecho?</span></h4>
{row('Hombres','','31',31/42*100,'--navy','de 100')}{row('Mujeres','','42',100,'--red','de 100')}</div>
<div class="sh">Lo que puede aparecer en lugar del dolor: <span>de golpe y sin explicación</span></div>
<div class="qq"><div><b>SÍ/NO</b>¿Falta de aire?</div><div><b>SÍ/NO</b>¿Sudor frío o náusea?</div><div><b>SÍ/NO</b>¿Dolor de mandíbula, espalda o brazo?</div><div><b>SÍ/NO</b>¿Cansancio raro y muy fuerte?</div></div>
<div class="yn"><div><i>1</i>Si aparece de golpe y no se pasa en minutos: llama al 911</div><div><i>2</i>No manejes tú ni esperes «a ver si se pasa»</div></div>
<div class="help w"><div class="ic">!</div><p><b class="y">En el infarto, cada minuto cuenta.</b> Mándaselo a tu mamá, tu tía y tu abuela.</p></div>
<div class="foot"><div class="warn"><b>Registro observacional</b> de EE. UU. (1994-2006). La diferencia fue mayor en mujeres más jóvenes. Esto no reemplaza una consulta.</div>
<div class="ref">Canto JG, et al.<br>JAMA 2012;307(8):813-822<br>doi:10.1001/jama.2012.199<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def posponer(av):
    return f"""{S}<div class="wrap">{head(av,'ESTUDIO','r')}
<div class="mir">«5 minutitos más…» (y suena la alarma otra vez)</div>
<h1 class="k"><em>56 de cada 100</em> mañanas<br>terminan en «posponer».<br>El problema no es el botón.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>Sci Rep</i> 2025</span><span class="chip">21.222 personas · 3 M de noches</span><span class="chip r">+ <i>J Sleep Res</i> 2023</span></div>
<div class="est"><h4>¿Te hace daño posponer?</h4>
<div class="cmp"><div class="rr"><b class="big">11 min</b>pospone en promedio quien usa el botón</div><div class="gg"><b class="big">6 min</b>de sueño perdió quien pospuso 30 min (experimento)</div></div>
<div class="cur"><b>Mismo ánimo y misma energía</b> en la tarde. Si lo necesitas cada día, mira cuántas horas duermes.</div></div>
<div class="sh">Para despertar sin pelear con la alarma:</div>
<div class="yn"><div><i>1</i>Acuéstate 15 minutos antes esta semana</div><div><i>2</i>Deja el celular lejos de la cama: tendrás que pararte</div><div><i>3</i>Abre la cortina apenas te levantes: la luz te despierta</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Si cada mañana necesitas «5 minutitos más», quizá te falta sueño, no fuerza de voluntad.</b> <b class="y">Mándaselo a quien tiene 5 alarmas seguidas.</b></p></div>
<div class="foot"><div class="warn"><b>Datos de una app de sueño</b> y un experimento pequeño (31 personas que ya posponían). No aplica a todos.</div>
<div class="ref">Robbins R, et al. Sci Rep 2025<br>doi:10.1038/s41598-025-99563-y<br>Sundelin T, et al. doi:10.1111/jsr.14054<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

JOBS = {
    'dr-viera-0730-pastilla-presion-hora': presion,
    'dr-viera-1230-infarto-sin-dolor-pecho': infarto,
    'dr-viera-1900-posponer-alarma': posponer,
}
if __name__ == '__main__':
    render(JOBS, pathlib.Path(__file__).resolve().parents[1] / '2026-11-17')
