# 30-oct-2026 · Modelo acv-v3, enfoque soluciones.
# 07:30 [MITO] «El café me hace daño al corazón.» Poole R, et al. BMJ 2017;359:j5024. doi:10.1136/bmj.j5024 (revisión paraguas: 201 metaanálisis observacionales y 17 de ensayos; 3-4 tazas/día vs nada: mortalidad total RR 0,83; cardiovascular RR 0,81).
# 12:30 [COMPRADOR] «Ya llevo años fumando, para qué dejarlo ahora.» Jha P, et al. N Engl J Med 2013;368:341-350. doi:10.1056/NEJMsa1211128 (113.752 mujeres y 88.496 hombres, EE. UU.; quien dejó a los 25-34, 35-44, 45-54 ganó ~10, 9 y 6 años).
# 19:00 [ALCANCE] «El protector solar es solo para ir a la playa.» Hughes MC, et al. Ann Intern Med 2013;158(11):781-790. doi:10.7326/0003-4819-158-11-201306040-00002 (ensayo al azar, 903 adultos <55, Nambour, Australia, 4,5 años; envejecimiento de la piel OR 0,76, IC 0,59-0,98).
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


def cafe(av):
    return f"""{S}<div class="wrap">{head(av,'MITO')}
<div class="mir">«El café me hace daño al corazón.»</div>
<h1 class="k">Quienes tomaban <em>3 a 4 tazas</em><br>de café al día tuvieron<br><em>17 % menos</em> riesgo de morir.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>BMJ</i> 2017</span><span class="chip">201 metaanálisis</span><span class="chip r">Estudios observacionales</span></div>
<div class="est"><h4>Riesgo de morir por cualquier causa <span>frente a no tomar café</span></h4>
<div class="b2"><div class="w">Sin café</div><div class="t"><div style="width:100%;background:var(--red)"></div></div><div class="n">1,00</div></div>
<div class="b2"><div class="w">3 a 4 tazas<small>al día</small></div><div class="t"><div style="width:83%;background:var(--navy)"></div></div><div class="n">0,83</div></div></div>
<div class="ojo">El mito dice que el café daña el corazón. Para la mayoría de adultos, <b>tomarlo con moderación no mostró daño.</b></div>
<div class="sh">Entonces, ¿qué hago? <span>Si ya lo tomas:</span></div>
<div class="yn"><div><i>1</i>Disfrútalo sin llenarlo de azúcar</div><div><i>2</i>Evita tomarlo tarde si te quita el sueño</div><div><i>3</i>Si te da palpitaciones, reduce y consulta</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Ojo:</b> en el embarazo conviene limitarlo, y en mujeres con riesgo de fracturas hay que consultar. Si no tomas café, no necesitas empezar. <b class="y">Mándaselo a quien te dice que el café le cae mal al corazón.</b></p></div>
<div class="foot"><div class="warn"><b>Se asoció, no se probó que cause.</b> Son estudios de<br>observación. Dolor de pecho o falta de aire: 911.</div>
<div class="ref">Poole R, et al. BMJ 2017;359:j5024<br>doi:10.1136/bmj.j5024<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def fumar(av):
    return f"""{S}<div class="wrap">{head(av,'COMPRADOR')}
<div class="mir">«Ya llevo años fumando. ¿Para qué dejarlo ahora?»</div>
<h1 class="k">Dejar de fumar a los<br><em>40 años</em> aún te devuelve<br>cerca de <em>9 años</em> de vida.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>NEJM</i> 2013</span><span class="chip">202.248 adultos</span><span class="chip r">Estudio de seguimiento · EE. UU.</span></div>
<div class="est"><h4>Años de vida que ganó quien dejó de fumar <span>frente a quien siguió</span></h4>
<div class="b2"><div class="w">Dejó a los<small>25 a 34 años</small></div><div class="t"><div style="width:100%;background:var(--navy)"></div></div><div class="n">10<small>años</small></div></div>
<div class="b2"><div class="w">Dejó a los<small>35 a 44 años</small></div><div class="t"><div style="width:90%;background:var(--navy)"></div></div><div class="n">9<small>años</small></div></div>
<div class="b2"><div class="w">Dejó a los<small>45 a 54 años</small></div><div class="t"><div style="width:60%;background:var(--navy)"></div></div><div class="n">6<small>años</small></div></div></div>
<div class="ojo">La excusa: «ya es tarde». <b>Dejarlo a cualquier edad suma años.</b></div>
<div class="sh">Entonces, ¿qué hago? <span>Esta semana:</span></div>
<div class="yn"><div><i>1</i>Escoge un día de estas 2 semanas</div><div><i>2</i>Cuéntaselo a tu familia: te acompañan</div><div><i>3</i>Pide a tu médico ayuda para dejarlo</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">No lo hagas solo:</b> con apoyo profesional es más fácil. Recaer no es fracasar. <b class="y">Mándaselo a quien fuma en tu casa.</b></p></div>
<div class="foot"><div class="warn"><b>Estudio de observación en EE. UU.:</b> se asoció, no se probó<br>que cause. Los años son promedios, no una promesa.</div>
<div class="ref">Jha P, et al. N Engl J Med 2013;368:341-350<br>doi:10.1056/NEJMsa1211128<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def solar(av):
    return f"""{S}<div class="wrap">{head(av,'ALCANCE')}
<div class="mir">«El protector solar es solo para la playa.»</div>
<h1 class="k">Ponerte protector <em>todos<br>los días</em> frenó <em>24 %</em><br>el envejecimiento de la piel.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>Annals of Internal Medicine</i> 2013</span><span class="chip">903 adultos</span><span class="chip r">Ensayo al azar · 4,5 años</span></div>
<div class="est"><h4>Envejecimiento de la piel <span>frente a usarlo solo a ratos</span></h4>
<div class="cmp"><div class="rr"><b class="big">A ratos</b>Más envejecimiento de la piel con los años.</div><div class="gg"><b class="big">Todos los días</b>24 % menos envejecimiento de la piel.</div></div></div>
<div class="ojo">En Ecuador el sol pega fuerte <b>aunque esté nublado.</b> La piel guarda el daño del sol año tras año.</div>
<div class="sh">Entonces, ¿qué hago? <span>Fácil, desde mañana:</span></div>
<div class="yn"><div><i>1</i>Cara, cuello y manos cada mañana</div><div><i>2</i>Vuelve a ponerte si pasas horas afuera</div><div><i>3</i>Gorra y sombra en las horas de más sol</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Hazlo hábito:</b> déjalo junto al cepillo de dientes. Pasó de «a veces» a «siempre» y la piel lo notó. <b class="y">Mándaselo a tu amigo que se asolea sin nada.</b></p></div>
<div class="foot"><div class="warn"><b>Ensayo en Australia:</b> el envejecimiento se midió en el dorso de la mano.<br>Lunar que cambia o sangra: consulta.</div>
<div class="ref">Hughes MC, et al. Ann Intern Med 2013;158(11):781-790<br>doi:10.7326/0003-4819-158-11-201306040-00002<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

JOBS = {
    'dr-viera-0730-cafe-corazon': cafe,
    'dr-viera-1230-dejar-de-fumar': fumar,
    'dr-viera-1900-protector-solar': solar,
}
if __name__ == '__main__':
    render(JOBS, pathlib.Path(__file__).resolve().parents[1] / '2026-10-30')
