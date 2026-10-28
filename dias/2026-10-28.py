# 28-oct-2026 · Modelo acv-v3.
# 07:30 [DATO ÚTIL] «Después de comer me siento a descansar.» Buffey AJ, et al. Sports Med 2022;52(8):1765-1787. doi:10.1007/s40279-022-01649-4 (7 estudios cruzados de 1 día; adultos mayormente con sobrepeso).
# 12:30 [COMPRADOR] Hígado graso: «Yo no tomo, mi hígado está bien.» Younossi ZM, et al. Hepatology 2023;77:1335-1347 (92 estudios, >9 M; 30,1 %, IC 27,9-32,3; DOI no verificado: PubMed bloqueado).
# 19:00 [ALCANCE] «Estoy agotado y sin ganas; ya se me pasará.» Noetel M, et al. BMJ 2024;384:e075847 (218 estudios, 14.170 personas; depresión).
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



def paseo(av):
    return f"""{S}<div class="wrap">{head(av,'DATO ÚTIL')}
<div class="mir">«Después de comer me siento a descansar.»</div>
<h1 class="k">Levantarte y caminar<br>suave <em>después de comer</em><br>baja tu azúcar más que sentarte.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>Sports Medicine</i> 2022</span><span class="chip">7 estudios</span><span class="chip r">Comparado con seguir sentado</span></div>
<div class="est"><h4>Azúcar e insulina en la sangre <span>después de comer</span></h4>
<div class="cmp"><div class="rr"><b class="big">Sentado</b>El azúcar y la insulina suben más tras la comida.</div><div class="gg"><b class="big">Caminata suave</b>Ambos quedaron más bajos. Mejor que solo pararse.</div></div></div>
<div class="ojo">El error común: <b>«caminar tiene que ser largo y agotador»</b>. Aquí eran pausas de caminata ligera.</div>
<div class="sh">Entonces, ¿qué hago? <span>Sin gimnasio:</span></div>
<div class="yn"><div><i>1</i>Después de comer, levántate un rato</div><div><i>2</i>Camina suave: al patio, la cuadra, la oficina</div><div><i>3</i>Hazlo cuando puedas, no hace falta perfecto</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Hoy:</b> tras el almuerzo, 5 minutos de caminata suave. <b class="y">Mándaselo a quien se tira al sofá después de comer.</b></p></div>
<div class="foot"><div class="warn"><b>Ensayos de un solo día,</b> mayormente en adultos con sobrepeso.<br>No prueba que prevenga diabetes. Si tienes<br>diabetes, consulta a tu médico.</div>
<div class="ref">Buffey AJ, et al. Sports Med 2022;52(8):1765-1787<br>doi:10.1007/s40279-022-01649-4<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def higado(av):
    people=''.join('<i class="r"></i>' if i<30 else '<i></i>' for i in range(100))
    return f"""{S}<style>.ppl.h{{grid-template-columns:repeat(20,1fr);gap:18px 6px;margin-top:30px}}.ppl.h i{{height:18px}}.ppl.h i:before{{top:-11px;width:11px;height:11px;margin-left:-5.5px}}</style><div class="wrap">{head(av,'DATO ÚTIL')}
<div class="mir">«Yo casi no tomo alcohol, mi hígado está bien.»</div>
<h1 class="k">Imagina <em>10 personas</em> adultas:<br>3 tienen hígado graso<br>y casi nunca da señales.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>Hepatology</i> 2023</span><span class="chip">92 estudios</span><span class="chip r">Más de 9 millones de personas</span></div>
<div class="est"><h4>Hígado graso en el mundo: <span>30 de cada 100 adultos</span></h4>
<div class="ppl h">{people}</div></div>
<div class="ojo">No es solo de quien toma: <b>se relaciona con la barriga, el azúcar alta y el colesterol.</b></div>
<div class="sh">¿Te toca preguntarlo? <span>Si respondes SÍ a 2 o más:</span></div>
<div class="yn"><div><i>?</i>¿Tu cintura ha crecido?</div><div><i>?</i>¿Azúcar o colesterol altos en un examen?</div><div><i>?</i>¿Tienes la presión alta?</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Consúltalo:</b> un examen de sangre o ecografía lo detecta. <b class="y">Pregúntales a tus papás: ¿se han revisado el hígado?</b></p></div>
<div class="foot"><div class="warn"><b>Metaanálisis mundial:</b> no son datos de Ecuador.<br>Cada persona y cada caso son distintos.<br>Tener grasa en el hígado se puede revertir.</div>
<div class="ref">Younossi ZM, et al. Hepatology 2023;77:1335-1347<br>The global epidemiology of NAFLD and NASH<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def animo(av):
    return f"""{S}<div class="wrap">{head(av,'ESTUDIO NUEVO','r')}
<div class="mir">«Estoy agotado y sin ganas. Ya se me pasará.»</div>
<h1 class="k">En <em>14.170 personas</em> con<br>depresión, moverse ayudó:<br>caminar, yoga y pesas.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>BMJ</i> 2024</span><span class="chip">218 estudios</span><span class="chip r">Ensayos con asignación al azar</span></div>
<div class="est"><h4>Qué tipo de ejercicio funcionó <span>mejor que no hacer nada</span></h4>
<div class="grid2"><div><i>1</i>Caminar o trotar</div><div><i>2</i>Yoga</div><div><i>3</i>Pesas o fuerza</div><div><i>4</i>Mejor si es intenso</div></div></div>
<div class="ojo">El error: <b>«estar triste o sin ganas es debilidad, hay que aguantar».</b> Es una condición de salud.</div>
<div class="sh">Si llevas más de 2 semanas así <span>(sin ganas, sin disfrutar):</span></div>
<div class="yn"><div><i>1</i>Cuéntaselo a alguien de confianza</div><div><i>2</i>Pide cita con un profesional de salud</div><div><i>3</i>Muévete: una caminata ya cuenta</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Hoy:</b> sal a caminar 10 minutos, aunque no tengas ganas. <b class="y">Mándaselo a ese amigo que dice «estoy bien» y no lo parece.</b></p></div>
<div class="foot"><div class="warn"><b>El ejercicio acompaña,</b> no reemplaza la ayuda profesional.<br>Si sientes que no puedes más: 911 o<br>línea 171 opción 6.</div>
<div class="ref">Noetel M, et al. BMJ 2024;384:e075847<br>doi:10.1136/bmj-2023-075847<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

JOBS = {
    'dr-viera-0730-caminar-tras-comer': paseo,
    'dr-viera-1230-higado-graso': higado,
    'dr-viera-1900-animo-ejercicio': animo,
}
if __name__ == '__main__':
    render(JOBS, pathlib.Path(__file__).resolve().parents[1] / '2026-10-28')
