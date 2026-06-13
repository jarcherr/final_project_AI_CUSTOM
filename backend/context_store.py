"""Base placeholder for student implementation."""


class ContextStore:
    def __init__(self):
        # Inicializamos un diccionario en memoria para almacenar el contexto por usuario
        self._storage = {}

    def save(self, user_id, key, value):
        # Si el usuario no existe en el almacenamiento, inicializamos su lista
        if user_id not in self._storage:
            self._storage[user_id] = []
        
        # Estructuramos el ítem de contexto de acuerdo a lo esperado
        context_item = {"key": key, "value": value}
        self._storage[user_id].append(context_item)
        
        # Retornamos el objeto guardado para cumplir con la respuesta esperada
        return context_item

    def list_for_user(self, user_id):
        # Retornamos la lista de contexto del usuario. Si no tiene, devolvemos una lista vacía.
        return self._storage.get(user_id, [])