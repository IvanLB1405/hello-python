# 📕 Cómo Generar el PDF de la Documentación

Este documento explica **4 métodos diferentes** para convertir `DOCUMENTACION_TECNICA.md` a PDF.

---

## Método 1: Script Automatizado (Linux/macOS) ⚡ RECOMENDADO

### Paso 1: Instalar Pandoc y LaTeX

**Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install pandoc texlive-latex-base texlive-fonts-recommended texlive-latex-extra
```

**macOS:**
```bash
brew install pandoc
brew install --cask basictex
```

### Paso 2: Dar permisos de ejecución al script

```bash
chmod +x generar_pdf.sh
```

### Paso 3: Ejecutar el script

```bash
./generar_pdf.sh
```

**Resultado:** `DOCUMENTACION_TECNICA.pdf` generado automáticamente ✅

### Paso 4: Abrir el PDF

```bash
# Linux
xdg-open DOCUMENTACION_TECNICA.pdf

# macOS
open DOCUMENTACION_TECNICA.pdf
```

---

## Método 2: Pandoc Manual (Todas las plataformas)

### Instalar Pandoc

**Windows:**
1. Descargar desde https://pandoc.org/installing.html
2. Instalar MiKTeX desde https://miktex.org/download

**Linux:** Ver Método 1

**macOS:** Ver Método 1

### Comando de conversión

```bash
pandoc DOCUMENTACION_TECNICA.md \
  -o DOCUMENTACION_TECNICA.pdf \
  --pdf-engine=pdflatex \
  -V geometry:margin=1in \
  -V fontsize=11pt \
  --toc \
  --toc-depth=3 \
  --highlight-style=tango \
  --metadata title="Documentación Técnica - MovieLib"
```

---

## Método 3: VS Code con Extension (Visual) 🎨 FÁCIL

### Paso 1: Instalar Visual Studio Code

Descargar desde https://code.visualstudio.com/

### Paso 2: Instalar Extension

1. Abrir VS Code
2. Ir a Extensions (Ctrl+Shift+X)
3. Buscar e instalar **"Markdown PDF"** by yzane

### Paso 3: Generar PDF

1. Abrir `DOCUMENTACION_TECNICA.md` en VS Code
2. Click derecho en el editor
3. Seleccionar **"Markdown PDF: Export (pdf)"**
4. Esperar unos segundos

**Resultado:** PDF generado en el mismo directorio ✅

**Ventajas:**
- ✅ Interfaz gráfica intuitiva
- ✅ No requiere comandos
- ✅ Preview en tiempo real
- ✅ Funciona en Windows, Linux y macOS

---

## Método 4: Herramientas Online (Sin instalación) 🌐

### Opción A: Markdown to PDF (Recomendada)

1. Ir a https://www.markdowntopdf.com/
2. Copiar y pegar el contenido de `DOCUMENTACION_TECNICA.md`
3. Click en "Convert to PDF"
4. Descargar el PDF generado

### Opción B: CloudConvert

1. Ir a https://cloudconvert.com/md-to-pdf
2. Subir `DOCUMENTACION_TECNICA.md`
3. Click en "Convert"
4. Descargar el PDF

### Opción C: Dillinger

1. Ir a https://dillinger.io/
2. Importar `DOCUMENTACION_TECNICA.md`
3. Click en "Export as" → "PDF"

**Ventajas:**
- ✅ Sin instalación
- ✅ Funciona en cualquier navegador
- ✅ Rápido para documentos pequeños

**Desventajas:**
- ⚠️ Requiere conexión a internet
- ⚠️ Límites de tamaño en algunas herramientas
- ⚠️ Menos control sobre el formato

---

## Método 5: Google Docs (Alternativa Simple)

### Paso 1: Abrir Google Docs

1. Ir a https://docs.google.com
2. Crear un nuevo documento

### Paso 2: Importar Markdown

1. Click en "Archivo" → "Abrir"
2. Ir a la pestaña "Subir"
3. Subir `DOCUMENTACION_TECNICA.md`
4. Google Docs convertirá automáticamente el formato

### Paso 3: Exportar a PDF

1. Click en "Archivo" → "Descargar" → "PDF (.pdf)"

**Ventajas:**
- ✅ Muy simple
- ✅ Buena conversión de tablas
- ✅ Permite editar antes de exportar

**Desventajas:**
- ⚠️ Pierde algo de formato del Markdown
- ⚠️ No mantiene syntax highlighting de código

---

## 🎯 ¿Cuál método elegir?

| Método | Dificultad | Calidad | Velocidad | Recomendado para |
|--------|------------|---------|-----------|------------------|
| Script automatizado | Media | ⭐⭐⭐⭐⭐ | ⚡⚡⚡ | Desarrolladores Linux/macOS |
| Pandoc manual | Alta | ⭐⭐⭐⭐⭐ | ⚡⚡ | Control total del formato |
| VS Code extension | Baja | ⭐⭐⭐⭐ | ⚡⚡⚡ | **Principiantes** |
| Online (markdowntopdf) | Muy baja | ⭐⭐⭐ | ⚡⚡⚡⚡ | Rápido y sin instalación |
| Google Docs | Muy baja | ⭐⭐⭐ | ⚡⚡ | Edición antes de exportar |

---

## 📊 Resultado Esperado

El PDF generado debería tener:

- ✅ Tabla de contenidos interactiva
- ✅ ~50-60 páginas (según método)
- ✅ Código con syntax highlighting
- ✅ Tablas formateadas
- ✅ Enlaces clicables
- ✅ Emojis (según método)
- ✅ Imágenes de diagramas (ASCII art)

---

## 🐛 Troubleshooting

### Error: "pdflatex not found"

**Solución:**
```bash
sudo apt-get install texlive-latex-base texlive-latex-extra
```

### Error: "! LaTeX Error: File `unicode-math.sty' not found"

