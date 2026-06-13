# Bitácora de Interacciones con IA - Examen Final Inteligencia Artificial
**Director de Proyecto:** Jorge Enrique Archer Rosales
**Asistente IA:** Gemini

## Entrada 1: Definición de Estrategia y Resolución Serie I
* **Fecha:** 12 de junio de 2026
* **Objetivo del prompt:** Instruir a la IA para analizar el enunciado del examen final adjunto, resolver la sección teórica bajo mi supervisión y trazar la ruta metodológica inicial.
* **Prompt usado:** "hola gemini, tengo mi examen final de inteligencia artificial, me ayudas a trabajarlo, ahora te comparto las preguntas teoricas, si me das la respuesta correcta con su explicacion, ademas te presento el problema que debemos de trabajar en clase para que lo vayamos trabajando paso a paso juntos"
* **Resumen de la respuesta recibida:** La IA propuso un plan de trabajo dividido en 5 fases lógicas (Teoría, Entorno, Scrum, Desarrollo CAG y Cierre) y devolvió las respuestas justificadas de la Serie I.
* **Decisión humana tomada:** Validar y aceptar las respuestas teóricas propuestas por la IA al comprobar que se alinean con los conceptos de redes neuronales del curso. Modificar el plan para priorizar la sincronización inmediata del repositorio mediante el Fork solicitado por el docente.
* **Cambios realizados en el proyecto:** Ninguno en código; preparación del espacio de trabajo conceptual.
* **Verificación aplicada:** Inspección visual de las respuestas de la Serie I contra el material de clase.

## Entrada 2: Inicialización del Entorno de Desarrollo y Registro de Estructura
* **Fecha:** 12 de junio de 2026
* **Objetivo del prompt:** Dirigir a la IA para obtener la secuencia exacta de comandos Git necesarios para realizar un Fork limpio, clonarlo localmente de manera estructurada y documentar la arquitectura base encontrada.
* **Prompt usado:** "inicialicemos el ingeniero esta pidiendo hacer el fork para que le cuadre la cantidad, empecemos por ahi y luego hacemos el resto, ayudame paso a paso a hacer el fork"
* **Resumen de la respuesta recibida:** La IA generó los pasos técnicos para bifurcar el repositorio en GitHub, realizar la clonación local y reconoció la arquitectura monolítica compuesta por carpetas backend, frontend, tests, data y el automatizador test.sh.
* **Decisión humana tomada:** Ejecutar el Fork público en mi cuenta de GitHub (jarcherr/final_project_AI_CUSTOM), clonarlo en mi entorno de desarrollo local y capturar la estructura de archivos inicial para evidencias. Ordenar la redacción cronológica de esta bitácora manteniendo mi rol de director de la solución.
* **Cambios realizados en el proyecto:** Creación e inicialización del archivo `PROMPTS.md` en la raíz.
* **Verificación aplicada:** Verificación de acceso al repositorio en la URL pública y confirmación de carpetas clonadas en el sistema local.

## Entrada 3: Análisis de Resultados del Test Base y Planificación Scrum
* **Fecha:** 12 de junio de 2026
* **Objetivo del prompt:** Suministrar el traceback de errores de la validación inicial (3 pruebas fallidas por códigos de estado 501 e incoherencia de contexto) y ordenar a la IA estructurar un Product Backlog formal dividido en 2 Sprints para abordar la solución de forma controlada.
* **Prompt usado:** "Obtuve esta respuesta del bash ejecutado en visual studio code HP@DESKTOP-FMCDRKJ MINGW64 ~/Documents/Jorge/Universidad/InteligenciArtificial/ExamenFinal/final_project_AI_CUSTOM (main) $ bash test.sh Running CAG validation tests... FFF ... [Traceback de fallas]"
* **Resumen de la respuesta recibida:** La IA diagnosticó que los fallos corresponden a la falta de implementación de los endpoints (HTTP 501) y a la ausencia de inyección de contexto. Propuso un plan de Product Backlog detallando los entregables del Sprint 1 (Persistencia y Endpoints) y del Sprint 2 (Lógica CAG e inyección de contexto).
* **Decisión humana tomada:** Aprobar la división de tareas en 2 Sprints bajo la metodología Scrum exigida por la rúbrica. Guardar la planificación en la documentación del proyecto e instruir el inicio del Sprint 1 enfocándonos en el código del backend.
* **Cambios realizados en el proyecto:** Creación/actualización del archivo de planificación Scrum (`docs/backlog.md`).

