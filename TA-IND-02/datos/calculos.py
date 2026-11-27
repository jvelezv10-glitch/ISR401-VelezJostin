# Calculos de TA-IND-02: clasificacion Kano, totales de la votacion y Spearman.
# Uso (desde la carpeta datos/):  python calculos.py
# Lee kano_respuestas.csv y votacion_respuestas.csv; escribe kano_clasificacion.csv y votacion_totales.csv.
import csv, io, math

RESP = {"Me gustaria": "L", "Lo espero": "E", "Me da igual": "N", "Puedo aceptarlo": "T", "No me gustaria": "D"}
ORDEN = "LENTD"
# Tabla de evaluacion de Kano: fila = respuesta funcional, columna = respuesta disfuncional
TABLA = ["QAAAO", "RIIIM", "RIIIM", "RIIIM", "RRRRQ"]
FEAT = [("K1", "RF-02"), ("K2", "RF-04"), ("K3", "RF-06"), ("K4", "RF-08"),
        ("K5", "RF-09"), ("K6", "RF-12"), ("K7", "RNF-01"), ("K8", "RNF-06")]
MOSCOW = {"RF-01": "Must", "RF-02": "Must", "RF-05": "Must", "RF-07": "Must", "RF-10": "Must", "RF-11": "Must",
          "RNF-05": "Must", "RNF-07": "Must", "RF-03": "Should", "RF-04": "Should", "RF-06": "Should",
          "RF-08": "Should", "RF-09": "Should", "RNF-03": "Should", "RF-12": "Could", "RNF-01": "Could",
          "RNF-04": "Could", "RNF-02": "Won't", "RNF-06": "Won't", "RNF-08": "Won't"}
VALOR = {"Must": 4, "Should": 3, "Could": 2, "Won't": 1}
DESEMPATE = "MOAIRQ"  # regla de desempate: Obligatoria > Desempeno > Atractiva > Indiferente


def leer(nombre):
    with io.open(nombre, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def escribir(nombre, filas):
    with io.open(nombre, "w", encoding="utf-8", newline="") as f:
        csv.writer(f, lineterminator="\n").writerows(filas)


def rangos(x):
    """Rango 1 = mayor valor; los empates reciben el promedio de sus rangos."""
    orden = sorted(range(len(x)), key=lambda i: -x[i])
    r = [0.0] * len(x)
    i = 0
    while i < len(orden):
        j = i
        while j + 1 < len(orden) and x[orden[j + 1]] == x[orden[i]]:
            j += 1
        for k in range(i, j + 1):
            r[orden[k]] = (i + j) / 2 + 1
        i = j + 1
    return r


def pearson(a, b):
    n = len(a)
    ma, mb = sum(a) / n, sum(b) / n
    cov = sum((x - ma) * (y - mb) for x, y in zip(a, b))
    return cov / math.sqrt(sum((x - ma) ** 2 for x in a) * sum((y - mb) ** 2 for y in b))


# ---------- Kano ----------
kano = leer("kano_respuestas.csv")
codigos = [p["codigo"] for p in kano]
filas = [["caracteristica", "requisito"] + codigos + ["A", "O", "M", "I", "R", "Q", "categoria", "CS", "DS"]]
for k, req in FEAT:
    cat = [TABLA[ORDEN.index(RESP[p[k + "-F"]])][ORDEN.index(RESP[p[k + "-D"]])] for p in kano]
    n = {c: cat.count(c) for c in "AOMIRQ"}
    gana = sorted("AOMIRQ", key=lambda c: (-n[c], DESEMPATE.index(c)))[0]
    base = n["A"] + n["O"] + n["M"] + n["I"]
    cs = (n["A"] + n["O"]) / base
    ds = -(n["O"] + n["M"]) / base
    filas.append([k, req] + cat + [n[c] for c in "AOMIRQ"] + [gana, f"{cs:.2f}", f"{ds:.2f}"])
    print(f"{k} {req:7} {''.join(cat)}  ->  {gana}  CS={cs:.2f}  DS={ds:.2f}")
escribir("kano_clasificacion.csv", filas)

# ---------- Votacion y Spearman ----------
vot = leer("votacion_respuestas.csv")
reqs = list(MOSCOW.keys())
reqs.sort(key=lambda r: (r.startswith("RNF"), int(r.split("-")[1])))
for v in vot:
    assert sum(int(v[r]) for r in reqs) == 100, "la votacion de " + v["codigo"] + " no suma 100"
total = [sum(int(v[r]) for v in vot) for r in reqs]
rv = rangos(total)
rm = rangos([VALOR[MOSCOW[r]] for r in reqs])
rho = pearson(rv, rm)
filas = [["requisito"] + [v["codigo"] for v in vot] + ["total", "rango_votacion", "moscow", "rango_moscow", "d", "d2"]]
for i, r in enumerate(reqs):
    d = rv[i] - rm[i]
    filas.append([r] + [v[r] for v in vot] + [total[i], rv[i], MOSCOW[r], rm[i], d, d * d])
filas.append(["spearman_rho", f"{rho:.4f}"])
escribir("votacion_totales.csv", filas)
print(f"Spearman rho = {rho:.4f} (n = {len(reqs)})")
