<script setup>
import { ref } from 'vue';

const props = defineProps({
  loading: Boolean
});

const emit = defineEmits(['add-item']);

const nombre = ref('');
const descripcion = ref('');
const precio = ref(0);

const handleSubmit = () => {
  if (!nombre.value) return;
  
  emit('add-item', {
    nombre: nombre.value,
    descripcion: descripcion.value,
    precio: Number(precio.value)
  });

  // Limpiar campos tras emitir
  nombre.value = '';
  descripcion.value = '';
  precio.value = 0;
};
</script>

<template>
  <form @submit.prevent="handleSubmit" class="item-form">
    <input 
      v-model="nombre" 
      placeholder="Nombre" 
      required 
      class="form-input" 
    />
    <input 
      v-model="descripcion" 
      placeholder="Descripción" 
      class="form-input" 
    />
    <input 
      v-model.number="precio" 
      type="number" 
      step="0.01" 
      placeholder="Precio" 
      required 
      class="form-input" 
    />
    <button type="submit" :disabled="loading" class="form-button">
      {{ loading ? 'Procesando...' : 'Agregar Registro' }}
    </button>
  </form>
</template>