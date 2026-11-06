# ISR401-VelezJostin

Repositorio personal de Ingeniería de Requerimientos (ISR-401), paralelo B, SPA 2026–2027.
Estudiante: Vélez Vinces Jostin Gustavo.

## Contenido

| Carpeta | Actividad |
|---|---|
| `FORM-TL-01/` | Taller de tipos de requisitos (formativa) |

## Cómo compilar

- Compilador: `pdflatex` (TeX Live o MiKTeX) y `bibtex`.
- Archivo principal de cada actividad: `main.tex`, dentro de su carpeta.
- Dependencias: paquetes estándar (`babel`, `geometry`, `longtable`, `array`, `booktabs`, `xcolor`, `hyperref`) y el estilo `IEEEtran.bst`. Todos vienen en TeX Live y MiKTeX.

Orden de comandos (ejemplo con FORM-TL-01):

```
cd FORM-TL-01
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

El resultado es `main.pdf` en la misma carpeta.
