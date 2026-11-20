# 20-nov-2026 · Modelo acv-v3, enfoque soluciones.
# 07:30 [MITO] «Una cucharada de aceite de coco en ayunas es buena para el corazón.» Neelakantan N, Seah JYH, van Dam RM. Circulation 2020;141(10):803-814. doi:10.1161/CIRCULATIONAHA.119.043052 (metaanálisis de 16 ensayos; frente a aceites vegetales no tropicales, el aceite de coco subió el colesterol LDL 10,47 mg/dL (IC 95 % 3,01-17,94; I² 84 %) y el HDL ~4 mg/dL; sin efecto en azúcar, inflamación ni grasa corporal).
# 12:30 [COMPRADOR] «Siempre me miden la presión en el mismo brazo.» Clark CE, Warren FC, Boddy K, et al. Hypertension 2022;79(10):2328-2335. doi:10.1161/HYPERTENSIONAHA.121.18921 (INTERPRESS-IPD; 53.172 participantes de 23 cohortes, edad media 60, 48 % mujeres; usar el brazo con la cifra más alta reclasificó 12,4 % en el umbral de 130 y 11,9 % en el de 140; los autores recomiendan medir ambos brazos y usar el más alto). Clark CE, et al. Hypertension 2021;77:650-661. doi:10.1161/HYPERTENSIONAHA.120.15997 (24 estudios, 53.827; diferencia ≥10 mmHg propuesta como límite de lo normal; HR 1,05 de muerte por cada 5 mmHg).
# 19:00 [ALCANCE] «Almuerzo en 10 minutos frente a la pantalla.» Ohkuma T, Hirakawa Y, Nakamura U, Kiyohara Y, Kitazono T, Ninomiya T. Int J Obes 2015;39(11):1589-1596. doi:10.1038/ijo.2015.96 (revisión sistemática y metaanálisis de estudios observacionales; comer rápido y obesidad OR 2,15; IC 95 % 1,84-2,51; los autores piden ensayos para probar si comer más lento ayuda a bajar de peso).
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'kit'))
from plantilla import *
import importlib.util
_s = importlib.util.spec_from_file_location('d19', str(pathlib.Path(__file__).with_name('2026-11-19.py')))
_m = importlib.util.module_from_spec(_s); _s.loader.exec_module(_m)
S, row = _m.S, _m.row

def coco(av):
    return f"""{S}<div class="wrap">{head(av,'MITO vs REALIDAD')}
<div class="mir">«Me tomo una cucharada de aceite de coco en ayunas: es buenísimo para el corazón.»</div>
<h1 class="k">En los estudios, el aceite de coco<br><em>subió el colesterol malo</em><br>más que otros aceites.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>Circulation</i> 2020</span><span class="chip">16 ensayos en personas</span><span class="chip r">comparado con aceites vegetales</span></div>
<div class="est"><h4>Cuánto subió el colesterol malo (LDL) <span>en mg/dL</span></h4>
{row('Aceites','de oliva, girasol…','0',1.5,'--grn','base')}{row('Aceite','de coco','+10',100,'--red','mg/dL')}
<div class="cur"><b>No bajó el azúcar, ni la grasa del cuerpo, ni la inflamación.</b> Es grasa saturada, como la manteca.</div></div>
<div class="sh">Lo que sí cuida tu corazón:</div>
<div class="yn"><div><i>1</i>Para cocinar a diario: aceite de oliva, girasol o canola</div><div><i>2</i>Un encocado de vez en cuando está bien; como «remedio» diario, no</div><div><i>3</i>Mídete el colesterol si nunca lo has hecho o ya pasó más de un año</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Natural no siempre es bueno para el corazón.</b> <b class="y">Mándaselo a quien toma aceite de coco «por salud».</b></p></div>
<div class="foot"><div class="warn"><b>Metaanálisis de ensayos</b> cortos (semanas a meses); los estudios variaron bastante. Mide el colesterol en sangre, no eventos como infartos.</div>
<div class="ref">Neelakantan N, et al.<br>Circulation 2020;141(10):803-814<br>doi:10.1161/CIRCULATIONAHA.119.043052<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def brazo(av):
    return f"""{S}<div class="wrap">{head(av,'DATO ÚTIL')}
