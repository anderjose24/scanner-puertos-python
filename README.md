# Escáner de Puertos TCP en Python

## Descripción

Aplicación básica desarrollada en Python para escanear puertos TCP de equipos autorizados e identificar puertos abiertos. Corresponde a una práctica académica grupal de Seguridad Informática de la Universidad Estatal de Milagro (UNEMI).

El código y el manual están integrados. El manual incluye capturas reales del inicio y de los resultados de esta versión, proporcionadas durante una ejecución sobre el propio equipo.

## Objetivo

"Desarrollar una aplicación básica en Python que permita realizar un escaneo de puertos TCP de un equipo autorizado e identificar los puertos abiertos, promoviendo el uso responsable de herramientas digitales e Inteligencia Artificial."

## Herramientas utilizadas

- Python.
- Visual Studio Code.
- GitHub.
- Biblioteca `socket`.

El código también utiliza `datetime`, incluida en Python, para medir la duración.

## Estructura del proyecto

```text
scanner-puertos-python/
│
├── scanner_puertos.py
├── README.md
├── MANUAL_USO.md
└── capturas/
    ├── inicio.png
    └── resultados.png
```

- `scanner_puertos.py`: código principal del escáner TCP entregado por el responsable técnico y conservado sin modificaciones.
- `README.md`: información general, estructura y documentación básica.
- `MANUAL_USO.md`: instrucciones de preparación, ejecución y utilización, adaptadas a partir del manual de la integrante responsable.

## Funcionalidades requeridas

De acuerdo con la guía, la aplicación permite:

- Ingresar una dirección IP.
- Ingresar un puerto inicial.
- Ingresar un puerto final.
- Realizar el escaneo TCP.
- Mostrar los puertos abiertos.
- Mostrar un resumen de resultados.

El programa solicita corregir las entradas que rechaza y muestra el tiempo empleado. El escaneo comienza automáticamente después de aceptar el puerto final. No solicita confirmación «S/N» ni clasifica por separado los puertos cerrados y filtrados.

## Requisitos

Python 3.6 o posterior. `socket` y `datetime` forman parte de la biblioteca estándar; no se requieren dependencias externas. Visual Studio Code es opcional para ejecutar el programa. El destino debe ser propio o estar expresamente autorizado.

## Ejecución

Desde la carpeta del proyecto:

```bash
python scanner_puertos.py
```

O bien:

```bash
python3 scanner_puertos.py
```

En Windows también puede utilizarse `py -3 scanner_puertos.py` si el lanzador está disponible. Ingresar los datos solicitados en `IP:`, `Desde:` y `Hasta:`.

## Manual de uso

Consultar [MANUAL_USO.md](MANUAL_USO.md) para conocer el procedimiento, la interpretación de resultados y las capturas de funcionamiento.

## Uso responsable

Esta herramienta tiene fines académicos y educativos. Debe utilizarse exclusivamente sobre equipos propios, máquinas virtuales, laboratorios autorizados o redes expresamente autorizadas. Un puerto abierto no demuestra por sí solo una vulnerabilidad.

## Información académica

- **Tipo:** proyecto académico grupal.
- **Universidad:** Universidad Estatal de Milagro - UNEMI.
- **Carrera:** Tecnologías de la Información.
- **Asignatura:** Seguridad Informática.
- **Práctica:** N.º 2.
- **Responsable de organización del repositorio GitHub:** Anderson Jose Vega Guillin.
- **Responsable del desarrollo técnico:** Alex Sorely Bahamonde Sánchez.
- **Responsable del manual de uso:** Pamela del Rocío Merizalde Ortiz.
