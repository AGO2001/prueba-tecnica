// frontend/src/services/api.js
const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

export async function getItems() {
  const response = await fetch(`${API_URL}/api/items`);
  if (!response.ok) throw new Error('Error al obtener los datos');
  return response.json();
}

export async function createItem(itemData) {
  const response = await fetch(`${API_URL}/api/items`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(itemData),
  });
  if (!response.ok) throw new Error('Error al guardar el ítem');
  return response.json();
}