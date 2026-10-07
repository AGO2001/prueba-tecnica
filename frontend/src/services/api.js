// frontend/src/services/api.js
const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

export async function getTasks(done = null) {
let url = `${API_URL}/api/tasks`;
if (done!== null && done !== '') {
  url += `?done=${done}`;
}
const response = await fetch(url);
if (!response.ok) throw new Error('Error al obtener las tareas');
return response.json();
}

export async function createTask(taskData) {
  const response = await fetch(`${API_URL}/api/tasks`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(taskData),
  });
  if (!response.ok) {
    const errorData = await response.json();
    throw new Error(errorData.detail || 'Error al crear la tarea');
  }
}

export async function updateTaskStatus(taskId, doneDtatus){
  const response = await fetch(`${API_URL}/api/tasks/${taskId}`, {
    method: 'PATCH',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({done: doneDtatus}),
  });
  if (!response.ok) {
    const errorData = await response.json();
    throw new Error(errorData.detail || 'Error al actualizar la tarea');
  }
  return response.json();
}

export async function deleteTask(taskId) {  
  const response = await fetch(`${API_URL}/api/tasks/${taskId}`, {
    method: 'DELETE',
  });
  if (!response.ok) {
    throw new Error('Error al eliminar la tarea');
  }
  return true;
}
  