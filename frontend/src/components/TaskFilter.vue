<script setup>
const props = defineProps({
    currenFilter: String
});

const  emit = defineEmits(['filter-change']);

const setFilter = (value) => {
    emit ('filter-change', value);
};
</script>
<template>
    <div class="filter-container">
        <span>Filtrar por estado</span>
        <button
        :class="['filter-btn', { active: currenFilter === '' }]"
        @click="setFilter('')">
        Todas
        </button>
        <button
        :class="['filter-btn', { active: currenFilter === 'false' }]"
        @click="setFilter('false')">
        Pendientes
        </button>
        <button
        :class="['filter-btn', { active: currenFilter === 'true' }]"
        @click="setFilter('true')">
        Terminadas
        </button>
    </div>
</template>