<div class="mir">«A mí siempre me miden la presión en el mismo brazo… y sale normal.»</div>
<h1 class="k">Midiendo en el brazo con la cifra<br>más alta, <em>12 de cada 100</em> pasaron<br>la raya de la presión alta.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>Hypertension</i> 2022</span><span class="chip">53.172 personas · 23 estudios</span><span class="chip r">edad promedio 60</span></div>
<div class="est"><h4>En una reunión familiar de 25 adultos: <span>3 cambiarían de «normal» a «alta»</span></h4>
<div class="cmp"><div class="gg"><b class="big">22 de 25</b>seguían igual: el brazo no cambiaba su resultado</div><div class="rr"><b class="big">3 de 25</b>su brazo «alto» pasaba el límite de presión alta</div></div></div>
<div class="sh">Hazlo así, en casa o en el chequeo:</div>
<div class="yn"><div><i>1</i>La primera vez, mide los dos brazos, sentado y tranquilo 5 minutos</div><div><i>2</i>Quédate con el brazo que marque más y mide siempre ese</div><div><i>3</i>Si un brazo marca 10 o más que el otro, cuéntaselo a tu médico</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Dos brazos, un minuto más, una cifra real.</b> <b class="y">Mándaselo a tu papá o tu mamá, que se miden en casa.</b></p></div>
<div class="foot"><div class="warn"><b>Análisis de 23 estudios</b> con datos de cada persona. Una sola medida alta no es diagnóstico: se confirma con varias medidas.</div>
<div class="ref">Clark CE, et al.<br>Hypertension 2022;79(10):2328-2335<br>doi:10.1161/HYPERTENSIONAHA.121.18921<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def rapido(av):
    return f"""{S}<div class="wrap">{head(av,'ESTUDIO','r')}
<div class="mir">«Almuerzo en 10 minutos, frente a la compu o el celular.»</div>
<h1 class="k">Quienes comían rápido tenían<br><em>el doble de probabilidad</em><br>de tener obesidad.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>Int J Obes</i> 2015</span><span class="chip">metaanálisis de estudios</span><span class="chip r">observacional</span></div>
<div class="est"><h4>Probabilidad de obesidad <span>(comer despacio = 1)</span></h4>
{row('Comer','despacio','1',1/2.15*100,'--navy','vez')}{row('Comer','rápido','2,15',100,'--red','veces')}
<div class="cur"><b>A tu cuerpo le toma un rato avisar que ya está lleno.</b> Si terminas en 10 minutos, comes antes de que llegue el aviso.</div></div>
<div class="sh">Prueba esto en tu próximo almuerzo:</div>
<div class="yn"><div><i>1</i>Dale al almuerzo 20 minutos: pon una alarma si hace falta</div><div><i>2</i>Suelta la cuchara entre bocado y bocado</div><div><i>3</i>Pantalla apagada: mira tu plato o conversa</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Mismo plato, más despacio: tu cuerpo alcanza a decir «ya».</b> <b class="y">Mándaselo a tu compañero que almuerza en el escritorio.</b></p></div>
<div class="foot"><div class="warn"><b>Estudios observacionales:</b> se asoció, no prueba que comer rápido cause obesidad. Aún faltan ensayos que prueben si comer lento ayuda a bajar de peso.</div>
<div class="ref">Ohkuma T, et al.<br>Int J Obes 2015;39(11):1589-1596<br>doi:10.1038/ijo.2015.96<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

JOBS = {
    'dr-viera-0730-aceite-coco': coco,
    'dr-viera-1230-presion-dos-brazos': brazo,
    'dr-viera-1900-comer-rapido': rapido,
}
if __name__ == '__main__':
    render(JOBS, pathlib.Path(__file__).resolve().parents[1] / '2026-11-20')
