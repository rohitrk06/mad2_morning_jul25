import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useMessageStore = defineStore('messageStore', () => {
  const errorMessages = ref('')
  
  function updateErrorMessages(message) {
    errorMessages.value = message
    setTimeout(() => {
      errorMessages.value = ''
    },5000)
  }

  return { errorMessages, updateErrorMessages }
})
