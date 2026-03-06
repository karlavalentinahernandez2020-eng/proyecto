# Estudiante: Karla Hernández
# Cédula: 32.051.352

import requests
from typing import Optional, Dict, Any

class PostManager:
    """Gestor de operaciones con posts"""
    BASE_URL = "https://jsonplaceholder.typicode.com"

    def __init__(self):
        self.session = requests.Session()

    def obtener_post(self, post_id: int) -> dict:
        url = f"{self.BASE_URL}/posts/{post_id}"
        response = self.session.get(url)
        response.raise_for_status()
        return response.json()

    def crear_post(self, titulo: str, cuerpo: str, usuario_id: int) -> dict:
        url = f"{self.BASE_URL}/posts"
        data = {"title": titulo, "body": cuerpo, "userId": usuario_id}
        response = self.session.post(url, json=data)
        response.raise_for_status()
        return response.json()

    def actualizar_parcial(self, post_id: int, **campos) -> dict:
        url = f"{self.BASE_URL}/posts/{post_id}"
        response = self.session.patch(url, json=campos)
        response.raise_for_status()
        return response.json()

    def eliminar_post(self, post_id: int) -> bool:
        url = f"{self.BASE_URL}/posts/{post_id}"
        response = self.session.delete(url)
        return response.status_code == 200

# === PRUEBAS ===
if __name__ == "__main__":
    manager = PostManager()

    # --- GET ---
    post_recuperado = manager.obtener_post(1)
    print("--- GET ---")
    print(f"Post obtenido: {post_recuperado['title']}")
    print()

    # --- POST ---
    nuevo_post = manager.crear_post("Prueba", "Contenido", 1)
    print("--- POST ---")
    print(f"Post creado ID: {nuevo_post['id']}")
    print()

    # --- PATCH ---
    post_editado = manager.actualizar_parcial(1, title="Título Actualizado")
    print("--- PATCH ---")
    print(f"Post actualizado: {post_editado['title']}")
    print()

    # --- DELETE ---
    eliminado_exitoso = manager.eliminar_post(1)
    print("--- DELETE ---")
    print(f"Post eliminado: {eliminado_exitoso}")

