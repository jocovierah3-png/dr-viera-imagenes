# Producción diaria automática — Dr. Joel Viera

Este repositorio es público: aloja las imágenes que Metricool descarga para publicar en Facebook e Instagram.
Lo usa la tarea programada diaria de Claude. Joel NO revisa antes de publicar: todo debe salir listo y correcto.

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
7. Programar en Metricool (`createScheduledPost`): blogId `7392899`, timezone `America/Guayaquil`, providers `facebook` + `instagram`, `facebookData {"type":"POST"}`, `instagramData {"type":"POST"}`, `autoPublish: true`, `media` = la URL raw. Horas 07:30, 12:30 y 19:00. Si una hora ya pasó, programarla 10 minutos después de ahora. Antes, revisar `getScheduledPosts` del día para no duplicar.
8. Añadir 3 filas a `registro.md`, commit + push.
9. Enviar a Joel con SendUserMessage un resumen corto para el celular: los 3 temas con hora, hook y fuente, y los enlaces raw de las 3 imágenes. Si algo falló, decir exactamente qué y qué quedó programado.

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
