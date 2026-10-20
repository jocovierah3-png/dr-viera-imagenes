# 20-oct-2026 · Modelo acv-v3: espejo → golpe → prueba a escala humana → romper la excusa → acción → salida.
# Tarde [COMPRADOR] Glucosa nunca medida. Barrera: «si tuviera azúcar, lo sentiría». STEPS Ecuador 2018: 50 % nunca se midió la glucosa; 7,1 % glucosa alta/diabetes (18–69 años).
# 19:00 [ALCANCE] ¿Normal o lo reviso? Palpitaciones. Miedo oculto: «¿me va a dar un infarto?». NHS (heart palpitations).
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'kit'))
from plantilla import *

S = """<style>
.mir{font:700 31px/1.3 Manrope;color:var(--g2);margin-top:30px}
h1.k{font:800 62px/1.05 Manrope;letter-spacing:-.03em;margin-top:10px}
.est{margin-top:26px;background:var(--g1);border-radius:16px;padding:22px 26px}
.est h4{font:800 25px/1.25 Manrope}.est h4 span{color:var(--g2);font-weight:600}
.ojo{margin-top:22px;font-size:27px}
.sh{font:800 25px Manrope;margin-top:22px}.sh span{color:var(--g2);font-weight:600}
.yn{margin-top:12px;display:flex;flex-direction:column;gap:10px}
.yn div{display:flex;gap:14px;align-items:center;font:700 25px/1.2 Manrope}
.yn i{flex:none;width:40px;height:40px;border-radius:10px;background:var(--red);color:#fff;font:800 20px Manrope;font-style:normal;display:flex;align-items:center;justify-content:center}
.yn.n i{background:var(--navy)}
.ppl{display:grid;grid-template-columns:repeat(10,1fr);gap:8px 10px;margin-top:14px;padding-top:16px;row-gap:24px}
.ppl i{display:block;height:38px;border-radius:20px 20px 6px 6px;background:#C9CFD8;position:relative}
.ppl i:before{content:"";position:absolute;left:50%;top:-17px;width:17px;height:17px;margin-left:-8.5px;border-radius:50%;background:inherit}
.ppl i.r{background:var(--red)}
.mf{display:flex;gap:14px;margin-top:12px}
.mf div{flex:1;background:#fff;border-radius:10px;padding:10px 14px;font:700 21px/1.25 Manrope}.mf b{font:800 34px Manrope;color:var(--red);margin-right:6px}
.sem{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:22px}
.sem>div{border-radius:14px;padding:18px 20px}
.sem h3{font:800 20px Manrope;letter-spacing:.1em;margin-bottom:10px;display:flex;align-items:center;gap:10px}
.sem h3 i{width:22px;height:22px;border-radius:50%;display:block}
.sem p{font:700 24px/1.4 Manrope}
.sem .v{background:#E8F8EE}.sem .v h3{color:#15803D}.sem .v h3 i{background:var(--grn)}
.sem .a{background:#FFF7D1}.sem .a h3{color:#8A6D00}.sem .a h3 i{background:var(--yel)}
.urg{margin-top:16px;background:#FDECEC;border-radius:14px;padding:16px 20px;font:700 24px/1.35 Manrope}.urg b{color:var(--red)}
.cau{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-top:14px}
.cau div{background:var(--g1);border-radius:12px;padding:20px 8px;text-align:center;font:800 22px/1.2 Manrope}
.cau div span{display:block;font-size:38px;margin-bottom:4px}
.help p{font-size:25px}
</style>"""

def glucosa(av):
    ppl = ''.join('<i class="r"></i>' if k % 2 == 0 else '<i></i>' for k in range(20))
    return f"""{S}<div class="wrap">{head(av,'DATO ÚTIL')}
<div class="mir">«Si tuviera el azúcar alto, ya lo sentiría.»</div>
<h1 class="k">La mitad de los adultos<br>en Ecuador <em>nunca se ha<br>medido el azúcar.</em></h1>
<div class="src" style="margin-top:22px"><span class="chip">Encuesta STEPS · MSP–OPS</span><span class="chip r">Ecuador · 18 a 69 años</span><span class="chip">50 %</span></div>
<div class="est"><h4>Imagina tu oficina o tu barrio: <span>20 adultos</span></h4>
<div class="ppl">{ppl}</div>
<div class="mf"><div><b>10</b>nunca se midieron<br>el azúcar en la sangre</div><div><b>7 de 100</b>ya tienen<br>el azúcar alto o diabetes</div></div></div>
<div class="ojo">Al inicio <b>casi no da síntomas.</b> Cuando aparecen, puede llevar años haciendo daño.</div>
<div class="sh">¿Te toca medirte? <span>Si respondes SÍ a una:</span></div>
<div class="yn n"><div><i>?</i>¿Nunca te lo mediste o no te acuerdas?</div><div><i>?</i>¿Tu papá, mamá o hermanos tienen diabetes?</div><div><i>?</i>¿Tienes sobrepeso o presión alta?</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Pide una glucosa en ayunas</b> en tu próximo chequeo. <b class="y">Y lleva a tus papás.</b></p></div>
<div class="foot"><div class="warn"><b>Encuesta poblacional:</b> mide cuántos,<br>no por qué. Es un examen de sangre sencillo<br>en tu centro de salud.</div>
<div class="ref">MSP–INEC–OPS. Encuesta STEPS<br>Ecuador 2018 · Resumen ejecutivo<br>salud.gob.ec<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def palpitaciones(av):
    return f"""{S}<div class="wrap">{head(av,'¿NORMAL O LO REVISO?')}
<div class="mir">«De la nada sentí el corazón a mil… ¿me estará dando algo?»</div>
<h1 class="k">Sentir el corazón<br>acelerado <em>casi nunca<br>es algo grave.</em></h1>
<div class="src" style="margin-top:22px"><span class="chip">NHS · Reino Unido</span><span class="chip">Guía para pacientes</span><span class="chip r">Serie: ¿normal o lo reviso?</span></div>
<div class="sh" style="margin-top:26px">¿Cuál te pasó esta semana? <span>Las causas más comunes:</span></div>
<div class="cau"><div><span>☕</span>Café o energizantes</div><div><span>😰</span>Estrés o ansiedad</div><div><span>😴</span>Mal sueño</div><div><span>🏃</span>Ejercicio intenso</div></div>
<div class="sem"><div class="v"><h3><i></i>NORMAL</h3><p>Dura segundos<br>o pocos minutos.<br>Te sientes bien.<br>Tiene un porqué.</p></div>
<div class="a"><h3><i></i>REVÍSALO SI</h3><p>Se repite cada vez más.<br>Dura varios minutos.<br>Tienes algo del corazón<br>o familia con eso.</p></div></div>
<div class="urg"><b>Emergencia, llama al 911:</b> si no se detiene, o viene con dolor de pecho, falta de aire o desmayo.</div>
<div class="help"><div class="ic">✓</div><p><b class="g">Esta semana:</b> baja el café y los energizantes y duerme mejor. <b class="y">Si se repite, anota cuándo pasa.</b></p></div>
<div class="foot"><div class="warn"><b>Contenido educativo:</b> no reemplaza<br>la consulta médica.</div>
<div class="ref">NHS. Heart palpitations<br>nhs.uk/conditions<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

JOBS = {
    'dr-viera-tarde-glucosa-nunca-medida': glucosa,
    'dr-viera-1900-palpitaciones': palpitaciones,
}
if __name__ == '__main__':
    render(JOBS, pathlib.Path(__file__).resolve().parents[1] / '2026-10-20')
