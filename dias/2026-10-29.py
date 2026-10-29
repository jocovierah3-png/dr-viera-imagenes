# 29-oct-2026 · Modelo acv-v3, enfoque soluciones.
# 07:30 [DATO ÚTIL] «Sin sal la comida no sabe a nada.» Neal B, et al. NEJM 2021;385:1067-1077. doi:10.1056/NEJMoa2105675 (SSaSS, 20.995 personas, 600 aldeas de China; 29,14 vs 33,65 derrames por 1.000 personas-año; RR 0,86, IC 0,77-0,96; seguimiento 4,74 años).
# 12:30 [COMPRADOR] «Mi papá ya camina lento; que no se esfuerce.» Sherrington C, et al. Cochrane Database Syst Rev 2019;(1):CD012424. doi:10.1002/14651858.CD012424.pub2 (versión abreviada BJSM 2020;54:885: 59 estudios, 12.981 personas; RaR 0,77, IC 0,71-0,83; equilibrio y funcional 0,76).
# 19:00 [ALCANCE] «Entre la oficina y el celular no tengo tiempo para nada.» White MP, et al. Sci Rep 2019;9:7730. doi:10.1038/s41598-019-44097-3 (19.806 personas, Inglaterra; transversal; 120-179 min/semana OR 1,59 salud buena).
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

def sal(av):
    return f"""{S}<div class="wrap">{head(av,'DATO ÚTIL')}
<div class="mir">«Sin sal, la comida no sabe a nada.»</div>
<h1 class="k">Cambiar el salero por<br>una sal con <em>potasio</em> redujo<br><em>14 %</em> los derrames cerebrales.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>NEJM</i> 2021</span><span class="chip">20.995 personas</span><span class="chip r">Ensayo al azar · casi 5 años</span></div>
<div class="est"><h4>Derrames cerebrales <span>por cada 1.000 personas al año</span></h4>
<div class="b2"><div class="w">Sal común</div><div class="t"><div style="width:100%;background:var(--red)"></div></div><div class="n">33,7</div></div>
<div class="b2"><div class="w">Sal con potasio</div><div class="t"><div style="width:86.6%;background:var(--navy)"></div></div><div class="n">29,1</div></div></div>
<div class="ojo">Son <b>4 a 5 derrames menos</b> por cada 1.000 personas cada año. Sin dejar de comer rico.</div>
<div class="sh">Entonces, ¿qué hago? <span>Fácil, desde hoy:</span></div>
<div class="yn"><div><i>1</i>Pregunta en la tienda por sal con potasio</div><div><i>2</i>Úsala en el salero, en lugar de la sal común</div><div><i>3</i>Quita el salero de la mesa: prueba antes de echar</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Antes de cambiar:</b> si tú o tus papás tienen enfermedad del riñón o toman pastillas que suben el potasio, consulten al médico. <b class="y">Mándaselo a quien más sal le echa a la comida.</b></p></div>
<div class="foot"><div class="warn"><b>Ensayo en aldeas de China</b> con adultos con derrame<br>previo o presión alta. En otros países puede variar.<br>Señales de derrame: 911.</div>
<div class="ref">Neal B, et al. N Engl J Med 2021;385:1067-1077<br>doi:10.1056/NEJMoa2105675<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def caidas(av):
    return f"""{S}<div class="wrap">{head(av,'DATO ÚTIL')}
<div class="mir">«Mi papá ya camina lento. Mejor que no se esfuerce.»</div>
<h1 class="k">Mover más a los abuelos<br>puede evitar <em>23 de cada<br>100 caídas.</em></h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>Cochrane</i> 2019</span><span class="chip">59 estudios</span><span class="chip r">12.981 adultos mayores</span></div>
<div class="est"><h4>Con ejercicios de equilibrio y fuerza, <span>menos caídas en casa</span></h4>
<div class="cmp"><div class="rr"><b class="big">Sin ejercicio</b>100 caídas</div><div class="gg"><b class="big">Con ejercicio</b>77 caídas</div></div></div>
<div class="ojo">El error: <b>«que repose, así no se cae»</b>. Quedarse quieto debilita las piernas y el equilibrio.</div>
<div class="sh">¿Tu papá o tu mamá…? <span>Si dices SÍ a 1:</span></div>
<div class="yn"><div><i>?</i>¿Se cayó en el último año?</div><div><i>?</i>¿Se agarra de los muebles al caminar?</div><div><i>?</i>¿Sale menos por miedo a caerse?</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Esta semana:</b> pídele que se pare y se siente de una silla firme 5 veces, con alguien cerca. Y consulta por un plan de ejercicios de equilibrio. <b class="y">¿Hace cuánto no se miden tus papás? Mándaselo a tus hermanos.</b></p></div>
<div class="foot"><div class="warn"><b>Metaanálisis de ensayos:</b> el ejercicio debe adaptarse a cada persona.<br>Consulta a su médico antes de empezar.<br>Tras una caída con golpe fuerte: 911.</div>
<div class="ref">Sherrington C, et al. Cochrane Database Syst Rev 2019;(1):CD012424<br>doi:10.1002/14651858.CD012424.pub2<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def naturaleza(av):
    return f"""{S}<div class="wrap">{head(av,'DATO ÚTIL')}
<div class="mir">«Entre la oficina y el celular, no tengo tiempo para nada.»</div>
<h1 class="k">Quienes pasaron <em>2 horas<br>a la semana</em> en la<br>naturaleza se sentían mejor.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>Scientific Reports</i> 2019</span><span class="chip">19.806 personas</span><span class="chip r">Inglaterra · encuesta</span></div>
<div class="est"><h4>Tiempo en parques, playa o campo <span>en la última semana</span></h4>
<div class="cmp"><div class="rr"><b class="big">Menos de 2 h</b>Sin diferencia frente a no salir.</div><div class="gg"><b class="big">2 h o más</b>1,6 veces más probabilidad de decir que su salud es buena.</div></div></div>
<div class="ojo">Lo mejor: <b>no tienen que ser seguidas.</b> Valía sumar visitas cortas durante la semana.</div>
<div class="sh">Entonces, ¿qué hago? <span>Suma 2 horas:</span></div>
<div class="yn"><div><i>1</i>20 minutos al día en un parque o jardín</div><div><i>2</i>Almuerza afuera, lejos de la pantalla</div><div><i>3</i>Un paseo largo el fin de semana</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Hoy:</b> sal 20 minutos a un parque o calle con árboles, sin celular. <b class="y">Mándaselo a tu amigo que vive pegado a la pantalla.</b></p></div>
<div class="foot"><div class="warn"><b>Estudio de encuesta:</b> asociación, no causa. Las personas<br>sanas quizá salen más. La salud la reportaron ellas mismas.<br>Si te sientes mal por semanas, consulta.</div>
<div class="ref">White MP, et al. Sci Rep 2019;9:7730<br>doi:10.1038/s41598-019-44097-3<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

JOBS = {
    'dr-viera-0730-sal-potasio': sal,
    'dr-viera-1230-caidas-padres': caidas,
    'dr-viera-1900-naturaleza-2h': naturaleza,
}
if __name__ == '__main__':
    render(JOBS, pathlib.Path(__file__).resolve().parents[1] / '2026-10-29')
