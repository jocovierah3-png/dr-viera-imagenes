# 24-nov-2026 · Modelo acv-v3, enfoque soluciones.
# 07:30 [MITO] «Yo siempre lavo el pollo antes de cocinarlo.» USDA FSIS / RTI International. Food Safety Consumer Research Project: meal preparation experiment related to poultry washing. Ago 2019 (experimento en cocina de prueba, ~300 adultos; de quienes lavaron el pollo, 60 % con bacterias en el fregadero y 14 % aún tras limpiarlo; ensalada contaminada 26 % en quienes lo lavaron y 31 % en quienes no: manos, tabla y superficies). USDA: lavar con agua, vinagre o limón no destruye bacterias; cocinar a 74 °C (165 °F).
# 12:30 [COMPRADOR] «Después de almorzar me siento y no me muevo.» Reynolds AN, Mann JI, Williams S, Venn BJ. Diabetologia 2016;59(12):2572-2578. doi:10.1007/s00125-016-4085-2 (ensayo cruzado al azar, 41 adultos con diabetes tipo 2; 10 min tras cada comida vs 30 min de una vez: azúcar después de comer 12 % menor, 0,88; 0,78-0,99; tras la cena 22 % según comunicado de la Universidad de Otago). Buffey AJ, et al. Sports Med 2022;52(8):1765-1787. doi:10.1007/s40279-022-01649-4 (7 ensayos: caminar suave bajó el azúcar después de comer vs seguir sentado).
# 19:00 [ALCANCE · ¿Normal o lo reviso?] «Ese lunar lo tengo desde siempre.» American Cancer Society, supervivencia relativa a 5 años del melanoma (SEER, diagnosticados 2015-2021): localizado >99 %, regional 76 %, a distancia 36 %. AAD: ABCDE. Tsao H, et al. J Am Acad Dermatol 2015;72(4):717-723 (PMID 25698455).
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'kit'))
from plantilla import *
import importlib.util
_s = importlib.util.spec_from_file_location('d22', str(pathlib.Path(__file__).with_name('2026-11-22.py')))
_m = importlib.util.module_from_spec(_s); _s.loader.exec_module(_m)
S, row = _m.S, _m.row

def pollo(av):
    return f"""{S}<div class="wrap">{head(av,'MITO vs REALIDAD')}
<div class="mir">«Yo siempre lavo el pollo antes de cocinarlo. Así sale limpio.»</div>
<h1 class="k">Lavar el pollo crudo<br><em>no le quita las bacterias:</em><br>las riega por tu cocina.</h1>
<div class="src" style="margin-top:22px"><span class="chip">USDA 2019</span><span class="chip">300 personas cocinando</span><span class="chip r">experimento en cocina</span></div>
<div class="est"><h4>De cada 100 que lavaron el pollo <span>(bacterias del pollo)</span></h4>
{row('En el fregadero','después de lavarlo','60',60,'--red','de 100')}{row('Seguían ahí','aun después de limpiarlo','14',14,'--red','de 100')}
<div class="cur"><b>¿Y la ensalada?</b> Se contaminó en 1 de cada 4 cocinas, por las manos y la tabla, se lavara o no el pollo.</div></div>
<div class="sh">Lo que sí lo deja seguro:</div>
<div class="yn"><div><i>1</i>Pásalo directo del empaque a la olla, sin lavarlo</div><div><i>2</i>Cocínalo hasta que por dentro no quede nada rosado ni jugo rojo</div><div><i>3</i>Lávate las manos con jabón y usa otra tabla para la ensalada</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Lo que mata las bacterias es el calor, no el chorro de agua.</b> <b class="y">Mándaselo a tu mamá, la que lava el pollo con limón.</b></p></div>
<div class="foot"><div class="warn"><b>Experimento del USDA</b> en cocina de prueba (EE. UU.). Lavarlo con vinagre o limón tampoco destruye las bacterias.</div>
<div class="ref">USDA FSIS · RTI International<br>Meal preparation experiment:<br>poultry washing. Agosto 2019<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def caminar(av):
    return f"""{S}<div class="wrap">{head(av,'DATO ÚTIL')}
