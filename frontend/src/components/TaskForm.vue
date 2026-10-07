<script setup>
import { ref } from 'vue';

const props = defineProps({
  loading: Boolean
});

const emit = defineEmits(['add-task']);

const title = ref('');
const priority = ref('medium');

const handleSubmit = () => {
  if (!title.value.trim()) return;
  
  emit('add-task', {
    title: title.value.trim(),
    priority: priority.value
  });

  // Limpiar campos tras emitir
  title.value = '';
  priority.value = 'medium';
};
</script>

<template>
  <form @submit.prevent="handleSubmit" class="item-form">
    <div class="form-group">
      <input
        v-model="title"
        type="text"
        placeholder="¿que tarea tienes pendiente?"
        required
        class="form-input"
      />
      <select v-model="priority" class="form-select">
        <option value="low">Baja</option>
        <option value="medium">Media</option>
        <option value="high">Alta</option>
      </select>
      <button type="submit" :disabled="loading" class="btn-primary">
        {{ loading ? 'Procesando...' : 'Agregar Tarea' }}
      </button>
    </div>
  </form>
</template> 