# TA-IND-01 · IEEE 29148 y tipos de requisitos de un sistema conocido

Trabajo autónomo individual (actividad sumativa) de Ingeniería de Requerimientos (ISR-401), paralelo B.
Estudiante: Vélez Vinces Jostin Gustavo.
Sistema elegido: aplicación de banca móvil de Banco Pichincha (Ecuador).

## Archivos

```
TA-IND-01/
├── README.md         este archivo
├── main.tex          archivo principal
├── referencias.bib   referencias (estilo IEEE)
├── main.pdf          PDF compilado
└── figuras/
    ├── logo-uteq.png
    ├── logo-fcc.png
    └── captura-01.png, captura-02.png, ...   capturas propias de la aplicación
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

1. En el repositorio de GitHub, pulsar el botón verde **Code → Download ZIP** y descomprimir el archivo.
2. Entrar a la carpeta `TA-IND-01` y comprimir **su contenido** (`main.tex`, `referencias.bib` y la carpeta `figuras`) en un nuevo archivo .zip.
3. En Overleaf: **New Project → Upload Project** y subir ese .zip.
4. Abrir **Menú** (arriba a la izquierda) y comprobar que *Compiler* sea **pdfLaTeX** y *Main document* sea **main.tex**.
5. Pulsar **Recompilar**. Overleaf genera el PDF con la bibliografía (ejecuta pdfLaTeX y BibTeX automáticamente).

### Si algo falla

- **«File `logo-uteq.png' not found»:** la carpeta `figuras` debe quedar al mismo nivel que `main.tex`, con los nombres en minúsculas.
- **Las referencias salen como [?]:** pulsar **Recompilar** otra vez, o en la flecha junto a *Recompilar* elegir **Recompile from scratch**.
- **Error con XeLaTeX o LuaLaTeX:** cambiar *Compiler* a **pdfLaTeX** en el Menú.
