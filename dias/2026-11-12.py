# 12-nov-2026 · Modelo acv-v3, enfoque soluciones.
# 07:30 [MITO] «Deja de tronarte los dedos, te va a dar artritis.» deWeber K, Olszewski M, Ortolano R. J Am Board Fam Med 2011;24(2):169-174. doi:10.3122/jabfm.2011.02.100156 (casos y controles retrospectivo; 215 personas de 50-89 años con radiografía de la mano; artritis 18,1 % en quienes se truenan los dedos vs 21,5 % en quienes no; p=0,548). Curiosidad: Unger DL. Arthritis Rheum 1998;41(5):949-950 (caso de 1 persona, 60 años tronándose solo una mano).
# 12:30 [COMPRADOR] «Veo bien; no necesito ir al oculista.» Soh Z, et al. Ophthalmology 2021;128(10):1393-1404. doi:10.1016/j.ophtha.2021.04.009 (revisión sistemática y metaanálisis; 55 estudios de población, 189.359 personas; más de la mitad de los casos de glaucoma no detectados en todas las regiones). Wolfs RC, et al. Arch Ophthalmol 1998;116(12):1640-1645. doi:10.1001/archopht.116.12.1640 (Rotterdam; riesgo de por vida 22,0 % en familiares de pacientes vs 2,3 %; RR 9,2, IC 1,2-73,9). AAO: control base a los 40 años; antes y más seguido con factores de riesgo.
# 19:00 [ALCANCE] «Cambiar mis hábitos es imposible; no tengo tiempo.» Koemel NA, Stamatakis E, et al. eClinicalMedicine 2026;103741. doi:10.1016/j.eclinm.2025.103741 (UK Biobank, 59.078 adultos, edad media 64, pulsera 7 días; mínimo combinado +5 min/día de sueño, +1,9 min/día de actividad moderada-vigorosa y +5 puntos de dieta: 1 año más de vida; lo óptimo 7,2-8,0 h de sueño, >42 min/día de actividad y buena dieta: 9,35 años más vs lo peor; observacional).
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'kit'))
from plantilla import *
import importlib.util
_s = importlib.util.spec_from_file_location('d3', str(pathlib.Path(__file__).with_name('2026-11-03.py')))
_m = importlib.util.module_from_spec(_s); _s.loader.exec_module(_m)
S = _m.S + """<style>
.qq{display:grid;grid-template-columns:1fr 1fr;gap:10px 18px;margin-top:12px}
.qq div{display:flex;align-items:center;gap:12px;background:var(--g1);border-radius:10px;padding:10px 14px;font:700 23px/1.2 Manrope}
.qq b{flex:none;font:800 16px Manrope;letter-spacing:.06em;color:#fff;background:var(--red);border-radius:6px;padding:5px 8px}
.cur{margin-top:14px;font:600 21px/1.35 Manrope;color:var(--navy)}.cur b{color:var(--red)}
.foot .ref{flex:none}.foot .warn{font-size:18px}
</style>"""

def row(lbl, sub, n, pct, col, unit):
    return f'<div class="b2"><div class="w">{lbl}<small>{sub}</small></div><div class="t"><div style="width:{pct}%;background:var({col})"></div></div><div class="n" style="font-size:46px;white-space:nowrap;color:var({col})">{n}<small>{unit}</small></div></div>'

def nudillos(av):
    return f"""{S}<div class="wrap">{head(av,'MITO vs REALIDAD')}
<div class="mir">«Deja de tronarte los dedos, te va a dar artritis.»</div>
<h1 class="k">Tronarte los dedos <em>no</em><br>se asoció con artritis<br>de las manos.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>J Am Board Fam Med</i> 2011</span><span class="chip">215 personas de 50 a 89 años</span><span class="chip r">radiografía de la mano</span></div>
<div class="est"><h4>Artritis en las manos <span>(de cada 100 personas)</span></h4>
{row('Se truenan','los dedos','18',18.1/21.5*100,'--navy','de cada 100')}{row('No se truenan','los dedos','21,5',100,'--g2','de cada 100')}
<div class="cur"><b>Curiosidad:</b> un médico se tronó solo la mano izquierda por 60 años. Ninguna de las dos manos tuvo artritis.</div></div>
<div class="sh">Entonces, ¿cuándo sí revisarlo? <span>Si al tronar:</span></div>
<div class="yn"><div><i>1</i>Duele, se hincha o queda caliente la articulación</div><div><i>2</i>Amaneces con los dedos rígidos más de media hora</div><div><i>3</i>El dedo se traba o pierdes fuerza al agarrar</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">El «crac» es gas dentro del líquido de la articulación.</b> <b class="y">Mándaselo a quien siempre te dice que dejes de tronártelos.</b></p></div>
<div class="foot"><div class="warn"><b>Estudio pequeño, de casos y controles:</b> no prueba que sea del todo inofensivo. El médico es un caso de 1 persona (Unger, Arthritis Rheum 1998).</div>
<div class="ref">deWeber K, et al.<br>J Am Board Fam Med 2011;24(2):169-174<br>doi:10.3122/jabfm.2011.02.100156<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def glaucoma(av):
    return f"""{S}<div class="wrap">{head(av,'DATO ÚTIL')}
