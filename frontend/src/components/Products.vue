<script setup>
defineProps(['product']);
</script>

<template>
    <tr>
        <td>
            {{ product.name }}
        </td>
        <td>
            <button>Edit</button>
            <button>Delete</button>
        </td>
    </tr>
</template>