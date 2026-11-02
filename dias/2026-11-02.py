# 2-nov-2026 · Modelo acv-v3, enfoque soluciones.
# 07:30 [DATO ÚTIL] «Con comer una frutita al día ya cumplo.» Wang DD, et al. Circulation 2021;143(17):1642-1654. doi:10.1161/CIRCULATIONAHA.120.048996 (2 cohortes de EE. UU. + metaanálisis de 26 cohortes, 1.892.885 personas, 145.015 muertes; 5 porciones/día vs 2: mortalidad total HR 0,87, IC 0,85-0,90; jugos y papas sin beneficio).
# 12:30 [COMPRADOR] «Mi mamá se olvida de todo, pero es normal por la edad.» Livingston G, et al. Lancet 2024;404:572-628. doi:10.1016/S0140-6736(24)01296-0 (Comisión Lancet: 14 factores modificables; hasta 45 % de los casos de demencia podrían prevenirse o retrasarse; pérdida de audición y colesterol LDL alto en la mediana edad ~7 % cada uno; estimación que asume causalidad).
# 19:00 [ALCANCE] «Me duele la espalda y siempre vuelve.» Pocovi NC, et al. Lancet 2024;404(10448):134-144 (WalkBack, ensayo al azar, 701 adultos recuperados de dolor lumbar, Australia; recaída que limita actividades HR 0,72, IC 0,60-0,85; mediana 208 vs 112 días). DOI no verificado (PubMed bloqueado).
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'kit'))
from plantilla import *

S = """<style>
.mir{font:700 31px/1.3 Manrope;color:var(--g2);margin-top:24px}
h1.k{font:800 62px/1.05 Manrope;letter-spacing:-.03em;margin-top:10px}
.est{margin-top:22px;background:var(--g1);border-radius:16px;padding:22px 26px}
.est h4{font:800 25px/1.25 Manrope}.est h4 span{color:var(--g2);font-weight:600}
.ojo{margin-top:22px;font-size:27px}
.sh{font:800 25px Manrope;margin-top:22px}.sh span{color:var(--g2);font-weight:600}
.yn{margin-top:12px;display:flex;flex-direction:column;gap:10px}
.yn div{display:flex;gap:14px;align-items:center;font:700 25px/1.2 Manrope}
.yn i{flex:none;width:40px;height:40px;border-radius:10px;background:var(--navy);color:#fff;font:800 20px Manrope;font-style:normal;display:flex;align-items:center;justify-content:center}
.ppl{display:grid;grid-template-columns:repeat(14,1fr);gap:8px;margin-top:30px}
.ppl i{display:block;height:38px;border-radius:20px 20px 6px 6px;background:#C9CFD8;position:relative}
.ppl i:before{content:"";position:absolute;left:50%;top:-17px;width:17px;height:17px;margin-left:-8.5px;border-radius:50%;background:inherit}
.ppl i.r{background:var(--red)}
.mf{display:flex;gap:14px;margin-top:14px}
.mf div{flex:1;background:#fff;border-radius:10px;padding:10px 14px;font:700 21px/1.25 Manrope}.mf b{font:800 34px Manrope;color:var(--red);margin-right:6px}
.b2{display:grid;grid-template-columns:200px 1fr 130px;align-items:center;gap:14px;margin-top:8px}
.b2 .w{font:800 25px/1.15 Manrope}.b2 .w small{display:block;font:600 17px Manrope;color:var(--g2)}
.b2 .t{height:46px;background:#fff;border-radius:6px;position:relative}.b2 .t div{position:absolute;left:0;top:0;bottom:0;border-radius:6px}
.b2 .n{font:800 50px/1 Manrope;letter-spacing:-.04em;text-align:right}.b2 .n small{display:block;font:700 15px Manrope;letter-spacing:0;color:var(--g2)}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:14px 22px;margin-top:14px}
.grid2 div{display:flex;gap:12px;align-items:center;font:700 25px/1.2 Manrope}
.grid2 i{flex:none;width:38px;height:38px;border-radius:10px;background:var(--red);color:#fff;font:800 22px Manrope;font-style:normal;display:flex;align-items:center;justify-content:center}
.help p{font-size:25px}
.cmp{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:14px}
.cmp div{background:#fff;border-radius:12px;padding:16px 18px;font:700 24px/1.25 Manrope}
.cmp b.big{display:block;font:800 40px/1.05 Manrope;margin-bottom:6px}
.cmp .rr b.big{color:var(--red)}.cmp .gg b.big{color:var(--navy)}
</style>"""






