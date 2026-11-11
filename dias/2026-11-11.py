# 11-nov-2026 · Modelo acv-v3, enfoque soluciones.
# 07:30 [MITO] «Le di dulce y se puso como loco.» Wolraich ML, Wilson DB, White JW. JAMA 1995;274(20):1617-1621. doi:10.1001/jama.1995.03530200053037 (metaanálisis de experimentos doble ciego con placebo: el azúcar no afectó conducta ni rendimiento cognitivo). Hoover DW, Milich R. J Abnorm Child Psychol 1994;22(4):501-515 (35 niños de 5-7 años; todos recibieron endulzante sin azúcar; las madres que creían que era azúcar los calificaron más hiperactivos).
# 12:30 [COMPRADOR] «Orino normal; mis riñones están bien.» GBD Chronic Kidney Disease Collaboration. Lancet 2020;395(10225):709-733. doi:10.1016/S0140-6736(20)30045-3 (2017: 697,5 millones con enfermedad renal crónica; prevalencia 9,1 %). CDC. Chronic Kidney Disease in the United States, 2023 (hasta 9 de cada 10 adultos con la enfermedad no lo saben; EE. UU.).
# 19:00 [ALCANCE] «Entre semana no tengo tiempo; solo el fútbol del sábado.» O'Donovan G, Lee IM, Hamer M, Stamatakis E. JAMA Intern Med 2017;177(3):335-342. doi:10.1001/jamainternmed.2016.8014 (63.591 adultos de 40+ en Inglaterra y Escocia; muerte por cualquier causa vs inactivos: fin de semana HR 0,70 (0,60-0,82); regularmente activos HR 0,65). Observacional.
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'kit'))
from plantilla import *
import importlib.util
_s = importlib.util.spec_from_file_location('d3', str(pathlib.Path(__file__).with_name('2026-11-03.py')))
_m = importlib.util.module_from_spec(_s); _s.loader.exec_module(_m)
S = _m.S + """<style>
.qq{display:grid;grid-template-columns:1fr 1fr;gap:10px 18px;margin-top:12px}
.qq div{display:flex;align-items:center;gap:12px;background:#fff;border-radius:10px;padding:10px 14px;font:700 23px/1.2 Manrope}
.qq b{flex:none;font:800 16px Manrope;letter-spacing:.06em;color:#fff;background:var(--red);border-radius:6px;padding:5px 8px}
.cmp div{font-size:22px}
.foot .ref{flex:none}.foot .warn{font-size:18px}
</style>"""

def azucar(av):
    return f"""{S}<div class="wrap">{head(av,'MITO vs REALIDAD')}
<div class="mir">«Le di dulce y se puso como loco.»</div>
<h1 class="k">El azúcar <em>no</em> vuelve<br>hiperactivos a los niños:<br>experimentos a ciegas<br>no vieron diferencia.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>JAMA</i> 1995</span><span class="chip">metaanálisis de experimentos</span><span class="chip r">doble ciego con placebo</span></div>
<div class="est"><h4>Lo que pasó cuando nadie sabía quién comió azúcar</h4>
<div class="cmp"><div class="gg"><b class="big">Sin cambio</b>Niños con azúcar vs con endulzante sin azúcar: igual conducta y atención</div><div class="rr"><b class="big">35 mamás</b>Todos los niños tomaron endulzante sin azúcar; las que creyeron que era azúcar vieron a su hijo más inquieto</div></div></div>
<div class="sh">Entonces, ¿qué lo pone así? <span>Y qué hacer:</span></div>
<div class="yn"><div><i>1</i>Mira la fiesta, el cansancio, la pantalla y la emoción</div><div><i>2</i>Igual limita los dulces: dañan dientes y suben el peso</div><div><i>3</i>Si la inquietud es diaria y afecta la escuela, consúltalo</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">No es el azúcar, pero tampoco es permiso.</b> <b class="y">Mándaselo al grupo de mamás y papás del colegio.</b></p></div>
<div class="foot"><div class="warn"><b>Estudios de los años 80 y 90.</b> No descartan que unos pocos niños sean sensibles. Hoover y Milich, J Abnorm Child Psychol 1994.</div>
<div class="ref">Wolraich ML, et al. JAMA 1995;274(20):1617-1621<br>doi:10.1001/jama.1995.03530200053037<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def rinon(av):
    ppl = ''.join('<i class="r"></i>' if k in (4,11) else '<i></i>' for k in range(14))
    return f"""{S}<div class="wrap">{head(av,'DATO ÚTIL')}
