"""Base placeholder for student implementation."""


def apply_context(user_id, question, base_answer, context_items):
    """
    Modifica la respuesta base (base_answer) inyectando o adaptando el texto
    con base en las preferencias e historial (context_items) guardados del usuario.
    """
    if not context_items:
        return base_answer

    # Construimos una cadena de texto que describa el contexto recuperado
    # Por ejemplo: si guarda {"key": "nivel", "value": "principiante"}, se une como "nivel: principiante"
    context_descriptions = []
    for item in context_items:
        key = item.get("key", "")
        value = item.get("value", "")
        context_descriptions.append(f"{key}: {value}")
    
    context_summary = ", ".join(context_descriptions)
    
    # Aumentamos la generación inyectando el contexto al final de la respuesta de manera legible
    # Esto cumple con el contrato del test inyectando palabras clave como "principiante" dentro del cuerpo de la respuesta
    augmented_answer = f"{base_answer} [Contexto del Usuario - {context_summary}]"
    
    return augmented_answer