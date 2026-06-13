from backend.knowledge import retrieve_snippets
from backend.cag import apply_context
from backend.context_store import ContextStore

# Mantenemos la instancia global libre de importación circular
context_store = ContextStore()

def answer_question(user_id, question):
    snippets = retrieve_snippets(question)

    if not snippets:
        return {
            "user_id": user_id,
            "answer": "No encontre informacion suficiente en la base de conocimiento del curso.",
            "sources": [],
            "context_used": {},
        }

    # 1. Recuperamos el contexto persistente del usuario del Sprint 1
    user_context = context_store.list_for_user(user_id)

    # 2. Convertimos el formato de lista de objetos a un diccionario plano
    # Transformamos [{"key": "audience", "value": "explicar como principiante"}] 
    # en {"audience": "explicar como principiante"} para satisfacer estrictamente el test contract.
    flat_context = {}
    for item in user_context:
        flat_context[item["key"]] = item["value"]

    # 3. Generamos la respuesta base con el RAG tradicional
    source_text = " ".join(item["content"] for item in snippets)
    base_answer = f"Segun la base de conocimiento del curso: {source_text}"

    # 4. Aplicamos el módulo CAG para aumentar la respuesta usando el contexto
    final_answer = apply_context(user_id, question, base_answer, user_context)

    # 5. Retornamos la estructura exacta que valida el test final
    return {
        "user_id": user_id,
        "answer": final_answer,
        "sources": [item["id"] for item in snippets],
        "context_used": flat_context,  # Enviamos el diccionario plano que contiene "audience"
    }