<script setup>

import { ref } from 'vue';

const email = ref('');
const password = ref('');
</script>

<template>
    <div class="container-fluid">
        <div class="row justify-content-center mt-3">
            <div class="col-6  align-items-center">
                <h1>Register</h1>
                <form>
                    <div class="mb-3">
                        <label for="exampleInputEmail1" class="form-label">Email address</label>
                        <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" v-model="email">
                    </div>
                    <div class="mb-3">
                        <label for="exampleInputPassword1" class="form-label">Password</label>
                        <input type="password" class="form-control" id="exampleInputPassword1" v-model="password">
                    </div>
                    <button type="submit" class="btn btn-primary">Submit</button>
                </form>
            </div>
        </div>
    </div>
</template>