<div class="mir">«Después de almorzar me siento y ya no me muevo.»</div>
<h1 class="k"><em>10 minutos caminando</em><br>después de comer bajaron<br>más el azúcar.</h1>
<div class="src" style="margin-top:22px"><span class="chip"><i>Diabetologia</i> 2016</span><span class="chip">41 adultos con diabetes</span><span class="chip r">ensayo al azar</span></div>
<div class="est"><h4>Azúcar después de comer <span>(30 minutos de una vez = 100)</span></h4>
{row('30 min','de una sola vez','100',100,'--g2','')}{row('10 min','después de cada comida','88',88,'--navy','')}{row('10 min','después de la cena','78',78,'--grn','')}
<div class="cur"><b>Los mismos 30 minutos al día.</b> Solo cambió el momento: justo después de comer.</div></div>
<div class="sh">¿Te pasa? Responde Sí o No:</div>
<div class="yn"><div><i>?</i>Después de comer te sientas, te acuestas o vas directo a la pantalla</div><div><i>?</i>En tu familia hay diabetes o «azúcar alta»</div><div><i>?</i>Hace más de 1 año que no te mides el azúcar</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Hoy: 10 minutos a pie al terminar de comer, en familia.</b> <b class="y">Mándaselo a quien hace siesta apenas almuerza.</b></p></div>
<div class="foot"><div class="warn"><b>Estudio pequeño</b> en personas con diabetes tipo 2; 7 ensayos más vieron el mismo efecto al caminar suave. No reemplaza tu tratamiento.</div>
<div class="ref">Reynolds AN, et al. Diabetologia<br>2016;59(12):2572-2578<br>doi:10.1007/s00125-016-4085-2<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def lunar(av):
    return f"""{S}<div class="wrap">{head(av,'¿NORMAL O LO REVISO?')}
<div class="mir">«Ese lunar lo tengo desde siempre. Nunca me ha dolido.»</div>
<h1 class="k">Un lunar que <em>cambia</em><br>puede no doler. Visto a<br>tiempo, casi siempre se cura.</h1>
<div class="src" style="margin-top:22px"><span class="chip">American Cancer Society</span><span class="chip">datos de EE. UU. 2015-2021</span><span class="chip r">melanoma</span></div>
<div class="est"><h4>Siguen vivos a los 5 años <span>(de cada 100)</span></h4>
{row('Visto a tiempo','solo en la piel','99',99,'--grn','de 100')}{row('Visto tarde','ya en otros órganos','36',36,'--red','de 100')}</div>
<div class="nv"><div class="a"><h5>NORMAL</h5>Lunar redondo, de un solo color, bordes lisos, igual desde hace años.</div><div class="b"><h5>REVÍSALO</h5>Bordes raros, varios colores, o que crece, cambia, pica o sangra.</div></div>
<div class="sh">Lo que puedes hacer desde hoy:</div>
<div class="yn"><div><i>1</i>Toma foto hoy a tus lunares, con una moneda al lado</div><div><i>2</i>Repite la foto cada 3 meses y compara</div><div><i>3</i>Si uno cambia o se ve distinto a los demás: dermatólogo</div></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Mírate la piel: 2 minutos.</b> <b class="y">Mándaselo a quien dice «siempre lo tuve».</b></p></div>
<div class="foot"><div class="warn"><b>Cifras de EE. UU.</b> La foto no reemplaza al médico.</div>
<div class="ref">American Cancer Society 2025 · AAD<br>Tsao H, et al. J Am Acad Dermatol<br>2015;72(4):717-723<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

JOBS = {
    'dr-viera-0730-lavar-pollo-crudo': pollo,
    'dr-viera-1230-caminar-despues-de-comer': caminar,
    'dr-viera-1900-lunar-que-cambia': lunar,
}
if __name__ == '__main__':
    render(JOBS, pathlib.Path(__file__).resolve().parents[1] / '2026-11-24')
