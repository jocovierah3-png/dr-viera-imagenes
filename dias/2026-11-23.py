# 23-nov-2026 · Modelo acv-v3, enfoque soluciones.
# 07:30 [MITO · ¿Normal o lo reviso?] «Me duele la cabeza casi a diario, me tomo una pastilla y sigo.» Cefalea por uso excesivo de medicación: NICE CG150 (analgésicos simples 15 días o más al mes; otros 10 días o más; más de 3 meses, criterios ICHD-3); prevalencia 1-2 % (revisiones). Carlsen LN, et al. JAMA Neurol 2020;77(9):1069-1078. doi:10.1001/jamaneurol.2020.1179 (ensayo al azar abierto, 120 adultos, Dinamarca; a 6 meses ya sin cefalea por abuso: retirada + preventivo 96,8 %, retirada sola 88,9 %, preventivo sin retirada 74,3 %).
# 12:30 [COMPRADOR] «En mi familia todos son del corazón, es hereditario.» Yusuf S, et al. Lancet 2004;364(9438):937-952. doi:10.1016/S0140-6736(04)17018-9 (INTERHEART, casos y controles, 52 países, 15.152 casos y 14.820 controles; 9 factores modificables = 90 % del riesgo atribuible en hombres y 94 % en mujeres; OR ApoB/ApoA1 3,25; fumar 2,87; psicosociales 2,67; diabetes 2,37; hipertensión 1,91).
# 19:00 [ALCANCE] «Mi perro es mi terapia.» Kramer CK, Mehmood S, Suen RS. Circ Cardiovasc Qual Outcomes 2019;12(10):e005554. doi:10.1161/CIRCOUTCOMES.119.005554 (metaanálisis de 10 estudios observacionales, >3,8 M personas según nota de AHA; mortalidad total RR 0,76, 0,67-0,86; CV RR 0,69; tras evento coronario RR 0,35, 0,17-0,69). Bauman A, et al. 2020: con HR ajustados el efecto fue menor.
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'kit'))
from plantilla import *
import importlib.util
_s = importlib.util.spec_from_file_location('d22', str(pathlib.Path(__file__).with_name('2026-11-22.py')))
_m = importlib.util.module_from_spec(_s); _s.loader.exec_module(_m)
S, row = _m.S, _m.row

def cabeza(av):
    return f"""{S}<div class="wrap">{head(av,'¿NORMAL O LO REVISO?')}
<div class="mir">«Me duele la cabeza casi a diario. Me tomo una pastilla y sigo.»</div>
<h1 class="k">Tomar pastillas para el dolor<br><em>muchos días al mes</em> puede<br>causar más dolor de cabeza.</h1>
<div class="src" style="margin-top:22px"><span class="chip">Guía NICE</span><span class="chip">1 a 2 de cada 100 adultos</span><span class="chip r"><i>JAMA Neurol</i> 2020 · ensayo</span></div>
<div class="est"><h4>Ya sin ese dolor a los 6 meses <span>(de cada 100)</span></h4>
{row('Bajar pastillas','con plan del médico','89',89,'--navy','de 100')}{row('Bajar + prevenir','tratamiento del médico','97',97,'--grn','de 100')}</div>
<div class="nv"><div class="a"><h5>NORMAL</h5>Dolor de vez en cuando, que pasa con descanso, agua o una pastilla ocasional.</div><div class="b"><h5>REVÍSALO</h5>Pastillas para el dolor 10 días o más al mes, por más de 3 meses.</div></div>
<div class="sh">Lo que puedes hacer desde hoy:</div>
<div class="yn"><div><i>1</i>Anota 1 mes en el celular cada día con dolor y cada pastilla</div><div><i>2</i>Lleva esa lista al médico: él te dice cómo bajarlas y cómo prevenir</div><div><i>3</i>Al bajarlas, los primeros días puede doler más: no te rindas</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Más pastillas no siempre es menos dolor.</b> <b class="y">Mándaselo a quien siempre carga pastillas en la cartera.</b></p></div>
<div class="foot"><div class="warn"><b>Ensayo en Dinamarca</b> (120 adultos, sin cegamiento). El peor dolor de tu vida, o con fiebre, cuello rígido o debilidad: <b>911</b>.</div>
<div class="ref">Carlsen LN, et al. JAMA Neurol<br>2020;77(9):1069-1078<br>doi:10.1001/jamaneurol.2020.1179<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def familia(av):
    return f"""{S}<div class="wrap">{head(av,'DATO ÚTIL')}
