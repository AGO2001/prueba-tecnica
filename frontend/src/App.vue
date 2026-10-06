<script setup>
import { ref, onMounted } from 'vue';
import { getItems, createItem } from './services/api';
import ItemForm from './components/ItemForm.vue';
import ItemList from './components/ItemList.vue';

const items = ref([]);
const loading = ref(false);
const error = ref(null);

const cargarDatos = async () => {
  loading.value = true;
  error.value = null;
  try {
    items.value = await getItems();
  } catch (err) {
    error.value = err.message;
  } finally {
    loading.value = false;
  }
};

const guardarItem = async (nuevoItem) => {
  loading.value = true;
  error.value = null;
  try {
    await createItem(nuevoItem);
    await cargarDatos();
  } catch (err) {
    error.value = err.message;
  } finally {
    loading.value = false;
  }
};

onMounted(cargarDatos);
</script>

<template>
  <div class="container">
    <h2>Panel de Pruebas - Fullstack</h2>

    <!-- Componente de Formulario Reutilizable -->
    <ItemForm :loading="loading" @add-item="guardarItem" />

    <!-- Componente de Lista Reutilizable -->
    <ItemList :items="items" :loading="loading" :error="error" />
  </div>
</template>