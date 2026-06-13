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

## Entrada 4: Inspección de Arquitectura de Red de Endpoints (server.py)
* **Fecha:** 12 de junio de 2026
* **Objetivo del prompt:** Suministrar el código fuente completo de server.py a la IA para diagnosticar el origen exacto de las excepciones HTTP 501 detectadas en las pruebas de integración del Sprint 1.
* **Prompt usado:** "muy bien jarvis, empecemos con el sprint 1, vamos a trabajar en habilitar los servicios te comparto el contenido del archivo server y vamos a trabajarlo en python que ya es la base que trae el sistema [Código fuente adjunto]"
* **Resumen de la respuesta recibida:** La IA determinó que server.py gestiona adecuadamente las rutas '/api/context' (GET y POST) pero delega la lógica de negocio en la clase ContextStore, la cual genera de manera explícita excepciones 'NotImplementedError', produciendo las fallas en el test contract.
* **Decisión humana tomada:** Mantener intacto el código de server.py debido a que cumple correctamente con la definición del API contract del examen. Ordenar la apertura inmediata de backend/context_store.py para programar la lógica de persistencia faltante.
* **Cambios realizados en el proyecto:** Ninguno en código; priorización del backlog técnico hacia el componente de almacenamiento.
* **Verificación aplicada:** Inspección cruzada entre las llamadas del servidor y las firmas esperadas del contrato de pruebas.

## Entrada 5: Implementación de la Persistencia del Contexto (Sprint 1)
* **Fecha:** 12 de junio de 2026
* **Objetivo del prompt:** Proveer el esqueleto de backend/context_store.py y solicitar el desarrollo de la lógica de almacenamiento y recuperación de contexto en Python utilizando estructuras de datos adecuadas para resolver las excepciones 'NotImplementedError'.
* **Prompt usado:** "te paso el contenido del archivo \"\"\"Base placeholder for student implementation.\"\"\" class ContextStore: ... [Código base adjunto]"
* **Resumen de la respuesta recibida:** La IA diseñó la inicialización del almacén de datos mediante un diccionario privado en memoria (`self._storage`) e implementó los métodos `save` y `list_for_user` estructurando los retornos como pares clave-valor empaquetados en listas por usuario.
* **Decisión humana tomada:** Adoptar el almacenamiento en memoria propuesto por ser óptimo y suficiente para satisfacer las aserciones de los contratos de pruebas automatizadas del proyecto sin añadir dependencias pesadas de bases de datos externas.
* **Cambios realizados en el proyecto:** Modificación completa de `backend/context_store.py`.
* **Verificación aplicada:** Ejecución del script `bash test.sh` para evaluar el impacto de los nuevos endpoints activos sobre la suite de pruebas.

## Entrada 6: Finalización del Sprint 1, Transición a Sprint 2 y Rediseño de README
* **Fecha:** 12 de junio de 2026
* **Objetivo del prompt:** Reportar la superación exitosa de 2 de las 3 pruebas base en la terminal bash (reducción de fallas a 1) y ordenar la reestructuración completa del archivo README.md bajo criterios formales de Scrum y la filosofía Stark/Jarvis.
* **Prompt usado:** "esto me respondio el bash test... [Imagen adjunta de 1 fallo restante] ...tambien te queria solicitar ayuda actualizando el archivo readme, esto es lo que tiene ahora al inicio..."
* **Resumen de la respuesta recibida:** La IA felicitó el avance del Sprint 1 al mitigar los errores 501 e interpretó el fallo restante como la falta de inyección del contexto en el prompt final. Proporcionó el código Markdown completo para transformar el README.md en una pieza de documentación técnica avanzada.
* **Decisión humana tomada:** Sobreescribir el README.md original para reflejar la documentación de la arquitectura real del examen y el flujo metodológico implementado. Disponerse a abrir el archivo encargado de la lógica del asistente para finiquitar el Sprint 2.
* **Cambios realizados en el proyecto:** Actualización radical de `README.md`.
* **Verificación aplicada:** Inspección visual del README.md usando la previsualización del editor de código.

