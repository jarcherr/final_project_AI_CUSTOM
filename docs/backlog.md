# Product Backlog y Planificación de Sprints - Módulo CAG
**Product Owner / Scrum Master / Dev:** Jorge

## Product Backlog (Historias de Usuario)
1. **HU-01: Configuración de Endpoints base para Contexto (POST/GET)** - Como sistema, necesito rutas para guardar y recuperar el contexto del usuario para persistir la información.
2. **HU-02: Almacenamiento Persistente de Contexto** - Como sistema, requiero almacenar las preferencias e historial del usuario en un archivo o estructura de datos para que no se borren entre consultas.
3. **HU-03: Integración de Contexto en el Motor de Generación (CAG)** - Como usuario, quiero que las respuestas del bot consideren mis preferencias guardadas anteriormente para recibir atención personalizada.
4. **HU-04: Pruebas Unitarias y Automatización** - Como desarrollador, necesito verificar el contrato de la API para asegurar estabilidad.

---

## 🏃 Sprint 1: Infraestructura de Persistencia y Contratos de API
**Objetivo del Sprint:** Lograr que los endpoints de contexto respondan correctamente (HTTP 201 y 200) resolviendo los errores 501 actuales.

### Sprint Backlog (Sprint 1)
* [ ] Tarea 1.1: Mapear y analizar el archivo `test_cag_contract.py` para entender la estructura exacta de datos esperada.
* [ ] Tarea 1.2: Implementar el endpoint `POST` para guardar el contexto del usuario (Retornar HTTP 201).
* [ ] Tarea 1.3: Implementar el endpoint `GET` para recuperar el contexto guardado (Retornar HTTP 200).
* [ ] Tarea 1.4: Ejecutar pruebas y verificar la resolución de las primeras 2 fallas del contrato.

---

## 🏃 Sprint 2: Lógica de Generación Aumentada por Contexto (CAG) y Cierre
**Objetivo del Sprint:** Modificar la lógica de respuestas para inyectar dinámicamente el contexto guardado en el prompt del LLM/RAG y pasar el 100% de las pruebas.

### Sprint Backlog (Sprint 2)
* [ ] Tarea 2.1: Modificar la función de consulta principal (`ask`) para que busque si el usuario tiene un contexto previo guardado.
* [ ] Tarea 2.2: Diseñar el nuevo prompt combinando el contexto del usuario ("principiante", etc.) con el conocimiento base del RAG.
* [ ] Tarea 2.3: Ejecutar suite completa de validación final (`test.sh`).
* [ ] Tarea 2.4: Realizar la documentación final, capturas de pantalla de evidencias y fusiones de ramas (Pull Request).