<div class="mir">«Veo bien; no necesito ir al oculista.»</div>
<h1 class="k">Glaucoma: <em>más de la mitad</em><br>no sabía que lo tenía.<br>Al inicio no duele ni avisa.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>Ophthalmology</i> 2021</span><span class="chip">55 estudios · 189.359 personas</span><span class="chip r">en todo el mundo</span></div>
<div class="est"><h4>Si tu papá, mamá o hermano lo tiene <span>(riesgo en la vida, de cada 100)</span></h4>
{row('Sin familiar','con glaucoma','2,3',2.3/22*100,'--g2','de cada 100')}{row('Con familiar','con glaucoma','22',100,'--red','de cada 100')}</div>
<div class="sh">¿Respondes «sí» a alguna? <span>Revísate los ojos:</span></div>
<div class="qq" style="margin-top:8px"><div><b>SÍ / NO</b>Tengo más de 40 años</div><div><b>SÍ / NO</b>Familiar con glaucoma</div><div><b>SÍ / NO</b>Tengo diabetes</div><div><b>SÍ / NO</b>Nunca me midieron el ojo</div></div>
<div class="yn" style="margin-top:12px;margin-bottom:18px"><div><i>1</i>Pide al oftalmólogo: presión del ojo y fondo de ojo</div><div><i>2</i>Primer control a los 40; antes y más seguido si hay familiar</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">La vista perdida no regresa, pero a tiempo se frena.</b> <b class="y">¿Tu papá o tu mamá usa gotas para el glaucoma? Mándaselo a tus hermanos.</b></p></div>
<div class="foot"><div class="warn"><b>Estudios de población.</b> Riesgo familiar: Wolfs, Arch Ophthalmol 1998 (Rotterdam, estudio pequeño). Control a los 40: Academia Americana de Oftalmología.</div>
<div class="ref">Soh Z, et al.<br>Ophthalmology 2021;128(10):1393-1404<br>doi:10.1016/j.ophtha.2021.04.009<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def pequenos(av):
    return f"""{S}<div class="wrap">{head(av,'ESTUDIO')}
<div class="mir">«Cambiar mis hábitos es imposible; no tengo tiempo.»</div>
<h1 class="k" style="font-size:56px">5 min más de sueño, 2 de moverte<br>y ½ porción más de verduras:<br>se asoció con <em>1 año más</em> de vida.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>eClinicalMedicine</i> 2026</span><span class="chip">59.078 adultos con pulsera</span><span class="chip r">observacional</span></div>
<div class="est"><h4>Años de vida extra frente a los peores hábitos</h4>
{row('Lo mínimo','los 3 cambios juntos','+1',1/9.35*100,'--grn','año')}{row('Lo ideal','7-8 h de sueño, 40 min de moverte','+9',100,'--grn','años')}</div>
<div class="sh">Empieza hoy por lo pequeño: <span>los 3 a la vez.</span></div>
<div class="yn"><div><i>1</i>Acuéstate 5 minutos antes esta noche</div><div><i>2</i>Sube escaleras o camina rápido 2 minutos</div><div><i>3</i>Suma media porción de verduras al almuerzo</div></div>
<div class="ojo" style="font-size:25px">El año extra se vio en quienes partían de los <b>peores hábitos</b>: ahí es donde lo pequeño pesa más.</div>
<div class="help"><div class="ic">✓</div><p><b class="g">Lo pequeño, sumado, sí cuenta.</b> <b class="y">Mándaselo a tu amigo que dice «el lunes empiezo».</b></p></div>
<div class="foot"><div class="warn"><b>Estudio observacional:</b> asociación, no causa. Reino Unido, edad promedio 64 años. El año extra es una estimación; expertos piden cautela.</div>
<div class="ref">Koemel NA, Stamatakis E, et al.<br>eClinicalMedicine 2026;103741<br>doi:10.1016/j.eclinm.2025.103741<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

JOBS = {
    'dr-viera-0730-tronarse-los-dedos': nudillos,
    'dr-viera-1230-glaucoma-familia': glaucoma,
    'dr-viera-1900-pequenos-cambios': pequenos,
}
if __name__ == '__main__':
    render(JOBS, pathlib.Path(__file__).resolve().parents[1] / '2026-11-12')
