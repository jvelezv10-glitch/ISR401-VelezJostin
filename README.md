# ISR401-VelezJostin

Repositorio personal de Ingeniería de Requerimientos (ISR-401), paralelo B, SPA 2026–2027.
Estudiante: Vélez Vinces Jostin Gustavo.

## Contenido

| Carpeta | Actividad | Archivo principal | PDF compilado |
|---|---|---|---|
| `FORM-TL-01/` | Taller de tipos de requisitos (formativa) | `main.tex` | `main.pdf` |
| `sga/` | Hoja de una página para el SGA | `FORM-TL-01-sga.tex` | — |

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