def fruta(av):
    return f"""{S}<div class="wrap">{head(av,'DATO ÚTIL')}
<div class="mir">«Con comer una frutita al día ya cumplo.»</div>
<h1 class="k">Con <em>5 porciones</em> al día<br>de fruta y verdura: <em>13 % menos</em><br>riesgo de morir.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>Circulation</i> 2021</span><span class="chip">26 estudios · 1,9 millones de personas</span><span class="chip r">145.015 muertes</span></div>
<div class="est"><h4>Riesgo de morir por cualquier causa <span>(1,00 = 2 porciones al día)</span></h4>
<div class="b2"><div class="w">2 porciones<small>al día</small></div><div class="t"><div style="width:50%;background:var(--navy)"></div></div><div class="n">1,00<small>referencia</small></div></div>
<div class="b2"><div class="w">5 porciones<small>al día</small></div><div class="t"><div style="width:43.5%;background:var(--grn)"></div></div><div class="n">0,87<small>0,85 a 0,90</small></div></div></div>
<div class="ojo">Más de 5 <b>no mejoró</b> el resultado. Y <b>jugos y papas no cuentan</b>: no mostraron beneficio.</div>
<div class="sh">Entonces, ¿qué hago? <span>Llega a 5 sin complicarte:</span></div>
<div class="yn"><div><i>1</i>2 de fruta: una al desayuno y otra de postre</div><div><i>2</i>3 de verdura: mitad del plato en almuerzo y cena</div><div><i>3</i>Fruta entera, no en jugo; ten una a la vista</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Una porción</b> es una fruta mediana o una taza de verdura. <b class="y">Mándaselo a quien come “una frutita” y ya.</b></p></div>
<div class="foot"><div class="warn"><b>Estudio observacional:</b> asociación, no causa.<br>Con enfermedad del riñón, pregunta a tu médico por el potasio.</div>
<div class="ref">Wang DD, et al. Circulation 2021;143:1642-1654<br>doi:10.1161/CIRCULATIONAHA.120.048996<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def demencia(av):
    gente=''.join('<i class="r"></i>' if k<9 else '<i></i>' for k in range(20))
    return f"""{S}<div class="wrap">{head(av,'COMPRADOR')}
<div class="mir">«Mi mamá se olvida de todo, pero es normal por la edad.»</div>
<h1 class="k">Hasta <em>45 de cada 100</em><br>casos de demencia se podrían<br><em>prevenir o retrasar.</em></h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>The Lancet</i> 2024</span><span class="chip">Comisión de expertos</span><span class="chip r">14 factores que sí se pueden cambiar</span></div>
<div class="est"><h4>De cada 100 casos de demencia <span>(estimación)</span></h4>
<div class="ppl" style="grid-template-columns:repeat(20,1fr);gap:6px">{gente}</div>
<div class="mf"><div><b>45</b>podrían evitarse o retrasarse</div><div><b>7</b>se vinculan a oír mal · <b>7</b>a colesterol malo alto</div></div></div>
<div class="ojo">Es una <b>estimación</b>: supone que esos factores causan demencia y que se corrigen todos. Aun así, <b>mucho se puede hacer.</b></div>
<div class="sh">Entonces, ¿qué hago? <span>Por tus papás (y por ti):</span></div>
<div class="yn"><div><i>1</i>Revisa su oído y su vista; si no oyen bien, consulta</div><div><i>2</i>Mide colesterol y presión, también a los 40 y 50</div><div><i>3</i>Que caminen, tengan compañía y no fumen</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Olvidos que estorban su día</b> merecen consulta. <b class="y">¿Hace cuánto no revisan el oído de tus papás? Mándaselo a tus hermanos.</b></p></div>
<div class="foot"><div class="warn"><b>Comisión de expertos:</b> estimación poblacional, no garantía individual.<br>No es un diagnóstico; ante dudas, consulta.</div>
<div class="ref">Livingston G, et al. Lancet 2024;404:572-628<br>doi:10.1016/S0140-6736(24)01296-0<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def espalda(av):
    return f"""{S}<div class="wrap">{head(av,'ESTUDIO NUEVO')}
<div class="mir">«Me duele la espalda y siempre vuelve.»</div>
<h1 class="k">Caminar con un plan<br>retrasó la recaída:<br><em>208 días</em> en vez de <em>112.</em></h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>The Lancet</i> 2024</span><span class="chip">Ensayo al azar · 701 adultos</span><span class="chip r">Australia</span></div>
<div class="est"><h4>Días hasta que el dolor de espalda volvió <span>(mediana)</span></h4>
<div class="b2"><div class="w">Sin plan<small>de caminata</small></div><div class="t"><div style="width:54%;background:var(--red)"></div></div><div class="n">112<small>días</small></div></div>
<div class="b2"><div class="w">Con plan<small>de caminata</small></div><div class="t"><div style="width:100%;background:var(--grn)"></div></div><div class="n">208<small>días</small></div></div></div>
<div class="ojo">Riesgo de recaída que limita tu día: <b>28 % menor</b> (HR 0,72; 0,60 a 0,85).</div>
<div class="sh">Entonces, ¿qué hago? <span>Cuando ya no te duele:</span></div>
<div class="yn"><div><i>1</i>Camina todos los días, empieza con pocos minutos</div><div><i>2</i>Sube el tiempo poco a poco, cada semana</div><div><i>3</i>Levántate cada hora si trabajas sentado</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Se estudió tras recuperarse</b> de un episodio. <b class="y">Mándaselo a tu amigo que vive con la espalda mal.</b></p></div>
<div class="foot"><div class="warn"><b>Ensayo al azar:</b> adultos ya recuperados. Si hay debilidad en las piernas,<br>fiebre o dolor tras un golpe: consulta pronto.</div>
<div class="ref">Pocovi NC, et al. Lancet 2024;404:134-144 (WalkBack)<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

JOBS = {
    'dr-viera-0730-fruta-verdura': fruta,
    'dr-viera-1230-demencia-padres': demencia,
    'dr-viera-1900-espalda-caminar': espalda,
}
if __name__ == '__main__':
    render(JOBS, pathlib.Path(__file__).resolve().parents[1] / '2026-11-02')
