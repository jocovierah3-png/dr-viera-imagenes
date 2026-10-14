# 14-oct-2026 · v2 "llevadera": una idea, un número, una acción. Director de arte + psicología de audiencia.
import sys, pathlib
sys.path.insert(0, '/tmp/claude-0/-home-claude/1f89a8fb-d9ec-542f-bc4e-25ccc8505639/scratchpad/repo/dr-viera-imagenes/kit')
from plantilla import *

S = """<style>
.mir{font:600 34px/1.3 Manrope;color:var(--g2);margin-top:auto}
.wrap>.help{margin-top:auto}
.mir q{quotes:"«" "»"}
h1.k{font:800 84px/1.0 Manrope;letter-spacing:-.035em;margin-top:18px}
.sub{font:600 30px/1.35 Manrope;color:var(--g2);margin-top:22px}
.sub b{color:var(--navy);font-weight:800}
/* números grandes */
.nums{display:grid;grid-template-columns:1fr 1fr;gap:28px;margin-top:56px}
.n b{display:block;font:800 104px/1 Manrope;letter-spacing:-.05em}
.n span{display:block;font:700 26px/1.25 Manrope;color:var(--g2);margin-top:8px}
.n.r b{color:var(--red)}
.arrow{display:flex;align-items:center;gap:30px;margin-top:52px}
.arrow .n b{font-size:132px}
.arrow .ar{font:800 96px/1 Manrope;color:var(--g2);margin-bottom:40px}
/* línea de excusa, sin caja */
.ex{font:700 30px/1.3 Manrope;margin-top:48px}
.ex span{color:var(--g2);font-weight:600}
/* escala de azúcar */
.scale{display:grid;grid-template-columns:1fr 1.5fr 1fr;margin-top:46px;border-radius:14px;overflow:hidden}
.scale div{padding:20px 22px}
.scale span{display:block;font:700 21px Manrope}
.scale b{display:block;font:800 40px/1.1 Manrope;margin-top:4px}
.sc1{background:var(--g1)}.sc2{background:var(--yel)}.sc3{background:var(--red);color:#fff}
.sc2 b{font-size:52px}
/* señales */
.sig{display:grid;grid-template-columns:1fr 1fr;gap:18px 26px;margin-top:22px}
.sig div{display:flex;gap:16px;align-items:center;font:700 29px/1.15 Manrope}
.sig i{flex:none;width:50px;height:50px;border-radius:12px;background:var(--red);color:#fff;font:800 27px Manrope;font-style:normal;display:flex;align-items:center;justify-content:center}
.lab2{font:800 22px Manrope;letter-spacing:.12em;color:var(--g2);margin-top:50px}
.help p{font-size:28px}
</style>"""

def vitc(av):
    return f"""{S}<div class="wrap">{head(av,'MITO')}
<div class="mir">¿Al primer estornudo, vitamina C?</div>
<h1 class="k">No evita<br><em>el resfriado.</em></h1>
<div class="nums" style="margin-top:44px"><div class="n"><b>29</b><span>estudios revisados</span></div><div class="n"><b>11.306</b><span>personas analizadas</span></div></div>
<div class="ex"><span>«Pero a mí sí me funciona.»</span><br>El resfriado se quita solo en unos días.</div>
<div class="help"><div class="ic">✓</div><p><b class="g">Lo que sí ayuda:</b> lavarte las manos y <b class="y">comer frutas.</b></p></div>
<div class="foot"><div class="warn">Solo ayudó a personas con ejercicio extremo.<br>¿Fiebre más de 4 días o falta de aire? Consulta.</div>
<div class="ref">Hemilä H, Chalker E. Cochrane 2013<br>doi:10.1002/14651858.CD000980.pub4<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def prediab(av):
    return f"""{S}<div class="wrap">{head(av,'DATO ÚTIL')}
<div class="mir">Te dijeron: «el azúcar, un poquito alta».</div>
<h1 class="k">No es «un poquito».<br><em>Es prediabetes.</em></h1>
<div class="sub" style="margin-top:40px">Tu azúcar en ayunas (mg/dL)</div>
<div class="scale" style="margin-top:14px"><div class="sc1"><span>Normal</span><b>hasta 99</b></div><div class="sc2"><span>Prediabetes</span><b>100 a 125</b></div><div class="sc3"><span>Diabetes</span><b>126 o más</b></div></div>
<div class="ex"><span>La buena noticia:</span><br>comer mejor y moverse bajó el riesgo<br>de diabetes a <em style="font-style:normal;color:var(--red)">menos de la mitad.</em></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Hoy:</b> camina 30 minutos. <b class="y">¿Salió alto? Llévalo a tu médico.</b></p></div>
<div class="foot"><div class="warn">Casi nadie siente síntomas.<br>Rangos: CDC / Asociación Americana de Diabetes.</div>
<div class="ref">Diabetes Prevention Program. N Engl J Med 2002<br>doi:10.1056/NEJMoa012512<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def acv(av):
    return f"""{S}<div class="wrap">{head(av,'ESTUDIO NUEVO','r')}
<div class="mir">«Eso les pasa a los mayores.»</div>
<h1 class="k">En menores de 55,<br><em>casi el doble.</em></h1>
<div class="sub">Derrames cerebrales por cada 100.000 personas al año</div>
<div class="arrow"><div class="n"><b>34</b><span>en 1993</span></div><div class="ar">→</div><div class="n r"><b>62</b><span>en 2020</span></div></div>
<div class="lab2">RECONÓCELO</div>
<div class="sig"><div><i>C</i>Cara caída</div><div><i>B</i>Brazo sin fuerza</div><div><i>H</i>Habla rara</div><div><i>T</i>Tiempo: llama al 911</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Hoy:</b> mídete la presión, <b class="y">aunque te sientas bien.</b></p></div>
<div class="foot"><div class="warn">Estudio observacional: muestra que aumentó,<br>no prueba por qué.</div>
<div class="ref">Fisher ER, et al. Neurology 2026<br>doi:10.1212/WNL.0000000000218622<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

JOBS = {'dr-viera-0730-vitamina-c': vitc, 'dr-viera-1230-prediabetes': prediab, 'dr-viera-1900-derrames-jovenes': acv}
if __name__ == '__main__':
    render(JOBS, pathlib.Path(__file__).resolve().parent / '2026-10-14-v2')
