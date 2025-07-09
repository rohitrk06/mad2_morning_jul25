<script setup>
import { ref } from 'vue';
import Products from './Products.vue';

const props = defineProps(['category'])
console.log(props.category);
// const categroy = {
//     name:'Fruits',
//     description: 'Fresh and organic fruits',
// }

console.log(props.category.products);
</script>

<template>
    <div class = "container-fluid">
        <div class="row md-3">
            <div class="col-9">
                <h2>{{ props.category.name }}</h2>
                <p>{{ props.category.description }}</p>
            </div>
            <div class="col-3">
                <button class="btn btn-primary">Edit</button>
                <button class="btn btn-danger">Delete</button>
            </div>
        </div>
        <div class="row md=3">
            <!-- Display products here -->
             <table>
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
                    <Products v-for="product in props.category.products" :key="product.name" :product="product" />
                </tbody>
             </table>
        </div>
    </div>
</template>