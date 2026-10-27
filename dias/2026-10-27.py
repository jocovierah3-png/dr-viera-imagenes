# 27-oct-2026 · Modelo acv-v3.
# 07:30 [MITO] «Una copita al día es buena para el corazón.» Zhao J, et al. JAMA Netw Open 2023;6(3):e236185 (107 estudios, ~4,8 M; bajo consumo sin ventaja; riesgo desde 25 g/día mujeres, 45 g/día hombres).
# 12:30 [COMPRADOR] Apnea del sueño: «Ronco, pero duermo toda la noche.» Benjafield AV, et al. Lancet Respir Med 2019;7(8):687-698 (425 M moderada-grave, 30-69 años; estimación basada en literatura, financiada por ResMed).
# 19:00 [ALCANCE] «Entre semana duermo 5 h, el finde me desquito.» Åkerstedt T, et al. J Sleep Res 2019 (Suecia, >38.000 adultos, hasta 13 años; DOI no verificado).
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


def alcohol(av):
    return f"""{S}<div class="wrap">{head(av,'MITO vs REALIDAD')}
<div class="mir">«Una copita al día es buena para el corazón.»</div>
<h1 class="k">Tomar poco <em>no te hace vivir más:</em><br>en 107 estudios no hubo<br>ventaja frente a no tomar.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>JAMA Network Open</i> 2023</span><span class="chip">107 estudios</span><span class="chip r">4,8 millones de personas</span></div>
<div class="est"><h4>Riesgo de morir, <span>comparado con quien nunca tomó</span></h4>
<div class="cmp"><div class="gg"><b class="big">Toma poco</b>Sin menor riesgo de morir. La «protección» no apareció.</div><div class="rr"><b class="big">Toma más</b>Mujeres desde 25 g de alcohol al día y hombres desde 45 g: más riesgo de morir.</div></div></div>
<div class="ojo">El error común: <b>«la copa me cuida el corazón».</b> Los estudios viejos comparaban con exbebedores enfermos.</div>
<div class="sh">Entonces, ¿qué hago? <span>Según tu caso:</span></div>
<div class="yn"><div><i>1</i>Si no tomas: no empieces «por salud»</div><div><i>2</i>Si tomas: que no sea tu excusa de salud</div><div><i>3</i>Si tomas seguido: cuéntaselo a tu médico</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Tu corazón se cuida con:</b> moverte, no fumar y revisar tu presión. <b class="y">Mándaselo a quien dice «una copita no hace daño».</b></p></div>
<div class="foot"><div class="warn"><b>Metaanálisis de estudios observacionales:</b><br>se asoció, no prueba causa. Cada persona<br>y cada caso son distintos.</div>
<div class="ref">Zhao J, et al. JAMA Netw Open 2023;6(3):e236185<br>doi:10.1001/jamanetworkopen.2023.6185<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def apnea(av):
    return f"""{S}<div class="wrap">{head(av,'DATO ÚTIL')}
<div class="mir">«Yo ronco, pero duermo toda la noche.»</div>
<h1 class="k"><em>425 millones</em> de adultos<br>de 30 a 69 años tienen apnea<br>del sueño moderada o grave.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>Lancet Respir Med</i> 2019</span><span class="chip">Estimación mundial</span><span class="chip r">Adultos de 30 a 69 años</span></div>
<div class="est"><h4>Apnea del sueño: <span>la respiración se corta mientras duermes</span></h4>
<div class="mf"><div><b>936 M</b>con apnea<br>leve a grave</div><div><b>425 M</b>moderada<br>o grave</div></div></div>
<div class="ojo">A menudo <b>no se nota:</b> lo ve quien duerme a tu lado.</div>
<div class="sh">¿Te toca revisarte? <span>Si respondes SÍ a 2 o más:</span></div>
<div class="yn"><div><i>?</i>¿Roncas fuerte?</div><div><i>?</i>¿Despiertas cansado aunque duermas?</div><div><i>?</i>¿Alguien notó que dejas de respirar?</div><div><i>?</i>¿Tienes la presión alta?</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Consúltalo:</b> existe un estudio del sueño que lo confirma. <b class="y">Pregúntales a tus papás: ¿roncan y se quedan sin aire?</b></p></div>
<div class="foot"><div class="warn"><b>Estimación basada en la literatura,</b> no un censo.<br>Estudio financiado por ResMed. El ronquido<br>solo no significa apnea.</div>
<div class="ref">Benjafield AV, et al. Lancet Respir Med<br>2019;7(8):687-698 · doi:10.1016/S2213-2600(19)30198-5<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def finde(av):
    return f"""{S}<div class="wrap">{head(av,'ESTUDIO NUEVO','r')}
<div class="mir">«De lunes a viernes duermo 5 horas. El sábado me desquito.»</div>
<h1 class="k">Dormir poco entre semana<br>solo se asoció con <em>más riesgo</em><br>si el finde no lo compensabas.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>J Sleep Res</i> 2019</span><span class="chip">Suecia · +38.000 adultos</span><span class="chip r">Hasta 13 años de seguimiento</span></div>
<div class="est"><h4>5 horas o menos entre semana, <span>menores de 65 años</span></h4>
<div class="cmp"><div class="rr"><b class="big">Poco el finde</b>Más riesgo de morir que quien dormía 6 a 7 horas.</div><div class="gg"><b class="big">Más el finde</b>Sin más riesgo de morir en este estudio.</div></div></div>
<div class="ojo">El error: <b>«me desquito el finde, duermo mal toda la semana».</b></div>
<div class="sh">Lo que sí dice el estudio <span>(el autor lo llama «tentativo»):</span></div>
<div class="yn"><div><i>1</i>Dormir cada noche sigue siendo lo mejor</div><div><i>2</i>Si te faltó, el finde ayuda a recuperar</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Esta semana:</b> acuéstate 30 minutos antes que hoy. <b class="y">Mándaselo a tu amigo que vive con 5 horas.</b></p></div>
<div class="foot"><div class="warn"><b>Estudio observacional:</b> se asoció, no prueba causa.<br>Una sola encuesta de sueño (1997). Conclusión<br>tentativa según los autores.</div>
<div class="ref">Åkerstedt T, et al. J Sleep Res 2019<br>Sleep duration and mortality: does weekend sleep matter?<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

JOBS = {
    'dr-viera-0730-copita-corazon': alcohol,
    'dr-viera-1230-apnea-ronquido': apnea,
    'dr-viera-1900-dormir-poco-finde': finde,
}
if __name__ == '__main__':
    render(JOBS, pathlib.Path(__file__).resolve().parents[1] / '2026-10-27')
