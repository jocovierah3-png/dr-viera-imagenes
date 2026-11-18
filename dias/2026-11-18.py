# 18-nov-2026 · Modelo acv-v3, enfoque soluciones.
# 07:30 [MITO] «Me tomo la glucosamina para las rodillas.» Wandel S, Jüni P, Tendal B, et al. BMJ 2010;341:c4675. doi:10.1136/bmj.c4675 (metaanálisis en red; 10 ensayos al azar, 3.803 personas con artrosis de cadera o rodilla; dolor frente a placebo en escala de 10 cm: glucosamina 0,4 cm menos (IC creíble 0,1-0,7), condroitina 0,3, combinación 0,5; diferencia mínima importante 0,9 cm; sin efecto en el espacio articular; ensayos pagados por la industria con más efecto). Solución: ejercicio, Cochrane CD004376 (2015/2024).
# 12:30 [COMPRADOR] «Mi mamá no duerme sin su pastilla.» Glass J, Lanctôt KL, Herrmann N, Sproule BA, Busto UE. BMJ 2005;331(7526):1169. doi:10.1136/bmj.38623.768588.47 (metaanálisis; 24 ensayos al azar contra placebo, 2.417 personas de 60 años o más con insomnio; +25,2 min de sueño total; 0,63 despertares menos; NNT 13 para mejor calidad de sueño; NNH 6 para cualquier efecto adverso; eventos cognitivos OR 4,78; psicomotores OR 2,61; cansancio de día OR 3,82).
# 19:00 [ALCANCE] «Me acuesto y mi cabeza no para.» Scullin MK, Krueger ML, Ballard HK, Pruett N, Bliwise DL. J Exp Psychol Gen 2018;147(1):139-146. doi:10.1037/xge0000374 (ensayo al azar en laboratorio de sueño con polisomnografía; 57 adultos de 18-30 sin problemas de sueño; 5 min escribiendo pendientes vs actividades ya hechas; se durmieron en ~15 vs ~25 min; más detalle = más rápido; sin grupo que no escribiera).
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'kit'))
from plantilla import *
import importlib.util
_s = importlib.util.spec_from_file_location('d17', str(pathlib.Path(__file__).with_name('2026-11-17.py')))
_m = importlib.util.module_from_spec(_s); _s.loader.exec_module(_m)
S, row = _m.S, _m.row
S += """<style>
.cmp{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:14px}
.cmp div{background:#fff;border-radius:12px;padding:16px 18px;font:700 24px/1.25 Manrope}
.cmp b.big{display:block;font:800 40px/1.05 Manrope;margin-bottom:6px}
.cmp .rr b.big{color:var(--red)}.cmp .gg b.big{color:var(--grn)}
</style>"""

def rodilla(av):
    return f"""{S}<div class="wrap">{head(av,'MITO vs REALIDAD')}
<div class="mir">«Me tomo la glucosamina para las rodillas.»</div>
<h1 class="k">Para el dolor de rodilla,<br>alivió <em>casi lo mismo</em><br>que una pastilla de mentira.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>BMJ</i> 2010</span><span class="chip">10 ensayos · 3.803 personas</span><span class="chip r">rodilla y cadera</span></div>
<div class="est"><h4>Alivio extra frente a placebo <span>(dolor de 0 a 10)</span></h4>
{row('Lo mínimo','que se nota','0,9',100,'--navy','puntos')}{row('Glucosamina','','0,4',0.4/0.9*100,'--red','puntos')}{row('Condroitina','','0,3',0.3/0.9*100,'--red','puntos')}
<div class="cur"><b>Ninguna llegó al mínimo que se nota.</b> Tampoco frenaron el desgaste en la radiografía.</div></div>
<div class="sh">Lo que sí alivia la rodilla: <span>moverla</span></div>
<div class="yn"><div><i>1</i>Ejercicios de fuerza para los muslos, 3 veces por semana</div><div><i>2</i>Camina o pedalea a tu ritmo: moverte no la gasta más</div><div><i>3</i>Si tienes sobrepeso, bajar un poco le quita carga</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">La rodilla que se mueve, duele menos.</b> <b class="y">Mándaselo a quien gasta en pastillas para las rodillas.</b></p></div>
<div class="foot"><div class="warn"><b>Metaanálisis de ensayos al azar.</b> Los pagados por fabricantes mostraron más efecto. Si la rodilla se hincha o se traba, consulta. No dejes un tratamiento indicado sin hablar con tu médico.</div>
<div class="ref">Wandel S, et al.<br>BMJ 2010;341:c4675<br>doi:10.1136/bmj.c4675<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def pastilla(av):
    return f"""{S}<div class="wrap">{head(av,'DATO ÚTIL')}