## Entrada 7: Resolución de Importación Circular en Arquitectura Monolítica
* **Fecha:** 12 de junio de 2026
* **Objetivo del prompt:** Reportar un fallo de tipo 'ImportError' por dependencia cíclica entre server.py y assistant.py al acoplar concurrentemente la referencia de 'context_store', y solicitar la refactorización correctiva.
* **Prompt usado:** "tengo este error HP@DESKTOP-FMCDRKJ MINGW64 ... ImportError: cannot import name 'context_store' from partially initialized module 'backend.server' (most likely due to a circular import)... [Traceback adjunto]"
* **Resumen de la respuesta recibida:** La IA diagnosticó un bloqueo de inicialización por llamadas mutuas simultáneas. Propuso migrar la instanciación de ContextStore hacia backend/assistant.py y modificar backend/server.py para consumirla desde allí, rompiendo el acoplamiento circular.
* **Decisión humana tomada:** Ejecutar la refactorización arquitectónica reubicando el ciclo de vida del almacén de contexto dentro del orquestador del asistente, garantizando un flujo unidireccional de dependencias de acuerdo a buenas prácticas de software.
* **Cambios realizados en el proyecto:** Modificación de `backend/assistant.py` y `backend/server.py`.
* **Verificación aplicada:** Re-ejecución del script `bash test.sh` para comprobar la correcta compilación y el éxito de las aserciones de software.

## Entrada 8: Refinamiento de Estructura de Salida JSON (Cierre del Sprint 2)
* **Fecha:** 12 de junio de 2026
* **Objetivo del prompt:** Corregir el fallo en el tipo de mapeo para 'context_used' en la última aserción del contrato de pruebas, donde se exige que las claves del contexto estén en formato de diccionario plano o directo.
* **Prompt usado:** "tenemos error aun HP@DESKTOP-FMCDRKJ MINGW64 ... AssertionError: 'audience' not found in [{'key': 'audience', 'value': 'explicar como principiante'}] ... [Traceback de falla]"
* **Resumen de la respuesta recibida:** La IA detectó que el test asume un diccionario plano indexado por las propiedades directamente. Proporcionó una lógica de conversión intermedia dentro de backend/assistant.py para aplanar los ítems del almacén antes de retornar el JSON de respuesta.
* **Decisión humana tomada:** Aprobar la refactorización en el formateo de salida de assistant.py. Esto garantiza la total compatibilidad con el marco de pruebas automatizado sin alterar el diseño de persistencia base de ContextStore.
* **Cambios realizados en el proyecto:** Modificación de `backend/assistant.py`.
* **Verificación aplicada:** Ejecución del script final de pruebas mediante `bash test.sh`.

## Entrada 9: Aprobación del Contrato de Pruebas y Cierre de Proyecto
* **Fecha:** 12 de junio de 2026
* **Objetivo del prompt:** Reportar la resolución exitosa del 100% de la suite de pruebas automatizadas (Estado Verde / OK) y solicitar el esquema del informe técnico de evidencias finales según la rúbrica del examen.
* **Prompt usado:** "ya tenemos exito, me pide un informe el ingeniero, me imagino que son las evidencias + [Captura de pantalla de bash test.sh con resultado OK]"
* **Resumen de la respuesta recibida:** La IA celebró el éxito de las pruebas y generó un reporte formal automatizado en PDF que documenta la arquitectura CAG, el mapeo de datos, la gestión de Scrum, y las fases de control de calidad. Proveyó además los comandos Git para ejecutar el flujo de Pull Request y Merge final.
* **Decisión humana tomada:** Aprobar el informe de evidencias consolidado, descargar el artefacto PDF generado para incorporarlo en las carpetas de entrega y proceder al cierre de ramas en el repositorio remoto GitHub mediante un flujo controlado de Pull Request.
* **Cambios realizados en el proyecto:** Inclusión del reporte formal en la carpeta `docs/evidencias/`.
* **Verificación aplicada:** Inspección visual de la suite de pruebas local ejecutando por última vez `bash test.sh` para ratificar la estabilidad del entregable.