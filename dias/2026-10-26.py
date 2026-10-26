# 26-oct-2026 · Modelo acv-v3: espejo → golpe → prueba a escala humana → romper la excusa → acción → salida.
# 07:30 [MITO] «Si no llego a 10.000 pasos no sirve.» Ding D, et al. Lancet Public Health 2025;10(8):e668-e681. HR 0,53 (IC95 0,46–0,60) 7.000 vs 2.000 pasos.
# 12:30 [COMPRADOR] Riñón: «me siento bien». CDC 2023: 14 % de adultos (EE. UU.), hasta 9 de cada 10 no lo sabe.
# 19:00 [ALCANCE] «Seguro son hemorroides.» Demb J, et al. JAMA Netw Open 2024 (81 estudios, <50 años): sangre en heces 45 %, dolor 40 %, cambio ritmo 27 %; demora media 6,4 meses.
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
</style>"""

def pasos(av):
    return f"""{S}<div class="wrap">{head(av,'MITO vs REALIDAD')}
<div class="mir">«Si no llego a los 10.000 pasos, ni camino.»</div>
<h1 class="k">No necesitas 10.000.<br>Con <em>7.000 pasos</em> el riesgo<br>de morir baja casi a la mitad.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>Lancet Public Health</i> 2025</span><span class="chip">57 estudios</span><span class="chip r">Adultos · comparado con 2.000 pasos</span></div>
<div class="est"><h4>Riesgo de morir, <span>comparado con quien camina 2.000 pasos al día</span></h4>
<div class="b2"><div class="w">2.000 pasos<small>referencia</small></div><div class="t"><div style="width:100%;background:#C9CFD8"></div></div><div class="n">1<small>riesgo base</small></div></div>
<div class="b2"><div class="w">7.000 pasos<small>3,5 veces más</small></div><div class="t"><div style="width:53%;background:var(--navy)"></div></div><div class="n" style="color:var(--red)">0,53<small>47 % menos</small></div></div></div>
<div class="ojo">El error más común: <b>«si no llego a 10.000, mejor no hago nada».</b> Cada paso suma.</div>
<div class="sh">Pasar de 2.000 a 7.000 <span>también se asoció con menos:</span></div>
<div class="grid2"><div><i>♥</i>Enfermedad del corazón</div><div><i>●</i>Diabetes tipo 2</div><div><i>◆</i>Depresión</div><div><i>▲</i>Demencia</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Esta semana:</b> suma 1.000 pasos más al día que hoy. <b class="y">Mándale esto a quien dice «no tengo tiempo».</b></p></div>
<div class="foot"><div class="warn"><b>Metaanálisis de estudios observacionales:</b><br>se asoció, no prueba causa. Más de 7.000 pasos<br>aportó poco extra en varios resultados.</div>
<div class="ref">Ding D, et al. Lancet Public Health 2025;10(8):e668<br>doi:10.1016/S2468-2667(25)00164-1<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def rinon(av):
    ppl = ''.join('<i class="r"></i>' if k < 2 else '<i></i>' for k in range(14))
    return f"""{S}<div class="wrap">{head(av,'DATO ÚTIL')}
<div class="mir">«Me siento bien. Si algo fallara en el riñón, me dolería.»</div>
<h1 class="k">Hasta <em>9 de cada 10</em><br>personas con enfermedad<br>del riñón no lo saben.</h1>
<div class="src" style="margin-top:22px"><span class="chip">CDC · 2023</span><span class="chip">Adultos de EE. UU.</span><span class="chip r">1 de cada 7 adultos</span></div>
<div class="est"><h4>Imagina una reunión familiar: <span>14 adultos</span></h4>
<div class="ppl">{ppl}</div>
<div class="mf"><div><b>2</b>tienen enfermedad<br>del riñón</div><div><b>Hasta 9 de 10</b>de ellos<br>no lo saben</div></div></div>
<div class="ojo">Al inicio <b>casi no duele ni se siente:</b> solo lo muestra un examen.</div>
<div class="sh">¿Te toca revisarte? <span>Si respondes SÍ a una:</span></div>
<div class="yn"><div><i>?</i>¿Tienes diabetes o presión alta?</div><div><i>?</i>¿Un familiar tuvo enfermedad del riñón?</div><div><i>?</i>¿Nunca te has hecho un examen del riñón?</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Pide en tu chequeo:</b> creatinina en sangre y examen de orina. <b class="y">Y pregúntales a tus papás: ¿cuándo fue el suyo?</b></p></div>
<div class="foot"><div class="warn"><b>Datos de EE. UU.:</b> no son cifras de Ecuador.<br>Las causas más comunes son la diabetes<br>y la presión alta.</div>
<div class="ref">CDC. Chronic Kidney Disease in the<br>United States, 2023 · cdc.gov/kidney-disease<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def colon(av):
    return f"""{S}<div class="wrap">{head(av,'ESTUDIO NUEVO','r')}
<div class="mir">«Seguro son hemorroides. Ya se me pasa.»</div>
<h1 class="k">Casi la mitad de los menores<br>de 50 con cáncer de colon<br><em>tenía sangre en las heces.</em></h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>JAMA Netw Open</i> 2024</span><span class="chip">81 estudios</span><span class="chip r">Menores de 50 años</span></div>
<div class="est"><h4>De cada 100 menores de 50 con cáncer de colon, <span>esto les pasaba:</span></h4>
<div class="b2"><div class="w">Sangre<small>en las heces</small></div><div class="t"><div style="width:45%;background:var(--red)"></div></div><div class="n" style="color:var(--red)">45<small>de 100</small></div></div>
<div class="b2"><div class="w">Dolor<small>de barriga</small></div><div class="t"><div style="width:40%;background:var(--red)"></div></div><div class="n" style="color:var(--red)">40<small>de 100</small></div></div>
<div class="b2"><div class="w">Cambio<small>al ir al baño</small></div><div class="t"><div style="width:27%;background:var(--red)"></div></div><div class="n" style="color:var(--red)">27<small>de 100</small></div></div></div>
<div class="ojo" style="margin-top:14px;font-size:25px">El error común: <b>«ya pasará».</b> Tardan 6,4 meses en promedio en diagnosticarlo.</div>
<div class="sh">Que se revise si dura o se repite: <span>no te quedes con la duda</span></div>
<div class="grid2"><div><i>1</i>Sangre que se repite</div><div><i>2</i>Dolor que no se va</div><div><i>3</i>Cambio por semanas</div><div><i>4</i>Anemia sin explicación</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Si te pasa:</b> pide una consulta, no lo dejes pasar. <b class="y">Mándaselo a quien siempre dice «son hemorroides».</b></p></div>
<div class="foot"><div class="warn"><b>Ojo:</b> la mayoría de las veces la sangre no es cáncer.<br>Revisarlo es lo que lo descarta. Sangrado<br>abundante o mareo: <b>911</b></div>
<div class="ref">Demb J, et al. JAMA Netw Open 2024<br>doi:10.1001/jamanetworkopen.2024.13157<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

JOBS = {
    'dr-viera-0730-7000-pasos': pasos,
    'dr-viera-1230-rinon-silencioso': rinon,
    'dr-viera-1900-sangre-heces-menores-50': colon,
}
if __name__ == '__main__':
    render(JOBS, pathlib.Path(__file__).resolve().parents[1] / '2026-10-26')
