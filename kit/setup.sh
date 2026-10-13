#!/usr/bin/env bash
# Prepara fuentes y navegador para renderizar. Ejecutar desde la raíz del repo.
set -e
cd "$(dirname "$0")"
if [ ! -d fontsource-manrope-5.1.0 ]; then
  npm pack @fontsource/manrope@5.1.0 @fontsource/newsreader@5.1.0 >/dev/null 2>&1
  mkdir -p fontsource-manrope-5.1.0 fontsource-newsreader-5.1.0
  tar xzf fontsource-manrope-5.1.0.tgz -C fontsource-manrope-5.1.0
  tar xzf fontsource-newsreader-5.1.0.tgz -C fontsource-newsreader-5.1.0
  rm -f *.tgz
fi
python3 -c "import playwright" 2>/dev/null || pip install --break-system-packages -q playwright
python3 -m playwright install chromium >/dev/null 2>&1 || true
echo "kit listo"
