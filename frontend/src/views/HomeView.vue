<script setup>
import Category from '@/components/Category.vue';

const categories = [
  { name: 'Fruits', description: 'Fresh and organic fruits', products : [{name:"apple"},{name:"banana"}] },
  { name: 'Vegetables', description: 'Fresh and organic vegetables' },
  { name: 'Dairy', description: 'Fresh dairy products' }
];

const category1 = {
  name: 'sdafas',
  description: 'Fresh and organic fruits',
};

</script>

<template>
<Category v-for="category in categories" :category="category" />

<Category :category = "category1" />

</template>
