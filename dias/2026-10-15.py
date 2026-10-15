# 15-oct-2026 · Modelo acv-v3: espejo → golpe → prueba a escala humana → romper la excusa → acción → salida.
# 07:30 [MITO] Antibióticos y resfriado. Público: todos (mamá que guarda antibiótico). Barrera: «a mí siempre me funciona».
#   Kenealy T, Arroll B. Cochrane 2025;(11):CD000247 — RR curación 0,83 (0,60–1,14); efectos adversos adultos RR 2,62 (1,32–5,18). CDC (2026): cuándo consultar.
# 12:30 [COMPRADOR] Colesterol alto Ecuador. Barrera: «me siento bien». STEPS 2018: 34,7 % (M 40,7 %, H 28,3 %). CDC: 4–6 años. GBD JAMA 2026: 3,6 M muertes.
# 19:00 [ALCANCE] ¿Normal o lo reviso? Párpado que tiembla. Miedo oculto: «¿será algo del cerebro?». NHS.
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'kit'))
from plantilla import *

S = """<style>
.mir{font:700 31px/1.3 Manrope;color:var(--g2);margin-top:30px}
h1.k{font:800 62px/1.05 Manrope;letter-spacing:-.03em;margin-top:10px}
.est{margin-top:26px;background:var(--g1);border-radius:16px;padding:22px 26px}
.est h4{font:800 25px/1.25 Manrope}.est h4 span{color:var(--g2);font-weight:600}
.cmp{display:grid;grid-template-columns:200px 1fr 120px;align-items:center;gap:14px;margin-top:14px}
.cmp .y{font:800 23px/1.15 Manrope}.cmp .y small{display:block;font:600 16px Manrope;color:var(--g2)}
.cmp .t{height:44px;background:#fff;border-radius:6px;position:relative}.cmp .t div{position:absolute;inset:0 auto 0 0;border-radius:6px}
.cmp .n{font:800 50px/1 Manrope;text-align:right;letter-spacing:-.04em}.cmp .n small{display:block;font:700 15px Manrope;letter-spacing:0;color:var(--g2)}
.ojo{margin-top:24px;font-size:27px}
.sh{font:800 25px Manrope;margin-top:24px}.sh span{color:var(--g2);font-weight:600}
.yn{margin-top:12px;display:flex;flex-direction:column;gap:10px}
.yn div{display:flex;gap:14px;align-items:center;font:700 25px/1.2 Manrope}
.yn i{flex:none;width:40px;height:40px;border-radius:10px;background:var(--red);color:#fff;font:800 20px Manrope;font-style:normal;display:flex;align-items:center;justify-content:center}
.yn.n i{background:var(--navy)}
.ppl{display:grid;grid-template-columns:repeat(15,1fr);gap:8px 6px;margin-top:14px}
.ppl i{display:block;height:38px;border-radius:20px 20px 6px 6px;background:#C9CFD8;position:relative}
.ppl i:before{content:"";position:absolute;left:50%;top:-17px;width:17px;height:17px;margin-left:-8.5px;border-radius:50%;background:inherit}
.ppl{padding-top:16px;row-gap:24px}
.ppl i.r{background:var(--red)}
.mf{display:flex;gap:14px;margin-top:12px}
.mf div{flex:1;background:#fff;border-radius:10px;padding:10px 14px;font:700 21px/1.25 Manrope}.mf b{font:800 34px Manrope;color:var(--red);margin-right:6px}
.sem{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:22px}
.sem>div{border-radius:14px;padding:18px 20px}
.sem h3{font:800 20px Manrope;letter-spacing:.1em;margin-bottom:10px;display:flex;align-items:center;gap:10px}
.sem h3 i{width:22px;height:22px;border-radius:50%;display:block}
.sem p{font:700 25px/1.4 Manrope}
.sem .v{background:#E8F8EE}.sem .v h3{color:#15803D}.sem .v h3 i{background:var(--grn)}
.sem .a{background:#FFF7D1}.sem .a h3{color:#8A6D00}.sem .a h3 i{background:var(--yel)}
.cau{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-top:14px}
.cau div{background:var(--g1);border-radius:12px;padding:22px 8px;text-align:center;font:800 22px/1.2 Manrope}
.cau div span{display:block;font-size:38px;margin-bottom:4px}
.help p{font-size:25px}
</style>"""

def cmp(lab, sub, w, col, val, small):
    return (f'<div class="cmp"><div class="y">{lab}<small>{sub}</small></div>'
            f'<div class="t"><div style="width:{w}%;background:{col}"></div></div>'
            f'<div class="n" style="color:{col}">{val}<small>{small}</small></div></div>')

