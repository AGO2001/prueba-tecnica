<script setup>
defineProps({
  task: {
    type: Object,
    required: true
  }
});
const emit = defineEmits(['toggle-status', 'delete-task']);
</script>

<template>
  <li :class="['task-card', {done: task.done}]">
    <div class="task-info">
      <input
        type="checkbox"
        :checked="task.done"
        @change="emit('toggle-status', task.id, !task.done)"
      />
      <span class="task-title">{{ task.title }}</span>
      <span :class="['priority-badge', task.priority]">
        {{ task.priority }}
      </span>
      </div>
      <button @click="emit('delete-task', task.id)" class="btn-delete">
        Eliminar
      </button>
      
  </li>
</template>