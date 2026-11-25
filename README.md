# ISR401-VelezJostin

Repositorio personal de Ingeniería de Requerimientos (ISR-401), paralelo B, SPA 2026–2027.
Estudiante: Vélez Vinces Jostin Gustavo.

## Contenido

| Carpeta | Actividad | Archivo principal | PDF compilado |
|---|---|---|---|
| `FORM-TL-01/` | Taller de tipos de requisitos (formativa) | `main.tex` | `main.pdf` |
| `TA-IND-01/` | IEEE 29148 y tipos de requisitos (sumativa). Cómo compilarla: [`TA-IND-01/README.md`](TA-IND-01/README.md) | `main.tex` | `main.pdf` |
| `EV-PRAC-01/` | Evaluación de la Unidad I, caso ALERTARÍO: transcripción fiel de la prueba escrita (sumativa) | `main.tex` | `main.pdf` |
| `TA-IND-02/` | Priorización de requisitos con MoSCoW, Kano y votación ponderada (sumativa), dominio: laboratorio clínico. Cómo compilarla: [`TA-IND-02/README.md`](TA-IND-02/README.md) | `main.tex` | `main.pdf` |
| `sga/` | Hoja de una página para el SGA | `FORM-TL-01-sga.tex` | — |

Las instrucciones de compilación de abajo son las de `FORM-TL-01`. Cada actividad nueva tiene su propio `README.md` dentro de su carpeta, salvo `EV-PRAC-01`, que se explica en la sección siguiente.

## EV-PRAC-01 · Evaluación de la Unidad I

`EV-PRAC-01/main.tex` es la guía-rúbrica del docente con la transcripción fiel de la prueba escrita a mano el 18 de noviembre de 2026, debajo de cada tarea respondida (T1 y T2). Las fotografías de las hojas están en `EV-PRAC-01/evidencias/` (`hoja-01.jpg`, `hoja-02.jpg`, `hoja-03.jpg`) y no se incluyen en el PDF.

```
EV-PRAC-01/
├── main.tex          archivo principal
├── referencias.bib   referencias de la guía (natbib, estilo unsrtnat)
├── main.pdf          PDF compilado
├── figuras/          logo-uteq.png, logo-fcc.png
└── evidencias/       fotografías de las hojas escritas a mano
```

| Elemento | Valor |
|---|---|
| Compilador | `pdflatex` + `bibtex` (TeX Live 2024 o posterior, o MiKTeX) |
| Archivo principal | `EV-PRAC-01/main.tex` |
| Bibliografía | `EV-PRAC-01/referencias.bib` con BibTeX (`natbib`, estilo `unsrtnat`) |
| Paquetes | `inputenc`, `fontenc`, `helvet`, `geometry`, `graphicx`, `array`, `tabularx`, `longtable`, `pdflscape`, `colortbl`, `xcolor`, `enumitem`, `fancyhdr`, `lastpage`, `tcolorbox`, `amsmath`, `natbib`, `url`, `needspace`, `caption`, `hyperref`; todos vienen en TeX Live completo y en Overleaf |

Compilar en una computadora (desde la carpeta del repositorio clonado):

```bash
cd EV-PRAC-01
pdflatex main
bibtex main
pdflatex main
pdflatex main
```

En Overleaf: subir `main.tex`, `referencias.bib` y la carpeta `figuras`, elegir *Compiler* = **pdfLaTeX** y *Main document* = **main.tex**, y pulsar **Recompilar** (Overleaf ejecuta BibTeX solo).

Estructura de `FORM-TL-01/`:

```
FORM-TL-01/
├── main.tex          archivo principal
├── refs.bib          referencias (estilo IEEE)
├── main.pdf          PDF compilado
└── figuras/
    ├── logo-uteq.png
    └── logo-fcc.png
```

## Cómo compilar en Overleaf

Configuración que debe tener el proyecto:

| Opción de Overleaf (Menú) | Valor |
|---|---|
| Compiler | **pdfLaTeX** |
| Main document | **main.tex** |
| TeX Live version | **2026** (o la más reciente) |

No se necesita instalar nada: todos los paquetes y el estilo de referencias IEEE (`IEEEtran.bst`) vienen incluidos en Overleaf.

### Pasos

1. En este repositorio de GitHub, pulsar el botón verde **Code → Download ZIP** y descomprimir el archivo.
2. Entrar a la carpeta `FORM-TL-01` y comprimir **su contenido** (`main.tex`, `refs.bib` y la carpeta `figuras`) en un nuevo archivo .zip.
3. En Overleaf: **New Project → Upload Project** y subir ese .zip.
4. Abrir **Menú** (arriba a la izquierda) y comprobar que *Compiler* sea **pdfLaTeX** y *Main document* sea **main.tex**.
5. Pulsar **Recompilar**. Overleaf genera el PDF con la bibliografía (ejecuta pdfLaTeX y BibTeX automáticamente).

### Si algo falla

- **«File `logo-uteq.png' not found»:** la carpeta `figuras` debe quedar al mismo nivel que `main.tex`, con los nombres en minúsculas.
- **Las referencias salen como [?]:** pulsar **Recompilar** otra vez, o en la flecha junto a *Recompilar* elegir **Recompile from scratch**.
- **Error con XeLaTeX o LuaLaTeX:** cambiar *Compiler* a **pdfLaTeX** en el Menú.

## Hoja para el SGA

Para compilar `sga/FORM-TL-01-sga.tex` en Overleaf: crear un proyecto nuevo, subir ese archivo (como `main.tex`) junto con la carpeta `figuras` de `FORM-TL-01`, usar el compilador **pdfLaTeX** y pulsar **Recompilar**. Debe resultar una sola página.