def antibioticos(av):
    return f"""{S}<div class="wrap">{head(av,'MITO vs REALIDAD')}
<div class="mir">«Tengo gripe, dame un antibiótico por si acaso.»</div>
<h1 class="k">El antibiótico<br><em>no cura el resfriado.</em><br>Y te puede caer mal.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>Cochrane</i> 2025</span><span class="chip">6 estudios · 1.147 personas</span><span class="chip r">Ensayos contra placebo</span></div>
<div class="est"><h4>Efectos secundarios en adultos con resfriado <span>(cuántas veces más)</span></h4>
{cmp('Sin antibiótico','pastilla falsa',100/2.62*0.95,'#102D50','1','vez')}
{cmp('Con antibiótico','y no se curaron antes',95,'#E92724','2,6','veces más')}</div>
<div class="ojo">«A mí siempre me funciona»: <b>el resfriado se quita solo</b> en 7 a 10 días, con o sin antibiótico.</div>
<div class="sh">Sí ve al médico si: <span>(CDC)</span></div>
<div class="yn"><div><i>!</i>Te falta el aire o respiras muy rápido</div><div><i>!</i>La fiebre dura más de 4 días</div><div><i>!</i>Mejoras y luego empeoras otra vez</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Lo que sí ayuda:</b> descanso, líquidos y manos limpias. <b class="y">Antibiótico solo con receta.</b></p></div>
<div class="foot"><div class="warn"><b>Revisión de ensayos:</b> los antibióticos atacan<br>bacterias; el resfriado es un virus. Usarlos sin<br>necesidad crea bacterias resistentes (OMS). <b>911</b></div>
<div class="ref">Kenealy T, Arroll B. Cochrane Database<br>Syst Rev 2025;(11):CD000247<br>doi:10.1002/14651858.CD000247.pub4<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def colesterol(av):
    ppl = ''.join('<i class="r"></i>' if k in (1,4,7,10,13,16,19,22,25,28) else '<i></i>' for k in range(30))
    return f"""{S}<div class="wrap">{head(av,'DATO ÚTIL')}
<div class="mir">«Me siento bien, ¿para qué me hago exámenes?»</div>
<h1 class="k">El colesterol alto<br><em>no duele.</em> Y lo tiene<br>1 de cada 3 adultos.</h1>
<div class="src" style="margin-top:22px"><span class="chip">Encuesta STEPS · MSP–OPS</span><span class="chip r">Ecuador · 18 a 69 años</span><span class="chip">34,7 %</span></div>
<div class="est"><h4>Imagina una reunión familiar: <span>30 adultos</span></h4>
<div class="ppl">{ppl}</div>
<div class="mf"><div><b>10</b>tendrían el colesterol alto</div><div><b>4 de 10</b>mujeres<br>y casi 3 de 10 hombres</div></div></div>
<div class="ojo" style="margin-top:18px">No da síntomas: <b>solo lo ve un examen de sangre.</b></div>
<div class="sh" style="margin-top:16px">¿Te toca medirte? <span>Si respondes SÍ a una:</span></div>
<div class="yn n" style="margin-bottom:18px"><div><i>?</i>¿Nunca te lo mediste o hace más de 4 años?</div><div><i>?</i>¿Tienes diabetes o presión alta?</div><div><i>?</i>¿Tu papá o mamá tiene colesterol alto?</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Pide un perfil de lípidos</b> en tu próximo chequeo. <b class="y">Y lleva a tus papás.</b></p></div>
<div class="foot"><div class="warn"><b>Encuesta poblacional:</b> mide cuántos, no por qué.<br>Sanos: cada 4 a 6 años; más seguido si hay<br>diabetes o familiares con colesterol alto (CDC).</div>
<div class="ref">MSP–INEC–OPS. Encuesta STEPS<br>Ecuador 2018 · CDC<br>GBD 2023 LDL Collaborators. JAMA 2026<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def parpado(av):
    return f"""{S}<div class="wrap">{head(av,'¿NORMAL O LO REVISO?')}
<div class="mir">«Me tiembla el ojo hace días… ¿será algo grave?»</div>
<h1 class="k">Que te tiemble<br>el párpado <em>casi siempre<br>es inofensivo.</em></h1>
<div class="src" style="margin-top:22px"><span class="chip">NHS · Reino Unido</span><span class="chip">Guía para pacientes</span><span class="chip r">Serie: ¿normal o lo reviso?</span></div>
<div class="sh" style="margin-top:28px">¿Cuántas tuviste esta semana? <span>Las causas más comunes:</span></div>
<div class="cau"><div><span>😩</span>Estrés</div><div><span>😴</span>Poco sueño</div><div><span>☕</span>Mucho café</div><div><span>🍺</span>Alcohol</div></div>
<div class="sem"><div class="v"><h3><i></i>NORMAL</h3><p>Solo el párpado.<br>Menos de 2 semanas.<br>Sin debilidad<br>ni rigidez.</p></div>
<div class="a"><h3><i></i>REVÍSALO SI</h3><p>Dura más de 2 semanas.<br>Aparece en otra parte.<br>La zona se siente débil o rígida.<br>Empezó con un medicamento.</p></div></div>
<div class="ojo">Lo curioso: <b>preocuparte puede empeorarlo.</b> El estrés es una de sus causas.</div>
<div class="help"><div class="ic">✓</div><p><b class="g">Esta semana:</b> duerme más y baja el café y el alcohol. <b class="y">Si tomas un medicamento, no lo dejes sin hablar con tu médico.</b></p></div>
<div class="foot"><div class="warn"><b>Contenido educativo:</b> no reemplaza<br>la consulta médica.</div>
<div class="ref">NHS. Twitching eyes and muscles<br>nhs.uk/symptoms<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

JOBS = {
    'dr-viera-0730-antibioticos-resfriado': antibioticos,
    'dr-viera-1230-colesterol-familia': colesterol,
    'dr-viera-1900-parpado-tiembla': parpado,
}
if __name__ == '__main__':
    render(JOBS, pathlib.Path(__file__).resolve().parents[1] / '2026-10-15')
