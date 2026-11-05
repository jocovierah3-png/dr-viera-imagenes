# 5-nov-2026 · Modelo acv-v3, enfoque soluciones.
# 07:30 [MITO] «Si entreno de noche, luego no puedo dormir.» Stutz J, Eiholzer R, Spengler CM. Sports Med 2019;49(2):269-287 (revisión sistemática y metaanálisis; 23 estudios, 275 adultos sanos buenos durmientes; ejercicio de noche no empeoró el sueño; excepción: ejercicio fuerte que termina ≤1 h antes de acostarse, un solo estudio). DOI no verificado (PubMed bloqueado).
# 12:30 [COMPRADOR] «Me siento bien, no necesito el Papanicolaou.» Ronco G, et al. Lancet 2014;383(9916):524-532 (4 ensayos europeos, 176.464 mujeres de 20-64 años, mediana 6,5 años; prueba VPH vs Papanicolaou: razón de tasas 0,60 de cáncer invasivo). DOI no verificado.
# 19:00 [ALCANCE] «Duermo mis horas, aunque cada día a una hora distinta.» Windred DP, et al. Sleep 2024;47(1):zsad253. doi:10.1093/sleep/zsad253 (cohorte UK Biobank, 60.977 adultos con pulsera; los 4 grupos más regulares tuvieron 20 % a 48 % menos riesgo de morir que el menos regular; observacional).
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'kit'))
from plantilla import *
import importlib.util
_s = importlib.util.spec_from_file_location('d3', str(pathlib.Path(__file__).with_name('2026-11-03.py')))
_m = importlib.util.module_from_spec(_s); _s.loader.exec_module(_m)
S = _m.S

def noche(av):
    return f"""{S}<div class="wrap">{head(av,'MITO vs REALIDAD')}
<div class="mir">«Si entreno de noche, luego no puedo dormir.»</div>
<h1 class="k">Hacer ejercicio de noche<br><em>no te quita el sueño</em><br>si lo haces con calma.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>Sports Med</i> 2019</span><span class="chip">23 estudios · 275 adultos sanos</span><span class="chip r">buenos durmientes</span></div>
<div class="est"><h4>Ejercicio de noche <span>(vs. no hacer ejercicio)</span></h4>
<div class="cmp"><div class="gg"><b class="big" style="color:var(--grn)">Sin daño</b>ejercicio moderado: el sueño no empeoró</div><div class="rr"><b class="big">Ojo</b>el fuerte que termina 1 hora o menos antes de acostarte sí pudo empeorarlo</div></div></div>
<div class="ojo">El «solo en la mañana» <b>no se confirmó</b>. Lo que importa es <b>la intensidad y cuándo terminas.</b></div>
<div class="sh">Entonces, ¿qué hago? <span>Entrena cuando sí puedas:</span></div>
<div class="yn"><div><i>1</i>Mejor de noche que no moverte: elige tu horario</div><div><i>2</i>Si es fuerte, termina 1 hora antes de acostarte</div><div><i>3</i>Cierra con estiramientos y respiración lenta</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Si te desvelas igual,</b> prueba terminar más temprano. <b class="y">Mándaselo a quien dice que no tiene otro horario.</b></p></div>
<div class="foot"><div class="warn"><b>Estudios cortos:</b> una sesión, adultos sanos, calidad limitada.<br>Con insomnio, consulta a tu médico.</div>
<div class="ref">Stutz J, Eiholzer R, Spengler CM. Sports Med 2019;49:269-287<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def vph(av):
    return f"""{S}<div class="wrap">{head(av,'COMPRADOR')}
<div class="mir">«Me siento bien, no necesito el Papanicolaou.»</div>
<h1 class="k">Con la prueba del VPH<br>hubo <em>40 % menos</em> cánceres<br>de cuello uterino.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>Lancet</i> 2014</span><span class="chip">4 ensayos · 176.464 mujeres de 20 a 64 años</span><span class="chip r">cáncer de cuello uterino</span></div>
<div class="est"><h4>Cánceres invasivos de cuello uterino <span>(comparando 100 con Papanicolaou)</span></h4>
<div class="b2"><div class="w">Papanicolaou<small>referencia</small></div><div class="t"><div style="width:100%;background:var(--navy)"></div></div><div class="n">100<small>cánceres</small></div></div>
<div class="b2"><div class="w">Prueba del VPH<small>seguimiento 6,5 años</small></div><div class="t"><div style="width:60%;background:var(--grn)"></div></div><div class="n">60<small>cánceres</small></div></div></div>
<div class="ojo">Las lesiones del inicio <b>casi nunca duelen.</b> Por eso se buscan antes de sentir algo, no después.</div>
<div class="sh">Entonces, ¿qué hago? <span>Esta semana:</span></div>
<div class="yn"><div><i>1</i>Pregunta en tu centro de salud qué prueba te toca</div><div><i>2</i>Anota la fecha de tu último control</div><div><i>3</i>Pide cita y ve acompañada de alguien</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">¿Hace cuánto no se hace el control tu mamá o tu hermana?</b> <b class="y">Mándaselo hoy.</b></p></div>
<div class="foot"><div class="warn"><b>Ensayos al azar en Europa:</b> el beneficio apareció desde la 2.ª ronda.<br>Pregunta a tu médico cada cuánto repetirla.</div>
<div class="ref">Ronco G, et al. Lancet 2014;383:524-532<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def regular(av):
    pp = ''.join('<i class="r"></i>' if k == 0 else '<i style="background:var(--grn)"></i>' for k in range(5))
    return f"""{S}<div class="wrap">{head(av,'ESTUDIO')}
<div class="mir">«Duermo mis horas, aunque cada día a una hora distinta.»</div>
<h1 class="k">No solo cuenta<br><em>cuánto</em> duermes:<br>también <em>a qué hora.</em></h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>Sleep</i> 2024</span><span class="chip">60.977 adultos · pulsera 7 días</span><span class="chip r">estudio observacional</span></div>
<div class="est"><h4>5 grupos, de horario más irregular a más regular <span>(riesgo de morir)</span></h4>
<style>.u5 i{{height:70px!important}}</style><div class="ppl u5" style="grid-template-columns:repeat(5,1fr);gap:26px;margin-top:34px">{pp}</div>
<div class="mf"><div><b>Rojo</b>horario más irregular</div><div><b style="color:var(--grn)">20 a 48 %</b>menos riesgo en los 4 grupos más regulares</div></div></div>
<div class="ojo">Es asociación: <b>quien duerme a horas fijas también vive más ordenado.</b></div>
<div class="sh">Entonces, ¿qué hago? <span>Empieza por una hora:</span></div>
<div class="yn"><div><i>1</i>Fija la hora de levantarte, también el fin de semana</div><div><i>2</i>Acuéstate a una hora parecida cada noche</div><div><i>3</i>Abre las cortinas y sal a la luz en la mañana</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">No tiene que ser exacto:</b> acercarte ya es avance. <b class="y">Mándaselo a quien trasnocha de jueves a domingo.</b></p></div>
<div class="foot"><div class="warn"><b>Observacional:</b> asociación, no causa.<br>Participantes de Reino Unido, de 40 a 69 años.</div>
<div class="ref">Windred DP, et al. Sleep 2024;47(1):zsad253<br>doi:10.1093/sleep/zsad253<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

JOBS = {
    'dr-viera-0730-ejercicio-noche': noche,
    'dr-viera-1230-vph-papanicolaou': vph,
    'dr-viera-1900-horario-sueno': regular,
}
if __name__ == '__main__':
    render(JOBS, pathlib.Path(__file__).resolve().parents[1] / '2026-11-05')
