<script setup>

import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();

const email = ref('');
const password = ref('');

const checkEmailMessage = ref('');
const passwordMessage = ref('');
function validatePassword() {
    if (password.value.length < 8) {
        passwordMessage.value = 'Password must be at least 8 characters long'
        return false;
    }
    else passwordMessage.value = '';
    return true;
}

async function register(){
    if (!validatePassword()){
        alert('Please enter a valid password');
        return;
    }
    if (checkEmailMessage.value !== 'email addres is available') {
        alert('Use a valid email address');
        return;
    }
    const user = {
        email: email.value,
        password: password.value
    }

    const response = await fetch('http://127.0.0.1:5000/api/register',{
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(user)
    })

    if (!response.ok) {
        const errorData = await response.json();
        alert(errorData.message);
    } else {
        const data = await response.json();
        alert(data.message);
       router.push('/login');
    }
}

function checkEmailAvailibility() {
        fetch('http://127.0.0.1:5000/api/check-email',{
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email: email.value })
        }).then(response => {
            if(response.ok){
                return response.json();
            }
            else{
                console.error('Error checking email availability');
            }
        }).then(data=>{
            if (data.available) {
                checkEmailMessage.value = 'email addres is available'
            }
            else {
                checkEmailMessage.value = 'email address already taken'
            }
        })
}
</script>

<template>
    <div class="container-fluid">
        <div class="row justify-content-center mt-3">
            <div class="col-6  align-items-center">
                <h1>Register</h1>
                <form @submit.prevent="register">
                    <div class="mb-3">
                        <label for="exampleInputEmail1" class="form-label">Email address</label>
                        <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" @input="checkEmailAvailibility" v-model="email">
                        <p class="form-text" v-if="checkEmailMessage">{{ checkEmailMessage }}</p>
                    </div>
                    <div class="mb-3">
                        <label for="exampleInputPassword1" class="form-label">Password</label>
                        <input type="password" class="form-control" id="exampleInputPassword1" v-model="password" @input="validatePassword">
                        <p class="form-text" v-if="passwordMessage">{{ passwordMessage }}</p>
                    </div>
                    <button type="submit" class="btn btn-primary">Submit</button>
                </form>
            </div>
        </div>
    </div>
</template>