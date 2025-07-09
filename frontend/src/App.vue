<script setup>
import { RouterLink, RouterView } from 'vue-router';
import { useMessageStore } from '@/stores/counter.js';
import { useAuthStore } from '@/stores/auth.js';
import { computed } from 'vue';

const message_store = useMessageStore();
const auth_store = useAuthStore();

const ErrorMessages = computed(() => {
  return message_store.errorMessages;
});

const userEmail = computed(() => {
  return auth_store.getUserEmail();
});

function logout() {
  // Sent a fetch request to the backend to log out the user

  auth_store.clearAuthToken();
  message_store.updateErrorMessages('You have been logged out successfully.');
}

</script>

<template>
<div class="container-fluid">
  <nav class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">Grocery Store</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item" v-if="!auth_store.isAuthenticated">
            <RouterLink class="nav-link" to="/login">Login</RouterLink>
          </li>
          <li class="nav-item" v-if="!auth_store.isAuthenticated">
            <RouterLink class="nav-link" to="/register">Register</RouterLink>
          </li>


          <li class="nav-item" v-if="auth_store.isAuthenticated">
            <p class="nav-link">Welcome, {{ userEmail }}</p>
          </li>
          <li class="nav-item" v-if="auth_store.isAuthenticated">
            <a class="nav-link" @click="logout">Logout</a>
          </li>


        </ul>
        <form class="d-flex" role="search">
          <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search"/>
          <button class="btn btn-outline-success" type="submit">Search</button>
        </form>
      </div>
    </div>
  </nav>

  <div class="container-fluid">
    <p class="text-center mt-3" v-if="ErrorMessages">{{ ErrorMessages }}</p>
  </div>

  <RouterView />
</div>
</template>