**Solución:**
```bash
sudo apt-get install texlive-xetex
```

### PDF con caracteres raros (encoding issues)

**Solución:** Usar `--pdf-engine=xelatex` en lugar de `pdflatex`:
```bash
pandoc DOCUMENTACION_TECNICA.md -o DOCUMENTACION_TECNICA.pdf --pdf-engine=xelatex
```

### El PDF está en blanco o incompleto

**Causa:** Documento demasiado largo para LaTeX por defecto

**Solución:** Usar VS Code extension o herramientas online que no tienen esta limitación

---

## 💡 Tips para mejor resultado

### 1. Optimizar para impresión

```bash
pandoc DOCUMENTACION_TECNICA.md \
  -o DOCUMENTACION_TECNICA.pdf \
  --pdf-engine=pdflatex \
  -V geometry:margin=0.75in \
  -V fontsize=10pt \
  -V papersize=a4
```

### 2. Generar versión con numeración de líneas

```bash
pandoc DOCUMENTACION_TECNICA.md \
  -o DOCUMENTACION_TECNICA.pdf \
  --pdf-engine=pdflatex \
  --number-sections
```

### 3. Personalizar colores

```bash
pandoc DOCUMENTACION_TECNICA.md \
  -o DOCUMENTACION_TECNICA.pdf \
  --pdf-engine=pdflatex \
  -V linkcolor=darkblue \
  -V urlcolor=darkgreen \
  -V toccolor=black
```

---

## 📝 Notas Finales

- El archivo `DOCUMENTACION_TECNICA.md` está completamente formateado en Markdown estándar
- Cualquier editor que soporte Markdown puede previsualizarlo
- Se recomienda usar el **Método 3 (VS Code)** para principiantes
- El **Método 1 (Script)** ofrece la mejor calidad para usuarios avanzados

---

**¿Problemas?** Abre un issue en el repositorio o contacta con el desarrollador.

**Última actualización:** Enero 2025
