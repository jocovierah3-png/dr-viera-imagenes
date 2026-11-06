# 6-nov-2026 · Modelo acv-v3, enfoque soluciones.
# 07:30 [MITO] «Tengo que tomar 8 vasos de agua al día, sí o sí.» Yamada Y, et al. Science 2022;378(6622):909-915 (n=5.604, 23 países, agua deuterada; promedio diario 1 a 6 L; hombres 4,3 L, mujeres 3,4 L; incluye agua de comida). DOI no verificado.
# 12:30 [COMPRADOR] «Mi mamá ya está mayor, pero está bien de la cabeza.» Eyting M, et al. Nature 2025;641:438-446. doi:10.1038/s41586-025-08800-x (experimento natural en Gales; vacuna contra el zóster: 20 % menos demencia nueva a 7 años, 3,5 puntos). Vacuna usada: Zostavax.
# 19:00 [ALCANCE] «Solo miro Instagram un ratito.» Calvert E, et al. JAMA Netw Open 2025;8(11):e2545245 (cohorte no aleatoria, 295 jóvenes de 18-24; ansiedad -16,1 %, depresión -24,8 %, insomnio -14,5 %). DOI no verificado.
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'kit'))
from plantilla import *
import importlib.util
_s = importlib.util.spec_from_file_location('d3', str(pathlib.Path(__file__).with_name('2026-11-03.py')))
_m = importlib.util.module_from_spec(_s); _s.loader.exec_module(_m)
S = _m.S

def agua(av):
    return f"""{S}<div class="wrap">{head(av,'MITO vs REALIDAD')}
<div class="mir">«Tengo que tomar 8 vasos de agua al día, sí o sí.»</div>
<h1 class="k">No hay una cifra igual<br>para todos: tu cuerpo usa<br>de <em>1 a 6 litros</em> al día.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>Science</i> 2022</span><span class="chip">5.604 personas · 23 países</span><span class="chip r">agua medida en el cuerpo</span></div>
<div class="est"><h4>Agua que el cuerpo renueva cada día <span>(incluye la de la comida)</span></h4>
<div class="cmp"><div class="gg"><b class="big" style="color:var(--grn)">1 a 6 L</b>el promedio varió así entre personas</div><div class="rr"><b class="big">4,3 vs 3,4 L</b>hombres vs mujeres, en promedio</div></div></div>
<div class="ojo">Lo que más la cambió: <b>cuánto te mueves, el calor y la edad.</b> No una regla fija.</div>
<div class="sh">Entonces, ¿qué hago? <span>Hazlo simple:</span></div>
<div class="yn"><div><i>1</i>Toma cuando tengas sed y con tus comidas</div><div><i>2</i>Más agua si hay calor, ejercicio o fiebre</div><div><i>3</i>Mira tu orina: amarillo claro es buena señal</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Con la comida también te hidratas.</b> <b class="y">Mándaselo a quien se obliga a tomar agua sin sed.</b></p></div>
<div class="foot"><div class="warn"><b>No es una receta:</b> con enfermedad del riñón o del corazón, sigue lo que te indique tu médico.<br>Estudio de medición, no de tratamiento.</div>
<div class="ref">Yamada Y, et al. Science 2022;378:909-915<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def zoster(av):
    return f"""{S}<div class="wrap">{head(av,'COMPRADOR')}
<div class="mir">«Mi mamá ya está mayor, pero está bien de la cabeza.»</div>
<h1 class="k">Quienes recibieron la vacuna<br>del zóster tuvieron<br><em>20 % menos demencia.</em></h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>Nature</i> 2025</span><span class="chip">Gales · 7 años de seguimiento</span><span class="chip r">adultos mayores</span></div>
<div class="est"><h4>Casos nuevos de demencia <span>(comparando 100 sin vacuna)</span></h4>
<div class="b2"><div class="w">Sin vacuna<small>referencia</small></div><div class="t"><div style="width:100%;background:var(--navy)"></div></div><div class="n">100<small>casos</small></div></div>
<div class="b2"><div class="w">Con vacuna<small>contra el zóster</small></div><div class="t"><div style="width:80%;background:var(--grn)"></div></div><div class="n">80<small>casos</small></div></div></div>
<div class="ojo">El zóster (culebrilla) lo causa el <b>virus de la varicela.</b></div>
<div class="sh">Entonces, ¿qué hago? <span>Esta semana:</span></div>
<div class="yn"><div><i>1</i>Revisa el carné de vacunas de tus papás</div><div><i>2</i>Pregunta a su médico si les toca la del zóster</div><div><i>3</i>Pregunta dónde la aplican y anota la fecha</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">¿Cuándo fue la última vez que revisaste las vacunas de tus papás?</b> <b class="y">Mándaselo a tus hermanos.</b></p></div>
<div class="foot"><div class="warn"><b>Experimento natural, no ensayo:</b> se asoció, no se probó causa. La vacuna usada fue la antigua.<br>Con la actual aún no se sabe.</div>
<div class="ref">Eyting M, et al. Nature 2025<br>doi:10.1038/s41586-025-08800-x<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def redes(av):
    def row(w, n, lab, pct, col='var(--grn)'):
        return f'<div class="b2"><div class="w">{lab}</div><div class="t"><div style="width:{pct}%;background:{col}"></div></div><div class="n">{n}<small>menos</small></div></div>'
    return f"""{S}<div class="wrap">{head(av,'ESTUDIO')}
<div class="mir">«Solo miro Instagram un ratito… y luego me siento peor.»</div>
<style>.rd .n{{white-space:nowrap;font-size:40px}}</style><h1 class="k">7 días sin redes y<br>los síntomas de depresión<br>bajaron <em>25 %.</em></h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>JAMA Netw Open</i> 2025</span><span class="chip">295 jóvenes de 18 a 24 años</span><span class="chip r">sin grupo al azar</span></div>
<div class="est rd"><h4>Cambio tras una semana sin redes <span>(escalas de síntomas)</span></h4>
{row(0,'24,8 %','Depresión',100)}{row(0,'16,1 %','Ansiedad',65)}{row(0,'14,5 %','Insomnio',58)}</div>
<div class="sh">Entonces, ¿qué hago? <span>Prueba 7 días:</span></div>
<div class="yn"><div><i>1</i>Borra del celular la red que más te enreda</div><div><i>2</i>Avisa a un amigo para hacerlo juntos</div><div><i>3</i>Cambia ese rato por caminar o llamar a alguien</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">No tienes que borrarlas para siempre.</b> <b class="y">Mándaselo al amigo que vive pegado al celular.</b></p></div>
<div class="foot"><div class="warn"><b>Sin grupo al azar:</b> eligieron hacerlo ellos. Efecto de 1 semana.<br>Si te sientes mal seguido, consulta.</div>
<div class="ref">Calvert E, et al. JAMA Netw Open 2025;8(11):e2545245<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

JOBS = {
    'dr-viera-0730-agua-8-vasos': agua,
    'dr-viera-1230-vacuna-zoster-demencia': zoster,
    'dr-viera-1900-semana-sin-redes': redes,
}
if __name__ == '__main__':
    render(JOBS, pathlib.Path(__file__).resolve().parents[1] / '2026-11-06')