<div class="mir">«Mi mamá no duerme sin su pastilla.»</div>
<h1 class="k">Después de los 60, la pastilla<br>para dormir dio <em>25 minutos</em><br>más de sueño… y más efectos.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>BMJ</i> 2005</span><span class="chip">24 ensayos · 2.417 personas</span><span class="chip r">60 años o más</span></div>
<div class="est"><h4>Si la toman 13 personas mayores:</h4>
<div class="cmp"><div class="gg"><b class="big">1 de 13</b>duerme mejor gracias a la pastilla</div><div class="rr"><b class="big">2 de 13</b>tienen olvidos, mareo, confusión u otro efecto (1 de cada 6)</div></div></div>
<div class="sh">¿Tu mamá o tu papá…? <span>revísalo con ellos</span></div>
<div class="qq"><div><b>SÍ/NO</b>¿Toma algo para dormir hace meses?</div><div><b>SÍ/NO</b>¿Se ha tropezado o caído este año?</div><div><b>SÍ/NO</b>¿Está más olvidadiza o confundida?</div><div><b>SÍ/NO</b>¿Amanece cansada o mareada?</div></div>
<div class="yn"><div><i>1</i>Al médico: ¿todavía la necesita? ¿Y la terapia sin pastillas?</div><div><i>2</i>No se la quiten de golpe: se baja poco a poco y con el médico</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Dormir bien a los 70 sí se puede.</b> <b class="y">Mándaselo a tus hermanos.</b></p></div>
<div class="foot"><div class="warn"><b>Metaanálisis de ensayos al azar</b> con pastillas para dormir de receta. No la cambies por tu cuenta.</div>
<div class="ref">Glass J, et al.<br>BMJ 2005;331:1169<br>doi:10.1136/bmj.38623.768588.47<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def lista(av):
    return f"""{S}<div class="wrap">{head(av,'ESTUDIO','r')}
<div class="mir">«Me acuesto y mi cabeza no para con lo de mañana.»</div>
<h1 class="k">Anotar los pendientes<br>5 minutos antes de dormir:<br>se durmieron <em>unos 10 min antes</em>.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>J Exp Psychol Gen</i> 2018</span><span class="chip">57 adultos de 18 a 30</span><span class="chip r">laboratorio de sueño · al azar</span></div>
<div class="est"><h4>¿Cuánto tardaron en dormirse? <span>(minutos, aprox.)</span></h4>
{row('Escribieron','lo que ya hicieron','25',100,'--navy','min')}{row('Escribieron','los pendientes','15',60,'--grn','min')}
<div class="cur"><b>Mientras más detallada la lista,</b> más rápido se durmieron.</div></div>
<div class="sh">Pruébalo esta noche:</div>
<div class="yn"><div><i>1</i>Papel y lápiz junto a la cama, no el celular</div><div><i>2</i>Escribe todo lo pendiente, con detalle, por 5 minutos</div><div><i>3</i>Cierra el cuaderno, apaga la luz: ya quedó anotado</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Saca los pendientes de tu cabeza y ponlos en el papel.</b> <b class="y">Mándaselo a quien te escribe a la 1 a. m. «no puedo dormir».</b></p></div>
<div class="foot"><div class="warn"><b>Ensayo pequeño</b> en jóvenes sin insomnio y sin un grupo que no escribiera. Si te cuesta dormir casi cada noche por semanas, consúltalo.</div>
<div class="ref">Scullin MK, et al.<br>J Exp Psychol Gen 2018;147(1):139-146<br>doi:10.1037/xge0000374<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

JOBS = {
    'dr-viera-0730-glucosamina-rodillas': rodilla,
    'dr-viera-1230-pastilla-para-dormir-mayores': pastilla,
    'dr-viera-1900-lista-pendientes-dormir': lista,
}
if __name__ == '__main__':
    render(JOBS, pathlib.Path(__file__).resolve().parents[1] / '2026-11-18')
