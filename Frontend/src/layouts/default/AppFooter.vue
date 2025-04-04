<template>
  <v-span app class="d-flex align-center">
    <small>{{ APP_VERSION }}</small>
  </v-span>
</template>

<script>
  import { APP_VERSION } from '@/config';

  export default {
    data() {
      return {
        APP_VERSION,
      }
    },

    // methods: {
    //   goToTerms() {
    //     window.location = 'https://site.zapghub.app/terms_and_privacy.pdf'
    //   }
    // }
  }
</script>
