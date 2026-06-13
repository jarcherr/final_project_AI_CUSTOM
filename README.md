# 🚀 Asistente de IA con Arquitectura CAG (Context-Augmented Generation)
[cite_start]**Estudiante:** Jorge Enrique Archer Rosales  
[cite_start]**Curso:** Inteligencia Artificial - Examen Final [cite: 12]  
**Catedrático:** Ing. [cite_start]Richard David Ortiz Sasvin [cite: 21]

[cite_start]Proyecto monolítico avanzado que integra un motor de recuperación de conocimiento (RAG) con un sistema de persistencia y aumento de contexto en tiempo de ejecución (CAG) para personalizar la experiencia del usuario de forma dinámica[cite: 72, 74].

---

## 👨‍✈️ Filosofía de Desarrollo: Piloto y Copiloto
[cite_start]Este proyecto fue diseñado bajo el principio rector del curso: **"Nosotros somos Tony Stark y la IA es nuestro Jarvis"**[cite: 78]. [cite_start]La IA actuó exclusivamente como un asistente técnico de soporte de código y diagnóstico de entornos bajo mi estricta dirección, toma de decisiones arquitectónicas y diseño estratégico[cite: 79]. [cite_start]Todo el progreso interactivo se encuentra fielmente registrado en el archivo `PROMPTS-REALIZADOS.md`[cite: 81, 95].

---

## 📊 Metodología de Trabajo (Scrum)
[cite_start]El desarrollo se dividió de forma estricta en dos bloques de entrega incremental[cite: 88, 95]:

### 🏃 Sprint 1: Infraestructura de Persistencia e Interfaces del Servidor
* **Objetivo:** Resolver el error HTTP 501 mediante la activación de endpoints de contexto.
* **Entregables:** Implementación de la clase `ContextStore` utilizando un almacén indexado en memoria para mapear preferencias de usuarios en pares clave-valor.

### 🏃 Sprint 2: Motor de Generación Aumentada y Cierre
* [cite_start]**Objetivo:** Integrar el contexto recuperado en el pipeline del generador para alterar las respuestas del modelo según el perfil del usuario, logrando la aprobación del 100% de los contratos de validación[cite: 74, 93].

---

## 🛠️ Arquitectura del Sistema

| Módulo | Descripción / Responsabilidad |
|---|---|
| `backend/server.py` | [cite_start]Servidor HTTP nativo en Python encargado de exponer el API Contract (`/api/ask`, `/api/context`). |
| `backend/context_store.py` | Componente de persistencia en memoria que gestiona el ciclo de vida del contexto del usuario. |
| `backend/cag.py` / `assistant.py` | [cite_start]Lógica de negocio del asistente, inyección de contexto persistente y aumento de prompts. |
| `data/knowledge_base.json` | [cite_start]Base documental estática para la consulta de datos base del RAG[cite: 72, 73]. |
| `tests/` | [cite_start]Suite automatizada de pruebas unitarias y contratos de software (TDD/BDD)[cite: 76, 92]. |

---

## 🚀 Guía de Ejecución

### 1. Ejecutar la Suite de Validación Final (TDD/BDD)
[cite_start]Para correr las pruebas de integración del contrato CAG, utilice el script automatizado desde una terminal Git Bash[cite: 93, 102]:
```bash
bash test.sh