<div class="mir">«Orino normal; mis riñones están bien.»</div>
<h1 class="k">Casi <em>1 de cada 10</em> adultos<br>tiene los riñones dañados<br>y casi nadie lo sabe.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>Lancet</i> 2020</span><span class="chip">697,5 millones en el mundo</span><span class="chip r">al inicio no duele</span></div>
<div class="est"><h4>En una reunión familiar de 14 adultos, <span>1 o 2 podrían tenerlo</span></h4>
<div class="ppl" style="margin-top:22px">{ppl}</div>
<div class="mf"><div><b>9,1 %</b>de los adultos del mundo</div><div><b>9 de 10</b>no lo saben (EE. UU.)</div></div></div>
<div class="sh">¿Respondes «sí» a alguna? <span>Revísate:</span></div>
<div class="qq" style="margin-top:8px"><div><b>SÍ / NO</b>Tengo diabetes</div><div><b>SÍ / NO</b>Tengo presión alta</div><div><b>SÍ / NO</b>Familiar con riñón enfermo</div><div><b>SÍ / NO</b>Tengo más de 60 años</div></div>
<div class="yn" style="margin-top:12px;margin-bottom:18px"><div><i>1</i>Pide 2 exámenes: creatinina en sangre y albúmina en orina</div><div><i>2</i>Controla presión y azúcar: es lo que más daña el riñón</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Son 2 exámenes sencillos.</b> <b class="y">¿Tus papás tienen diabetes o presión? Pregúntales cuándo se los hicieron.</b></p></div>
<div class="foot"><div class="warn"><b>Estimaciones de población.</b> «9 de 10»: EE. UU., CDC 2023. Evita analgésicos a diario sin indicación médica.</div>
<div class="ref">GBD CKD. Lancet 2020;395:709-733<br>doi:10.1016/S0140-6736(20)30045-3<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def finde(av):
    def row(lbl, sub, n, pct, col):
        return f'<div class="b2"><div class="w">{lbl}<small>{sub}</small></div><div class="t"><div style="width:{pct}%;background:var({col})"></div></div><div class="n" style="font-size:46px;white-space:nowrap">{n}<small>por cada 100</small></div></div>'
    return f"""{S}<div class="wrap">{head(av,'ESTUDIO')}
<div class="mir">«Entre semana no tengo tiempo; solo el fútbol del sábado.»</div>
<h1 class="k">Ejercicio solo el finde:<br>se asoció con <em>30 % menos</em><br>riesgo de morir.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>JAMA Intern Med</i> 2017</span><span class="chip">63.591 adultos de 40 años o más</span><span class="chip r">observacional</span></div>
<div class="est"><h4>Riesgo de morir frente a no hacer ejercicio <span>(por cada 100)</span></h4>
{row('Sin ejercicio','comparación','100',100,'--red')}{row('Solo 1 o 2 días','fin de semana','70',70,'--grn')}{row('Varios días','a la semana','65',65,'--grn')}</div>
<div class="sh">La clave: <span>sumar 150 minutos a la semana, aunque sea en 1 o 2 días.</span></div>
<div class="yn"><div><i>1</i>Ejemplo: 90 minutos de fútbol el sábado y 60 caminando el domingo</div><div><i>2</i>Calienta 10 minutos y sube el esfuerzo poco a poco</div><div><i>3</i>Si te falta el aire o duele el pecho al esforzarte, revísate</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Cuenta el total de la semana, no cuántos días.</b> <b class="y">Mándaselo a tu pana del fútbol del sábado.</b></p></div>
<div class="foot"><div class="warn"><b>Estudio observacional:</b> asociación, no causa. Inglaterra y Escocia. Moverte varios días sigue siendo lo mejor.</div>
<div class="ref">O'Donovan G, et al.<br>JAMA Intern Med 2017;177(3):335-342<br>doi:10.1001/jamainternmed.2016.8014<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

JOBS = {
    'dr-viera-0730-azucar-ninos-hiperactivos': azucar,
    'dr-viera-1230-rinones-dos-examenes': rinon,
    'dr-viera-1900-ejercicio-fin-de-semana': finde,
}
if __name__ == '__main__':
    render(JOBS, pathlib.Path(__file__).resolve().parents[1] / '2026-11-11')