<div class="mir">«En mi familia todos son del corazón. Es hereditario.»</div>
<h1 class="k"><em>9 de cada 10</em> infartos se<br>asociaron a cosas que<br>sí se pueden cambiar.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>Lancet</i> 2004</span><span class="chip">52 países · casi 30.000 personas</span><span class="chip r">casos y controles</span></div>
<div class="est"><h4>Cuánto más riesgo de infarto <span>(sin ese factor = 1)</span></h4>
{row('Colesterol','desbalanceado','3,3',3.25/3.5*100,'--red',' veces')}{row('Fumar','hoy','2,9',2.87/3.5*100,'--red',' veces')}{row('Presión alta','','1,9',1.91/3.5*100,'--red',' veces')}
<div class="cur"><b>La familia suma, pero no decide sola:</b> 9 factores así explicaron 90 % (hombres) y 94 % (mujeres).</div></div>
<div class="sh">Su plan en familia, esta semana:</div>
<div class="yn"><div><i>1</i>Mídanse presión, azúcar y colesterol, más si hubo infartos en casa</div><div><i>2</i>Si alguien fuma, dejarlo es el cambio que más pesa</div><div><i>3</i>Fruta o verdura en cada comida y 30 minutos de caminata</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Tu historia familiar es un aviso, no una sentencia.</b> <b class="y">Mándaselo al primo que dice «es de familia».</b></p></div>
<div class="foot"><div class="warn"><b>Casos y controles:</b> asociación. El 90 % es una cifra de población, no tu riesgo personal.</div>
<div class="ref">Yusuf S, et al. (INTERHEART)<br>Lancet 2004;364(9438):937-952<br>doi:10.1016/S0140-6736(04)17018-9<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def perro(av):
    return f"""{S}<div class="wrap">{head(av,'ESTUDIO','r')}
<div class="mir">«Mi perro es mi terapia… y mi entrenador sin saberlo.»</div>
<h1 class="k">Tener perro se asoció con<br><em>24 % menos riesgo</em><br>de morir.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>Circ Cardiovasc Qual Outcomes</i> 2019</span><span class="chip">10 estudios · +3,8 millones</span><span class="chip r">observacional</span></div>
<div class="est"><h4>Riesgo de morir en el seguimiento <span>(sin perro = 100)</span></h4>
{row('Sin perro','','100',100,'--g2','de 100')}{row('Con perro','','76',76,'--navy','de 100')}{row('Con perro','tras infarto (vs sin perro)','35',35,'--grn','de 100')}
<div class="cur"><b>¿Por qué?</b> Se cree que por caminar más y estresarse menos. No está probado que el perro sea la causa.</div></div>
<div class="sh">Lo que puedes copiar, tengas perro o no:</div>
<div class="yn"><div><i>1</i>Con perro: 2 paseos al día de 15 minutos, sin mirar el celular</div><div><i>2</i>Sin perro: sal a caminar con un amigo a la misma hora</div><div><i>3</i>Adoptar es un compromiso de años: hazlo por cariño, no solo por salud</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">El paseo diario es la parte que puedes copiar hoy.</b> <b class="y">Etiqueta a quien vive pegado a su perro.</b></p></div>
<div class="foot"><div class="warn"><b>Estudios observacionales:</b> se asoció, no prueba causa. Análisis con más ajustes vieron un efecto menor.</div>
<div class="ref">Kramer CK, Mehmood S, Suen RS.<br>Circ Cardiovasc Qual Outcomes 2019<br>doi:10.1161/CIRCOUTCOMES.119.005554<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

JOBS = {
    'dr-viera-0730-pastillas-dolor-cabeza': cabeza,
    'dr-viera-1230-infarto-es-hereditario': familia,
    'dr-viera-1900-perro-vivir-mas': perro,
}
if __name__ == '__main__':
    render(JOBS, pathlib.Path(__file__).resolve().parents[1] / '2026-11-23')
