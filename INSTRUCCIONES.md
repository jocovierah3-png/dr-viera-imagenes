# Producción diaria automática — Dr. Joel Viera

Este repositorio es público: aloja las imágenes que Metricool descarga para publicar en Facebook e Instagram.
Lo usa la tarea programada diaria de Claude. Desde el 14-oct-2026 Joel APRUEBA cada imagen antes de publicarla: se programan como borrador (draft true) y solo se publican cuando él responde que sí.

## Flujo diario (en este orden)
1. Clonar el repo, ejecutar `./kit/setup.sh`.
2. Leer `registro.md` (temas ya usados: no repetir tema, hook ni formato).
3. Radar: investigar en la web (24 h → 3 días → 7 días → 30 días) y elegir 3 temas:
   - **07:30 [MITO / DATO ÚTIL]**: mito vs realidad o dato práctico de guía clínica (OMS, OPS, MSP, CDC, sociedades médicas). Puede ser evergreen.
   - **12:30 [COMPRADOR]**: público 30–55 años en Ecuador; presión alta, prediabetes/diabetes, colesterol, chequeos, interpretación de exámenes, cuidado de padres mayores.
   - **19:00 [ALCANCE]**: público 20–35; estudio reciente y llamativo (salud mental, sueño, hábitos, etc.).
   - Solo evidencia A o B. Verificar cada estudio en PubMed o la web de la revista (autores, revista, año, DOI, diseño, n, cifras exactas). Nada de resúmenes de congreso sin abstract, estudios en animales, pilotos pequeños ni notas de prensa sin artículo.
4. Crear `dias/AAAA-MM-DD.py` copiando la estructura de `dias/2026-10-13.py` (funciones que devuelven el HTML, `JOBS` y `render`). Ejecutarlo. Si imprime "DESBORDA", acortar textos y repetir.
5. Abrir cada PNG y revisarlo visualmente (ortografía, cifras, nada cortado, foto en la cabecera).
6. Commit + push a `main` (carpeta `AAAA-MM-DD/`). Comprobar que la URL pública responde 200:
   `https://raw.githubusercontent.com/jocovierah3-png/dr-viera-imagenes/main/AAAA-MM-DD/<archivo>.png`
7. Programar en Metricool como BORRADOR (`createScheduledPost` con `draft: true`), mandar las 3 imágenes y textos a Joel y esperar su sí; al aprobar, `updateScheduledPost` con `draft: false`. Datos: blogId `7392899`, timezone `America/Guayaquil`, providers `facebook` + `instagram`, `facebookData {"type":"POST"}`, `instagramData {"type":"POST"}`, `autoPublish: true`, `media` = la URL raw. Horas 07:30, 12:30 y 19:00. Si una hora ya pasó, programarla 10 minutos después de ahora. Antes, revisar `getScheduledPosts` del día para no duplicar.
8. Añadir 3 filas a `registro.md`, commit + push.
9. Enviar a Joel con SendUserMessage un resumen corto para el celular: los 3 temas con hora, hook y fuente, y los enlaces raw de las 3 imágenes. Si algo falló, decir exactamente qué y qué quedó programado.

## Preferencia de Joel (14-oct-2026)
- REGLA FIJA (Joel, 14-oct-2026): TODAS las publicaciones deben ser (1) ENTENDIBLES para cualquier persona, (2) con alta probabilidad de viralidad y (3) apelar al «YO»: que quien la vea piense «esto me pasa a mí / a los míos». Modelo: `dias/2026-10-14-acv-v3.py` (espejo con la frase que la gente dice → golpe → cifra a escala humana tipo «estadio lleno de gente de tu edad» → romper la excusa real → señales/acción → salida). Antes de cada imagen: público, barrera («soy joven», «me siento bien»), miedo oculto, momento «esto me pasa», quién la comparte y a quién.
- Prefiere las imágenes BIEN EXPLICADAS (titular-hook completo, chips de evidencia, preguntas Sí/No o franjas de rangos, gráfico de barras con cifras, «romper la excusa», franja «Lo que ayuda» y pie con límites). NO usar la versión simplificada de «una idea, un número, una acción».

## Preferencia de Joel (28-oct-2026): más SOLUCIONES, menos problemas
- Cada imagen debe dar más espacio a la SOLUCIÓN que al problema: titular y cifra planteando el problema en 1 golpe, y el resto (al menos la mitad de la imagen) en qué hacer: 3 pasos concretos, fáciles y que cualquiera pueda hacer hoy, más la franja «Lo que ayuda».
- Fácil de entender para cualquier persona: frases cortas, lenguaje de mamá, una sola idea por bloque. Menos cifras, riesgos y tecnicismos; solo la cifra que impacta.
- Con potencial de viralidad: espejo del «YO», solución sencilla que la gente quiera guardar y CTA de moneda social con destinatario concreto («mándaselo a…»).
- Prefiere temas de soluciones y hábitos (qué sí hacer) sobre temas de miedo o enfermedad. Mantener rigor: evidencia A/B, límites y firma «Médico».

## Sistema visual (no cambiar)
- 1080 × 1350 px, fondo blanco. Fuentes: Manrope (texto) + Newsreader (referencias).
- Paleta: azul marino #102D50, rojo #E92724 (datos/riesgo), amarillo #FFD200 (acento puntual), gris #667085, blanco. Verde solo para beneficio/protección ("Lo que ayuda").
- Cabecera: foto real de Joel (`kit/avatar.png`) + "Dr. Joel Viera" + "@dr.joelviera · Médico" (nunca "Médico general") + etiqueta (ESTUDIO NUEVO en rojo, o MITO vs REALIDAD / DATO ÚTIL).
- Titular grande con la cifra o la idea clave en rojo. Pocas letras, hechos grandes.
- Chips de evidencia (revista en cursiva, n, años de seguimiento o país).
- Gráfico que responda una pregunta: barras horizontales con IC 95 % cuando exista. Para HR/RR usar barras pareadas "Referencia vs exposición" (barra más corta = menos riesgo), nunca una barra roja larga que se lea como "más riesgo".
- Franja azul marino "Lo que ayuda" con UNA acción concreta.
- Pie: tipo de estudio y su límite (ej. "Estudio observacional: asociación, no causa") + 911 (o línea 171 opción 6 cuando aplique) + referencia con DOI + "DR. VIERA · SALUD PARA TODOS".
- Formatos disponibles en el ejemplo: "Mito vs realidad" con checklist (`dengue`), barras simples (`hta`), barras pareadas HR (`rem`). Variar formato entre días.

## Reglas de contenido
- Nunca convertir "se asoció" en "causó". Decir si es observacional.
- Sin dosis, sin automedicación, sin marcas comerciales.
- Cifras sin dobles negaciones ni signo "−" que se lea como "menos riesgo" (ej. "hasta 5,8 años antes").
- Sin miedo como gancho principal; nada sensacionalista.
- Vapeo, suicidio, trastornos alimentarios y temas para menores: no publicar en automático.

## Texto de cada publicación (caption)
- 5–8 líneas cortas: hook en la 1.ª línea con 1 emoji, qué encontró (con revista y año), aclaración de límites si es observacional, ✅ acción concreta, CTA natural (guardar, compartir, etiquetar, pregunta para comentar; alternar), 4 hashtags incluyendo #saludparatodos.
- Para [COMPRADOR], cerrar invitando a cuidar a la familia ("¿Hace cuánto no se miden tus papás?"). Invitar al Club Salud para todos solo cuando Joel avise que el WhatsApp está activo.
