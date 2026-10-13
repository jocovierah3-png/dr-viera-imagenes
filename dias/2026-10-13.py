# Imágenes del 13-oct-2026 (ejemplo de archivo diario)
import sys,pathlib; sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]/'kit'))
from plantilla import *
def dengue(av):
    al=["Dolor de barriga intenso","Vómito que no para","Sangrado de encías o nariz","Sangre en vómito o heces","Respiración rápida","Mucho cansancio o inquietud"]
    items=''.join(f'<div class="it"><i>!</i>{a}</div>' for a in al)
    return f"""<div class="wrap">{head(av,'MITO vs REALIDAD')}
<h1>¿Ya tuviste dengue?<br><em>La segunda vez puede<br>ser más grave</em></h1>
<div class="src"><span class="chip">OMS · CDC</span><span class="chip r">Ecuador 2026: 34.058 casos</span><span class="chip">+18 % vs 2025</span></div>
<div class="mv"><div class="box m"><h3>✗ MITO</h3><p>«Ya me dio dengue, ya estoy protegido»</p></div>
<div class="box r"><h3>✓ REALIDAD</h3><p>Hay 4 virus del dengue. Puedes contagiarte otra vez, y <b>una segunda infección aumenta el riesgo de dengue grave.</b></p></div></div>
<div class="al"><h4>Señales de alarma <span>suelen aparecer cuando la fiebre ya bajó</span></h4><div class="grid">{items}</div></div>
<div class="help w"><div class="ic">!</div><p><b class="y">Con cualquiera de estas señales, ve a emergencia de inmediato.</b><br>No te automediques: evita ibuprofeno y aspirina, aumentan el riesgo de sangrado.</p></div>
<div class="foot"><div class="warn"><b>Contenido educativo.</b> No reemplaza la consulta médica.<br>Emergencias: <b>911</b></div>
<div class="ref">OMS. Dengue y dengue grave (2025) · CDC. About Dengue<br>MSP Ecuador, gaceta epidemiológica (corte 6-sep-2026)<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def hta(av):
    return f"""<div class="wrap">{head(av,'ESTUDIO NUEVO','r')}
<h1>De cada 10 personas<br>con presión alta,<br><em>casi 6 no lo saben</em></h1>
<div class="src"><span class="chip"><i>BMJ Public Health</i> · 2026</span><span class="chip">1,3 millones de adultos</span><span class="chip">Inglaterra</span></div>
<div class="ct">Personas con presión alta que no lo sabían <span>%</span></div>
{bar('Inglaterra','estudio 2022–2025',58.8,100,'#E92724','59 %')}
{bar('Ecuador','encuesta STEPS 2018',45.2,100,'#102D50','45 %')}
{bar('Mundo','estimación OMS',44,100,'#102D50','44 %')}
<div class="note">Fuentes y métodos distintos: sirven para dimensionar el problema, no para compararse entre sí.</div>
<div class="ojo">La mayoría <b>no siente ningún síntoma.</b> La única forma de saberlo es medirse.</div>
<div class="help"><div class="ic">✓</div><p><b class="g">Lo que ayuda:</b> desde los 40 años (o antes si tienes sobrepeso o familiares con presión alta), <b>mídete cada año.</b> De 18 a 39, cada 3 a 5 años. Si sale alta, confírmala con tu médico.</p></div>
<div class="foot"><div class="warn"><b>Estudio transversal:</b> mide cuántos,<br>no explica por qué.<br>¿Dolor de pecho o falta de aire? <b>911</b></div>
<div class="ref">Liu W, et al. BMJ Public Health 2026;4:e004815<br>doi:10.1136/bmjph-2025-004815<br>MSP Ecuador STEPS 2018 · OMS 2025<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""

def rem(av):
    return f"""<div class="wrap">{head(av,'ESTUDIO NUEVO','r')}
<h1>Más sueño REM se asoció<br>con menos riesgo de<br><em>83 enfermedades</em></h1>
<div class="src"><span class="chip"><i>PLOS Medicine</i> · 2026</span><span class="chip">95.559 adultos</span><span class="chip">8,9 años de seguimiento</span></div>
<div class="ct">Riesgo relativo con ~48 min más de sueño REM <span>por noche</span></div>
{pair('Insuficiencia cardíaca',0.74,0.68,0.80,'26 %')}
{pair('Demencia',0.54,0.47,0.62,'46 %')}
<div class="note">Barra más corta = menos riesgo · línea negra: IC 95 % · sueño medido con pulsera</div>
<div class="ojo">Dormir <b>menos de 5 horas</b> se asoció con más riesgo de <b>37 enfermedades.</b></div>
<div class="help"><div class="ic">✓</div><p><b class="g">Lo que ayuda:</b> el riesgo más bajo se vio con <b>6 a 8 horas</b>, y dormir a horas irregulares también se asoció a más riesgo.<br><b class="y">Esta semana: misma hora para dormir y despertar.</b></p></div>
<div class="foot"><div class="warn"><b>Estudio observacional:</b> asociación, no causa.<br>¿Insomnio más de 3 semanas? Consulta a tu médico.</div>
<div class="ref">Luo J, Liu R, et al. PLOS Med 2026;23(9):e1005213<br>doi:10.1371/journal.pmed.1005213<br><b>DR. VIERA · SALUD PARA TODOS</b></div></div></div>"""


JOBS={'dr-viera-0730-dengue':dengue,'dr-viera-1230-presion-alta':hta,'dr-viera-1900-sueno-rem':rem}
if __name__=='__main__': render(JOBS, pathlib.Path(__file__).resolve().parents[1]/'2026-10-13')
