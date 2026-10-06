<script setup>
defineProps({
  items: {
    type: Array,
    required: true
  },
  loading: Boolean,
  error: String
});
</script>

<template>
  <div>
    <div v-if="error" class="error-message">{{ error }}</div>
    <div v-if="loading && items.length === 0">Cargando...</div>

    <ul v-else-if="items.length > 0" class="item-list">
      <li v-for="item in items" :key="item.id" class="item-card">
        <strong>{{ item.nombre }}</strong> - {{ item.descripcion }} (${{ item.precio }})
      </li>
    </ul>

    <p v-else class="empty-state">No hay registros almacenados.</p>
  </div>
</template>