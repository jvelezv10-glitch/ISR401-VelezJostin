# TA-IND-02 · Priorización de requisitos con MoSCoW, Kano y votación ponderada

Trabajo autónomo individual (actividad sumativa) de Ingeniería de Requerimientos (ISR-401), paralelo B.
Estudiante: Vélez Vinces Jostin Gustavo.
Dominio asignado por sorteo: **10. Laboratorio clínico: órdenes, muestras y resultados**.

## Archivos

```
TA-IND-02/
├── README.md         este archivo
├── main.tex          archivo principal
├── referencias.bib   referencias (estilo IEEE)
├── main.pdf          PDF compilado
├── figuras/          logo-uteq.png, logo-fcc.png
├── datos/            respuestas Kano y votaciones (CSV) y sus cálculos
└── evidencias/
    └── MANIFIESTO.md registro de participantes, sin datos personales
```

## Cómo compilar

| Elemento | Valor |
|---|---|
| Compilador | `pdflatex` + `bibtex` (TeX Live 2024 o posterior, o MiKTeX) |
| Archivo principal | `TA-IND-02/main.tex` |
| Bibliografía | `TA-IND-02/referencias.bib` con BibTeX, estilo `IEEEtran` |
| Paquetes | `inputenc`, `fontenc`, `babel`, `geometry`, `graphicx`, `longtable`, `array`, `xcolor`, `url`, `hyperref`; todos vienen en TeX Live completo, en MiKTeX y en Overleaf |

En una computadora, desde la carpeta del repositorio clonado:

```bash
cd TA-IND-02
pdflatex main
bibtex main
pdflatex main
pdflatex main
```

En Overleaf: subir `main.tex`, `referencias.bib` y la carpeta `figuras`, elegir *Compiler* = **pdfLaTeX** y *Main document* = **main.tex**, y pulsar **Recompilar** (Overleaf ejecuta BibTeX solo).
