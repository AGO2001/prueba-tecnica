<script setup>
import { ref, onMounted } from 'vue';
import { getTasks, createTask, updateTaskStatus, deleteTask } from './services/api';
import TaskForm from './components/TaskForm.vue';
import TaskItem from './components/TaskItem.vue';
import TaskFilter from './components/TaskFilter.vue';

const tasks = ref([]);
const loading = ref(false);
const error = ref(null);
const currentFilter = ref('');

const fetchTasks = async () => {
  loading.value = true;
  error.value = null;
  try {
    const filterParam = currentFilter.value === '' ? null : currentFilter.value;
    tasks.value = await getTasks(filterParam);
  } catch (err) {
    error.value = err.message;
  } finally {
    loading.value = false;
  }
};

const handleAddTask = async (newTask) => {
  loading.value = true;
  error.value = null;
  try {
    await createTask(newTask);
    await fetchTasks();
  } catch (err) {
    error.value = err.message;
  } finally {
    loading.value = false;
  }
};

const handleToggleStatus = async (taskId, newStatus) => {
  error.value = null;
  try {
    await updateTaskStatus(taskId, newStatus);
    await fetchTasks();
  } catch (err) {
    error.value = err.message;
  }
};
const handleDeleteTask = async (taskId) => {
  error.value = null;
  try {
    await deleteTask(taskId);
    await fetchTasks();
  } catch (err) {
    error.value = err.message;
  }
};
const handleFilterChange = (newFilter) => {
  currentFilter.value = newFilter;
};

onMounted(fetchTasks);

</script>

<template>
  <main class="app-container">
    <h2>Gestor de Tareas</h2>
    <!-- Formulario de Creación -->
      <TaskForm :loading="loading" @add-task="handleAddTask" />

      <!-- Barra de Filtros -->
       <TaskFilter :currenFilter="currentFilter" @filter-change="handleFilterChange" />
      <!-- Mensaje de Estado -->
        <div v-if="error" class="error-banner">{{ error }}</div>
        <div v-if="loading && tasks.length === 0" class="loading-state">Cargando tareas...</div>
      <!-- Lista de Tareas -->
        <ul v-else-if="tasks.length > 0" class="task-list">
          <TaskItem
            v-for="task in tasks"
            :key="task.id"
            :task="task"
            @toggle-status="handleToggleStatus"
            @delete-task="handleDeleteTask"
        />
        </ul>
        <p v-else class="empty-state">No hay tareas registradas.</p>
  </main>
</template> 